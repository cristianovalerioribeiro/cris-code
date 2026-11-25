# -*- coding: utf-8 -*-
"""Checagens automáticas do manual + folhas de contato. Uso: python3 check_all.py [--no-sheets]"""
import os, re, json, sys
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE); sys.path.insert(0, HERE)
import pymupdf
from PIL import Image
from interp import INTERP

doc = pymupdf.open("Manual_de_Radiestesia_Terapeutica.pdf"); n = len(doc)
man = json.load(open("charts/manifest.json")); html = open("livro.html", encoding="utf-8").read()
problems = []
def rep(label, lst):
    print(f"{label}: {lst if lst else 'ok'}")
    if lst: problems.append(label)
print("páginas:", n, "| gráficos:", len(man), "| seções:", html.count("<h1") + html.count("<h2"))
rep("links vazios", [i+1 for i, p in enumerate(doc) if "(p. )" in p.get_text().replace("\n", "")])
rep("páginas quase vazias", [i+1 for i, p in enumerate(doc) if len(p.get_text().strip()) < 160 and not p.get_images()])
rep("Drive/arquivos/sites", [i+1 for i, p in enumerate(doc) if re.search(r"Drive|drive\.google|seu acervo|\.pdf|\.docx|\.pptx|subtil\.net", p.get_text())])
rep("animais", [i+1 for i, p in enumerate(doc) if re.search(r"\b(pets?|animais)\b", p.get_text(), re.I)])
rep("campos de preenchimento", [i+1 for i, p in enumerate(doc) if re.search(r"_{4,}", p.get_text())])
rep("instrução repetida", [i+1 for i, p in enumerate(doc) if "Pêndulo no ponto azul, testemunho no retângulo" in p.get_text()])
rep("gráficos sem figura no livro", [m["id"] for m in man if f'id="fig-{m["id"]}"' not in html])
rep("gráficos sem interpretação", [m["id"] for m in man if m["id"] not in INTERP])
rep("interpretações sem gráfico", [k for k in INTERP if k not in {m["id"] for m in man}])
ids = {m["id"] for m in man}
cited = set(re.findall(r"\bG\d{1,3}b?\b|\bC[1-7]-(?:sinais|emocoes|corpo|causas)\b", html))
rep("ids citados sem gráfico", sorted(c for c in cited if c not in ids and c not in ("G8b",)))
rep("links internos quebrados", sorted({h for h in re.findall(r'href="#([^"]+)"', html) if f'id="{h}"' not in html})[:30])
try:
    from routes import ROUTES
    rep("gráficos sem rota", [m["id"] for m in man if m["id"] not in ROUTES])
except Exception as ex:
    print("routes.py:", ex)
blank = []
for i, p in enumerate(doc):
    bl = [b for b in p.get_text("blocks") if b[4].strip()]
    ymax = max([b[3] for b in bl], default=0)
    for im in p.get_image_info(): ymax = max(ymax, im["bbox"][3])
    if 0 < ymax < p.rect.height * 0.5: blank.append(i+1)
print("páginas com metade inferior vazia (conferir se é fim de seção):", blank)
if "--no-sheets" not in sys.argv:
    os.makedirs("pages", exist_ok=True)
    def render(p, dpi=50):
        pix = doc[p-1].get_pixmap(dpi=dpi); return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    for si in range(0, n, 12):
        ims = [render(p) for p in range(si+1, min(si+13, n+1))]
        w, h = ims[0].size
        sheet = Image.new("RGB", (w*4+50, h*3+40), "white")
        for i, im in enumerate(ims): sheet.paste(im, (10 + (i%4)*(w+10), 10 + (i//4)*(h+10)))
        sheet.save(f"pages/sw_{si//12+1:02d}.png")
    print("folhas de contato:", (n+11)//12, "em pages/sw_NN.png")
print("RESULTADO:", "OK" if not problems else "PROBLEMAS: " + ", ".join(problems))
