# -*- coding: utf-8 -*-
"""Imposição: duas páginas A5 lado a lado em cada folha A4 deitada (sequencial: 1-2, 3-4, ...).
Uso: python3 impose_2up.py entrada_A5.pdf saida_A4.pdf"""
import sys, pymupdf
src = pymupdf.open(sys.argv[1]); out = pymupdf.open()
W, H = 841.89, 595.28  # A4 deitado em pt
for i in range(0, len(src), 2):
    pg = out.new_page(width=W, height=H)
    pg.show_pdf_page(pymupdf.Rect(0, 0, W / 2, H), src, i)
    if i + 1 < len(src): pg.show_pdf_page(pymupdf.Rect(W / 2, 0, W, H), src, i + 1)
    # linha fina de dobra/corte no meio
    pg.draw_line(pymupdf.Point(W / 2, 0), pymupdf.Point(W / 2, H), color=(0.75, 0.75, 0.75), width=0.3, dashes="[3 3] 0")
out.save(sys.argv[2], garbage=3, deflate=True)
print("folhas A4:", len(out), "| páginas A5:", len(src))
