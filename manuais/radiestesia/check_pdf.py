import sys, os, pymupdf
HERE = os.path.dirname(os.path.abspath(__file__))
pdf = os.path.join(HERE, "Manual_de_Radiestesia_Terapeutica.pdf")
doc = pymupdf.open(pdf)
print("páginas:", len(doc))
pages = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else []
os.makedirs(os.path.join(HERE, "pages"), exist_ok=True)
for pno in pages:
    pix = doc[pno - 1].get_pixmap(dpi=70)
    pix.save(os.path.join(HERE, "pages", f"p{pno:03d}.png"))
# índice de títulos por página
for i, page in enumerate(doc):
    t = page.get_text("text").strip().split("\n")
    first = next((ln for ln in t if ln.strip() and not ln.startswith("Manual de") and ln.strip() not in ("Sumário",)), "")
    if i < 400:
        print(i + 1, "|", first[:70])
