from playwright.sync_api import sync_playwright
import os, sys
D=os.path.dirname(os.path.abspath(__file__))
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    pg=b.new_page(); pg.goto('file://'+D+'/doc.html'); pg.wait_for_timeout(1500)
    pg.emulate_media(media='print')
    pg.pdf(path=D+'/DALETH-Modelagem-do-Empreendimento.pdf', format='A4', print_background=True, prefer_css_page_size=True)
    b.close()
print(os.path.getsize(D+'/DALETH-Modelagem-do-Empreendimento.pdf')//1024,'KB')
