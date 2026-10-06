from playwright.sync_api import sync_playwright
from urllib.parse import urlencode
import shutil, os, re, json
SITE='/home/user/cris-code/daleth/site'
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'img')
shutil.copy(SITE+'/docs/render/render.html', SITE+'/dist/__render.html')
js=open(SITE+'/assets/js/modelagem.js').read()
frentes=[]
for m in re.finditer(r'\{ id: "(\w+)", num: "(\d+)".*?sub: \[(.*?)\]', js, re.S):
    frentes.append((m.group(1), json.loads('['+m.group(3)+']')))
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
        args=['--enable-unsafe-swiftshader','--use-angle=swiftshader','--ignore-gpu-blocklist'])
    for fid,sub in frentes:
        q={'cena':'modelagem','rot':'|'.join(sub)}
        pg=b.new_page(viewport={'width':1600,'height':1000},device_scale_factor=1.5)
        pg.goto('http://localhost:8765/__render.html?'+urlencode(q)); pg.wait_for_timeout(7500)
        out=f'{OUT}/{fid}.jpg'; pg.screenshot(path=out,type='jpeg',quality=88); pg.close()
        print(fid, os.path.getsize(out)//1024,'KB')
    # capa: sem rótulos
    pg=b.new_page(viewport={'width':1600,'height':1000},device_scale_factor=1.5)
    pg.goto('http://localhost:8765/__render.html?cena=modelagem&rot=#limpo'); pg.wait_for_timeout(7500)
    pg.screenshot(path=f'{OUT}/capa.jpg',type='jpeg',quality=88); pg.close()
    b.close()
os.remove(SITE+'/dist/__render.html')
