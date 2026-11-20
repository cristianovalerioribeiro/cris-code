const { chromium } = require('playwright');
(async () => {
  const [src, out] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + src, { waitUntil: 'load' }); await p.waitForTimeout(800);
  await p.pdf({ path: out, format: 'A4', printBackground: true, displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;font-family:DejaVu Sans,sans-serif;font-size:7pt;color:#6b645a;padding:0 17mm;display:flex;justify-content:space-between"><span>Símbolos de proteção, limpeza e prosperidade para a porta de casa</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
    margin: { top: '20mm', bottom: '20mm', left: '17mm', right: '17mm' } });
  await b.close();
})();
