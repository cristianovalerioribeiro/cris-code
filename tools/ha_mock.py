#!/usr/bin/env python3
"""
Simulacao minima do Home Assistant, usada pela pre-visualizacao.

Reproduz o suficiente para desenhar o painel numa pagina antes de instalar:
uma maquina de estados falsa, os filtros/testes Jinja que o HA adiciona
(``area_entities``, ``is_state``, ``match``) e a expansao do ``auto-entities``.

Nada aqui vai para o Home Assistant.
"""

from __future__ import annotations

import fnmatch
import re
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path

import yaml
from jinja2 import Environment

RAIZ = Path(__file__).resolve().parent.parent


# --------------------------------------------------------------------------- #
#  Estado
# --------------------------------------------------------------------------- #
@dataclass
class Entidade:
    entity_id: str
    name: str
    state: str
    area: str
    unidade: str = ""
    classe: str = ""
    attributes: dict = field(default_factory=dict)

    @property
    def dominio(self) -> str:
        return self.entity_id.split(".", 1)[0]

    @property
    def ligada(self) -> bool:
        return self.state in ("on", "open", "playing", "home", "cool", "heat", "cooling")

    @property
    def dimeriza(self) -> bool:
        """Lampada que aceita brilho. A maioria das casas tem poucas."""
        return bool(self.attributes.get("dimeriza", False))

    @property
    def brilho(self) -> int:
        return int(self.attributes.get("brilho", 0))

    @property
    def posicao(self) -> int:
        return int(self.attributes.get("posicao", 0))

    def __str__(self) -> str:  # {{ ... }} de uma entidade devolve o estado
        return self.state


class Estados:
    """Equivalente do objeto ``states``: chamavel e navegavel por dominio."""

    def __init__(self, entidades: list[Entidade]):
        self._lista = entidades
        self._por_id = {e.entity_id: e for e in entidades}

    def __call__(self, entity_id: str, *_, **__) -> str:
        ent = self._por_id.get(entity_id)
        return ent.state if ent else "unknown"

    def __getattr__(self, dominio: str) -> list[Entidade]:
        return [e for e in self._lista if e.dominio == dominio]

    def __iter__(self):
        return iter(self._lista)


class Casa:
    def __init__(self, dados: dict):
        self.entidades: list[Entidade] = []
        for area, itens in (dados.get("areas") or {}).items():
            for it in itens or []:
                extras = {k: v for k, v in it.items()
                          if k not in ("id", "nome", "estado", "unidade", "classe")}
                self.entidades.append(
                    Entidade(
                        entity_id=it["id"],
                        name=it.get("nome", it["id"]),
                        state=str(it.get("estado", "off")),
                        area=area,
                        unidade=it.get("unidade", ""),
                        classe=it.get("classe", ""),
                        attributes=extras,
                    )
                )
        self.por_id = {e.entity_id: e for e in self.entidades}
        self.states = Estados(self.entidades)

    @classmethod
    def carregar(cls, caminho: Path) -> "Casa":
        return cls(yaml.safe_load(caminho.read_text(encoding="utf-8")) or {})

    def area_entities(self, area: str) -> list[str]:
        alvo = area.lower().replace("_", " ")
        return [
            e.entity_id
            for e in self.entidades
            if e.area.lower() == alvo or e.area.lower().replace(" ", "_") == area.lower()
        ]

    def de_area(self, area: str, dominios: tuple[str, ...]) -> list[Entidade]:
        return [self.por_id[i] for i in self.area_entities(area)
                if self.por_id[i].dominio in dominios]

    # ---------------------------------------------------------------- Jinja --
    def ambiente(self) -> Environment:
        env = Environment()

        def is_state(alvo, valor) -> bool:
            eid = alvo.entity_id if isinstance(alvo, Entidade) else str(alvo)
            ent = self.por_id.get(eid)
            return bool(ent and ent.state == valor)

        def combina(alvo, padrao) -> bool:
            eid = alvo.entity_id if isinstance(alvo, Entidade) else str(alvo)
            return re.match(padrao, eid) is not None

        def state_attr(eid, atributo):
            ent = self.por_id.get(eid)
            if ent is None:
                return None
            fixos = {
                "friendly_name": ent.name,
                "unit_of_measurement": ent.unidade or None,
                "device_class": ent.classe or None,
                "current_position": ent.attributes.get("posicao"),
                "supported_color_modes": (["brightness"] if ent.dimeriza else ["onoff"]),
            }
            if atributo in fixos:
                return fixos[atributo]
            return ent.attributes.get(atributo)

        env.globals["area_entities"] = self.area_entities
        env.globals["states"] = self.states
        env.globals["state_attr"] = state_attr
        env.globals["areas"] = lambda: sorted({e.area for e in self.entidades})
        env.globals["area_name"] = lambda a: a
        for nome, fn in (("is_state", is_state), ("match", combina)):
            env.tests[nome] = fn
            env.filters[nome] = fn
        return env

    def render(self, texto: str) -> str:
        if not isinstance(texto, str) or ("{{" not in texto and "{%" not in texto):
            return texto
        return self.ambiente().from_string(texto).render().strip()


# --------------------------------------------------------------------------- #
#  auto-entities
# --------------------------------------------------------------------------- #
def _bate(ent: Entidade, regra: dict) -> bool:
    if "domain" in regra and ent.dominio != regra["domain"]:
        return False
    if "area" in regra and ent.area.lower() != str(regra["area"]).lower():
        return False
    if "entity_id" in regra and not fnmatch.fnmatch(ent.entity_id, regra["entity_id"]):
        return False
    if "state" in regra and ent.state != regra["state"]:
        return False
    return True


def expandir_auto_entities(card: dict, casa: Casa) -> dict | None:
    """Resolve um auto-entities no card concreto que ele produziria.

    Devolve None quando o filtro nao casa com nada e ``show_empty`` e falso —
    exatamente o que o card faz no Home Assistant.
    """
    filtro = card.get("filter") or {}
    incluir = filtro.get("include") or []
    excluir = filtro.get("exclude") or []

    achados: list[tuple[Entidade, dict]] = []
    vistos: set[str] = set()
    for regra in incluir:
        opcoes = regra.get("options") or {}
        for ent in casa.entidades:
            if ent.entity_id in vistos or not _bate(ent, regra):
                continue
            if any(_bate(ent, ex) for ex in excluir):
                continue
            vistos.add(ent.entity_id)
            achados.append((ent, opcoes))

    if (card.get("sort") or {}).get("method") == "friendly_name":
        achados.sort(key=lambda p: p[0].name.lower())

    if not achados and not card.get("show_empty", True):
        return None

    param = card.get("card_param", "entities")
    filhos = [dict(opcoes, entity=ent.entity_id) for ent, opcoes in achados]

    interno = dict(card.get("card") or {"type": "entities"})
    interno[param] = filhos
    if "grid_options" in card:
        interno["grid_options"] = card["grid_options"]
    interno["_auto"] = True
    interno["_n"] = len(filhos)
    return interno
