# -*- coding: utf-8 -*-
"""Gera Graficos_para_Impressao_Negocios.pdf: só os gráficos, dois por folha A4 (meia folha cada), listas em paisagem, silhuetas em página inteira."""
import os, re, json, sys, html as H
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE); sys.path.insert(0, HERE)
import gen_charts
from interp import INTERP

# ---- 1) charts_land: todos os gráficos (os reaproveitados copiados, os novos gerados) e as listas regeneradas em paisagem pelo motor do manual terapêutico ----
LAND = os.path.join(HERE, "charts_land"); os.makedirs(LAND, exist_ok=True)
import math, shutil, importlib.util
gen_charts.OUT = LAND
gen_charts.build()
gen_charts.OUT = os.path.join(HERE, "charts")
def _land_lists():
    spec = importlib.util.spec_from_file_location("rgen", os.path.join(os.path.dirname(HERE), "radiestesia", "gen_charts.py"))
    rg = importlib.util.module_from_spec(spec); spec.loader.exec_module(rg)
    _orig = rg.list_chart
    def _list_land(items, groups=None, cols=2, w=190, row_h=7.2, font=3.3, header_colors=None, max_h=226, **kw):
        n = len(items) + (len(groups) if groups else 0); maxlen = max(len(t) for t in items)
        best = None
        for c in (2, 3, 4):
            rows = math.ceil(n / c) + 1; rh = min(13.0, 162 / rows); cw = 267 / c
            f = min(6.0, rh * 0.5, (cw - 19) / (maxlen * 0.52))
            if best is None or f > best[0] + 0.05: best = (f, c)
        return _orig(items, groups=groups, cols=best[1], w=277, max_h=172, max_row=13.0, max_font=6.0)
    rg.list_chart = _list_land
    tmp = os.path.join(HERE, "pages", "land_tmp"); os.makedirs(tmp, exist_ok=True); rg.OUT = tmp; rg.build()
    for f in os.listdir(tmp):
        if f.endswith(".svg") and os.path.exists(os.path.join(HERE, "charts", f)): shutil.copy(os.path.join(tmp, f), os.path.join(LAND, f))
    shutil.rmtree(tmp, ignore_errors=True)
_land_lists()

man = json.load(open("charts/manifest.json"))
by_id = {m["id"]: m for m in man}
livro = open("livro.html", encoding="utf-8").read()

# ---- 2) ordem do manual e seção de cada gráfico ----
order, section = [], {}
for mm in re.finditer(r'<h1[^>]*>(.*?)</h1>|<h2[^>]*>(.*?)</h2>|id="fig-([^"]+)"', livro):
    if mm.group(1): cur_h1 = re.sub("<.*?>", "", mm.group(1)); cur = cur_h1
    elif mm.group(2): cur = re.sub("<.*?>", "", mm.group(2))
    elif mm.group(3) and mm.group(3) not in section:
        order.append(mm.group(3)); section[mm.group(3)] = cur
for m in man:
    if m["id"] not in section: order.append(m["id"]); section[m["id"]] = "Outros"

FULL_PORTRAIT = {"G6", "G6b", "G13", "G29", "G72", "G73", "G69", "G56"}
def mode(cid):
    k = by_id[cid]["kind"]
    if k == "lista" or cid == "G56": return "land"
    if cid in FULL_PORTRAIT or k in ("silhueta", "grade", "rosa", "réguas"): return "full"
    return "half"

def perg(cid):
    it = INTERP.get(cid); p = it.get("pergunta") if it else None
    if not p: return ""
    if isinstance(p, str): p = [p]
    return " · ".join(f"“{q}”" for q in p[:2])

def card(cid, src="charts"):
    m = by_id[cid]
    return (f'<div class="card"><div class="head"><span class="id">{cid}</span><span class="title">{H.escape(m["title"])}</span>'
            f'<span class="sec">{H.escape(section[cid])}</span></div>'
            f'<div class="imgbox"><img src="{src}/{m["file"]}"/></div>'
            f'<div class="perg">{H.escape(perg(cid))}</div></div>')

# ---- 3) pares de meia folha ----
halves = [c for c in order if mode(c) == "half"]
pages, i = [], 0
while i < len(halves):
    a = halves[i]; b = halves[i + 1] if i + 1 < len(halves) else None
    tem = bool(b) and (section[a] == section[b] or (a[0] == 'C' and b[0] == 'C' and a[:2] == b[:2]))
    pages.append(("half", a, b, tem)); i += 2
fulls = [c for c in order if mode(c) == "full"]
lands = [c for c in order if mode(c) == "land"]

# ---- 4) HTML ----
CSS = """
@page { size: A4 portrait; margin: 0; }
@page land { size: A4 landscape; margin: 0; }
body { font-family: Inter, 'DejaVu Sans', sans-serif; margin: 0; color: #111; }
.sheet { width: 210mm; height: 297mm; position: relative; page-break-after: always; overflow: hidden; }
.sheet.land { page: land; width: 297mm; height: 210mm; }
.half { position: absolute; left: 0; width: 210mm; height: 148.5mm; box-sizing: border-box; padding: 7mm 10mm 5mm 10mm; }
.half.top { top: 0; } .half.bottom { top: 148.5mm; }
.cut { position: absolute; top: 148.5mm; left: 0; width: 210mm; border-top: 0.4pt dashed #888; }
.cutlabel { position: absolute; top: 145.2mm; right: 6mm; font-size: 6.5pt; color: #777; background: white; padding: 0 2mm; }
.card { height: 100%; display: flex; flex-direction: column; }
.head { display: flex; align-items: baseline; gap: 4mm; border-bottom: 1pt solid #111; padding-bottom: 1.2mm; margin-bottom: 1.5mm; }
.id { font-weight: 800; font-size: 13pt; color: #1f4e8c; } .title { font-weight: 600; font-size: 10pt; flex: 1; } .sec { font-size: 7pt; color: #666; }
.imgbox { flex: 1; display: flex; align-items: center; justify-content: center; overflow: hidden; }
.imgbox img { max-width: 190mm; max-height: 118mm; width: auto; height: auto; }
.full .imgbox img { max-height: 262mm; }
.land .card { padding: 7mm 10mm 5mm 10mm; box-sizing: border-box; }
.land .imgbox img { max-width: 277mm; max-height: 178mm; }
.perg { font-size: 7.5pt; color: #1f4e8c; font-style: italic; margin-top: 1mm; }
.fullpage { position: absolute; inset: 0; padding: 8mm 10mm 6mm 10mm; box-sizing: border-box; }
.index { padding: 10mm 10mm; font-size: 6.5pt; }
.index h1 { font-size: 18pt; margin: 0 0 3mm 0; } .index p { margin: 0 0 3mm 0; }
.index table { border-collapse: collapse; width: 100%; } .index td, .index th { border-bottom: 0.3pt solid #ccc; padding: 0.45mm 1mm; text-align: left; vertical-align: top; }
.index .cols { display: flex; gap: 4mm; align-items: flex-start; } .index .cols table { width: 25%; }
"""
out = []
# índice
rows = []; n_sheet = 0
sheet_of = {}
for kind, a, b, tem in pages:
    n_sheet += 1; sheet_of[a] = f"{n_sheet} · cima"
    if b: sheet_of[b] = f"{n_sheet} · baixo" + (" · par" if tem else "")
for c in fulls: n_sheet += 1; sheet_of[c] = f"{n_sheet} · inteira"
for c in lands: n_sheet += 1; sheet_of[c] = f"{n_sheet} · deitada"
nh = len(pages); f1, f2 = nh + 1, nh + len(fulls); l1, l2 = f2 + 1, f2 + len(lands)
import math as _m
_per = _m.ceil(len(order) / 4)
idx = "".join('<table><thead><tr><th>Nº</th><th>Gráfico</th><th>Folha</th></tr></thead><tbody>' + "".join(f"<tr><td><b>{c}</b></td><td>{H.escape(by_id[c]['title'])}</td><td>{sheet_of[c]}</td></tr>" for c in order[k:k+_per]) + '</tbody></table>' for k in range(0, len(order), _per))
out.append('<div class="sheet"><div class="index"><h1>Gráficos para impressão</h1>'
           f'<p><b>Como está montado.</b> Folhas 1 a {nh}: dois gráficos por folha A4, um em cada metade (cartões A5 após o corte na linha tracejada). Quando os dois gráficos são par da mesma seção, a folha vem marcada “par”: mantenha inteira, sem cortar (emoções e corpo de cada chakra, escalas irmãs, etapas seguidas de um mesmo roteiro). '
           'Folhas {f1} a {f2}: silhuetas, grade e rosa de direções em folha inteira, em pé. Folhas {l1} a {l2}: listas penduláveis em folha inteira deitada, com o número de colunas escolhido para a maior letra. '
           'Cada gráfico traz a pergunta padrão; a interpretação de cada resultado fica no manual (consulta no computador). '
           '<b>Sugestões:</b> papel de 120 g ou mais; plastificar os cartões de uso diário; furar e prender em argolas por seção (a coluna “Folha” segue a ordem do manual); imprimir as folhas deitadas frente e verso para formar um bloco só de listas.</p>'
           f'<div class="cols">{idx}</div></div></div>')
# meias folhas
for kind, a, b, tem in pages:
    out.append('<div class="sheet">' + f'<div class="half top">{card(a)}</div>' +
               (f'<div class="half bottom">{card(b)}</div>' if b else '') +
               '<div class="cut"></div>' + f'<div class="cutlabel">{"par da mesma seção: pode ficar inteira" if tem else "corte aqui"}</div></div>')
for c in fulls:
    out.append(f'<div class="sheet full"><div class="fullpage">{card(c)}</div></div>')
for c in lands:
    out.append(f'<div class="sheet land">{card(c, "charts_land")}</div>')

doc = f"<!DOCTYPE html><html lang='pt-BR'><head><meta charset='utf-8'><title>Gráficos para impressão</title><style>{CSS}</style></head><body>{''.join(out)}</body></html>"
open("graficos_print.html", "w", encoding="utf-8").write(doc)
from weasyprint import HTML
HTML(string=doc, base_url=HERE).write_pdf("Graficos_para_Impressao_Negocios.pdf")
print("folhas:", n_sheet, "| meias:", len(pages), "| inteiras retrato:", len(fulls), "| paisagem:", len(lands), "| pares temáticos:", sum(1 for p in pages if p[3]))
print("PDF:", os.path.getsize("Graficos_para_Impressao_Negocios.pdf") // 1024, "KB")
