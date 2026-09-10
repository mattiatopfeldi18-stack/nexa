const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [src, out] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(src), { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const fit = await page.evaluate(() => {
    const el = document.querySelector('.foglio');
    const prev = el.style.height;
    el.style.height = 'auto';                       // altezza naturale del contenuto
    const mm = el.getBoundingClientRect().height / (96 / 25.4);
    el.style.height = prev;
    return { mm: +mm.toFixed(1), residuo: +(297 - mm).toFixed(1) };
  });
  await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true,
                   margin: { top: '0', right: '0', bottom: '0', left: '0' } });
  await browser.close();
  const pages = (require('fs').readFileSync(out).toString('latin1').match(/\/Type\s*\/Page[^s]/g) || []).length;
  const flag = fit.mm > 297.5 ? 'DEBORDA' : 'una pagina';
  console.log(`altezza contenuto ${fit.mm} mm  ·  residuo ${fit.residuo} mm  ·  ${flag}  ·  pagine PDF: ${pages}`);
})();
