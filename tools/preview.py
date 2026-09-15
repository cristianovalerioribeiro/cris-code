#!/usr/bin/env python3
"""
Desenha o painel numa pagina HTML e tira fotos dele em varias larguras.

    python3 tools/preview.py                 # gera HTML + PNG de todas as telas
    python3 tools/preview.py --so-html       # so o HTML (abre no navegador)
    python3 tools/preview.py --view casa --larguras 1440

Serve para conferir a usabilidade ANTES de instalar no Home Assistant: e uma
aproximacao fiel do tema escuro do HA com os cards Mushroom, alimentada pela
casa de exemplo em config/casa_exemplo.yaml.

Nao e o Home Assistant: fontes e espacamentos sao proximos, nao identicos.
"""

from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ha_mock import Casa  # noqa: E402
from ha_mock import Entidade  # noqa: E402
from ha_mock import expandir_auto_entities  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent


def curto(caminho: Path) -> str:
    """Caminho relativo a raiz do projeto quando possivel; absoluto quando nao."""
    try:
        return str(caminho.resolve().relative_to(RAIZ))
    except ValueError:
        return str(caminho)
ICONES = json.loads((RAIZ / "tools" / "icones.json").read_text(encoding="utf-8"))

CORES = {
    "amber": "255,152,0",
    "red": "244,67,54",
    "green": "76,175,80",
    "blue": "33,150,243",
    "purple": "156,39,176",
    "teal": "0,150,136",
    "orange": "255,152,0",
    "pink": "233,30,99",
    "indigo": "63,81,181",
    "cyan": "0,188,212",
    "yellow": "255,235,59",
    "grey": "158,158,158",
    "disabled": "110,110,110",
}

CSS = """
*,*::before,*::after{box-sizing:border-box}
body{margin:0;background:#111213;color:#e1e1e1;
 font-family:Roboto,-apple-system,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased}
.topo{width:100%;position:sticky;top:0;z-index:9;background:#1c1c1c;border-bottom:1px solid #2a2a2a;
 display:flex;align-items:center;gap:14px;padding:0 16px;height:56px}
.topo .titulo{font-size:20px;font-weight:400}
.abas{display:flex;gap:4px;margin-left:auto;overflow:auto}
.aba{padding:6px 14px;border-radius:16px;font-size:13px;color:#9b9b9b;white-space:nowrap}
.aba.ativa{color:#03a9f4;background:rgba(3,169,244,.12)}
.regua{font-size:11px;color:#6f6f6f;padding:6px 16px;border-bottom:1px solid #2a2a2a;
 letter-spacing:.4px;text-transform:uppercase}

.vista{padding:16px 12px 48px}
.secoes{columns:var(--cols,4) 300px;column-gap:16px;margin:0 auto}
.secoes>.secao{break-inside:avoid;margin:0 0 28px}
.secoes>.secao.larga{column-span:all;margin-bottom:20px}
.secao{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:8px;align-content:start}
.item{grid-column:span 6;min-width:0}
.item.full{grid-column:span 12}

/* ---- heading ---- */
.h{display:flex;align-items:center;gap:8px;padding:6px 2px 2px;grid-column:span 12}
.h .txt{font-size:16px;font-weight:500;color:#e1e1e1}
.h.sub .txt{font-size:14px;color:#c9c9c9}
.h svg{width:18px;height:18px;fill:#9b9b9b;flex:none}
.h .badges{margin-left:auto;display:flex;gap:6px}
.badge{display:flex;align-items:center;gap:4px;background:#242424;border-radius:14px;
 padding:3px 9px;font-size:12px;color:#c9c9c9;white-space:nowrap}
.badge svg{width:13px;height:13px;fill:#9b9b9b}

/* ---- cards ---- */
.card{background:#1c1c1c;border-radius:12px;padding:12px;min-width:0}
.linha{display:flex;align-items:center;gap:12px;min-width:0}
.col{display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center}
.forma{width:42px;height:42px;border-radius:50%;display:flex;align-items:center;
 justify-content:center;flex:none}
.forma svg{width:22px;height:22px}
.txts{min-width:0;flex:1}
.nome{font-size:14px;font-weight:500;color:#e1e1e1;white-space:nowrap;overflow:hidden;
 text-overflow:ellipsis}
.sec{font-size:12px;color:#9b9b9b;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.col .txts{width:100%;text-align:center}

.slider{margin-top:10px;height:42px;border-radius:12px;position:relative;overflow:hidden}
.slider .fill{position:absolute;inset:0 auto 0 0;border-radius:12px}
.slider .lbl{position:absolute;inset:0;display:flex;align-items:center;padding:0 12px;
 font-size:13px;font-weight:500;color:#fff;mix-blend-mode:difference}

.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips.centro{justify-content:center}
.chip{height:36px;border-radius:18px;background:#1c1c1c;display:flex;align-items:center;
 gap:6px;padding:0 8px;font-size:13px;color:#e1e1e1}
.chip.so-icone{width:36px;padding:0;justify-content:center}
.chip svg{width:19px;height:19px}

.grade{display:grid;gap:8px}
.slider.ctemp{margin-top:0;background:linear-gradient(90deg,#ffb765,#fff,#9ec6ff)}
.roda{width:42px;height:42px;border-radius:12px;flex:none;display:flex;align-items:center;
 justify-content:center;background:conic-gradient(#f44,#fd0,#4f4,#0ff,#44f,#f4f,#f44)}
.roda svg{width:20px;height:20px}
.grade>*{grid-column:auto!important}
.slider .lbl{mix-blend-mode:normal;color:#1a1a1a;text-shadow:0 0 2px rgba(255,255,255,.35)}
.vazio{font-size:12px;color:#5a5a5a;font-style:italic;padding:4px 2px;grid-column:span 12}
"""

JS_NADA = ""


# --------------------------------------------------------------------------- #
#  Helpers de desenho
# --------------------------------------------------------------------------- #
def svg(nome: str, cor: str = "currentColor") -> str:
    d = ICONES.get(nome) or ICONES.get("mdi:lightbulb")
    return f'<svg viewBox="0 0 24 24"><path fill="{cor}" d="{d}"/></svg>'


def rgb(nome: str) -> str:
    return CORES.get((nome or "").strip(), CORES["disabled"])


def esc(t) -> str:
    return html.escape(str(t if t is not None else ""))


def icone_de(ent: Entidade) -> str:
    d, cls = ent.dominio, (ent.classe or "")
    if d == "light":
        n = ent.name.lower()
        if "fita" in n or "led" in n or "backlight" in n:
            return "mdi:led-strip-variant"
        if "abajur" in n or "luminaria" in n:
            return "mdi:floor-lamp"
        if "arandela" in n:
            return "mdi:wall-sconce-flat"
        if "teto" in n or "plafon" in n or "spot" in n or "lustre" in n:
            return "mdi:ceiling-light"
        return "mdi:lightbulb"
    if d == "cover":
        n = ent.name.lower()
        if "cortina" in n:
            return "mdi:curtains"
        if "blackout" in n:
            return "mdi:blinds-horizontal"
        return "mdi:window-shutter"
    if d == "binary_sensor":
        return {"motion": "mdi:motion-sensor", "window": "mdi:window-closed-variant",
                "door": "mdi:door", "gas": "mdi:gas-cylinder"}.get(cls, "mdi:eye")
    if d == "sensor":
        if "%" in ent.unidade:
            return "mdi:water-percent"
        if "C" in ent.unidade:
            return "mdi:thermometer"
        return "mdi:gauge"
    return {"climate": "mdi:air-conditioner", "fan": "mdi:fan",
            "media_player": "mdi:television", "switch": "mdi:toggle-switch-variant",
            "lock": "mdi:door"}.get(d, "mdi:dots-horizontal")


def cor_de(ent: Entidade) -> str:
    if ent.dominio == "sensor":
        return "blue" if "C" in ent.unidade else "cyan"
    if not ent.ligada:
        return "disabled"
    return {"light": "amber", "cover": "blue", "binary_sensor": "red",
            "climate": "teal", "fan": "green", "media_player": "indigo",
            "switch": "green"}.get(ent.dominio, "amber")


def texto_estado(ent: Entidade) -> str:
    d = ent.dominio
    if d == "light":
        if ent.ligada and ent.dimeriza and ent.brilho:
            return f"{ent.brilho}%"
        return "Acesa" if ent.ligada else "Apagada"
    if d == "cover":
        if ent.posicao >= 100:
            return "Aberta"
        if ent.posicao <= 0:
            return "Fechada"
        return f"Aberta {ent.posicao}%"
    if d == "sensor":
        return f"{ent.state}{' ' + ent.unidade if ent.unidade else ''}"
    if d == "binary_sensor":
        pares = {"motion": ("Detectado", "Sem movimento"), "window": ("Aberta", "Fechada"),
                 "door": ("Aberta", "Fechada"), "gas": ("Detectado", "Normal")}
        sim, nao = pares.get(ent.classe, ("Ativo", "Inativo"))
        return sim if ent.state == "on" else nao
    return {"cool": "Refrigerando", "heat": "Aquecendo", "playing": "Tocando",
            "on": "Ligado", "off": "Desligado", "open": "Aberto",
            "closed": "Fechado"}.get(ent.state, ent.state)


# --------------------------------------------------------------------------- #
#  Renderizador
# --------------------------------------------------------------------------- #
class Desenho:
    def __init__(self, casa: Casa):
        self.casa = casa

    # -- cards ------------------------------------------------------------- #
    def card(self, c: dict) -> str:
        if not isinstance(c, dict):
            return ""
        t = c.get("type", "")
        if t == "custom:auto-entities":
            interno = expandir_auto_entities(c, self.casa)
            return self.card(interno) if interno else ""
        fn = {
            "heading": self.heading,
            "grid": self.grid,
            "tile": self.tile,
            "custom:mushroom-light-card": self.luz,
            "custom:mushroom-template-card": self.template,
            "custom:mushroom-chips-card": self.chips,
            "custom:mushroom-cover-card": self.persiana,
        }.get(t)
        return fn(c) if fn else f'<div class="card item full"><div class="sec">{esc(t)}</div></div>'

    def heading(self, c: dict) -> str:
        cls = "h sub" if c.get("heading_style") == "subtitle" else "h"
        badges = ""
        for b in c.get("badges") or []:
            ent = self.casa.por_id.get(b.get("entity", ""))
            if not ent:
                continue
            badges += (f'<span class="badge">{svg(icone_de(ent), "#9b9b9b")}'
                       f"{esc(texto_estado(ent))}</span>")
        if badges:
            badges = f'<span class="badges">{badges}</span>'
        ic = svg(c.get("icon", "mdi:home"), "#9b9b9b") if c.get("icon") else ""
        return f'<div class="{cls}">{ic}<span class="txt">{esc(c.get("heading",""))}</span>{badges}</div>'

    def grid(self, c: dict) -> str:
        n = int(c.get("columns", 2) or 2)
        filhos = "".join(self.card(f) for f in (c.get("cards") or []))
        if not filhos:
            return ""
        span = "full" if (c.get("grid_options") or {}).get("columns") == "full" else ""
        return (f'<div class="item {span}"><div class="grade" '
                f'style="grid-template-columns:repeat({n},minmax(0,1fr))">{filhos}</div></div>')

    def _bloco(self, ic: str, cor: str, nome: str, sec: str, vertical: bool,
               extra: str = "", span: str = "") -> str:
        r = rgb(cor)
        forma = (f'<div class="forma" style="background:rgba({r},.2)">'
                 f'{svg(ic, f"rgb({r})")}</div>')
        txt = f'<div class="txts"><div class="nome">{esc(nome)}</div>' \
              f'<div class="sec">{esc(sec)}</div></div>'
        corpo = (f'<div class="col">{forma}{txt}</div>' if vertical
                 else f'<div class="linha">{forma}{txt}</div>')
        return f'<div class="card item {span}">{corpo}{extra}</div>'

    def luz(self, c: dict) -> str:
        ent = self.casa.por_id.get(c.get("entity", ""))
        if not ent:
            return ""
        vertical = c.get("layout") == "vertical"
        cor = "amber" if ent.ligada else "disabled"
        slider = ""
        # O mushroom-light-card so desenha o slider se a lampada aceitar brilho.
        # Lampada comum de liga/desliga fica com o card de uma linha so.
        mostrar = (c.get("show_brightness_control") and ent.dimeriza
                   and (ent.ligada or not c.get("collapsible_controls", True)))
        if mostrar:
            r = rgb("amber")
            largura = ent.brilho if ent.ligada else 0
            slider = (f'<div class="slider" style="background:rgba({r},.2)">'
                      f'<div class="fill" style="width:{largura}%;background:rgb({r})"></div>'
                      f'<div class="lbl">{largura}%</div></div>')
            # controle de cor: barra de temperatura + botao de roda de cores
            if ent.ligada and (c.get("show_color_temp_control") or c.get("show_color_control")):
                partes = ""
                if c.get("show_color_temp_control"):
                    partes += ('<div class="slider ctemp" style="flex:1"></div>')
                if c.get("show_color_control"):
                    partes += '<div class="roda">' + svg("mdi:palette", "#fff") + "</div>"
                slider += f'<div class="linha" style="margin-top:8px;gap:8px">{partes}</div>' 
        span = "full" if (c.get("grid_options") or {}).get("columns") == "full" else ""
        return self._bloco(icone_de(ent), cor, ent.name, texto_estado(ent),
                           vertical, slider, span)

    def persiana(self, c: dict) -> str:
        ent = self.casa.por_id.get(c.get("entity", ""))
        if not ent:
            return ""
        r = rgb("blue")
        botoes = "".join(
            f'<div class="chip so-icone" style="background:rgba({r},.15)">'
            f'{svg(i, f"rgb({r})")}</div>'
            for i in ("mdi:arrow-up", "mdi:stop", "mdi:arrow-down"))
        barra = ""
        if c.get("show_position_control"):
            barra = (f'<div class="slider" style="background:rgba({r},.2)">'
                     f'<div class="fill" style="width:{ent.posicao}%;background:rgb({r})">'
                     f'</div><div class="lbl">{ent.posicao}%</div></div>')
        span = "full" if (c.get("grid_options") or {}).get("columns") == "full" else ""
        vertical = c.get("layout") == "vertical"
        if vertical:
            extra = f'<div class="chips" style="margin-top:10px">{botoes}</div>{barra}'
            return self._bloco(icone_de(ent), cor_de(ent), ent.name,
                               texto_estado(ent), True, extra, span)
        # horizontal: botoes na mesma linha do nome, card com altura de uma linha
        forma = (f'<div class="forma" style="background:rgba({r},.2)">'
                 f'{svg(icone_de(ent), f"rgb({r})")}</div>')
        txt = (f'<div class="txts"><div class="nome">{esc(ent.name)}</div>'
               f'<div class="sec">{esc(texto_estado(ent))}</div></div>')
        return (f'<div class="card item {span}"><div class="linha">{forma}{txt}'
                f'<div class="chips" style="flex:none">{botoes}</div></div>{barra}</div>')

    def template(self, c: dict) -> str:
        r = self.casa.render
        span = "full" if (c.get("grid_options") or {}).get("columns") == "full" else ""
        return self._bloco(r(c.get("icon", "mdi:home")), r(c.get("icon_color", "grey")),
                           r(c.get("primary", "")), r(c.get("secondary", "")),
                           False, "", span)

    def chips(self, c: dict) -> str:
        saida = ""
        for ch in c.get("chips") or []:
            if ch.get("type") == "template":
                cor = self.casa.render(ch.get("icon_color", "grey"))
                txt = self.casa.render(ch.get("content", ""))
                ic = self.casa.render(ch.get("icon", "mdi:lightbulb"))
            else:
                ent = self.casa.por_id.get(ch.get("entity", ""))
                if not ent:
                    continue
                cor, ic = cor_de(ent), icone_de(ent)
                info = ch.get("content_info", "state")
                txt = {"none": "", "name": ent.name}.get(info, texto_estado(ent))
            r = rgb(cor)
            cls = "chip so-icone" if not txt else "chip"
            saida += (f'<div class="{cls}">{svg(ic, f"rgb({r})")}'
                      f'{f"<span>{esc(txt)}</span>" if txt else ""}</div>')
        if not saida:
            return ""
        al = "centro" if c.get("alignment") == "center" else ""
        span = "full" if (c.get("grid_options") or {}).get("columns") == "full" else ""
        return f'<div class="item {span}"><div class="chips {al}">{saida}</div></div>'

    def tile(self, c: dict) -> str:
        ent = self.casa.por_id.get(c.get("entity", ""))
        if not ent:
            return ""
        span = "full" if (c.get("grid_options") or {}).get("columns") == "full" else ""
        return self._bloco(icone_de(ent), cor_de(ent), ent.name, texto_estado(ent),
                           bool(c.get("vertical")), "", span)

    # -- estrutura --------------------------------------------------------- #
    def secao(self, s: dict, max_cols: int) -> str:
        cards = "".join(self.card(c) for c in (s.get("cards") or []))
        # column_span so importa para ocupar a largura toda. Usar "span N" criaria
        # colunas implicitas quando a tela cabe menos que N, estourando a pagina.
        larga = " larga" if s.get("column_span") else ""
        return f'<div class="secao{larga}">{cards}</div>'

    def vista(self, v: dict) -> str:
        mc = int(v.get("max_columns", 4) or 4)
        secoes = "".join(self.secao(s, mc) for s in (v.get("sections") or []))
        return (f'<div class="vista"><div class="secoes" '
                f'style="--cols:{mc};max-width:{mc * 420}px">{secoes}</div></div>')


# --------------------------------------------------------------------------- #
#  Pagina
# --------------------------------------------------------------------------- #
def pagina(dash: dict, casa: Casa, path: str, largura: int) -> str:
    views = dash.get("views") or []
    atual = next((v for v in views if v.get("path") == path), None)
    if atual is None:
        raise SystemExit(f"erro: view '{path}' nao existe no painel")

    abas = "".join(
        f'<div class="aba{" ativa" if v.get("path") == path else ""}">{esc(v.get("title"))}</div>'
        for v in views if not v.get("subview")
    )
    marca = "SUBVIEW (pagina do comodo)" if atual.get("subview") else "VIEW PRINCIPAL"
    corpo = Desenho(casa).vista(atual)

    return f"""<!doctype html><html lang="pt-br"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(atual.get('title'))} — {largura}px</title><style>{CSS}</style></head><body>
<div class="topo"><span class="titulo">{esc(atual.get('title'))}</span><div class="abas">{abas}</div></div>
<div class="regua">{marca} &nbsp;·&nbsp; simulacao {largura}px &nbsp;·&nbsp; path /{esc(path)}</div>
{corpo}
<script>{JS_NADA}</script></body></html>"""


# Chromium ja vem instalado no ambiente; a versao pode nao bater com a do pacote
# playwright, entao apontamos o binario explicitamente em vez de baixar outro.
CHROMIUMS = [
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell",
]


def achar_chromium() -> str | None:
    import glob

    for padrao in ("/opt/pw-browsers/chromium-*/chrome-linux/chrome",
                   "/opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell"):
        achados = sorted(glob.glob(padrao))
        if achados:
            return achados[-1]
    return None


def fotografar(htmls: dict[Path, int], destino: Path) -> list[Path]:
    from playwright.sync_api import sync_playwright

    feitas = []
    destino.mkdir(parents=True, exist_ok=True)
    binario = achar_chromium()
    with sync_playwright() as pw:
        nav = pw.chromium.launch(executable_path=binario) if binario else pw.chromium.launch()
        for arq, largura in htmls.items():
            pg = nav.new_page(viewport={"width": largura, "height": 900},
                              device_scale_factor=1)
            pg.goto(arq.as_uri())
            pg.wait_for_timeout(120)
            png = destino / (arq.stem + ".png")
            pg.screenshot(path=str(png), full_page=True)
            feitas.append(png)
            pg.close()
        nav.close()
    return feitas


ALVOS_PADRAO = [("terreo", 1440), ("terreo", 820), ("terreo", 390),
                ("2o-pav-intimo", 1440), ("2o-pav-escritorio", 1440),
                ("casa", 1440), ("suite", 390)]

# Mede quanto de cada coluna fica vazio. Blocos de comodo nao se dividem entre
# colunas, entao comodos de tamanhos muito diferentes deixam sobra no pe das
# colunas mais curtas. Menos colunas costuma equilibrar melhor.
MEDIR_JS = """() => {
  const secs = [...document.querySelectorAll('.secoes>.secao:not(.larga)')];
  if (!secs.length) return null;
  const cols = {};
  secs.forEach(s => { const r = s.getBoundingClientRect();
    const k = Math.round(r.left); (cols[k] = cols[k] || []).push(r); });
  const grupos = Object.values(cols);
  const alturas = grupos.map(rs => Math.max(...rs.map(r => r.bottom))
                                 - Math.min(...rs.map(r => r.top)));
  const usado = grupos.reduce((a, rs) => a + rs.reduce((b, r) => b + r.height, 0), 0);
  const maior = Math.max(...alturas);
  return { colunas: alturas.length, pagina: Math.round(document.body.scrollHeight),
           vazio: Math.round(100 * (1 - usado / (maior * alturas.length))) };
}"""


def medir(htmls: dict[Path, int]) -> None:
    from playwright.sync_api import sync_playwright

    binario = achar_chromium()
    print("\nespaco vazio nas colunas (quanto menor, melhor):")
    with sync_playwright() as pw:
        nav = pw.chromium.launch(executable_path=binario) if binario else pw.chromium.launch()
        for arq, largura in htmls.items():
            pg = nav.new_page(viewport={"width": largura, "height": 900})
            pg.goto(arq.as_uri())
            m = pg.evaluate(MEDIR_JS)
            if m:
                print(f"  {arq.stem:22} {m['colunas']} coluna(s), "
                      f"pagina {m['pagina']}px, {m['vazio']}% vazio")
            pg.close()
        nav.close()


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Pre-visualiza o painel.")
    p.add_argument("--painel", type=Path, default=RAIZ / "dashboards" / "painel-novo.yaml")
    p.add_argument("--casa", type=Path, default=RAIZ / "config" / "casa_exemplo.yaml")
    p.add_argument("--saida", type=Path, default=RAIZ / "preview")
    p.add_argument("--view", action="append", help="path da view (pode repetir)")
    p.add_argument("--larguras", type=int, nargs="*", help="larguras em px")
    p.add_argument("--so-html", action="store_true", help="nao tira screenshots")
    p.add_argument("--metricas", action="store_true",
                   help="mede quanto de espaco vazio sobra nas colunas")
    args = p.parse_args(argv)

    dash = yaml.safe_load(args.painel.read_text(encoding="utf-8"))
    casa = Casa.carregar(args.casa)

    if args.view or args.larguras:
        vistas = args.view or ["casa"]
        larguras = args.larguras or [1440]
        alvos = [(v, w) for v in vistas for w in larguras]
    else:
        alvos = ALVOS_PADRAO

    args.saida.mkdir(parents=True, exist_ok=True)
    htmls: dict[Path, int] = {}
    for path, largura in alvos:
        arq = args.saida / f"{path}-{largura}.html"
        arq.write_text(pagina(dash, casa, path, largura), encoding="utf-8")
        htmls[arq] = largura
        print(f"html: {curto(arq)}")

    if not args.so_html:
        for png in fotografar(htmls, args.saida):
            print(f"png : {curto(png)}")
    if args.metricas:
        medir(htmls)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
