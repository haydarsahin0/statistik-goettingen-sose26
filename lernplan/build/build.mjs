/**
 * Lernplan-Builder
 * -----------------------------------------------------------
 * Baut aus den HTML-Quellen in ../src fertige PDFs in ../pdf.
 *
 *   node build/build.mjs            -> alle Dateien
 *   node build/build.mjs tag-01     -> nur eine Datei
 *
 * Mathe wird mit KaTeX gesetzt:  \( ... \) inline,  \[ ... \] abgesetzt.
 * Innerhalb von <pre>-Blöcken (R-Code) wird nichts ersetzt.
 */

import { readFileSync, writeFileSync, readdirSync, mkdirSync, existsSync } from 'node:fs';
import { dirname, join, basename } from 'node:path';
import { fileURLToPath } from 'node:url';
import katex from 'katex';
import { chromium } from 'playwright-core';

const HERE = dirname(fileURLToPath(import.meta.url));
const SRC = join(HERE, '..', 'src');
const OUT = join(HERE, '..', 'pdf');
const TMP = join(HERE, '.tmp');

const CHROME = process.env.CHROME_PATH || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

const fontsCss = readFileSync(join(HERE, 'assets', 'fonts.css'), 'utf8');
const katexCss = readFileSync(join(HERE, 'assets', 'katex.css'), 'utf8');
const themeCss = readFileSync(join(HERE, 'theme.css'), 'utf8');

/* ---------- Mathe rendern (außerhalb von <pre>) ---------- */

function renderMathSegment(text) {
  // abgesetzte Formeln:  \[ ... \]
  text = text.replace(/\\\[([\s\S]+?)\\\]/g, (_, tex) =>
    katex.renderToString(tex.trim(), { displayMode: true, throwOnError: true, strict: false })
  );
  // Formeln im Text:  \( ... \)
  text = text.replace(/\\\(([\s\S]+?)\\\)/g, (_, tex) =>
    katex.renderToString(tex.trim(), { displayMode: false, throwOnError: true, strict: false })
  );
  return text;
}

function renderMath(html) {
  // <pre>-Blöcke herausschneiden, damit R-Code ($, \) unangetastet bleibt
  const parts = html.split(/(<pre[\s\S]*?<\/pre>)/g);
  return parts.map((p) => (p.startsWith('<pre') ? p : renderMathSegment(p))).join('');
}

/* ---------- Front-Matter lesen ---------- */

function parseSource(raw) {
  const m = raw.match(/^<!--meta\s*([\s\S]*?)-->\s*/);
  if (!m) throw new Error('Front-Matter <!--meta {...} --> fehlt.');
  return { meta: JSON.parse(m[1]), body: raw.slice(m[0].length) };
}

/* ---------- HTML-Seite zusammensetzen ---------- */

function buildHtml(meta, body) {
  return `<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<title>${meta.title}</title>
<style>${fontsCss}</style>
<style>${katexCss}</style>
<style>${themeCss}</style>
</head>
<body>
${renderMath(body)}
</body>
</html>`;
}

/* ---------- Fuߟzeile ---------- */

const footerTemplate = (meta) => `
<div style="width:100%;font-family:'Helvetica',sans-serif;font-size:7.2pt;color:#9A93AC;
            padding:0 16mm;display:flex;justify-content:space-between;align-items:center;">
  <span style="letter-spacing:0.06em;">${meta.footer || meta.title}</span>
  <span>Seite <span class="pageNumber"></span> / <span class="totalPages"></span></span>
</div>`;

/* ---------- Hauptlauf ---------- */

const only = process.argv[2];
for (const d of [OUT, TMP]) if (!existsSync(d)) mkdirSync(d, { recursive: true });

const files = readdirSync(SRC)
  .filter((f) => f.endsWith('.html'))
  .filter((f) => !only || basename(f, '.html') === only)
  .sort();

if (files.length === 0) {
  console.error('Keine Quelldateien gefunden' + (only ? ` für "${only}".` : '.'));
  process.exit(1);
}

const browser = await chromium.launch({ executablePath: CHROME, args: ['--no-sandbox'] });
const page = await browser.newPage();

for (const file of files) {
  const { meta, body } = parseSource(readFileSync(join(SRC, file), 'utf8'));
  const htmlPath = join(TMP, file);
  writeFileSync(htmlPath, buildHtml(meta, body));

  await page.goto('file://' + htmlPath, { waitUntil: 'load' });
  await page.emulateMedia({ media: 'print' });

  const pdfPath = join(OUT, meta.out);
  await page.pdf({
    path: pdfPath,
    format: 'A4',
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: footerTemplate(meta),
    margin: { top: '16mm', bottom: '15mm', left: '16mm', right: '16mm' },
  });

  console.log(`✓ ${meta.out}`);
}

await browser.close();
