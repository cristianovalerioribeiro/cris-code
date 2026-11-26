# -*- coding: utf-8 -*-
"""Pares de desenhos: diferença de altura entre os dois (branco embaixo do menor) e quanto o menor poderia crescer
sem passar da largura livre (ganho de legibilidade a custo zero de páginas)."""
import sys, re, pymupdf
pdf = sys.argv[1] if len(sys.argv) > 1 else "Manual_de_Radiestesia_Terapeutica.pdf"
doc = pymupdf.open(pdf); W = doc[0].rect.width; mm = lambda pt: pt / 72 * 25.4
ID = re.compile(r"^(G\d{1,3}b?|C[1-7]-(?:sinais|emocoes|corpo))$")
out = []
for pg in range(1, len(doc)):
    p = doc[pg]; d = p.get_text("dict")
    heads = sorted([(round(s["bbox"][1]), s["bbox"][0], s["text"].strip(), s["bbox"]) for b in d["blocks"] for l in b.get("lines", []) for s in l["spans"] if 10.8 < s["size"] < 12.4 and ID.match(s["text"].strip())])
    rects = [x["rect"] for x in p.get_drawings() if x["rect"].width > 60 and x["rect"].height > 40 and x["rect"].x0 < W - 45]
    by_y = {}
    for y, x, cid, bb in heads: by_y.setdefault(y // 6, []).append((x, cid, bb))
    for grp in by_y.values():
        if len(grp) < 2: continue
        grp.sort(); info = []
        for x, cid, bb in grp:
            cand = [r for r in rects if abs(r.x0 - bb[0]) < 40 and bb[3] - 2 < r.y0 < bb[3] + 60]
            if not cand: continue
            r = max(cand, key=lambda r: r.width * r.height)
            spans = [s for b in d["blocks"] for l in b.get("lines", []) for s in l["spans"] if r.x0 <= s["bbox"][0] and s["bbox"][2] <= r.x1 + 2 and r.y0 <= s["bbox"][1] and s["bbox"][3] <= r.y1 + 2 and s["text"].strip()]
            info.append((cid, r, min((s["size"] for s in spans), default=0)))
        if len(info) < 2: continue
        hmax = max(i[1].height for i in info); used = sum(i[1].width for i in info); free = (W - 45 - 28) - used - 14 * (len(info) - 1)
        for cid, r, mn in info:
            if r.height < hmax - 10:
                grow = min(hmax / r.height, (r.width + max(free, 0)) / r.width)
                out.append((pg + 1, cid, round(mm(hmax - r.height)), round(mn, 1), round(grow, 2), round(mn * grow, 1)))
print("pares com desenho menor que o vizinho (página, gráfico, branco embaixo mm, rótulo mínimo pt, fator possível, rótulo depois):")
for o in sorted(out, key=lambda o: -o[2]): print("  ", o)
print("total de branco embaixo dos menores:", sum(o[2] for o in out), "mm | pares em que o menor pode crescer ≥ 15%:", sum(1 for o in out if o[4] >= 1.15))
