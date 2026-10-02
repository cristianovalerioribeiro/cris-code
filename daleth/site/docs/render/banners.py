from playwright.sync_api import sync_playwright
from urllib.parse import urlencode
import shutil, os
SITE='/home/user/cris-code/daleth/site'
shutil.copy(str(__import__('pathlib').Path(__file__).with_name('render.html')), SITE+'/dist/__render.html')
V={
 'empresas':dict(cena='rede',rot='Gestão|Financeiro|Societário|Contábil|Crédito|Resultado'),
 'empreendimentos':dict(cena='jornada',z='1',rot='Terreno|Produto|Orçamento|Caixa|Vendas|Obra'),
 'capital':dict(cena='heroi',rot='Banco|Investidor|Sócio|Vendas|Permuta|Caixa'),
 'inteligencia':dict(cena='heroi',tema='claro',fundo='#F2F5F8',rot='Permuta|Faseamento|SPE|SCP|Afetação|Caixa'),
}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
        args=['--enable-unsafe-swiftshader','--use-angle=swiftshader','--ignore-gpu-blocklist'])
    for nome,q in V.items():
        q=dict(q,centro='1')
        for suf,(w,h,d) in {'':(1600,520,1),'-m':(400,260,2)}.items():
            pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=d)
            pg.goto('http://localhost:8765/__render.html?'+urlencode(q)); pg.wait_for_timeout(7000)
            out=f'{SITE}/assets/img/{nome}-3d{suf}.jpg'
            pg.screenshot(path=out,type='jpeg',quality=82); pg.close()
            print(out.split('/')[-1], os.path.getsize(out)//1024,'KB')
    b.close()
os.remove(SITE+'/dist/__render.html')
