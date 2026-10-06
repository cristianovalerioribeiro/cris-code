#!/usr/bin/env bash
# Regera o PDF e o Word da Modelagem. Rodar de dentro desta pasta, com o site servido em localhost:8765
# (python3 build.py --local && python3 -m http.server 8765 --directory dist, a partir de daleth/site).
set -e
cd "$(dirname "$0")"
cp ../../../assets/fonts/*.woff2 . && cp ../../../assets/marca/horizontal-negative.svg ../../../assets/marca/horizontal-color.svg .
python3 render_frentes.py            # 11 imagens da cena 3D (img/*.jpg) + capa
python3 gerar_html.py && python3 pdf.py
python3 - <<'PY'
from playwright.sync_api import sync_playwright
import os, json, dados as D
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    for nome in ['horizontal-color','horizontal-negative']:
        pg=b.new_page(viewport={'width':1041,'height':275},device_scale_factor=2)
        pg.set_content(f'<img src="file://{os.getcwd()}/{nome}.svg" style="width:1041px;height:275px;display:block">'); pg.wait_for_timeout(400)
        pg.screenshot(path=f'{nome}.png',omit_background=True); pg.close()
    b.close()
json.dump(dict(frentes=D.FRENTES, apoio=D.APOIO, caminhos=D.CAMINHOS, cadeia=D.CADEIA, movimentos=D.MOVIMENTOS, entrega=D.ENTREGA, site=D.SITE, slogan=D.SLOGAN), open('dados.json','w',encoding='utf-8'), ensure_ascii=False)
PY
node gerar_docx.js
mv DALETH-Modelagem-do-Empreendimento.pdf DALETH-Modelagem-do-Empreendimento.docx ..
rm -f *.woff2 *.svg *.png dados.json doc.html
