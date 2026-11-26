# -*- coding: utf-8 -*-
"""Onde ainda há espaço: caudas de todas as páginas, brancos laterais (meia largura), desenhos maiores que o alvo de rótulo,
linhas de tabela que encolheriam com colunas mais largas, aberturas de capítulo. Uso: python3 analise_paginas.py [pdf] [html]"""
import sys, re, math, json, pymupdf
from PIL import Image
pdf = sys.argv[1] if len(sys.argv) > 1 else "Manual_de_Radiestesia_Terapeutica.pdf"
htmlf = sys.argv[2] if len(sys.argv) > 2 else "pages/livro_final.html"
doc = pymupdf.open(pdf); n = len(doc); W, H = doc[0].rect.width, doc[0].rect.height
TOP, BOT = 10 / 25.4 * 72, H - 10 / 25.4 * 72; mm = lambda pt: pt / 72 * 25.4
ID = re.compile(r"^(G\d{1,3}b?|C[1-7]-(?:sinais|emocoes|corpo))$")
# (a) caudas de todas as páginas e (b) brancos de meia largura, por faixas de 4 mm
tails = {}; halfblank = {}; chap_tail = {}
for pg in range(1, n):
    p = doc[pg]
    bl = [b for b in p.get_text("blocks") if b[4].strip() and b[0] < W - 45 and TOP - 3 < b[1] and b[3] < BOT + 1]
    ys = [b[3] for b in bl] + [d["rect"].y1 for d in p.get_drawings() if TOP < d["rect"].y1 < BOT and d["rect"].x0 < W - 45]
    tails[pg + 1] = round(mm(BOT - max(ys))) if ys else 0
    pix = p.get_pixmap(dpi=36, clip=pymupdf.Rect(28, TOP, W - 45, BOT)); im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples).convert("L")
    px = im.load(); w, h = im.size; band = max(1, round(4 / 25.4 * 36)); half = w // 2; hb = 0
    for y0 in range(0, h - band, band):
        def white(x0, x1): return all(px[x, y] > 245 for y in range(y0, y0 + band, 2) for x in range(x0, x1, 3))
        l, r = white(0, half), white(half, w)
        if l != r: hb += 4
    halfblank[pg + 1] = hb
    if bl and bl[0][4].strip().startswith("PARTE") and pg > 0: chap_tail[pg + 1] = tails.get(pg, 0)
tot = sum(v for k, v in tails.items() if k < n)
print(f"(a) caudas de todas as páginas (sem a última): soma {tot} mm ≈ {tot / 190:.1f} páginas | acima de 20 mm: {sorted([(k, v) for k, v in tails.items() if v > 20 and k < n])}")
print(f"(b) brancos de meia largura (uma metade vazia, a outra com conteúdo), soma por página, só acima de 40 mm: {sorted([(k, v) for k, v in halfblank.items() if v > 40])} | total {sum(halfblank.values())} mm ≈ {sum(halfblank.values()) / 2 / 190:.1f} páginas equivalentes")
print(f"(e) aberturas de Parte em página nova e a cauda deixada antes: {chap_tail}")
# (c) desenhos: menor rótulo e altura, e o que encolher até 6,5 pt pouparia (só onde o desenho é mais alto que o texto ao lado)
saves = []; labels = []
for pg in range(1, n):
    p = doc[pg]; d = p.get_text("dict")
    heads = [(s["bbox"], s["text"].strip()) for b in d["blocks"] for l in b.get("lines", []) for s in l["spans"] if 10.8 < s["size"] < 12.4 and ID.match(s["text"].strip())]
    rects = [x["rect"] for x in p.get_drawings() if x["rect"].width > 60 and x["rect"].height > 40 and x["rect"].x0 < W - 45]
    for bb, cid in heads:
        cand = [r for r in rects if abs(r.x0 - bb[0]) < 40 and bb[3] - 2 < r.y0 < bb[3] + 60]
        if not cand: continue
        r = max(cand, key=lambda r: r.width * r.height)
        spans = [s for b in d["blocks"] for l in b.get("lines", []) for s in l["spans"] if r.x0 <= s["bbox"][0] and s["bbox"][2] <= r.x1 + 2 and r.y0 <= s["bbox"][1] and s["bbox"][3] <= r.y1 + 2 and s["text"].strip()]
        if not spans: continue
        mn = min(s["size"] for s in spans)
        right = [b for b in p.get_text("blocks") if b[0] > r.x1 + 5 and b[0] < W - 45 and b[1] >= bb[1] - 2 and b[1] < r.y1 and b[4].strip()]
        text_bottom = max((b[3] for b in right), default=bb[3])
        labels.append((cid, round(mn, 1)))
        if mn >= 7.0:
            new_h = r.height * 6.5 / mn; gain = min(r.height - new_h, max(0.0, r.y1 - text_bottom))
            if gain > 8: saves.append((pg + 1, cid, round(mn, 1), round(mm(r.height)), round(mm(gain))))
labels.sort(key=lambda x: x[1])
print(f"(c) rótulo mínimo dos desenhos: abaixo de 6,2 pt: {[l for l in labels if l[1] < 6.2]} | de 7,0 pt para cima: {sum(1 for l in labels if l[1] >= 7.0)} de {len(labels)}")
print(f"    encolher esses até 6,5 pt (só onde o desenho manda na altura do bloco) pouparia: {sum(s[4] for s in saves)} mm ≈ {sum(s[4] for s in saves) / 190:.1f} páginas; maiores: {sorted(saves, key=lambda s: -s[4])[:10]}")
# (d) tabelas de resultado: colunas 24/34/42 → 20/28/52: linhas que encolheriam
html = open(htmlf, encoding="utf-8").read(); saved_lines = 0; rows_n = 0
for m in re.finditer(r'<table class="legend">.*?</table>', html, re.S):
    t = m.group(0); wide = 150.0  # largura típica da célula direita; colunas estreitas pioram, largura cheia melhora
    for row in re.findall(r"<tr>(.*?)</tr>", t, re.S):
        cells = [len(re.sub("<.*?>", "", c)) for c in re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)]
        if len(cells) != 3: continue
        rows_n += 1; cpl = wide / 1.45
        old = max(math.ceil(cells[0] / (cpl * .24)), math.ceil(cells[1] / (cpl * .34)), math.ceil(cells[2] / (cpl * .42)), 1)
        new = max(math.ceil(cells[0] / (cpl * .20)), math.ceil(cells[1] / (cpl * .28)), math.ceil(cells[2] / (cpl * .52)), 1)
        saved_lines += old - new
print(f"(d) tabelas de resultado: {rows_n} linhas; colunas 20/28/52 em vez de 24/34/42 mudariam {saved_lines:+d} linhas de texto ≈ {-saved_lines * 3.1 / 190:+.1f} páginas (estimativa a 150 mm de largura)")
