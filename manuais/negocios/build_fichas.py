# -*- coding: utf-8 -*-
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import bookkit, content_fichas
from build_book import CSS

def main():
    body = content_fichas.build()
    css = CSS.replace("Manual de Radiestesia para Negócios · apostila de apoio à decisão", "Fichas · Manual de Radiestesia para Negócios")
    html = ("<!DOCTYPE html><html lang='pt-BR'><head><meta charset='utf-8'><title>Fichas de Decisão Empresarial</title>"
            f"<style>{css}</style></head><body>" + body + "</body></html>")
    with open(os.path.join(HERE, "fichas.html"), "w", encoding="utf-8") as f: f.write(html)
    from weasyprint import HTML
    out = os.path.join(HERE, "Fichas_de_Decisao_Empresarial.pdf")
    HTML(string=html, base_url=HERE).write_pdf(out)
    print("PDF:", out, os.path.getsize(out) // 1024, "KB")

if __name__ == "__main__":
    main()
