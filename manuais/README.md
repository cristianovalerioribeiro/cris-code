# Manuais (apostilas) gerados com o motor de diagramação

Pasta `radiestesia/`: o Manual de Radiestesia Terapêutica (edição 16, 105 páginas) com tudo o que o produz. Pasta `negocios/`: o Manual de Radiestesia para Negócios (edição 1), feito com o mesmo motor; reaproveita 35 gráficos do manual terapêutico (copiados de `radiestesia/charts/` por `gen_charts.py`, sem alteração e com a mesma numeração) e acrescenta os gráficos G111 a G120. O mesmo motor serve para um manual novo.

## Como começar um manual novo numa conversa nova
1. Abra a conversa com este repositório (ramo `manuais`) e peça: "leia `manuais/README.md` e `manuais/radiestesia/README_ESTADO.md`; vamos fazer um manual novo sobre …".
2. Crie uma pasta irmã (`manuais/<tema>/`) copiando de `radiestesia/` só o motor: `build_book.py`, `bookkit.py`, `gen_charts.py`, `audit_breaks.py`, `check_all.py`, `analise_paginas.py`, `analise_pares.py`, `censo_tabelas.py`, `weigh.py`, `make_map.py`, `build_print.py`, `word/` (versão Word). O conteúdo fica nos módulos `content_*.py`, `interp.py` (interpretações por gráfico), `routes.py` (rotas "vem de / vai para" e cartões de decisão), `chakra_data.py`, e os gráficos em `charts/*.svg` (gerados por `gen_charts.py` a partir de listas em Python).
3. Montagem: `python3 build_book.py` (seis passagens, ~12 min) → `Manual_….pdf`; `python3 audit_breaks.py` e `python3 check_all.py` conferem quebras, links e rotas; `python3 word/html2ir.py && node word/build_docx.js && python3 word/fix_docx.py <arquivo>.docx` geram o Word.
4. Dependências: Python 3 com weasyprint, pymupdf, bs4, pillow, pyphen; Node com `docx`; LibreOffice para conferir o Word; fonte Inter instalada.

## O que o `README_ESTADO.md` de cada manual guarda
Decisões de diagramação, armadilhas do motor de PDF (WeasyPrint) e do Word, histórico de edições e as ferramentas de auditoria. Leia antes de mexer.
