# -*- coding: utf-8 -*-
"""Censo das tabelas de resultado: pedaços, continuações de página e de coluna, pedaços com 1 linha. Uso: python3 censo_tabelas.py [pdf] [html]"""
import sys, re, pymupdf
pdf = sys.argv[1] if len(sys.argv) > 1 else "Manual_de_Radiestesia_para_Negocios.pdf"
htmlf = sys.argv[2] if len(sys.argv) > 2 else "pages/livro_final.html"
norm = lambda t: re.sub(r"[^a-z0-9à-ú]", "", t.lower().replace("­", ""))[:12]
doc = pymupdf.open(pdf); n = len(doc)
html = open(htmlf, encoding="utf-8").read(); firsts = set(); n_tables = 0
for m in re.finditer(r'<table class="legend[^"]*">.*?</table>', html, re.S):
    n_tables += 1; body = m.group(0)[m.group(0).find("<tbody"):]; r = re.search(r"<tr><td>(.*?)</td>", body, re.S)
    if r: firsts.add(norm(re.sub("<.*?>", "", r.group(1))))
conts = []; heads_n = 0; two_line = 0
for pg in range(1, n):
    p = doc[pg]; d = p.get_text("dict")
    lines = [(l["bbox"], "".join(s["text"] for s in l["spans"]).strip()) for b in d["blocks"] for l in b.get("lines", []) if b.get("lines")]
    for bb, t in lines:
        if not re.match(r"^(?:[A-Za-z0-9\-]+ · )?Resultado( \(cont\.\))?$", t): continue
        if not any(abs(b2[1] - bb[1]) < 2 and t2.startswith("O que significa") for b2, t2 in lines): continue
        heads_n += 1
        below = sorted([(b2, t2) for b2, t2 in lines if abs(b2[0] - bb[0]) < 3 and b2[1] > bb[3] - 1 and b2[1] < bb[3] + 14], key=lambda x: x[0][1])
        first = below[0][1] if below else ""
        rows = sorted([b for b in p.get_text("blocks") if abs(b[0] - bb[0]) < 3 and b[1] > bb[3] - 1], key=lambda b: b[1]); cnt = 0; last = bb[3]
        for b in rows:
            if b[1] - last > 9: break
            cnt += 1; last = b[3]
        if norm(first) not in firsts: conts.append((pg + 1, bb[1] < 46, cnt, t))
print(f"páginas: {n} | tabelas de resultado: {n_tables} | pedaços no PDF: {heads_n} | continuações: {len(conts)} (de página: {sum(1 for c in conts if c[1])}, de coluna: {sum(1 for c in conts if not c[1])})")
print("  pedaços de continuação com 1 linha:", [(c[0], c[3]) for c in conts if c[2] <= 1])
print("  no alto de página par (verso):", sum(1 for c in conts if c[1] and c[0] % 2 == 0), "| ímpar:", sum(1 for c in conts if c[1] and c[0] % 2 == 1))
