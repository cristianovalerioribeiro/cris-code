# -*- coding: utf-8 -*-
"""Edição 8 final: página A4 deitada. Texto corrido em duas colunas (trechos curtos em coluna única); gráficos, listas, pares,
mapa, trilhas, tabelas largas, sumário e índice em largura total. Abas coloridas por Parte na margem direita; paginação no canto externo."""
import os, sys, re, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bookkit
from bookkit import toc_html, TOC, SPAN0, SPAN1
import content_front, content_chakras, content_rest

FONT = "Inter, 'DejaVu Sans', Arial, sans-serif"
GROUPS = [("g0", "", "#1f4e8c"), ("g4", "", "#8e44ad"), ("g5", "", "#c0392b")]
POS = ["right-top", "right-middle", "right-bottom"]

def tabs_css():
    """Abas coloridas na margem direita como elemento corrente (não força quebra ao mudar de Parte); rótulo curto horizontal numa barra alta."""
    out = ["@page { @right-middle { content: element(tab); width: 10mm; margin-left: 1mm; vertical-align: middle; } }",
           f".tab {{ position: running(tab); color: white; font-family: {FONT}; font-size: 7.3pt; font-weight: 700; text-align: center; white-space: nowrap; padding: 24mm 0; border-radius: 1.5mm 0 0 1.5mm; }}"]
    for g, label, color in GROUPS: out.append(f".tab.{g} {{ background: {color}; }}")
    return "\n".join(out)

CSS = r"""
@page { size: A4 landscape; margin: 10mm 11.5mm 10mm 10mm;
  @top-left { content: "Manual de Radiestesia Terapêutica"; font-family: FONT; font-size: 7.5pt; color: #555; vertical-align: bottom; padding-bottom: 1.6mm; }
  @top-right { content: string(chap); font-family: FONT; font-size: 7.5pt; color: #555; vertical-align: bottom; padding-bottom: 1.6mm; } }
@page :right { @bottom-right { content: string(chap) "   ·   " counter(page); font-family: FONT; font-size: 8pt; font-weight: 600; color: #222; border-top: 0.5pt solid #bbb; padding-top: 1mm; width: 100%; text-align: right; } }
@page :left { @bottom-left { content: counter(page) "   ·   " string(chap); font-family: FONT; font-size: 8pt; font-weight: 600; color: #222; border-top: 0.5pt solid #bbb; padding-top: 1mm; width: 100%; text-align: left; } }
@page cover { margin: 0; @top-left { content: none } @top-right { content: none } @bottom-left { content: none } @bottom-right { content: none } @right-middle { content: none } }
@page toc { @top-right { content: "Sumário" } }
TABS
html { font-family: FONT; font-size: 8.2pt; line-height: 1.27; color: #111; hyphens: auto; -weasy-hyphens: auto; hyphenate-limit-chars: 6 3 3; }
body { margin: 0; }
h1 { font-size: 15pt; font-weight: 800; margin: 0 0 4pt 0; string-set: chap content(); color: #111; line-height: 1.1; hyphens: manual; }
h1[data-short] { string-set: chap attr(data-short); }
h2, h3, .chart-head, .chip, th { hyphens: manual; }
h2 { font-size: 10.2pt; font-weight: 700; margin: 6pt 0 2pt 0; color: #1f4e8c; page-break-after: avoid; line-height: 1.15; border-bottom: 0.4pt solid #c9d2e0; padding-bottom: 1pt; }
h3 { font-size: 8.8pt; font-weight: 700; margin: 5pt 0 1.5pt 0; page-break-after: avoid; color: #1f4e8c; }
p { margin: 0 0 3pt 0; text-align: left; }
ul, ol { margin: 0 0 3pt 0; padding-left: 12pt; }
li { margin-bottom: 1.2pt; }
ol.steps > li { margin-bottom: 2pt; }
section.chapter { page-break-before: always; }
section.chapter.flow { page-break-before: auto; margin-top: 9pt; border-top: 1.5pt solid #1f4e8c; padding-top: 5pt; }
.kicker { font-size: 6.8pt; letter-spacing: 1.1pt; text-transform: uppercase; color: #1f4e8c; margin-bottom: 2pt; }
.cols { column-count: 2; column-gap: 9mm; column-rule: 0.3pt solid #d5dce6; margin-bottom: 4pt; }
.cols.one { column-count: auto; column-gap: 0; column-rule: none; width: 64%; }
table.two { width: 100%; border-collapse: collapse; margin: 0 0 3pt 0; page-break-inside: avoid; break-inside: avoid; table-layout: fixed; }
table.two > tbody > tr > td { border: none; padding: 0; vertical-align: top; width: 48%; }
table.two > tbody > tr > td.gap { width: 4%; border: none; }
.one { width: 72%; }
.h2wide { page-break-after: avoid; break-after: avoid; break-inside: avoid; page-break-inside: avoid; } .h2wide h2 { margin-top: 6pt; } .h2wide p { margin-bottom: 2pt; }
.keep { break-inside: avoid; page-break-inside: avoid; }
p, li, td { orphans: 3; widows: 3; }
ol.steps > li:last-child, ul > li:last-child, p.base { page-break-before: avoid; break-before: avoid; }
ol.cont > li:last-child, ul.cont > li:last-child { page-break-before: auto; break-before: auto; }   /* senão o resto da lista puxa a linha do desenho para a página seguinte */
.chapstart { break-inside: avoid; page-break-inside: avoid; }
.chapstart .intro { width: 64%; } .chapstart .intro p { margin-bottom: 3pt; }
.wide-lado { margin-bottom: 2pt; }
td.hrow { padding: 0 0 3pt 0 !important; border: none !important; } td.hrow .h2wide h2 { margin-top: 0; }
ol.steps + ol.steps, ul + ul { margin-top: -2pt; }
.lb .keep { page-break-after: avoid; break-after: avoid; } table.lista.rest { margin-top: -0.6pt; }
.keep { break-inside: avoid; page-break-inside: avoid; }
table { border-collapse: collapse; width: 100%; margin: 2pt 0 4pt 0; font-size: 7.5pt; page-break-inside: auto; line-height: 1.26; }
th, td { border: 0.4pt solid #9a9a9a; padding: 1.6pt 3pt; vertical-align: top; text-align: left; }
th { background: #eef2f7; font-weight: 600; }
tr { page-break-inside: avoid; }
table.legend tbody tr:first-child { page-break-after: avoid; break-after: avoid; } table.legend tbody tr:last-child { page-break-before: avoid; break-before: avoid; }   /* nem cabeçalho + 1 linha no pé, nem 1 linha só na continuação (o motor ignora break-inside em tbody) */
.beside.tfb { margin-top: 0; border-top: none; padding-top: 0; }
table.legend th:first-child { white-space: nowrap; }   /* "G86 · Resultado" numa linha só */   /* duas últimas linhas juntas: nunca sobra uma linha só na continuação */
table.small { font-size: 7pt; }
table.form td { height: 13pt; }
table.grid td { font-size: 8pt; padding: 4pt; }
table.grid.big td { font-size: 8.5pt; height: 18pt; width: 16.6%; }
a { color: #1f4e8c; text-decoration: none; }
a.go { font-weight: 600; }
a.go::after { content: " (p. " target-counter(attr(href), page) ")"; font-weight: 400; color: #444; }
.sym { display: inline-block; font-weight: 700; color: #1f4e8c; }
.pergunta { display: inline; font-style: italic; color: #17407a; background: #eef2f8; padding: 0 3pt; border-radius: 2pt; }
td .pergunta, td .q { background: none; padding: 0; }
p > .pergunta:only-child, div > .pergunta:only-child { display: block; border-left: 2pt solid #1f4e8c; padding: 1pt 5pt; margin: 2pt 0 3pt 0; }
.box { border: 0.6pt solid #1f4e8c; border-radius: 2.5pt; padding: 3pt 6pt; margin: 3pt 0 5pt 0; font-size: 8.2pt; page-break-inside: avoid; break-inside: avoid; }
.box.alerta { border-color: #c62828; }
.box.variacao { border-color: #2e7d32; background: #f3f9f3; }
.box-title { font-weight: 700; font-size: 7pt; text-transform: uppercase; letter-spacing: 0.7pt; margin-bottom: 1.5pt; }
figure { margin: 0; }
div.chart { margin: 3pt 0 5pt 0; }
table.cb { width: 100%; border-collapse: collapse; margin: 0 0 2pt 0; page-break-inside: avoid; }
table.cb > tbody > tr > td, table.cb > tr > td { border: none; padding: 0; vertical-align: top; }
table.cb > tbody > tr > td.l { padding-right: 6mm; }
table.cb > tbody > tr > td.r { padding-top: 1pt; }
table.cb td.l2 { width: 28%; padding-right: 5mm; } table.cb td.r2 { width: 44%; }
div.chart img { width: 100%; display: block; }
div.chart.compact td.l img { width: 82%; }
div.chart.k-lista table.cb td.l img.thumb { width: auto; height: 34mm; border: 0.3pt solid #ccc; }
table.lista { table-layout: fixed; margin: 3pt 0 5pt 0; font-size: 8pt; line-height: 1.2; border-collapse: separate; border-spacing: 2.5mm 0.6pt; width: calc(100% + 5mm); margin-left: -2.5mm; }
table.lista td { border: none; padding: 0; vertical-align: middle; }
table.lista td.lh { font-weight: 700; font-size: 7.5pt; padding: 0.9pt 4pt; border-radius: 2pt; }
table.lista td.li { padding: 0.9pt 4pt; border-left: 2pt solid #9a9a9a; background: #fafbfd; }
table.lista td.li.empty { background: none; border: none; }
.lista .li b { color: #1f4e8c; margin-right: 2pt; }
.lista .dot { display: inline-block; width: 4pt; height: 4pt; border: 0.9pt solid #777; border-radius: 50%; margin-right: 2.5pt; vertical-align: -0.3pt; }
.interp { font-size: 7.7pt; }
.interp p { margin: 1pt 0 2pt 0; }
.interp .q { font-style: italic; color: #17407a; }
.interp .base { color: #444; font-size: 7.2pt; margin-top: 2pt; }
.interp .rota { background: #f3f6fb; border-left: 2pt solid #1f4e8c; padding: 2pt 5pt; margin: 3pt 0; font-size: 7.3pt; }
.interp .vai { display: inline; color: #1f4e8c; font-weight: 600; }
.interp .vai a.go { white-space: nowrap; }
.res1 { margin: 1pt 0 2pt 0; }
.interp .vai a.go::after { font-weight: 400; }
.interp table.legend { margin: 2pt 0 2pt 0; font-size: 7.8pt; }
.interp table.legend td:first-child { font-weight: 600; width: 14%; }
.interp table.legend td:nth-child(2) { width: 36%; }
table.cb td.r table.legend td:first-child { width: 24%; } table.cb td.r table.legend td:nth-child(2) { width: 34%; }
.interp table.legend th.cap { background: #1f4e8c; color: white; font-weight: 700; }
.pi { border-bottom: 0.3pt dashed #bbb; padding-bottom: 3pt; margin-bottom: 3pt; } .pi:last-child { border: none; }
.pi-id { font-weight: 800; color: #1f4e8c; font-size: 9pt; }
.chart-head { display: flex; justify-content: space-between; align-items: baseline; border-bottom: 1pt solid #111; margin-bottom: 3pt; padding-bottom: 1.5pt; }
.chart-id { font-weight: 800; font-size: 11.5pt; color: #1f4e8c; }
.chart-title { font-weight: 600; font-size: 8.8pt; text-align: right; }
.chart-title.long { font-size: 7.6pt; line-height: 1.15; max-width: 72%; }
.chart-note { font-size: 7.4pt; color: #444; margin-top: 2pt; }
table.legend { font-size: 7.3pt; }
table.idx td, table.idx th { padding: 0.8pt 2pt; font-size: 6.6pt; } table.idx a.go::after { content: target-counter(attr(href), page); }
figure.pic { text-align: center; margin: 4pt 0 6pt 0; page-break-inside: avoid; }
figure.pic img { display: inline-block; }
figure.pic.flow img { width: 100%; }
figcaption { font-size: 7.3pt; color: #444; margin-top: 2pt; }
.pb { page-break-before: always; }
.tec { page-break-inside: avoid; break-inside: avoid; margin-bottom: 6pt; }
.trilha { display: flex; flex-wrap: wrap; align-items: center; gap: 1.5pt 2.5pt; margin: 1pt 0 4pt 0; padding: 2pt 4pt; background: #f3f6fb; border-radius: 3pt; font-size: 7.1pt; page-break-inside: avoid; }
.trilha-t { font-weight: 800; text-transform: uppercase; letter-spacing: 0.6pt; font-size: 6.4pt; color: #1f4e8c; margin-right: 3pt; }
.chip { display: inline-block; border: 0.5pt solid #1f4e8c; border-radius: 8pt; padding: 0.5pt 4pt; color: #111; background: white; line-height: 1.2; font-size: 6.8pt; }
.chip b { color: #1f4e8c; }
a.chip::after { content: " · " target-counter(attr(href), page); color: #666; font-size: 6.2pt; }
.arrow { color: #1f4e8c; font-weight: 800; font-size: 9pt; }
.dcard { break-inside: avoid; page-break-inside: avoid; border: 0.5pt solid #b7c3d6; border-radius: 3pt; padding: 4pt 5pt 2pt 5pt; margin: 0 0 6pt 0; background: #fcfdff; }
.dhead { display: flex; gap: 6pt; align-items: flex-start; margin-bottom: 3pt; }
.dhead img.thumb { width: 22mm; display: block; }
.dtxt { flex: 1; } .did { font-weight: 800; color: #1f4e8c; font-size: 8.4pt; } .dtxt .q { font-style: italic; color: #1f4e8c; font-size: 7.3pt; }
.dcard table { margin: 2pt 0 1pt 0; font-size: 6.7pt; } .dcard td:first-child { width: 40%; font-weight: 600; }
.cols.cards { column-count: 4; column-gap: 5mm; }
.card { border: 0.5pt solid #b7c3d6; border-radius: 3pt; padding: 4pt 6pt; margin: 0 0 5pt 0; font-size: 7.5pt; page-break-inside: avoid; break-inside: avoid; }
.card h4 { margin: 0 0 1.5pt 0; font-size: 8.6pt; color: #1f4e8c; }
.card .orig { color: #666; font-size: 6.8pt; margin-bottom: 2pt; }
.card p { margin: 1pt 0; }
.gloss { font-size: 7.3pt; }
.gloss p { margin: 0 0 2pt 0; break-inside: avoid; }
section.cover { page: cover; position: relative; width: 297mm; height: 210mm; color: white; overflow: hidden; }
.cover-bg { position: absolute; left: 0; top: 0; width: 297mm; height: 210mm; }
.cover-text { position: absolute; left: 18mm; top: 24mm; width: 150mm; }
.cover-kicker { font-size: 8pt; letter-spacing: 2.2pt; text-transform: uppercase; color: #e6c36b; }
.cover-title { font-size: 40pt; font-weight: 800; margin: 7mm 0 6mm 0; line-height: 1.02; color: white; string-set: none; }
.cover-sub { font-size: 9.6pt; line-height: 1.45; opacity: 0.95; max-width: 118mm; margin-bottom: 6mm; }
.cover-meta { font-size: 8pt; opacity: 0.9; max-width: 118mm; }
.cover-foot { position: absolute; left: 18mm; top: 193mm; width: 200mm; font-size: 6.8pt; color: #dfe6f2; }
nav.toc { page: toc; page-break-before: always; }
nav.toc h1 { string-set: chap "Sumário"; }
nav.toc ul { list-style: none; padding: 0; margin: 0; column-count: 3; column-gap: 12pt; }
nav.toc li { margin: 0; padding: 0.7pt 0; font-size: 7.3pt; break-inside: avoid; line-height: 1.25; }
nav.toc li.l1 { font-weight: 700; margin-top: 2pt; }
nav.toc li.l2 { padding-left: 7pt; font-size: 6.9pt; color: #333; }
nav.toc li a { display: block; color: #111; }
nav.toc li a::after { content: leader(".") target-counter(attr(href), page); color: #555; font-weight: 400; }

.cols.three { column-count: 3; column-gap: 8mm; }
.cols.lcols { column-count: 2; column-gap: 8mm; margin-bottom: 2pt; }
table.cb.grp > tbody > tr > td.gap, table.gi > tbody > tr > td.gap { width: 5mm; padding: 0; border: none; }
table.gi { border-collapse: collapse; width: 100%; margin: 2pt 0 4pt 0; table-layout: fixed; }
table.gi > tbody > tr > td { border: none; padding: 0; vertical-align: top; }
table.cb.grp.side, table.cb.grp.side tr { page-break-inside: auto; break-inside: auto; }
.keepimg { break-inside: avoid; page-break-inside: avoid; }
table.cb.grp.side > tbody > tr > td { padding-top: 0; }
.interp.stk { margin-top: 5pt; }
.cols.grpflow { column-count: 2; column-gap: 7mm; column-rule: 0.3pt solid #d5dce6; margin-top: 2pt; }
.grpflow .interp.gi { break-inside: auto; }
.grpflow .pi-id { margin-top: 2pt; }
.cellhead { font-weight: 700; color: #1f4e8c; font-size: 8.4pt; margin: 0 0 2pt 0; }
div.chart.tf > .chart-head { page-break-after: avoid; break-after: avoid; }
div.chart.tf .interp { margin-top: 2pt; } div.chart.tf table.cb { margin-top: 3pt; }
.nextrun h2 { margin-top: 2pt; } .nextrun table { font-size: 7.2pt; }
.tec { page-break-inside: auto; break-inside: auto; }
.beside { margin-top: 5pt; border-top: 0.5pt solid #c9d2e0; padding-top: 4pt; }
.beside h3 { margin-top: 1pt; } .beside h2 { margin-top: 2pt; font-size: 9.4pt; }
.beside table { font-size: 7.4pt; }
.beside .lb .chart-head { margin-top: 2pt; }
.lb .lista { margin-top: 2pt; }
table.cam td:first-child { width: 48%; font-weight: 600; }
table.cam td { padding: 1.3pt 2.5pt; }
.card { font-size: 7.2pt; }
.gloss { column-count: 1; }
""".replace("FONT", FONT).replace("TABS", tabs_css())

ROTEIRO_CHAKRA = [("C{k}-sinais", "sinais do chakra"), ("G8", "categoria da causa"), ("C{k}-emocoes", "emoções do chakra"), ("G9", "sessenta emoções"),
                  ("G10", "famílias de crença"), ("G11", "feridas"), ("C{k}-corpo", "corpo do chakra"), ("G22", "técnica"), ("G23", "tempo e dose"), ("G2", "remedir")]

def auto_trilhas(html_part):
    """Trilha após o título de cada capítulo: ordem de uso dos gráficos. Chakras: roteiro fixo. Capítulos longos: uma trilha por seção."""
    secs = re.split(r'(?=<section class="chapter)', html_part)
    out = []
    for s in secs:
        m_id = re.search(r'<section class="chapter[^"]*" id="([^"]+)"', s)
        sid = m_id.group(1) if m_id else ""
        if re.fullmatch(r"ch[1-7]", sid):
            k = sid[2]
            items = [(d.replace("{k}", k), lab) for d, lab in ROTEIRO_CHAKRA]
            s = s.replace("</h1>", "</h1>" + bookkit.trilha(items, "Roteiro deste chakra, na ordem de uso"), 1)
            out.append(s); continue
        ids = []
        for m in re.finditer(r'id="fig-([^"]+)"', s):
            if m.group(1) not in ids: ids.append(m.group(1))
        if len(ids) >= 2 and "</h1>" in s:
            if False:
                pass
            else:
                items = [(cid, bookkit.short_title(cid)) for cid in ids if cid in bookkit.MANIFEST]
                s = s.replace("</h1>", "</h1>" + bookkit.trilha(items, "Gráficos deste capítulo, na ordem de uso"), 1)
        out.append(s)
    return "".join(out)

def _promote_tables(run):
    """Tabelas de nível superior (fora de figuras, de outras tabelas e de divs) com 3+ colunas e 3+ linhas saem das colunas (largura total)."""
    out = []; pos = 0
    tok = re.compile(r"<figure\b|</figure>|<table\b|</table>|<div\b|</div>")
    fig = tbl = div = 0
    for m in re.finditer(r"<table[^>]*>.*?</table>", run, flags=re.S):
        before = run[pos:m.start()]
        for t in tok.finditer(before):
            s = t.group(0)
            if s.startswith("<figure"): fig += 1
            elif s == "</figure>": fig -= 1
            elif s.startswith("<table"): tbl += 1
            elif s == "</table>": tbl -= 1
            elif s.startswith("<div"): div += 1
            else: div -= 1
        t_ = m.group(0)
        ncols = len(re.findall(r"<th[\s>]", t_.split("</thead>")[0])) if "</thead>" in t_ else 0
        nrows = t_.count("<tr>") - 1
        if fig == 0 and tbl == 0 and div == 0 and ncols >= 3 and nrows >= 3 and "idx" not in t_[:40] and "<table" not in t_[7:]:
            out.append(before); out.append(SPAN0 + '<div class="wide">' + t_ + "</div>" + SPAN1)
        else:
            out.append(before + t_)
            for t in tok.finditer(t_):   # o trecho casado pode abrir mais do que fecha (tabela aninhada)
                s = t.group(0)
                if s.startswith("<figure"): fig += 1
                elif s == "</figure>": fig -= 1
                elif s.startswith("<table"): tbl += 1
                elif s == "</table>": tbl -= 1
                elif s.startswith("<div"): div += 1
                else: div -= 1
        pos = m.end()
    out.append(run[pos:])
    return "".join(out)

def _keep_headings(run):
    """Título h2/h3 preso ao que vem logo depois: parágrafo (até 700 caracteres), tabela curta (até 420), ou o primeiro item de uma lista
    (a lista é dividida; a numeração continua)."""
    def rep(m):
        h, nxt = m.group(1), m.group(2)
        plain = re.sub("<.*?>", "", nxt)
        if nxt.lstrip().startswith("<p>"):
            return f'<div class="keep">{h}{nxt}</div>' if len(plain) <= 700 else m.group(0)
        if nxt.lstrip().startswith("<table"):
            return f'<div class="keep">{h}{nxt}</div>' if len(plain) <= 700 else m.group(0)
        if len(plain) <= 420: return f'<div class="keep">{h}{nxt}</div>'
        mm = re.match(r"\s*(<(ol|ul)([^>]*)>)(<li>(?:(?!</li>).)*</li>)(.*)$", nxt, flags=re.S)
        if not mm: return m.group(0)
        open_tag, tag, attrs, first, rest = mm.groups()
        start = re.search(r'start="(\d+)"', attrs); n0 = int(start.group(1)) if start else 1
        attrs2 = re.sub(r'\s*start="\d+"', "", attrs) + (f' start="{n0 + 1}" style="counter-reset: list-item {n0}"' if tag == "ol" else "")
        # o motor ignora o atributo start (sem presentational hints): a numeração continua pelo contador CSS
        if tag == "ol" and n0 > 1: open_tag = re.sub(r"<ol", f'<ol style="counter-reset: list-item {n0 - 1}"', open_tag, count=1)
        return f'<div class="keep">{h}{open_tag}{first}</{tag}></div><{tag}{attrs2}>{rest}'
    return re.sub(r"(<h[23][^>]*>[^<]*</h[23]>)(\s*(?:<p>(?:(?!</p>).)*</p>|<ul[^>]*>(?:(?!</ul>).)*</ul>|<ol[^>]*>(?:(?!</ol>).)*</ol>|<table[^>]*>(?:(?!</table>).)*</table>))", rep, run, flags=re.S)

def _bind_heading(hw, block):
    """Prende o título ao primeiro bloco indivisível que o segue: trilha + gráfico, tabela do desenho (linha extra), keep da lista,
    tabela larga curta ou trecho em duas células."""
    m = re.match(r'(\s*<div class="trilha">(?:(?!</div>).)*</div>)', block)
    if m: return _bind_heading(hw + m.group(1), block[m.end():])
    m = re.match(r'\s*(<table class="two">|<div class="one">|<div class="keep">|<div class="box)', block)
    if m:
        first = _split_blocks(block)[0]
        return '<div class="keep">' + hw + first + '</div>' + block[block.index(first) + len(first):]
    m = re.match(r'(\s*<div class="chart k-lista"><div class="lb"[^>]*><div class="keep">)', block)
    if m: return block[:m.end()] + hw + block[m.end():]
    m = re.match(r'(\s*<div class="chart[^"]*"[^>]*><table class="cb[^"]*"[^>]*>)', block)
    if m: return block[:m.end()] + '<tr><td colspan="5" class="hrow">' + hw + '</td></tr>' + block[m.end():]
    m = re.match(r'\s*<div class="wide">(<table.*?</table>)</div>', block, flags=re.S)
    if m and m.group(1).count("<tr>") <= 10: return '<div class="keep">' + hw + block[:m.end()] + '</div>' + block[m.end():]
    return hw + block

def _split_blocks(run):
    """Divide um trecho HTML nos seus blocos de nível superior (p, ul, ol, h2, h3, div, table, figure)."""
    out = []; i = 0; n = len(run)
    tag_re = re.compile(r"<(p|ul|ol|h2|h3|h4|div|table|figure)\b[^>]*>")
    while i < n:
        m = tag_re.search(run, i)
        if not m:
            rest = run[i:].strip()
            if rest: out.append(rest)
            break
        if m.start() > i and run[i:m.start()].strip(): out.append(run[i:m.start()].strip())
        tag = m.group(1); depth = 0; j = m.start()
        pair = re.compile(rf"<{tag}\b[^>]*>|</{tag}>")
        for mm in pair.finditer(run, m.start()):
            depth += 1 if not mm.group(0).startswith("</") else -1
            if depth == 0: j = mm.end(); break
        else: j = n
        out.append(run[m.start():j]); i = j
    return out

def _two_cells(run):
    """Duas colunas 'manuais' (tabela de duas células, largura total, indivisível): equilibradas por quantidade de texto."""
    blocks = _split_blocks(run)
    lens = [len(re.sub("<.*?>", "", b)) for b in blocks]; total = sum(lens)
    if total < 320 or len(blocks) < 2: return f'<div class="one">{run}</div>'
    acc = 0; cut = len(blocks)
    for k, L in enumerate(lens):
        acc += L
        if acc >= total / 2: cut = k + 1; break
    if cut >= len(blocks): cut = len(blocks) - 1
    left, right = "".join(blocks[:cut]), "".join(blocks[cut:])
    return f'<table class="two"><tr><td>{left}</td><td class="gap"></td><td>{right}</td></tr></table>'

def layout_sections(html_part):
    """Dentro de cada capítulo: blocos marcados ficam em largura total; o resto vai para duas colunas (trechos curtos: duas células indivisíveis)."""
    def wrap(run):
        run = run.strip()
        if not run: return ""
        run = _keep_headings(run)
        plain = re.sub(r"<[^>]+>", "", run)
        if "dcard" in run: return f'<div class="cols cards">{run}</div>'
        if len(plain) < 1200: return _two_cells(run)
        return f'<div class="cols">{run}</div>'
    secs = re.split(r'(?=<section class="chapter)', html_part)
    out = []
    for s in secs:
        if not s.startswith("<section"): out.append(s); continue
        head_end = s.find("</h1>")
        if head_end < 0: out.append(s); continue
        head_end += len("</h1>")
        body = s[head_end:]; tail = ""
        if body.rstrip().endswith("</section>"):
            k = body.rstrip().rfind("</section>"); tail = body[k:]; body = body[:k]
        body = _promote_tables(body)
        parts = re.split(re.escape(SPAN0) + r"(.*?)" + re.escape(SPAN1), body, flags=re.S)
        for i in range(0, len(parts) - 1, 2):
            m = re.search(r"(<h[23][^>]*>(?:(?!<h[23])(?!</div>).)*</h[23]>)(\s*<p>(?:(?!</p>).)*</p>)?\s*$", parts[i], flags=re.S)
            if m and parts[i + 1].strip() and len(re.sub("<.*?>", "", m.group(2) or "")) <= 300:
                parts[i] = parts[i][:m.start()]; parts[i + 1] = _bind_heading('<div class="h2wide">' + m.group(1) + (m.group(2) or "") + "</div>", parts[i + 1])
        # pergunta do gráfico que já está no passo a passo da mesma seção: sai do bloco (fica no passo a passo)
        txt = re.sub(r"<[^>]+>", "", "".join(parts[0::2]))
        def _dedupe(m):
            qs = re.findall(r"“([^”]{20,})”", m.group(0))
            if qs and all(q[:35] in txt for q in qs): return ""
            return m.group(0)
        parts = [re.sub(r'<p><b>Pergunta\.</b> (?:(?!</p>).)*</p>', _dedupe, part, flags=re.S) if i % 2 else part for i, part in enumerate(parts)]
        # desenho de bloco texto-antes: o trecho seguinte (até ~2 400 caracteres, por blocos inteiros) corre ao lado dele
        for i in range(1, len(parts) - 1, 2):
            while "<!--NEXTRUN-->" in parts[i] and parts[i + 1].strip():
                pos = parts[i].find("<!--NEXTRUN-->")
                tbl = parts[i][parts[i].rfind('<table class="cb', 0, pos):pos]
                blocks = _split_blocks(parts[i + 1]); take = []; acc = 0
                # orçamento pela altura do desenho da linha deste marcador (a linha é indivisível) menos o que já está na célula
                cells = re.findall(r'<td class="l"(?: id="fig-([^"]+)")? style="width:([\d.]+)%"', tbl)
                mid = re.search(r'<div class="chart tf" id="fig-([^"]+)"', parts[i])
                ws = [float(w) / 100 for _, w in cells]; ids_ = [c or (mid.group(1) if mid else "") for c, _ in cells]
                hs = [bookkit.PAGE_W * w * bookkit._svg_height(bookkit.MANIFEST[c]["file"]) / 190.0 + 7 for c, w in zip(ids_, ws) if c in bookkit.MANIFEST]
                draw_h = max(hs) if hs else 80.0; right_w = bookkit.PAGE_W * (1 - sum(ws)) - 7 * len(ws)
                pre = parts[i][parts[i].rfind('<td class="r">', 0, pos):pos]
                acc_h = bookkit._est_h(pre, right_w); n_full = 0; partial = None
                for bl in blocks:
                    L = len(re.sub("<.*?>", "", bl)); hb = bookkit._est_h(bl, right_w)
                    if acc + L > 2400 or acc_h + hb > draw_h - 3:
                        m_ = re.match(r"(<(ol|ul)[^>]*>)(.*)(</\2>)\s*$", bl, re.S)
                        if m_:   # lista: leva só os itens que cabem ao lado do desenho; o resto continua abaixo, com a numeração certa
                            items = re.findall(r"<li\b.*?</li>", m_.group(3), re.S); fit = []
                            for it in items:
                                h_it = bookkit._est_h(it, right_w)
                                if acc_h + h_it > draw_h - 3: break
                                fit.append(it); acc_h += h_it
                            if fit and len(fit) < len(items):
                                take.append(m_.group(1) + "".join(fit) + m_.group(4))
                                tag = m_.group(1) if m_.group(2) == "ul" else re.sub(r"<ol", f'<ol style="counter-reset: list-item {len(fit)}"', m_.group(1), count=1)
                                tag = tag.replace('class="', 'class="cont ', 1) if 'class="' in tag else tag.replace("<" + m_.group(2), f'<{m_.group(2)} class="cont"', 1)
                                partial = tag + "".join(items[len(fit):]) + m_.group(4)   # .cont: continuação de lista partida ao lado de um desenho; sem a regra do último item
                        break
                    take.append(bl); acc += L; acc_h += hb; n_full += 1
                if not take: break
                moved = "".join(take)
                rest = (partial or "") + parts[i + 1][len("".join(blocks[:n_full + (1 if partial else 0)])):]
                parts[i] = parts[i].replace("<!--NEXTRUN-->", _keep_headings(moved), 1); parts[i + 1] = rest
        parts = [p_.replace("<!--NEXTRUN-->", "") if i % 2 else p_ for i, p_ in enumerate(parts)]
        new = [part if i % 2 else wrap(part) for i, part in enumerate(parts)]
        page = s[:head_end] + "".join(new) + tail
        # título movido que ficou seguido da trilha da seção: prende título + trilha ao bloco seguinte
        while True:
            m = re.search(r'(<div class="h2wide">(?:(?!</div>).)*</div>)(?=<div class="trilha">)', page)
            if not m: break
            head = m.group(1).replace('class="h2wide"', 'class="h2wide done"', 1); rest = page[m.end():]
            page = page[:m.start()] + _bind_heading(head, rest)
        page = re.sub(r'(<div class="kicker">(?:(?!</h1>).)*</h1>)(<div class="trilha">(?:(?!</div>).)*</div>)?(<div class="cols(?: one)?">|<table class="two"><tr><td>|<div class="one">)(<p>(?:(?!</p>).)*</p>)',
                      lambda m: ('<div class="chapstart">' + m.group(1) + (m.group(2) or "") + '<div class="intro">' + m.group(4) + '</div></div>' + m.group(3)) if len(re.sub("<.*?>", "", m.group(4))) <= 300 else ('<div class="chapstart">' + m.group(1) + (m.group(2) or "") + '</div>' + m.group(3) + m.group(4)), page, count=1, flags=re.S)
        out.append(page)
    return "".join(out)

def capa_svg():
    """Capa para A4 deitado: fundo em gradiente, leque grande atravessando a base, linha dourada."""
    W, H = 297, 210
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">',
           '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#15396f"/><stop offset="1" stop-color="#2358a0"/></linearGradient>'
           '<clipPath id="c"><rect x="0" y="0" width="297" height="210"/></clipPath></defs>',
           f'<rect width="{W}" height="{H}" fill="url(#g)"/>', '<g clip-path="url(#c)">']
    cx, cy = 205, 262
    for i, (r0, r1) in enumerate([(70, 100), (100, 128), (128, 154), (154, 178), (178, 200), (200, 220)]):
        n = 10 + i * 2
        for j in range(n):
            a0 = math.pi + j * math.pi / n; a1 = math.pi + (j + 1) * math.pi / n
            def pt(r, a): return (cx + r * math.cos(a), cy + r * math.sin(a))
            x0, y0 = pt(r1, a0); x1, y1 = pt(r1, a1); x2, y2 = pt(r0, a1); x3, y3 = pt(r0, a0)
            op = 0.04 + 0.05 * ((i + j) % 3)
            out.append(f'<path d="M{x0:.1f} {y0:.1f} A{r1} {r1} 0 0 1 {x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f} A{r0} {r0} 0 0 0 {x3:.1f} {y3:.1f} Z" fill="#ffffff" fill-opacity="{op:.2f}" stroke="#ffffff" stroke-opacity="0.35" stroke-width="0.3"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="52" fill="#ffffff" fill-opacity="0.06" stroke="#e6c36b" stroke-width="0.6"/>')
    out.append(f'<circle cx="{cx}" cy="{cy - 36}" r="2.2" fill="#e6c36b"/><line x1="{cx}" y1="{cy - 36}" x2="{cx}" y2="{cy - 150}" stroke="#e6c36b" stroke-width="0.6"/>')
    out.append('</g><rect x="18" y="18" width="40" height="0.8" fill="#e6c36b"/></svg>')
    open(os.path.join(HERE, "figs", "capa_land.svg"), "w", encoding="utf-8").write("".join(out))

def _keep_last_rows(html_):
    """As duas últimas linhas de cada tabela de resultado ficam num tbody indivisível (sem linha órfã na continuação)."""
    def rep(m):
        t = m.group(0); i = t.find("<tbody>")
        if i < 0: return t
        rows = re.findall(r"<tr>.*?</tr>", t[i:], re.S)
        if len(rows) < 3: return t
        if len(rows) <= 4:   # tabela curta: inteira num bloco só (o motor ignora break-inside em tbody; na tabela respeita)
            return t.replace('<table class="legend">', '<table class="legend whole">', 1)
        first2, last2 = "".join(rows[:2]), "".join(rows[-2:])   # nem linha só no começo (cabeçalho + 1), nem no fim
        body = t[i:].replace("<tbody>" + first2, '<tbody class="k2">' + first2 + '</tbody><tbody>', 1)
        return t[:i] + body.replace(last2 + "</tbody>", '</tbody><tbody class="k2">' + last2 + "</tbody>", 1)
    return re.sub(r'<table class="legend">.*?</table>', rep, html_, flags=re.S)

def _legend_ids(html_):
    """Cabeçalho da tabela de resultado leva o número do gráfico ("G86 · Resultado"): cada pedaço de tabela diz de que gráfico é."""
    pat = re.compile(r'id="fig-([A-Za-z0-9\-]+)"|class="pi-id">([A-Za-z0-9\-]+) ·|<table class="legend"><thead><tr><th>Resultado( \(cont\.\))?</th>')
    out = []; pos = 0; cur = ""
    for m in pat.finditer(html_):
        if m.group(1) or m.group(2): cur = m.group(1) or m.group(2); continue
        out.append(html_[pos:m.start()])
        out.append(f'<table class="legend"><thead><tr><th>{cur} · Resultado{m.group(3) or ""}</th>' if cur else m.group(0)); pos = m.end()
    out.append(html_[pos:]); return "".join(out)

def assemble():
    TOC.clear()
    front = content_front.build()
    chak = content_chakras.build()
    rest = content_rest.build()
    toc = toc_html()
    front, chak, rest = (layout_sections(auto_trilhas(x)) for x in (front, chak, rest))
    idx = front.index("</section>") + len("</section>")
    html = ("<!DOCTYPE html><html lang='pt-BR'><head><meta charset='utf-8'><title>Manual de Radiestesia Terapêutica</title>"
            f"<style>{CSS}</style></head><body>" + front[:idx] + toc + front[idx:] + chak + rest + "</body></html>")
    return _legend_ids(html.replace(SPAN0, "").replace(SPAN1, ""))   # linhas presas via CSS (tr:first-child / tr:last-child)

def jumpers(pdf_path):
    """{id do gráfico: mm livres na página anterior} para blocos que começam no alto de uma página deixando mais de 40 mm vazios antes."""
    import pymupdf
    doc = pymupdf.open(pdf_path); out = {}; prev_tail = 0.0
    ID = re.compile(r"^(G\d{1,3}b?|C[1-7]-(?:sinais|emocoes|corpo))$")
    for i, p in enumerate(doc):
        W, H = p.rect.width, p.rect.height
        bl = [b for b in p.get_text("blocks") if b[4].strip() and b[0] < W - 40]
        TOP, BOT = 10 / 25.4 * 72, H - 10 / 25.4 * 72
        body = [b for b in bl if b[1] > TOP - 3 and b[3] < BOT + 1]
        if i > 0 and prev_tail > 40 and body:
            top = min(b[1] for b in body)
            if top < TOP + 16:
                ids = []
                for b in p.get_text("dict")["blocks"]:
                    for l in b.get("lines", []):
                        for s in l["spans"]:
                            t = s["text"].strip()
                            if 10.8 < s["size"] < 12.4 and ID.match(t) and s["bbox"][1] < TOP + 128: ids.append((s["bbox"][0], t, s["bbox"][1]))
                if ids:
                    x0, cid, y_id = min(ids)
                    out[cid] = round(max(0.0, prev_tail - max(0.0, (y_id - top)) / 72 * 25.4), 1)
                    bookkit.TAIL_REAL[cid] = round(prev_tail, 1)
        ys = [b[3] for b in body] + [im["bbox"][3] for im in p.get_image_info()] + [d["rect"].y1 for d in p.get_drawings() if TOP < d["rect"].y1 < BOT and d["rect"].x0 < W - 40]
        prev_tail = (BOT - max(ys)) / 72 * 25.4 if ys else 0.0
    return out

REDUCED = set()
def main():
    import sys as _s
    capa_svg()
    from weasyprint import HTML
    out = os.path.join(HERE, "Manual_de_Radiestesia_Terapeutica.pdf")
    passes = 1 if "--one-pass" in _s.argv else 6
    if os.environ.get("BOOK_STATE"):   # reproduzir uma passagem com o estado de uma montagem anterior
        import json as _j; st = _j.load(open(os.environ["BOOK_STATE"]))
        bookkit.FALLBACK.update(st["FALLBACK"]); bookkit.TEXTFIRST.update(st["TEXTFIRST"]); bookkit.TF_TAIL.update(st["TF_TAIL"]); bookkit.TAIL_REAL.update(st.get("TAIL_REAL", {})); REDUCED.update(st["REDUCED"])
    for n_pass in range(passes):
        html = assemble()
        with open(os.path.join(HERE, "livro.html"), "w", encoding="utf-8") as f:
            f.write(html)
        HTML(string=html, base_url=HERE).write_pdf(out)
        j = jumpers(out); new = {}
        for k, v in j.items():
            if k in bookkit.TEXTFIRST:
                if k not in bookkit.TF_TAIL and v >= 40:
                    bookkit.TF_TAIL[k] = v; new[k] = v   # desenho de bloco texto-antes ainda saltou: encolher pela cauda medida (piso 0,75)
                continue
            if k not in bookkit.FALLBACK: new[k] = v
            elif k not in REDUCED:
                REDUCED.add(k); new[k] = v
                if bookkit.TAIL_REAL.get(k, v) >= 55: bookkit.TEXTFIRST.add(k)   # ainda salta depois de encolher: texto antes, desenho na página seguinte
        print(f"passagem {n_pass + 1}: blocos que saltaram: {new or 'nenhum'} | todos: {j} | TF_TAIL: {bookkit.TF_TAIL} | texto-antes: {sorted(bookkit.TEXTFIRST)}", flush=True)
        import json as _j; _j.dump({"FALLBACK": bookkit.FALLBACK, "TEXTFIRST": sorted(bookkit.TEXTFIRST), "TF_TAIL": bookkit.TF_TAIL, "REDUCED": sorted(REDUCED), "TAIL_REAL": bookkit.TAIL_REAL}, open(os.path.join(HERE, "pages", "state.json"), "w"))
        if not new: break
        bookkit.FALLBACK.update(new)
    print("PDF:", os.path.getsize(out) // 1024, "KB; seções no sumário:", len(TOC), "| recuos:", bookkit.FALLBACK)

if __name__ == "__main__":
    main()
