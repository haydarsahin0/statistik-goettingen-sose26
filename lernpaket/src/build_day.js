// Baut ein Tagesheft: content/<PART> + day.css → PDF ohne Ränder (jede .pg = 1 Seite)
const fs = require('fs'), path = require('path'), katex = require('katex');
const SRC = __dirname, PART = process.env.PART, OUT = process.env.OUTNAME;
const dec = t => t.replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&amp;/g,'&').replace(/&nbsp;/g,'~');
let body = fs.readFileSync(path.join(SRC, 'content', PART), 'utf8');
const pres = []; body = body.replace(/<pre[\s\S]*?<\/pre>/g, m => { pres.push(m); return `@@PRE${pres.length-1}@@`; });
body = body.replace(/\\\[([\s\S]+?)\\\]/g, (_, t) => katex.renderToString(dec(t), {displayMode: true, throwOnError: true, strict: false}));
body = body.replace(/\\\(([\s\S]+?)\\\)/g, (_, t) => katex.renderToString(dec(t), {displayMode: false, throwOnError: true, strict: false}));
body = body.replace(/@@PRE(\d+)@@/g, (_, i) => pres[+i]);
const css = fs.readFileSync(path.join(SRC, 'day.css'), 'utf8');
const html = `<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><title>${process.env.TITLE || 'Klausurtraining'}</title>
<link rel="stylesheet" href="fonts_day.css"><link rel="stylesheet" href="node_modules/katex/dist/katex.min.css">
<style>${css}</style></head><body>${body}</body></html>`;
fs.writeFileSync(path.join(SRC, 'day.html'), html);
(async () => {
  const { chromium } = require('/opt/node22/lib/node_modules/playwright');
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const pg = await b.newPage();
  await pg.goto('file://' + path.join(SRC, 'day.html'), { waitUntil: 'networkidle' });
  await pg.evaluate(async () => { await Promise.all([...document.fonts].map(f => f.load().catch(() => null))); await document.fonts.ready; });
  await pg.pdf({ path: path.join(SRC, '..', OUT), format: 'A4', printBackground: true, preferCSSPageSize: true, margin: {top: 0, bottom: 0, left: 0, right: 0} });
  await b.close(); console.log('PDF fertig');
})();
