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


def luzes_da_area(area: str) -> str:
    """Expressao Jinja com a lista de entidades light.* da area."""
    return f"area_entities('{area}') | select('match', 'light\\\\.') | list"


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


def _acao_alternar(comodo: dict, cfg: dict) -> dict:
    area = comodo["area"]
    if cfg["painel"].get("usar_script_inteligente", True):
        # Passa o NOME da area: area_entities() aceita nome ou id, e o nome e o
        # mesmo valor ja usado nos filtros do auto-entities.
        return {"action": "perform-action",
                "perform_action": "script.alternar_luzes_da_area",
                "data": {"area": area}}
    return {"action": "perform-action", "perform_action": "light.toggle",
            "target": {"area_id": comodo.get("area_id") or slug(area)}}


def _acao_abrir(comodo: dict, cfg: dict) -> dict:
    if not cfg["painel"].get("subviews", True):
        return {"action": "more-info"}
    return {"action": "navigate",
            "navigation_path": f"/{cfg['painel']['url']}/{slug(comodo['area'], '-')}"}


def mestre_de_luz(comodo: dict, cfg: dict, cor: str, com_cor: bool = True) -> dict:
    """Controle unico do comodo inteiro, no topo do bloco.

    Com ``grupo:`` definido vira um card de luz de verdade, com slider de
    brilho do comodo todo. Sem ele, vira um card de template que mostra a
    contagem e alterna tudo no toque.
    """
    comum = {
        "tap_action": _acao_alternar(comodo, cfg),
        "hold_action": _acao_abrir(comodo, cfg),
        "double_tap_action": _acao_abrir(comodo, cfg),
        "grid_options": {"columns": "full"},
    }

    if comodo.get("grupo"):
        return {
            "type": "custom:mushroom-light-card",
            "entity": comodo["grupo"],
            "name": "Luzes do comodo",
            "icon": "mdi:lightbulb-group",
            "show_brightness_control": True,
            "show_color_temp_control": com_cor,
            "show_color_control": com_cor,
            "use_light_color": True,
            "collapsible_controls": False,
            "layout": "horizontal",
            **comum,
        }

    area = comodo["area"]
    luzes = luzes_da_area(area)
    return {
        "type": "custom:mushroom-template-card",
        "primary": "Luzes",
        "secondary": Bloco(
            f"{{% set l = {luzes} %}}"
            f"{{% set on = l | select('is_state', 'on') | list %}}"
            f"{{% if l | count == 0 %}}Nenhuma luz nesta area"
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


def _excluir_luzes(comodo: dict, cfg: dict) -> list[dict]:
    padroes = list(cfg.get("globais", {}).get("excluir_luzes") or [])
    padroes += list(comodo.get("excluir") or [])
    if comodo.get("grupo"):
        padroes.append(comodo["grupo"])  # o grupo ja e o card mestre
    return [{"entity_id": p} for p in padroes]


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


def botoes_de_luz(comodo: dict, cfg: dict) -> dict:
    """Um botao por luminaria, com o nome dela.

    O nome e o que responde "o que tem dentro deste comodo" sem precisar tocar
    em nada. So o icone economizaria espaco, mas seis bolinhas identicas nao
    dizem qual e o abajur e qual e a fita de LED.
    """
    return _auto(
        {"type": "custom:mushroom-chips-card", "alignment": "start"},
        "chips",
        [{"domain": "light", "area": comodo["area"], "options": {
            "type": "entity",
            "content_info": "name",
            "use_light_color": True,
            "tap_action": {"action": "toggle"},
            "hold_action": {"action": "more-info"},
        }}],
        _excluir_luzes(comodo, cfg),
    )


def cards_de_luz(comodo: dict, cfg: dict, colunas: int, com_cor: bool = True) -> dict:
    """Grade de luminarias com brilho e, opcionalmente, temperatura e cor.

    ``collapsible_controls`` mantem os sliders escondidos enquanto a luz esta
    apagada: uma barra de brilho em 0% nao controla nada e so gera ruido.
    """
    return _auto(
        {"type": "grid", "columns": colunas, "square": False},
        "cards",
        [{"domain": "light", "area": comodo["area"], "options": {
            "type": "custom:mushroom-light-card",
            "layout": "vertical" if colunas > 1 else "horizontal",
            "show_brightness_control": True,
            "show_color_temp_control": com_cor,
            "show_color_control": com_cor,
            "use_light_color": True,
            "collapsible_controls": True,
            "tap_action": {"action": "toggle"},
            "hold_action": {"action": "more-info"},
        }}],
        _excluir_luzes(comodo, cfg),
    )


def cards_de_persiana(comodo: dict, colunas: int, com_posicao: bool) -> dict:
    """Persianas e cortinas.

    Na tela principal vao em linha unica e sem barra de posicao: abrir, parar e
    fechar cobre o uso do dia a dia e o card fica com a altura de uma linha.
    A barra de posicao aparece so na pagina do comodo.
    """
    return _auto(
        {"type": "grid", "columns": colunas, "square": False},
        "cards",
        [{"domain": "cover", "area": comodo["area"], "options": {
            "type": "custom:mushroom-cover-card",
            "layout": "horizontal",
            "show_buttons_control": True,
            "show_position_control": com_posicao,
            "tap_action": {"action": "more-info"},
            "hold_action": {"action": "more-info"},
        }}],
    )


def cards_de_sensor(comodo: dict) -> dict:
    """Sensores do comodo, exceto os que ja aparecem como etiqueta no titulo.

    Vao como tile e nao como pilula de proposito: no painel, pilula significa
    "botao que eu aperto" (as luminarias) e card significa "coisa que eu leio".
    Se sensor e luminaria tivessem a mesma forma, "Janela" e "Abajur" ficariam
    indistinguiveis.
    """
    ja_no_titulo = [{"entity_id": e} for e in sensores_do_cabecalho(comodo)]
    # Coluna unica: a secao tem ~300px tanto no desktop quanto no celular, entao
    # meia largura truncaria nomes como "Vazamento de gas".
    return _auto(
        {"type": "grid", "columns": 1, "square": False},
        "cards",
        [{"domain": d, "area": comodo["area"], "options": {
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


def etiquetas(comodo: dict) -> list[dict]:
    return [{"type": "entity", "entity": comodo[k]}
            for k in ("temperatura", "umidade") if comodo.get(k)]


# --------------------------------------------------------------------------- #
#  Secoes
# --------------------------------------------------------------------------- #
def secao_resumo(cfg: dict) -> dict:
    url = cfg["painel"]["url"]
    acesas = "states.light | selectattr('state', 'eq', 'on') | list | count"
    abertas = (
        "states.cover | rejectattr('state', 'eq', 'closed') "
        "| rejectattr('state', 'eq', 'unavailable') | list | count"
    )

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
         "tap_action": ({"action": "navigate", "navigation_path": f"/{url}/luzes"}
                        if cfg["painel"].get("view_luzes", True) else {"action": "none"})},
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

    return {
        "type": "grid",
        "column_span": cfg["painel"].get("colunas_max", 4),
        "cards": [
            titulo(cfg["painel"].get("titulo", "Casa"), "mdi:home-heart"),
            {"type": "custom:mushroom-chips-card", "alignment": "center",
             "chips": chips, "grid_options": {"columns": "full"}},
        ],
    }


def secao_comodo(comodo: dict, cfg: dict, indice: int) -> dict:
    """Bloco do comodo na tela principal: resumo, nao central de controle.

    Ordem fixa para o olho aprender o padrao:
      titulo -> mestre de luz -> um botao por luminaria -> persianas -> sensores.
    """
    cor = cor_do_comodo(comodo, indice)
    cabecalho = titulo(comodo["area"], comodo.get("icone", "mdi:home"),
                       badges=etiquetas(comodo), tap_action=_acao_abrir(comodo, cfg))

    cards = [cabecalho, mestre_de_luz(
        comodo, cfg, cor,
        com_cor=bool(cfg["painel"].get("cor_na_tela_inicial", True)))]

    if cfg["painel"].get("estilo_luzes", "botoes") == "cards":
        cards.append(cards_de_luz(comodo, cfg,
                                  cfg["painel"].get("colunas_luzes", 2), com_cor=False))
    else:
        cards.append(botoes_de_luz(comodo, cfg))

    if cfg["painel"].get("mostrar_persianas", True):
        cards.append(cards_de_persiana(comodo, colunas=1, com_posicao=False))
    if cfg["painel"].get("mostrar_sensores", True):
        cards.append(cards_de_sensor(comodo))

    extras = comodo.get("extras") or []
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
def view_casa(cfg: dict) -> dict:
    return {
        "title": cfg["painel"].get("titulo", "Casa"),
        "path": "casa",
        "icon": "mdi:home",
        "type": "sections",
        "max_columns": cfg["painel"].get("colunas_max", 4),
        "dense_section_placement": bool(cfg["painel"].get("densidade", True)),
        "sections": [secao_resumo(cfg)]
        + [secao_comodo(c, cfg, i) for i, c in enumerate(cfg["comodos"])],
    }


def view_luzes(cfg: dict) -> dict:
    """Controle fino: toda luminaria da casa com slider, agrupada por comodo."""
    secoes = []
    for i, comodo in enumerate(cfg["comodos"]):
        cor = cor_do_comodo(comodo, i)
        secoes.append({"type": "grid", "cards": [
            titulo(comodo["area"], comodo.get("icone", "mdi:home"),
                   tap_action=_acao_abrir(comodo, cfg)),
            mestre_de_luz(comodo, cfg, cor),
            cards_de_luz(comodo, cfg, colunas=1, com_cor=True),
        ]})
    return {
        "title": "Luzes",
        "path": "luzes",
        "icon": "mdi:lightbulb-group",
        "type": "sections",
        "max_columns": cfg["painel"].get("colunas_max", 4),
        "dense_section_placement": True,
        "sections": secoes,
    }


def view_comodo(comodo: dict, cfg: dict, indice: int) -> dict:
    """O ambiente completo: tudo que existe naquele comodo, seccionado."""
    area = comodo["area"]
    cor = cor_do_comodo(comodo, indice)

    secoes = [
        {"type": "grid", "cards": [
            titulo("Iluminação", "mdi:lightbulb-group"),
            mestre_de_luz(comodo, cfg, cor),
            cards_de_luz(comodo, cfg, colunas=1, com_cor=True),
        ]},
        {"type": "grid", "cards": [
            titulo("Persianas e cortinas", "mdi:window-shutter"),
            cards_de_persiana(comodo, colunas=1, com_posicao=True),
        ]},
        {"type": "grid", "cards": [
            titulo("Clima", "mdi:thermostat"),
            cards_por_dominio(area, DOMINIOS_CLIMA),
        ]},
        {"type": "grid", "cards": [
            titulo("Sensores", "mdi:gauge"),
            cards_por_dominio(area, DOMINIOS_SENSOR, colunas=2, vertical=True),
        ]},
        {"type": "grid", "cards": [
            titulo("Mídia e outros", "mdi:dots-horizontal"),
            cards_por_dominio(area, DOMINIOS_OUTROS),
        ]},
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
RESERVADOS = {"casa", "luzes"}


def validar(cfg: dict) -> list[str]:
    erros: list[str] = []

    if not isinstance(cfg.get("painel"), dict):
        erros.append("config: bloco 'painel' ausente ou invalido")
    elif not cfg["painel"].get("url"):
        erros.append("config: 'painel.url' e obrigatorio")

    estilo = (cfg.get("painel") or {}).get("estilo_luzes", "botoes")
    if estilo not in ("botoes", "cards"):
        erros.append(f"config: 'painel.estilo_luzes' deve ser 'botoes' ou 'cards' (veio '{estilo}')")

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
            erros.append(f"comodo #{i} ('{comodo['area']}') gera o mesmo caminho "
                         f"'{caminho}' do comodo #{vistos[caminho]} — renomeie um deles")
        vistos[caminho] = i
        if caminho in RESERVADOS:
            erros.append(f"comodo #{i} ('{comodo['area']}'): o caminho '{caminho}' e "
                         "reservado pelo painel — renomeie a area")
        cor = comodo.get("cor")
        if cor and cor not in PALETA:
            erros.append(f"comodo #{i} ('{comodo['area']}'): cor '{cor}' desconhecida. "
                         f"Use uma de: {', '.join(PALETA)}")
        grupo = comodo.get("grupo")
        if grupo and not str(grupo).startswith("light."):
            erros.append(f"comodo #{i} ('{comodo['area']}'): 'grupo' precisa ser uma "
                         f"entidade light.* (veio '{grupo}')")
    return erros


# --------------------------------------------------------------------------- #
#  Main
# --------------------------------------------------------------------------- #
def montar(cfg: dict) -> dict:
    views = [view_casa(cfg)]
    if cfg["painel"].get("view_luzes", True):
        views.append(view_luzes(cfg))
    if cfg["painel"].get("subviews", True):
        views += [view_comodo(c, cfg, i) for i, c in enumerate(cfg["comodos"])]
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
    print(f"  {len(cfg['comodos'])} comodo(s), {len(painel['views'])} view(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
