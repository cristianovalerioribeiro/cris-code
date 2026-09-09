#!/usr/bin/env python3
"""
Gera o dashboard Lovelace "Painel Novo" a partir de config/comodos.yaml.

    python3 tools/gerar_painel.py [--config ARQ] [--saida ARQ] [--check]

O painel nao lista luminarias uma a uma: cada comodo usa auto-entities para
descobrir em tempo real todas as luzes da area correspondente. Por isso o
layout se adapta sozinho a comodos com 1, 3 ou 12 lampadas.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
CONFIG_PADRAO = RAIZ / "config" / "comodos.yaml"
SAIDA_PADRAO = RAIZ / "dashboards" / "painel-novo.yaml"

CABECALHO = """\
# =============================================================================
#  ARQUIVO GERADO AUTOMATICAMENTE — NAO EDITE A MAO.
#
#  Fonte:   config/comodos.yaml
#  Comando: python3 tools/gerar_painel.py
#
#  Qualquer alteracao feita diretamente aqui e perdida na proxima geracao.
# =============================================================================
"""


# --------------------------------------------------------------------------- #
#  YAML: blocos literais para os templates Jinja ficarem legiveis
# --------------------------------------------------------------------------- #
class Bloco(str):
    """String escrita como bloco literal (|-), sem escapes de barra invertida.

    Importante para os templates Jinja: em bloco literal o YAML nao interpreta
    ``\\`` , entao ``light\\.`` chega ao Home Assistant exatamente como escrito.
    """


class Dumper(yaml.SafeDumper):
    """SafeDumper que indenta itens de lista (mais legivel no Lovelace)."""

    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def _repr_bloco(dumper: yaml.Dumper, data: Bloco):
    return dumper.represent_scalar("tag:yaml.org,2002:str", str(data), style="|")


Dumper.add_representer(Bloco, _repr_bloco)


# --------------------------------------------------------------------------- #
#  Helpers
# --------------------------------------------------------------------------- #
def curto(caminho: Path) -> str:
    """Caminho relativo a raiz do projeto quando possivel; absoluto quando nao."""
    try:
        return str(caminho.resolve().relative_to(RAIZ))
    except ValueError:
        return str(caminho)


def sem_acento(texto: str) -> str:
    normal = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in normal if not unicodedata.combining(c))


def slug(texto: str, sep: str = "_") -> str:
    base = sem_acento(texto).lower()
    base = re.sub(r"[^a-z0-9]+", sep, base).strip(sep)
    return re.sub(sep + r"{2,}", sep, base)


def jinja_luzes_da_area(area: str) -> str:
    """Lista de entidades light.* da area, como expressao Jinja."""
    return f"area_entities('{area}') | select('match', 'light\\\\.') | list"


# --------------------------------------------------------------------------- #
#  Cards reutilizaveis
# --------------------------------------------------------------------------- #
def card_titulo(texto: str, icone: str, estilo: str = "title", **extra) -> dict:
    card = {"type": "heading", "heading": texto, "heading_style": estilo, "icon": icone}
    card.update(extra)
    return card


def card_mestre_comodo(comodo: dict, cfg: dict) -> dict:
    """Card grande do comodo: nome, contagem de luzes acesas e toque para alternar."""
    area = comodo["area"]
    area_id = comodo.get("area_id") or slug(area)
    luzes = jinja_luzes_da_area(area)

    secundario = Bloco(
        f"{{% set luzes = {luzes} %}}"
        f"{{% set acesas = luzes | select('is_state', 'on') | list %}}"
        f"{{% if luzes | count == 0 %}}Nenhuma luz nesta area"
        f"{{% elif acesas | count == 0 %}}Tudo apagado"
        f"{{% else %}}{{{{ acesas | count }}}} de {{{{ luzes | count }}}} acesa(s)"
        f"{{% endif %}}"
    )
    cor = Bloco(
        f"{{% if {luzes} | select('is_state', 'on') | list | count > 0 %}}amber"
        f"{{% else %}}disabled{{% endif %}}"
    )

    if cfg["painel"].get("usar_script_inteligente", True):
        # Apaga tudo se houver qualquer luz acesa; senao acende tudo.
        # Passa o NOME da area (nao o id): area_entities() aceita os dois, e o
        # nome e o mesmo valor ja usado no filtro do auto-entities.
        tap = {
            "action": "perform-action",
            "perform_action": "script.alternar_luzes_da_area",
            "data": {"area": area},
        }
    else:
        tap = {
            "action": "perform-action",
            "perform_action": "light.toggle",
            "target": {"area_id": area_id},
        }

    card = {
        "type": "custom:mushroom-template-card",
        "primary": area,
        "secondary": secundario,
        "icon": comodo.get("icone", "mdi:home"),
        "icon_color": cor,
        "multiline_secondary": False,
        "tap_action": tap,
        "hold_action": {"action": "more-info"},
        "grid_options": {"columns": "full"},
    }
    if cfg["painel"].get("subviews", True):
        card["hold_action"] = {
            "action": "navigate",
            "navigation_path": f"/{cfg['painel']['url']}/{slug(area, '-')}",
        }
    return card


def _excluir(comodo: dict, cfg: dict) -> list[dict]:
    padroes = list(cfg.get("globais", {}).get("excluir_luzes") or [])
    padroes += list(comodo.get("excluir") or [])
    return [{"entity_id": p} for p in padroes]


def card_luzes_do_comodo(comodo: dict, cfg: dict, colunas: int, compacto: bool) -> dict:
    """Grade de luminarias descoberta automaticamente pela area."""
    opcoes = {
        "type": "custom:mushroom-light-card",
        "layout": "vertical" if colunas > 1 else "horizontal",
        "show_brightness_control": True,
        "show_color_temp_control": True,
        "show_color_control": True,
        "use_light_color": True,
        "collapsible_controls": compacto,
        "tap_action": {"action": "toggle"},
        "hold_action": {"action": "more-info"},
        "double_tap_action": {"action": "more-info"},
    }
    return {
        "type": "custom:auto-entities",
        "card": {"type": "grid", "columns": colunas, "square": False},
        "card_param": "cards",
        "show_empty": False,
        "filter": {
            "include": [{"domain": "light", "area": comodo["area"], "options": opcoes}],
            "exclude": _excluir(comodo, cfg),
        },
        "sort": {"method": "friendly_name"},
        "grid_options": {"columns": "full"},
    }


def card_chips_luzes(comodo: dict, cfg: dict) -> dict:
    """Linha de botoes redondos, um por luminaria da area."""
    return {
        "type": "custom:auto-entities",
        "card": {"type": "custom:mushroom-chips-card", "alignment": "start"},
        "card_param": "chips",
        "show_empty": False,
        "filter": {
            "include": [
                {
                    "domain": "light",
                    "area": comodo["area"],
                    "options": {
                        "type": "entity",
                        "content_info": "none",
                        "use_light_color": True,
                        "tap_action": {"action": "toggle"},
                        "hold_action": {"action": "more-info"},
                    },
                }
            ],
            "exclude": _excluir(comodo, cfg),
        },
        "sort": {"method": "friendly_name"},
        "grid_options": {"columns": "full"},
    }


def card_extras(comodo: dict) -> dict | None:
    extras = comodo.get("extras") or []
    if not extras:
        return None
    return {
        "type": "grid",
        "columns": 2,
        "square": False,
        "cards": [
            {
                "type": "tile",
                "entity": ent,
                "vertical": False,
                "tap_action": {"action": "toggle"},
                "hold_action": {"action": "more-info"},
            }
            for ent in extras
        ],
        "grid_options": {"columns": "full"},
    }


def badges_do_comodo(comodo: dict) -> list[dict]:
    badges = []
    for chave in ("temperatura", "umidade"):
        ent = comodo.get(chave)
        if ent:
            badges.append({"type": "entity", "entity": ent})
    return badges


# --------------------------------------------------------------------------- #
#  Secoes / views
# --------------------------------------------------------------------------- #
def secao_resumo(cfg: dict) -> dict:
    url = cfg["painel"]["url"]
    acesas = "states.light | selectattr('state', 'eq', 'on') | list | count"

    chips = [
        {
            "type": "template",
            "icon": "mdi:lightbulb-group",
            "icon_color": Bloco(f"{{% if {acesas} > 0 %}}amber{{% else %}}grey{{% endif %}}"),
            "content": Bloco(
                f"{{% set n = {acesas} %}}"
                f"{{% if n == 0 %}}Tudo apagado"
                f"{{% elif n == 1 %}}1 luz acesa"
                f"{{% else %}}{{{{ n }}}} luzes acesas{{% endif %}}"
            ),
            "tap_action": (
                {"action": "navigate", "navigation_path": f"/{url}/luzes"}
                if cfg["painel"].get("view_luzes", True)
                else {"action": "none"}
            ),
        },
        {
            "type": "template",
            "icon": "mdi:lightbulb-off-outline",
            "icon_color": "red",
            "content": "Apagar tudo",
            "tap_action": {
                "action": "perform-action",
                "perform_action": "light.turn_off",
                "target": {"entity_id": "all"},
            },
            "confirmation": {"text": "Apagar todas as luzes da casa?"},
        },
    ]

    return {
        "type": "grid",
        "column_span": cfg["painel"].get("colunas_max", 4),
        "cards": [
            card_titulo(cfg["painel"].get("titulo", "Casa"), "mdi:home-heart"),
            {
                "type": "custom:mushroom-chips-card",
                "alignment": "center",
                "chips": chips,
                "grid_options": {"columns": "full"},
            },
        ],
    }


def secao_comodo(comodo: dict, cfg: dict) -> dict:
    area = comodo["area"]
    titulo = card_titulo(
        area,
        comodo.get("icone", "mdi:home"),
        badges=badges_do_comodo(comodo) or None,
    )
    if titulo.get("badges") is None:
        titulo.pop("badges")
    if cfg["painel"].get("subviews", True):
        titulo["tap_action"] = {
            "action": "navigate",
            "navigation_path": f"/{cfg['painel']['url']}/{slug(area, '-')}",
        }

    cards = [
        titulo,
        card_mestre_comodo(comodo, cfg),
        card_luzes_do_comodo(
            comodo, cfg, colunas=cfg["painel"].get("colunas_luzes", 2), compacto=True
        ),
    ]
    extras = card_extras(comodo)
    if extras:
        cards.append(extras)

    return {"type": "grid", "cards": cards}


def view_principal(cfg: dict) -> dict:
    return {
        "title": cfg["painel"].get("titulo", "Casa"),
        "path": "casa",
        "icon": "mdi:home",
        "type": "sections",
        "max_columns": cfg["painel"].get("colunas_max", 4),
        "dense_section_placement": bool(cfg["painel"].get("densidade", True)),
        "sections": [secao_resumo(cfg)] + [secao_comodo(c, cfg) for c in cfg["comodos"]],
    }


def view_luzes(cfg: dict) -> dict:
    """Visao compacta: por comodo, uma linha de botoes redondos + um mestre."""
    secoes = []
    for comodo in cfg["comodos"]:
        secoes.append(
            {
                "type": "grid",
                "cards": [
                    card_titulo(comodo["area"], comodo.get("icone", "mdi:home"), estilo="subtitle"),
                    card_chips_luzes(comodo, cfg),
                    card_mestre_comodo(comodo, cfg),
                ],
            }
        )
    return {
        "title": "Luzes",
        "path": "luzes",
        "icon": "mdi:lightbulb-group",
        "type": "sections",
        "max_columns": cfg["painel"].get("colunas_max", 4),
        "dense_section_placement": True,
        "sections": secoes,
    }


def _auto_dominios(area: str, dominios: list[str], opcoes: dict, colunas: int = 1) -> dict:
    return {
        "type": "custom:auto-entities",
        "card": {"type": "grid", "columns": colunas, "square": False},
        "card_param": "cards",
        "show_empty": False,
        "filter": {
            "include": [{"domain": d, "area": area, "options": opcoes} for d in dominios]
        },
        "sort": {"method": "friendly_name"},
        "grid_options": {"columns": "full"},
    }


def view_comodo(comodo: dict, cfg: dict) -> dict:
    area = comodo["area"]
    tile = {
        "type": "tile",
        "vertical": False,
        "hold_action": {"action": "more-info"},
    }

    secoes = [
        {
            "type": "grid",
            "cards": [
                card_titulo("Iluminacao", "mdi:lightbulb-group"),
                card_mestre_comodo(comodo, cfg),
                card_luzes_do_comodo(comodo, cfg, colunas=1, compacto=False),
            ],
        },
        {
            "type": "grid",
            "cards": [
                card_titulo("Clima", "mdi:thermostat"),
                _auto_dominios(area, ["climate", "fan", "humidifier"], dict(tile)),
            ],
        },
        {
            "type": "grid",
            "cards": [
                card_titulo("Sensores", "mdi:gauge"),
                _auto_dominios(area, ["sensor", "binary_sensor"], dict(tile), colunas=2),
            ],
        },
        {
            "type": "grid",
            "cards": [
                card_titulo("Outros", "mdi:dots-horizontal"),
                _auto_dominios(
                    area, ["switch", "cover", "media_player", "vacuum", "lock"], dict(tile)
                ),
            ],
        },
    ]

    return {
        "title": area,
        "path": slug(area, "-"),
        "icon": comodo.get("icone", "mdi:home"),
        "type": "sections",
        "subview": True,
        "max_columns": 3,
        "dense_section_placement": True,
        "sections": secoes,
    }


# --------------------------------------------------------------------------- #
#  Validacao
# --------------------------------------------------------------------------- #
def validar(cfg: dict) -> list[str]:
    erros: list[str] = []

    if not isinstance(cfg.get("painel"), dict):
        erros.append("config: bloco 'painel' ausente ou invalido")
    elif not cfg["painel"].get("url"):
        erros.append("config: 'painel.url' e obrigatorio")

    comodos = cfg.get("comodos")
    if not isinstance(comodos, list) or not comodos:
        erros.append("config: 'comodos' deve ser uma lista com pelo menos um item")
        return erros

    vistos: dict[str, int] = {}
    for i, comodo in enumerate(comodos, start=1):
        if not isinstance(comodo, dict) or not comodo.get("area"):
            erros.append(f"comodo #{i}: campo 'area' e obrigatorio")
            continue
        caminho = slug(comodo["area"], "-")
        if caminho in vistos:
            erros.append(
                f"comodo #{i} ('{comodo['area']}') gera o mesmo caminho "
                f"'{caminho}' do comodo #{vistos[caminho]} — renomeie um deles"
            )
        vistos[caminho] = i
        if caminho in ("casa", "luzes"):
            erros.append(
                f"comodo #{i} ('{comodo['area']}'): o caminho '{caminho}' e reservado "
                "pelo painel — renomeie a area"
            )
    return erros


# --------------------------------------------------------------------------- #
#  Main
# --------------------------------------------------------------------------- #
def montar(cfg: dict) -> dict:
    views = [view_principal(cfg)]
    if cfg["painel"].get("view_luzes", True):
        views.append(view_luzes(cfg))
    if cfg["painel"].get("subviews", True):
        views.extend(view_comodo(c, cfg) for c in cfg["comodos"])
    return {"views": views}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Gera o dashboard Painel Novo.")
    p.add_argument("--config", type=Path, default=CONFIG_PADRAO)
    p.add_argument("--saida", type=Path, default=SAIDA_PADRAO)
    p.add_argument(
        "--check",
        action="store_true",
        help="nao escreve; falha se o arquivo gerado estiver desatualizado",
    )
    args = p.parse_args(argv)

    if not args.config.exists():
        print(f"erro: config nao encontrada: {args.config}", file=sys.stderr)
        return 2

    cfg = yaml.safe_load(args.config.read_text(encoding="utf-8")) or {}
    cfg.setdefault("painel", {})
    cfg.setdefault("globais", {})

    erros = validar(cfg)
    if erros:
        for e in erros:
            print(f"erro: {e}", file=sys.stderr)
        return 1

    corpo = yaml.dump(
        montar(cfg),
        Dumper=Dumper,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
        width=100,
        indent=2,
    )
    conteudo = CABECALHO + "\n" + corpo

    if args.check:
        atual = args.saida.read_text(encoding="utf-8") if args.saida.exists() else ""
        if atual != conteudo:
            print(
                f"erro: {curto(args.saida)} esta desatualizado — "
                "rode 'python3 tools/gerar_painel.py'",
                file=sys.stderr,
            )
            return 1
        print(f"ok: {curto(args.saida)} esta atualizado")
        return 0

    args.saida.parent.mkdir(parents=True, exist_ok=True)
    args.saida.write_text(conteudo, encoding="utf-8")

    n_comodos = len(cfg["comodos"])
    n_views = len(montar(cfg)["views"])
    print(f"gerado: {curto(args.saida)}")
    print(f"  {n_comodos} comodo(s), {n_views} view(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
