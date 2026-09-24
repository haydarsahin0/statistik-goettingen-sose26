// Baut das Lernbuch: HTML-Fragmente + KaTeX -> buch.html -> PDF (Chromium via Playwright)
const fs = require('fs');
const path = require('path');
const katex = require('katex');

const SRC = __dirname;
const OUT = path.join(SRC, '..');
const parts = process.env.PARTS ? process.env.PARTS.split(',') :
  ['titel.html', 'tag1.html', 'tag2.html', 'tag3.html', 'tag4.html', 'tag5.html', 'anhang.html'];
const OUTNAME = process.env.OUTNAME || 'Lernbuch_Statistik_SoSe26.pdf';

const dec = t => t.replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&amp;/g,'&').replace(/&nbsp;/g,'~');
function renderMath(html) {
  // <pre>-Blöcke schützen (R-Code enthält $ und Backslashes)
  const pres = [];
  html = html.replace(/<pre[\s\S]*?<\/pre>/g, m => { pres.push(m); return `@@PRE${pres.length - 1}@@`; });
  html = html.replace(/\\\[([\s\S]+?)\\\]/g, (_, tex) =>
    katex.renderToString(dec(tex), { displayMode: true, throwOnError: true, strict: false }));
  html = html.replace(/\\\(([\s\S]+?)\\\)/g, (_, tex) =>
    katex.renderToString(dec(tex), { displayMode: false, throwOnError: true, strict: false }));
  html = html.replace(/@@PRE(\d+)@@/g, (_, i) => pres[+i]);
  return html;
}

let body = '';
for (const p of parts) {
  const f = path.join(SRC, 'content', p);
  if (!fs.existsSync(f)) continue;
  try {
    body += renderMath(fs.readFileSync(f, 'utf8')) + '\n';
  } catch (e) {
    console.error('Fehler in', p, e.message);
    process.exit(1);
  }
}

const css = fs.readFileSync(path.join(SRC, 'style.css'), 'utf8');
const katexCss = 'node_modules/katex/dist/katex.min.css';
const html = `<!DOCTYPE html><html lang="de"><head><meta charset="utf-8">
<title>Statistik-Lernbuch</title>
<link rel="stylesheet" href="fonts.css">
<link rel="stylesheet" href="${katexCss}">
<style>${css}</style></head><body>${body}</body></html>`;
fs.writeFileSync(path.join(SRC, 'buch.html'), html);

(async () => {
  const { chromium } = require('/opt/node22/lib/node_modules/playwright');
  const browser = await chromium.launch({ executablePath: process.env.CHROME || undefined });
  const page = await browser.newPage();
  await page.goto('file://' + path.join(SRC, 'buch.html'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({
    path: path.join(OUT, OUTNAME),
    format: 'A4',
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: `<div style="width:100%;font-family:Nunito,Arial,sans-serif;font-size:8px;color:#8a94a6;padding:0 15mm;display:flex;justify-content:space-between;">
      <span>Statistik-Lernbuch · SoSe 26 · Göttingen</span><span>Seite <span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
    margin: { top: '14mm', bottom: '16mm', left: '15mm', right: '15mm' }
  });
  await browser.close();
  console.log('PDF fertig');
})();
