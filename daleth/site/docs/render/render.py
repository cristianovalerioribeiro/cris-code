from playwright.sync_api import sync_playwright
import shutil, os
SITE='/home/user/cris-code/daleth/site'
shutil.copy(str(__import__('pathlib').Path(__file__).with_name('render.html')), SITE+'/dist/__render.html')
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
        args=['--enable-unsafe-swiftshader','--use-angle=swiftshader','--ignore-gpu-blocklist'])
    def foto(w,h,dpr,hash_,saida,tipo='jpeg'):
        pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=dpr)
        pg.goto('http://localhost:8765/__render.html'+hash_); pg.wait_for_timeout(7000)
        kw={'quality':84} if tipo=='jpeg' else {}
        pg.screenshot(path=saida,type=tipo,**kw); pg.close(); print(saida, os.path.getsize(saida)//1024,'KB')
    foto(1600,900,1,'#limpo',SITE+'/assets/img/heroi-poster.jpg')
    foto(390,300,2,'#limpo',SITE+'/assets/img/heroi-poster-m.jpg')
    foto(1200,630,1,'#og',SITE+'/assets/og.png','png')
    b.close()
os.remove(SITE+'/dist/__render.html')
