# -*- coding: utf-8 -*-
"""Peso de cada seção h2 em mm de altura ocupada no PDF (para decidir consolidações)."""
import pymupdf, re, json, sys
doc = pymupdf.open("Manual_de_Radiestesia_Terapeutica.pdf"); n = len(doc)
html = open("livro.html", encoding="utf-8").read()
h2s = [(m.group(1), re.sub("<.*?>", "", m.group(2)).strip()) for m in re.finditer(r'<h2 id="([^"]+)"[^>]*>(.*?)</h2>', html)]
h1s = [re.sub("<.*?>", "", m).strip() for m in re.findall(r"<h1[^>]*>(.*?)</h1>", html)]
titles = {t for _, t in h2s} | set(h1s)
# posição de cada título no PDF
pos = []
for i, p in enumerate(doc):
    W, H = p.rect.width, p.rect.height
    for b in p.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            t = "".join(s["text"] for s in l["spans"]).strip(); sz = max(s["size"] for s in l["spans"])
            if t in titles and sz >= 8.7 and l["bbox"][0] < W - 45:
                pos.append((i, l["bbox"][1], t, sz)); break
pos.sort()
usable = (doc[0].rect.height - 24 - 30)
out = []
for k, (pg, y, t, sz) in enumerate(pos):
    if k + 1 < len(pos): pg2, y2 = pos[k + 1][0], pos[k + 1][1]
    else: pg2, y2 = n - 1, doc[0].rect.height - 24
    mm = ((pg2 - pg) * usable + (y2 - y)) / 72 * 25.4
    out.append((t, pg + 1, round(mm), "h1" if sz > 13 else "h2"))
json.dump(out, open("pages/weigh.json", "w"), ensure_ascii=False)
if "--print" in sys.argv:
    for t, pg, mm, lv in out: print(f"{'#' if lv == 'h1' else ' '} p.{pg:>3} {mm:>5} mm  {t[:70]}")
