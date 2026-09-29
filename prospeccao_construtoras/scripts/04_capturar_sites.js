// Tira um print da home de cada site das 30 (fichas/img/<dominio>.jpg) e
// registra se o site respondeu. Depende de a rede do ambiente liberar os sites.
// Uso: NODE_PATH=$(npm root -g) node scripts/04_capturar_sites.js
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const raiz = path.join(__dirname, '..');
const sel = JSON.parse(fs.readFileSync(path.join(raiz, 'dados/selecao30.json')));
fs.mkdirSync(path.join(raiz, 'fichas/img'), { recursive: true });
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const status = {};
  for (const c of sel) {
    const p = path.join(raiz, 'dados/pesquisa', c.dominio + '.json');
    const url = (fs.existsSync(p) && JSON.parse(fs.readFileSync(p)).site?.url) || 'https://' + c.dominio;
    const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
    try {
      const r = await page.goto(url, { timeout: 25000, waitUntil: 'domcontentloaded' });
      await page.waitForTimeout(2500);
      await page.screenshot({ path: path.join(raiz, 'fichas/img', c.dominio + '.jpg'), quality: 70, type: 'jpeg' });
      status[c.dominio] = { url, http: r?.status(), no_ar: (r?.status() || 0) < 400, data: new Date().toISOString() };
    } catch (e) {
      status[c.dominio] = { url, erro: String(e.message).split('\n')[0], no_ar: false, data: new Date().toISOString() };
    }
    await page.close();
    console.log(c.dominio, JSON.stringify(status[c.dominio]));
  }
  fs.writeFileSync(path.join(raiz, 'dados/sites_status.json'), JSON.stringify(status, null, 1));
  await browser.close();
})();
