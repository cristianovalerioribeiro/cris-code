#!/usr/bin/env python3
"""
Gera o dashboard Lovelace "Painel Novo" a partir de config/comodos.yaml.

    python3 tools/gerar_painel.py [--config ARQ] [--saida ARQ] [--check]

Ideia central: nenhuma luminaria e listada. Cada comodo aponta para uma AREA
do Home Assistant e o auto-entities descobre em tempo real o que existe la
dentro. Um comodo com 1 lampada e outro com 12 usam exatamente a mesma
configuracao, e lampada nova aparece sozinha.

Arquitetura das telas
---------------------
  Casa    resumo. Um bloco por comodo: mestre de luz + um botao por
          luminaria + persianas + sensores. Compacto de proposito.
  Luzes   controle fino de brilho de TODAS as luminarias, agrupadas por comodo.
  <Comodo> o ambiente completo: iluminacao com cor e brilho, persianas,
          clima, sensores e o resto.
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

# Cores de destaque distribuidas automaticamente quando o comodo nao define
# uma. Sao os nomes de cor do Mushroom, que seguem o tema do Home Assistant.
PALETA = ["amber", "blue", "green", "purple", "teal", "pink",
          "indigo", "cyan", "orange", "light-green", "deep-purple", "red"]

DOMINIOS_CLIMA = ["climate", "fan", "humidifier"]
DOMINIOS_SENSOR = ["sensor", "binary_sensor"]
DOMINIOS_OUTROS = ["media_player", "switch", "vacuum", "lock", "input_boolean"]

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
#  YAML
# --------------------------------------------------------------------------- #
class Bloco(str):
    """String escrita como bloco literal (|-), sem escapes de barra invertida.

    Importante para os templates Jinja: em bloco literal o YAML nao interpreta
    ``\\\\``, entao ``light\\\\.`` chega ao Home Assistant como escrito.
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
    try:
        return str(caminho.resolve().relative_to(RAIZ))
    except ValueError:
        return str(caminho)


def sem_acento(texto: str) -> str:
    normal = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in normal if not unicodedata.combining(c))


def slug(texto: str, sep: str = "_") -> str:
    base = re.sub(r"[^a-z0-9]+", sep, sem_acento(texto).lower()).strip(sep)
    return re.sub(sep + r"{2,}", sep, base)


def glob_regex(padrao: str) -> str:
    """Converte um padrao de entity_id ('light.*lavabo*') em expressao regular.

    O auto-entities casa os padroes com fnmatch; o Jinja do Home Assistant usa
    regex. Os dois precisam concordar, entao a conversao fica num lugar so.
    """
    return "".join(".*" if c == "*" else "." if c == "?" else re.escape(c)
                   for c in padrao)


def regex_de(padroes) -> str:
    return "|".join(glob_regex(p) for p in (padroes or []))


def jinja_str(texto: str) -> str:
    """Escapa para dentro de uma string Jinja de aspas simples."""
    return texto.replace("\\", "\\\\").replace("'", "\\'")


def padroes_excluidos(bloco: dict, cfg: dict) -> list[str]:
    padroes = list(cfg.get("globais", {}).get("excluir_luzes") or [])
    padroes += list(bloco.get("excluir") or [])
    if bloco.get("grupo"):
        padroes.append(bloco["grupo"])  # o grupo ja e o card mestre
    return padroes


def luzes_do_bloco(bloco: dict, cfg: dict) -> str:
    """Expressao Jinja com as entidades light.* que pertencem a este bloco.

    Reproduz em Jinja exatamente o que o auto-entities faz com os filtros, para
    a contagem do card mestre bater com a lista de luminarias mostrada.
    """
    area = bloco.get("area")
    todas = "states.light | map(attribute='entity_id') | list"
    base = f"area_entities('{jinja_str(area)}')" if area else todas
    expr = f"({base} | select('match', 'light\\\\.') | list)"

    pad = regex_de(bloco.get("luzes"))
    if pad:
        expr = f"({expr} | select('match', '{jinja_str(pad)}') | list)"

    fora = regex_de(bloco.get("luzes_de_fora"))
    if fora:
        expr = (f"({expr} + ({todas} | select('match', "
                f"'{jinja_str(fora)}') | list))")

    exc = regex_de(padroes_excluidos(bloco, cfg))
    if exc:
        expr = f"({expr} | reject('match', '{jinja_str(exc)}') | list)"
    return f"({expr} | unique | list)"


def rotulo(bloco: dict) -> str:
    """Nome do bloco na tela. Cai para o nome da area quando nao informado."""
    return bloco.get("nome") or bloco.get("area") or "?"


def tem_brilho(cfg: dict) -> bool:
    """Se o painel deve oferecer controle de brilho e cor.

    Casa com lampadas comuns de liga/desliga ganha em desligar isso: sem slider,
    todo card de luz fica com a altura de uma linha e duas colunas encaixam sem
    sobra. Com slider em algumas luzes e nao em outras, a grade iguala as alturas
    da linha e a luz sem slider vira uma caixa grande e vazia ao lado da que tem.
    """
    return cfg["painel"].get("brilho", "auto") != "nunca"



def cor_do_comodo(comodo: dict, indice: int) -> str:
    return comodo.get("cor") or PALETA[indice % len(PALETA)]


def sensores_do_cabecalho(comodo: dict) -> list[str]:
    """Entidades ja mostradas como etiqueta no titulo — nao repetir nos chips."""
    return [comodo[k] for k in ("temperatura", "umidade") if comodo.get(k)]


# --------------------------------------------------------------------------- #
#  Blocos de card
# --------------------------------------------------------------------------- #
def titulo(texto: str, icone: str, estilo: str = "title", **extra) -> dict:
    card = {"type": "heading", "heading": texto, "heading_style": estilo}
    if icone:
        card["icon"] = icone
    card.update({k: v for k, v in extra.items() if v})
    return card


def _acao_alternar(bloco: dict, cfg: dict) -> dict:
    """Acende ou apaga o bloco inteiro num toque.

    Manda para o script os mesmos filtros que o auto-entities usa, para o toque
    agir exatamente nas luminarias que o bloco mostra. Sem isso, um bloco
    partido (Lavanderia dentro da area Cozinha) apagaria a cozinha toda.
    """
    if not cfg["painel"].get("usar_script_inteligente", True):
        return {"action": "perform-action", "perform_action": "light.toggle",
                "target": {"area_id": bloco.get("area_id") or slug(bloco.get("area", ""))}}

    dados: dict = {}
    if bloco.get("area"):
        dados["area"] = bloco["area"]
    if bloco.get("luzes"):
        dados["padrao"] = regex_de(bloco["luzes"])
    if bloco.get("luzes_de_fora"):
        dados["de_fora"] = regex_de(bloco["luzes_de_fora"])
    excluir = regex_de(padroes_excluidos(bloco, cfg))
    if excluir:
        dados["excluir"] = excluir
    return {"action": "perform-action",
            "perform_action": "script.alternar_luzes_do_bloco",
            "data": dados}


def _acao_abrir(bloco: dict, cfg: dict) -> dict:
    if not cfg["painel"].get("subviews", True):
        return {"action": "more-info"}
    return {"action": "navigate",
            "navigation_path": f"/{cfg['painel']['url']}/{slug(rotulo(bloco), '-')}"}


def mestre_de_luz(bloco: dict, cfg: dict, cor: str, com_cor: bool = True) -> dict:
    """Controle unico do bloco inteiro, no topo dele."""
    comum = {
        "tap_action": _acao_alternar(bloco, cfg),
        "hold_action": _acao_abrir(bloco, cfg),
        "double_tap_action": _acao_abrir(bloco, cfg),
        "grid_options": {"columns": "full"},
    }

    if bloco.get("grupo"):
        return {
            "type": "custom:mushroom-light-card",
            "entity": bloco["grupo"],
            "name": "Luzes",
            "icon": "mdi:lightbulb-group",
            "show_brightness_control": tem_brilho(cfg),
            "show_color_temp_control": com_cor and tem_brilho(cfg),
            "show_color_control": com_cor and tem_brilho(cfg),
            "use_light_color": True,
            "collapsible_controls": False,
            "layout": "horizontal",
            **comum,
        }

    luzes = luzes_do_bloco(bloco, cfg)
    return {
        "type": "custom:mushroom-template-card",
        "primary": "Luzes",
        "secondary": Bloco(
            f"{{% set l = {luzes} %}}"
            f"{{% set on = l | select('is_state', 'on') | list %}}"
            f"{{% if l | count == 0 %}}Nenhuma luz encontrada"
            f"{{% elif on | count == 0 %}}Tudo apagado"
            f"{{% elif on | count == l | count %}}Todas acesas ({{{{ l | count }}}})"
            f"{{% else %}}{{{{ on | count }}}} de {{{{ l | count }}}} acesas{{% endif %}}"
        ),
        "icon": Bloco(
            f"{{% if {luzes} | select('is_state', 'on') | list | count > 0 %}}"
            f"mdi:lightbulb-group{{% else %}}mdi:lightbulb-group-off{{% endif %}}"
        ),
        "icon_color": Bloco(
            f"{{% if {luzes} | select('is_state', 'on') | list | count > 0 %}}"
            f"{cor}{{% else %}}disabled{{% endif %}}"
        ),
        "multiline_secondary": False,
        **comum,
    }


def _regras_de_luz(bloco: dict, opcoes: dict) -> list[dict]:
    """Filtros do auto-entities que definem as luminarias do bloco."""
    area = bloco.get("area")
    regras: list[dict] = []

    padroes = bloco.get("luzes") or []
    if padroes:
        for p in padroes:
            regra = {"domain": "light", "entity_id": p}
            if area:
                regra["area"] = area
            regra["options"] = dict(opcoes)
            regras.append(regra)
    elif area:
        regras.append({"domain": "light", "area": area, "options": dict(opcoes)})

    # luzes de outra area que pertencem visualmente a este bloco
    for p in bloco.get("luzes_de_fora") or []:
        regras.append({"domain": "light", "entity_id": p, "options": dict(opcoes)})
    return regras


def _excluir_luzes(bloco: dict, cfg: dict) -> list[dict]:
    return [{"entity_id": p} for p in padroes_excluidos(bloco, cfg)]


def _auto(card_interno: dict, param: str, regras: list[dict],
          excluir: list[dict] | None = None, ordenar: bool = True) -> dict:
    saida = {
        "type": "custom:auto-entities",
        "card": card_interno,
        "card_param": param,
        "show_empty": False,
        "filter": {"include": regras, "exclude": excluir or []},
        "grid_options": {"columns": "full"},
    }
    if ordenar:
        saida["sort"] = {"method": "friendly_name"}
    return saida


def botoes_de_luz(bloco: dict, cfg: dict) -> dict:
    """Um botao por luminaria, com o nome dela."""
    return _auto(
        {"type": "custom:mushroom-chips-card", "alignment": "start"},
        "chips",
        _regras_de_luz(bloco, {
            "type": "entity",
            "content_info": "name",
            "use_light_color": True,
            "tap_action": {"action": "toggle"},
            "hold_action": {"action": "more-info"},
        }),
        _excluir_luzes(bloco, cfg),
    )


def cards_de_luz(bloco: dict, cfg: dict, colunas: int, com_cor: bool = True) -> dict:
    """Grade de luminarias com brilho e, opcionalmente, temperatura e cor.

    ``collapsible_controls`` mantem os sliders escondidos enquanto a luz esta
    apagada: uma barra de brilho em 0% nao controla nada e so gera ruido.
    """
    brilho = tem_brilho(cfg)
    return _auto(
        {"type": "grid", "columns": colunas, "square": False},
        "cards",
        _regras_de_luz(bloco, {
            "type": "custom:mushroom-light-card",
            # Sem slider o card cabe numa linha, entao segue horizontal mesmo em
            # varias colunas: assim todos tem a mesma altura e nao sobra caixa.
            "layout": "vertical" if (colunas > 1 and brilho) else "horizontal",
            "show_brightness_control": brilho,
            "show_color_temp_control": com_cor and brilho,
            "show_color_control": com_cor and brilho,
            "use_light_color": True,
            "collapsible_controls": True,
            "tap_action": {"action": "toggle"},
            "hold_action": {"action": "more-info"},
        }),
        _excluir_luzes(bloco, cfg),
    )


def cards_de_persiana(bloco: dict, colunas: int, com_posicao: bool) -> dict:
    """Persianas e cortinas da area do bloco."""
    return _auto(
        {"type": "grid", "columns": colunas, "square": False},
        "cards",
        [{"domain": "cover", "area": bloco["area"], "options": {
            "type": "custom:mushroom-cover-card",
            "layout": "horizontal",
            "show_buttons_control": True,
            "show_position_control": com_posicao,
            "tap_action": {"action": "more-info"},
            "hold_action": {"action": "more-info"},
        }}],
    )


def cards_de_sensor(bloco: dict) -> dict:
    """Sensores da area, exceto os que ja aparecem como etiqueta no titulo.

    Vao como tile e nao como pilula de proposito: no painel, pilula significa
    "botao que eu aperto" (as luminarias) e card significa "coisa que eu leio".
    """
    ja_no_titulo = [{"entity_id": e} for e in sensores_do_cabecalho(bloco)]
    return _auto(
        {"type": "grid", "columns": 1, "square": False},
        "cards",
        [{"domain": d, "area": bloco["area"], "options": {
            "type": "tile", "vertical": False, "hide_state": False,
            "tap_action": {"action": "more-info"},
        }} for d in DOMINIOS_SENSOR],
        ja_no_titulo,
    )


def cards_por_dominio(area: str, dominios: list[str], colunas: int = 1,
                      vertical: bool = False) -> dict:
    return _auto(
        {"type": "grid", "columns": colunas, "square": False},
        "cards",
        [{"domain": d, "area": area, "options": {
            "type": "tile", "vertical": vertical,
            "hold_action": {"action": "more-info"},
        }} for d in dominios],
    )


def etiquetas(bloco: dict) -> list[dict]:
    return [{"type": "entity", "entity": bloco[k]}
            for k in ("temperatura", "umidade") if bloco.get(k)]


# --------------------------------------------------------------------------- #
#  Blocos e pavimentos
# --------------------------------------------------------------------------- #
def pavimentos_de(cfg: dict) -> list[dict]:
    """Normaliza o config: uma lista de 'comodos' solta vira um pavimento so."""
    if cfg.get("pavimentos"):
        return [p for p in cfg["pavimentos"] if p.get("comodos")]
    if cfg.get("comodos"):
        return [{"nome": cfg["painel"].get("titulo", "Casa"),
                 "icone": "mdi:home", "comodos": cfg["comodos"]}]
    return []


def todos_os_blocos(cfg: dict) -> list[dict]:
    return [b for p in pavimentos_de(cfg) for b in p["comodos"]]


def secao_comodo(bloco: dict, cfg: dict, indice: int) -> dict:
    """Bloco do comodo na tela do pavimento: resumo, nao central de controle.

    Ordem fixa para o olho aprender o padrao:
      titulo -> mestre de luz -> um botao por luminaria -> persianas -> sensores.
    """
    cor = cor_do_comodo(bloco, indice)
    cabecalho = titulo(rotulo(bloco), bloco.get("icone", "mdi:home"),
                       badges=etiquetas(bloco), tap_action=_acao_abrir(bloco, cfg))

    cards = [cabecalho, mestre_de_luz(
        bloco, cfg, cor,
        com_cor=bool(cfg["painel"].get("cor_na_tela_inicial", True)))]

    if cfg["painel"].get("estilo_luzes", "botoes") == "cards":
        cards.append(cards_de_luz(bloco, cfg,
                                  cfg["painel"].get("colunas_luzes", 2), com_cor=False))
    else:
        cards.append(botoes_de_luz(bloco, cfg))

    # Blocos partidos (Lavanderia dentro da Cozinha) desligam persianas e
    # sensores para nao repetir os do bloco principal da mesma area.
    quer_persianas = bloco.get("persianas", cfg["painel"].get("mostrar_persianas", True))
    quer_sensores = bloco.get("sensores", cfg["painel"].get("mostrar_sensores", True))
    if quer_persianas and bloco.get("area"):
        cards.append(cards_de_persiana(bloco, colunas=1, com_posicao=False))
    if quer_sensores and bloco.get("area"):
        cards.append(cards_de_sensor(bloco))

    extras = bloco.get("extras") or []
    if extras:
        cards.append({
            "type": "grid", "columns": 2, "square": False,
            "cards": [{"type": "tile", "entity": e,
                       "hold_action": {"action": "more-info"}} for e in extras],
            "grid_options": {"columns": "full"},
        })

    return {"type": "grid", "cards": cards}


# --------------------------------------------------------------------------- #
#  Views
# --------------------------------------------------------------------------- #
def view_pavimento(pav: dict, cfg: dict, deslocamento: int) -> dict:
    return {
        "title": pav["nome"],
        "path": slug(pav["nome"], "-"),
        "icon": pav.get("icone", "mdi:home"),
        "type": "sections",
        "max_columns": cfg["painel"].get("colunas_max", 3),
        "dense_section_placement": bool(cfg["painel"].get("densidade", True)),
        "sections": [secao_comodo(b, cfg, deslocamento + i)
                     for i, b in enumerate(pav["comodos"])],
    }


def view_resumo(cfg: dict) -> dict:
    """O "painel geral": estado da casa toda e um atalho por pavimento.

    Fica por ultimo de proposito (``resumo_no_fim``): no dia a dia quem manda
    sao as abas de pavimento.
    """
    url = cfg["painel"]["url"]
    acesas = "states.light | selectattr('state', 'eq', 'on') | list | count"
    abertas = ("states.cover | rejectattr('state', 'eq', 'closed') "
               "| rejectattr('state', 'eq', 'unavailable') | list | count")

    chips = [
        {"type": "template",
         "icon": Bloco(f"{{% if {acesas} > 0 %}}mdi:lightbulb-group"
                       f"{{% else %}}mdi:lightbulb-group-off{{% endif %}}"),
         "icon_color": Bloco(f"{{% if {acesas} > 0 %}}amber{{% else %}}grey{{% endif %}}"),
         "content": Bloco(
             f"{{% set n = {acesas} %}}"
             f"{{% if n == 0 %}}Tudo apagado"
             f"{{% elif n == 1 %}}1 luz acesa"
             f"{{% else %}}{{{{ n }}}} luzes acesas{{% endif %}}"),
         "tap_action": {"action": "none"}},
        {"type": "template",
         "icon": "mdi:window-shutter-open",
         "icon_color": Bloco(f"{{% if {abertas} > 0 %}}blue{{% else %}}grey{{% endif %}}"),
         "content": Bloco(
             f"{{% set n = {abertas} %}}"
             f"{{% if n == 0 %}}Tudo fechado"
             f"{{% elif n == 1 %}}1 aberta"
             f"{{% else %}}{{{{ n }}}} abertas{{% endif %}}"),
         "tap_action": {"action": "none"}},
        {"type": "template",
         "icon": "mdi:lightbulb-off-outline",
         "icon_color": "red",
         "content": "Apagar tudo",
         "tap_action": {"action": "perform-action",
                        "perform_action": "light.turn_off",
                        "target": {"entity_id": "all"}},
         "confirmation": {"text": "Apagar todas as luzes da casa?"}},
    ]

    secoes = [{
        "type": "grid",
        "column_span": cfg["painel"].get("colunas_max", 3),
        "cards": [titulo(cfg["painel"].get("titulo", "Casa"), "mdi:home-heart"),
                  {"type": "custom:mushroom-chips-card", "alignment": "center",
                   "chips": chips, "grid_options": {"columns": "full"}}],
    }]

    # um card por pavimento, com a contagem de luzes acesas nele
    cards = []
    for pav in pavimentos_de(cfg):
        areas = list(dict.fromkeys(b["area"] for b in pav["comodos"] if b.get("area")))
        if not areas:
            continue
        soma = " + ".join(f"area_entities('{jinja_str(a)}')" for a in areas)
        luzes = (f"(({soma}) | unique | select('match', 'light\\\\.') | list)")
        cards.append({
            "type": "custom:mushroom-template-card",
            "primary": pav["nome"],
            "secondary": Bloco(
                f"{{% set l = {luzes} %}}"
                f"{{% set on = l | select('is_state', 'on') | list %}}"
                f"{{% if on | count == 0 %}}Tudo apagado"
                f"{{% else %}}{{{{ on | count }}}} de {{{{ l | count }}}} acesas{{% endif %}}"),
            "icon": pav.get("icone", "mdi:home"),
            "icon_color": Bloco(
                f"{{% if {luzes} | select('is_state', 'on') | list | count > 0 %}}"
                f"amber{{% else %}}disabled{{% endif %}}"),
            "multiline_secondary": False,
            "tap_action": {"action": "navigate",
                           "navigation_path": f"/{url}/{slug(pav['nome'], '-')}"},
            "grid_options": {"columns": "full"},
        })
    if cards:
        # lado a lado: a tela e curta e os atalhos ficam na mesma linha de leitura
        secoes.append({
            "type": "grid",
            "column_span": cfg["painel"].get("colunas_max", 3),
            "cards": [
                titulo("Pavimentos", "mdi:layers-outline"),
                {"type": "grid", "columns": min(3, len(cards)), "square": False,
                 "cards": cards, "grid_options": {"columns": "full"}},
            ],
        })

    return {
        "title": cfg["painel"].get("titulo", "Casa"),
        "path": "casa",
        "icon": "mdi:home-heart",
        "type": "sections",
        "max_columns": cfg["painel"].get("colunas_max", 3),
        "dense_section_placement": True,
        "sections": secoes,
    }


def view_luzes(cfg: dict) -> dict:
    """Controle fino: toda luminaria da casa, agrupada por bloco."""
    secoes = []
    for i, bloco in enumerate(todos_os_blocos(cfg)):
        cor = cor_do_comodo(bloco, i)
        secoes.append({"type": "grid", "cards": [
            titulo(rotulo(bloco), bloco.get("icone", "mdi:home"),
                   tap_action=_acao_abrir(bloco, cfg)),
            mestre_de_luz(bloco, cfg, cor),
            cards_de_luz(bloco, cfg, cfg["painel"].get("colunas_luzes", 2), com_cor=True),
        ]})
    return {
        "title": "Luzes",
        "path": "luzes",
        "icon": "mdi:lightbulb-group",
        "type": "sections",
        "max_columns": cfg["painel"].get("colunas_max", 3),
        "dense_section_placement": True,
        "sections": secoes,
    }


def view_comodo(bloco: dict, cfg: dict, indice: int) -> dict:
    """O ambiente completo do bloco, seccionado."""
    cor = cor_do_comodo(bloco, indice)
    area = bloco.get("area")

    secoes = [{"type": "grid", "cards": [
        titulo("Iluminação", "mdi:lightbulb-group"),
        mestre_de_luz(bloco, cfg, cor),
        cards_de_luz(bloco, cfg, cfg["painel"].get("colunas_luzes", 2), com_cor=True),
    ]}]

    quer_persianas = bloco.get("persianas", cfg["painel"].get("mostrar_persianas", True))
    quer_sensores = bloco.get("sensores", cfg["painel"].get("mostrar_sensores", True))

    if area and quer_persianas:
        secoes.append({"type": "grid", "cards": [
            titulo("Persianas e cortinas", "mdi:window-shutter"),
            cards_de_persiana(bloco, colunas=1, com_posicao=True),
        ]})
    if area and quer_sensores:
        secoes += [
            {"type": "grid", "cards": [
                titulo("Clima", "mdi:thermostat"),
                cards_por_dominio(area, DOMINIOS_CLIMA)]},
            {"type": "grid", "cards": [
                titulo("Sensores", "mdi:gauge"),
                cards_por_dominio(area, DOMINIOS_SENSOR, colunas=2, vertical=True)]},
            {"type": "grid", "cards": [
                titulo("Mídia e outros", "mdi:dots-horizontal"),
                cards_por_dominio(area, DOMINIOS_OUTROS)]},
        ]

    return {
        "title": rotulo(bloco),
        "path": slug(rotulo(bloco), "-"),
        "icon": bloco.get("icone", "mdi:home"),
        "type": "sections",
        "subview": True,
        "max_columns": 3,
        "dense_section_placement": True,
        "sections": secoes,
    }


# --------------------------------------------------------------------------- #
#  Validacao
# --------------------------------------------------------------------------- #
RESERVADOS = {"casa", "luzes"}


def validar(cfg: dict) -> list[str]:
    erros: list[str] = []
    painel = cfg.get("painel")

    if not isinstance(painel, dict):
        erros.append("config: bloco 'painel' ausente ou invalido")
        return erros
    if not painel.get("url"):
        erros.append("config: 'painel.url' e obrigatorio")

    modo = painel.get("brilho", "auto")
    if modo not in ("auto", "nunca"):
        erros.append(f"config: 'painel.brilho' deve ser 'auto' ou 'nunca' (veio '{modo}')")

    estilo = painel.get("estilo_luzes", "botoes")
    if estilo not in ("botoes", "cards"):
        erros.append(f"config: 'painel.estilo_luzes' deve ser 'botoes' ou 'cards' "
                     f"(veio '{estilo}')")

    if not cfg.get("pavimentos") and not cfg.get("comodos"):
        erros.append("config: informe 'pavimentos' (recomendado) ou 'comodos'")
        return erros

    pavs = pavimentos_de(cfg)
    if not pavs:
        erros.append("config: nenhum pavimento tem blocos — nada a gerar")
        return erros

    caminhos: dict[str, str] = {}
    for pav in pavs:
        if not pav.get("nome"):
            erros.append("pavimento sem 'nome'")
            continue
        p = slug(pav["nome"], "-")
        if p in RESERVADOS:
            erros.append(f"pavimento '{pav['nome']}': o caminho '{p}' e reservado")
        if p in caminhos:
            erros.append(f"pavimento '{pav['nome']}' gera o caminho '{p}', "
                         f"ja usado por '{caminhos[p]}'")
        caminhos[p] = f"pavimento {pav['nome']}"

    for pav in pavs:
        for i, bloco in enumerate(pav.get("comodos") or [], start=1):
            onde = f"'{pav.get('nome')}' bloco #{i}"
            if not isinstance(bloco, dict):
                erros.append(f"{onde}: deve ser um mapa de campos")
                continue
            if not bloco.get("nome") and not bloco.get("area"):
                erros.append(f"{onde}: precisa de 'nome' ou 'area'")
                continue
            if not bloco.get("area") and not bloco.get("luzes_de_fora"):
                erros.append(f"{onde} ('{rotulo(bloco)}'): sem 'area' o bloco so "
                             "funciona com 'luzes_de_fora'")

            p = slug(rotulo(bloco), "-")
            if p in RESERVADOS:
                erros.append(f"{onde} ('{rotulo(bloco)}'): o caminho '{p}' e reservado "
                             "pelo painel — renomeie o bloco")
            if p in caminhos:
                erros.append(f"{onde} ('{rotulo(bloco)}') gera o caminho '{p}', "
                             f"ja usado por {caminhos[p]} — renomeie um dos dois")
            caminhos[p] = f"bloco {rotulo(bloco)}"

            cor = bloco.get("cor")
            if cor and cor not in PALETA:
                erros.append(f"{onde} ('{rotulo(bloco)}'): cor '{cor}' desconhecida. "
                             f"Use uma de: {', '.join(PALETA)}")
            grupo = bloco.get("grupo")
            if grupo and not str(grupo).startswith("light."):
                erros.append(f"{onde} ('{rotulo(bloco)}'): 'grupo' precisa ser uma "
                             f"entidade light.* (veio '{grupo}')")
            for campo in ("luzes", "luzes_de_fora", "excluir"):
                valor = bloco.get(campo)
                if valor is not None and not isinstance(valor, list):
                    erros.append(f"{onde} ('{rotulo(bloco)}'): '{campo}' deve ser uma "
                                 "lista de padroes de entity_id")

            partido = bool(bloco.get("luzes") or bloco.get("luzes_de_fora")
                           or bloco.get("excluir"))
            if partido and not painel.get("usar_script_inteligente", True):
                erros.append(
                    f"{onde} ('{rotulo(bloco)}'): usa filtros de luz, entao precisa de "
                    "'usar_script_inteligente: true' — sem o script o toque no mestre "
                    "agiria na area inteira")
    return erros


# --------------------------------------------------------------------------- #
#  Montagem
# --------------------------------------------------------------------------- #
def montar(cfg: dict) -> dict:
    painel = cfg["painel"]
    views = []

    deslocamento = 0
    for pav in pavimentos_de(cfg):
        views.append(view_pavimento(pav, cfg, deslocamento))
        deslocamento += len(pav["comodos"])

    if painel.get("resumo", True):
        resumo = view_resumo(cfg)
        if painel.get("resumo_no_fim", True):
            views.append(resumo)
        else:
            views.insert(0, resumo)

    if painel.get("view_luzes", False):
        views.append(view_luzes(cfg))

    if painel.get("subviews", True):
        views += [view_comodo(b, cfg, i) for i, b in enumerate(todos_os_blocos(cfg))]

    return {"views": views}



def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Gera o dashboard Painel Novo.")
    p.add_argument("--config", type=Path, default=CONFIG_PADRAO)
    p.add_argument("--saida", type=Path, default=SAIDA_PADRAO)
    p.add_argument("--check", action="store_true",
                   help="nao escreve; falha se o arquivo gerado estiver desatualizado")
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

    painel = montar(cfg)
    conteudo = CABECALHO + "\n" + yaml.dump(
        painel, Dumper=Dumper, sort_keys=False, allow_unicode=True,
        default_flow_style=False, width=100, indent=2)

    if args.check:
        atual = args.saida.read_text(encoding="utf-8") if args.saida.exists() else ""
        if atual != conteudo:
            print(f"erro: {curto(args.saida)} esta desatualizado — "
                  "rode 'python3 tools/gerar_painel.py'", file=sys.stderr)
            return 1
        print(f"ok: {curto(args.saida)} esta atualizado")
        return 0

    args.saida.parent.mkdir(parents=True, exist_ok=True)
    args.saida.write_text(conteudo, encoding="utf-8")
    print(f"gerado: {curto(args.saida)}")
    pavs = pavimentos_de(cfg)
    print(f"  {len(pavs)} pavimento(s), {len(todos_os_blocos(cfg))} bloco(s), "
          f"{len(painel['views'])} view(s)")
    for pav in pavs:
        nomes = ", ".join(rotulo(b) for b in pav["comodos"])
        print(f"    {pav['nome']}: {nomes}")
    vazios = [p["nome"] for p in (cfg.get("pavimentos") or []) if not p.get("comodos")]
    for nome in vazios:
        print(f"  aviso: pavimento '{nome}' esta sem blocos — aba nao gerada")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
