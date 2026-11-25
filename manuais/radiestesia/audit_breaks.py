# -*- coding: utf-8 -*-
"""Pente fino de quebras: cabeçalhos/títulos órfãos no pé da página, restos minúsculos no alto da página seguinte, caudas vazias."""
import pymupdf, re, sys, json, collections
PDF = sys.argv[1] if len(sys.argv) > 1 else "Manual_de_Radiestesia_Terapeutica.pdf"
doc = pymupdf.open(PDF); n = len(doc)
html = open("livro.html", encoding="utf-8").read()
heads = set(re.sub("<.*?>", "", m).strip() for m in re.findall(r"<h[123][^>]*>(.*?)</h[123]>", html))
cellheads = set(re.sub("<.*?>", "", m).strip() for m in re.findall(r'<div class="cellhead"[^>]*>(.*?)</div>', html))
ID_RE = re.compile(r"^(G\d{1,3}b?|C[1-7]-(?:sinais|emocoes|corpo))$")
def page_items(p):
    W, H = p.rect.width, p.rect.height
    items = []
    for b in p.get_text("dict")["blocks"]:
        if b["type"] != 0: continue
        x0, y0, x1, y1 = b["bbox"]
        if x0 > W - 45 or y1 < 27 or y0 > H - 28: continue  # abas, cabeçalho e rodapé
        lines = b["lines"]; text = " ".join("".join(s["text"] for s in l["spans"]).strip() for l in lines).strip()
        size = max((s["size"] for l in lines for s in l["spans"]), default=0)
        first = "".join(s["text"] for s in lines[0]["spans"]).strip() if lines else ""
        items.append(dict(x0=x0, y0=y0, x1=x1, y1=y1, text=text, first=first, size=size, nlines=len(lines)))
    for im in p.get_image_info():
        x0, y0, x1, y1 = im["bbox"]
        if x1 - x0 > 60: items.append(dict(x0=x0, y0=y0, x1=x1, y1=y1, text="[img]", first="[img]", size=0, nlines=0))
    return items, W, H
def kind(it):
    t = it["first"]
    if ID_RE.match(t) and it["size"] > 10.5: return "chart"
    if t in heads and it["size"] >= 8.8: return "h"
    if t in cellheads: return "cellhead"
    if it["size"] >= 8.8 and len(t) < 70 and t in heads: return "h"
    return "txt"
report = []; tails = []
prev_items = None
for i, p in enumerate(doc):
    items, W, H = page_items(p)
    body_bottom = H - 28.35
    # cauda
    ys = [it["y1"] for it in items] + [d["rect"].y1 for d in p.get_drawings() if 27 < d["rect"].y1 < H - 28 and d["rect"].x0 < W - 45]
    tail = (body_bottom - max(ys)) / 72 * 25.4 if ys else 186
    if tail > 45: tails.append((i + 1, round(tail)))
    # órfãos: título / cabeçalho de gráfico / cellhead no último quarto, sem conteúdo abaixo na mesma coluna
    for it in items:
        k = kind(it)
        if k in ("h", "chart", "cellhead") and it["y0"] > (H * 0.80 if it["size"] < 14 else H * 0.70):
            below = [o for o in items if o is not it and o["y0"] >= it["y1"] - 2 and o["x0"] < it["x1"] and o["x1"] > it["x0"] and o["text"] != "[img]"]
            below_h = sum(o["y1"] - o["y0"] for o in below) / 72 * 25.4
            if below_h < 3: report.append((i + 1, "órfão no pé", k, it["first"][:40], f"{round((H - 24 - it['y0']) / 72 * 25.4)} mm até o fim"))
    # resto minúsculo no alto: primeiro item é texto curto (≤ 3 linhas, altura < 10 mm) e logo abaixo vem título ou gráfico
    top = sorted([it for it in items if it["text"] != "[img]"], key=lambda o: (o["y0"], o["x0"]))
    if top and i > 0:
        f = top[0]
        if kind(f) == "txt" and f["nlines"] <= 3 and (f["y1"] - f["y0"]) / 72 * 25.4 < 10:
            nxt = [o for o in top[1:] if o["y0"] >= f["y1"] - 1 and o["x0"] < f["x1"] and o["x1"] > f["x0"]]
            if nxt and kind(nxt[0]) in ("h", "chart") and (nxt[0]["y0"] - f["y1"]) / 72 * 25.4 < 12:
                report.append((i + 1, "resto no alto", "txt", f["text"][:40], f"{f['nlines']} linha(s) antes de “{nxt[0]['first'][:30]}”"))
    prev_items = items
print(f"páginas: {n}")
print(f"órfãos e restos: {len(report)}")
for r in report: print("  p.%3d | %-14s | %-8s | %-40s | %s" % r)
print(f"caudas > 45 mm: {len(tails)} | soma {sum(t for _, t in tails)} mm")
print("  " + ", ".join(f"p.{a} ({b})" for a, b in tails))
json.dump(dict(report=report, tails=tails, pages=n), open("pages/audit_breaks.json", "w"), ensure_ascii=False)
