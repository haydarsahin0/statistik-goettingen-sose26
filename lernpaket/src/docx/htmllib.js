// HTML/PDF-Version der Formelsammlungen (gleiche API wie fslib.js), gedruckt mit Chromium
const fs = require('fs'), path = require('path');
const SRC = path.join(__dirname, '..');
const PALETTE = ['1F4E79', '7030A0', 'C55A11', '2E7D32', 'AD1457', '00838F', '6A1B9A', 'B71C1C', '283593', '00695C', '8D6E00', '4E342E', '1565C0', '558B2F', '880E4F', '37474F'];
const BOX = { retter: ['retter', '★ Punkte-Retter'], satz: ['satz', '✎ Antwortsatz'], falle: ['falle', '⚠ Falle'], tr: ['tr', 'TR'], tipp: ['tipp', '➜ Rezept'] };

const esc = t => String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
function inl(t) {
  let s = esc(t);
  s = s.replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>').replace(/`([^`]+)`/g, '<code>$1</code>');
  s = s.replace(/\^\{([^}]*)\}/g, '<sup>$1</sup>').replace(/_\{([^}]*)\}/g, '<sub>$1</sub>');
  s = s.split(/(<code>[\s\S]*?<\/code>)/).map(part => part.startsWith('<code>') ? part :
    part.replace(/([A-Za-zα-ωΑ-Ω²*̂̄)])_([A-Za-z0-9α-ω.]+)/g, '$1<sub>$2</sub>')).join('');
  return s;
}

class Book {
  constructor(title) { this.title = title; this.out = []; this.ch = 0; this.color = PALETTE[0]; this.chapters = []; }
  h1(text) {
    this.color = PALETTE[this.ch % PALETTE.length]; this.ch++;
    const m = text.match(/^(\d+)\s+(.*)$/); const num = m ? m[1] : '', rest = m ? m[2] : text;
    const id = 'k' + this.ch; this.chapters.push({ id, num, text: rest, color: this.color });
    this.out.push(`</section><section class="chap" style="--c:#${this.color}"><h1 id="${id}"><span class="num">${num}</span><span class="t">${inl(rest)}</span></h1>`);
  }
  h2(t) { this.out.push(`<h2>${inl(t)}</h2>`); }
  h3(t) { this.out.push(`<h3>${inl(t)}</h3>`); }
  p(t) { this.out.push(`<p>${inl(t)}</p>`); }
  f(...lines) { this.out.push(`<div class="fm">${lines.map(l => `<div>${inl(l)}</div>`).join('')}</div>`); }
  ul(items) { this.out.push(`<ul>${items.map(i => `<li>${inl(i)}</li>`).join('')}</ul>`); }
  ol(items) { this.out.push(`<ol>${items.map(i => `<li>${inl(i)}</li>`).join('')}</ol>`); }
  box(type, ...lines) { const [c, l] = BOX[type]; this.out.push(`<div class="box ${c}"><div class="bl">${l}</div>${lines.map(x => `<div>${inl(x)}</div>`).join('')}</div>`); }
  ex(title, task, steps, result) {
    this.out.push(`<div class="ex"><div class="exh"><span>Beispiel – Schritt für Schritt</span>${inl(title)}</div>` +
      (task ? `<div class="ext">${inl(task)}</div>` : '') +
      `<ol class="steps">${steps.map(s => `<li>${inl(s)}</li>`).join('')}</ol>` + (result ? `<div class="exr">${inl(result)}</div>` : '') + `</div>`);
  }
  code(lines) {
    this.out.push(`<pre class="code">${lines.map(l => { const e = esc(l || ' ');
      if (/^\s*#/.test(l)) return `<span class="c">${e}</span>`;
      if (/^\s*\[\d+\]/.test(l) || /^\s{2,}\S/.test(l) && !/[<(=]/.test(l)) return `<span class="o">${e}</span>`;
      return e.replace(/(#.*)$/, '<span class="c">$1</span>'); }).join('\n')}</pre>`);
  }
  table(head, rows, widths) {
    const tot = widths.reduce((a, b) => a + b, 0);
    this.out.push(`<table class="t"><colgroup>${widths.map(w => `<col style="width:${(w / tot * 100).toFixed(2)}%">`).join('')}</colgroup>` +
      `<thead><tr>${head.map(h => `<th>${inl(h)}</th>`).join('')}</tr></thead><tbody>` +
      rows.map(r => `<tr>${r.map(c => `<td>${String(c).split('\n').map(inl).join('<br>')}</td>`).join('')}</tr>`).join('') + `</tbody></table>`);
  }
  pagebreak() { this.out.push('<div class="pb"></div>'); }
  cover(title, sub, lines) { this.coverHtml = { title, sub, lines }; }
  toc(entries) { this.tocEntries = entries; }
  render(pages) {
    const c = this.coverHtml;
    const cover = `<section class="cover"><div class="cv-top"><div class="chip">Statistik und Data Science I · Göttingen · Zweittermin 09.10.2026</div>
      <h1>${inl(c.title)}</h1><div class="sub">${inl(c.sub)}</div></div>
      <div class="cv-legend"><div class="lg retter">★ Punkte-Retter</div><div class="lg tipp">➜ Rezept</div><div class="lg ex2">Beispiel Schritt für Schritt</div><div class="lg satz">✎ Antwortsatz</div><div class="lg falle">⚠ Falle</div><div class="lg tr">TR Türkçe</div></div>
      <div class="cv-lines">${c.lines.map(l => `<p>${inl(l)}</p>`).join('')}</div></section>`;
    const toc = `<section class="tocp"><h2 class="toch">Inhalt</h2><div class="toc">${this.chapters.map(k =>
      `<a href="#${k.id}" style="--c:#${k.color}"><span class="tn">${k.num}</span><span class="tt">${inl(k.text)}</span><span class="dots"></span><span class="tp">${pages && pages[k.id] ? pages[k.id] : '00'}</span></a>`).join('')}</div></section>`;
    const css = fs.readFileSync(path.join(__dirname, 'fsbook.css'), 'utf8');
    return `<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><base href="file://${SRC}/">
<link rel="stylesheet" href="fonts.css"><link rel="stylesheet" href="fonts_day.css"><style>${css}</style></head>
<body>${cover}${toc}<section>${this.out.join('\n')}</section></body></html>`;
  }
  async save(file) {
    file = file.replace(/\.docx$/, '.pdf');
    const { chromium } = require('/opt/node22/lib/node_modules/playwright');
    const br = await chromium.launch({ executablePath: process.env.CHROME || undefined });
    const pg = await br.newPage();
    const tmp = path.join(SRC, '_fsbook.html');
    const opts = { path: file, format: 'A4', printBackground: true, displayHeaderFooter: true, margin: { top: '13mm', bottom: '15mm', left: '13mm', right: '13mm' },
      headerTemplate: '<div></div>',
      footerTemplate: `<div style="width:100%;font-family:Helvetica,Arial;font-size:7.5px;color:#8a8f98;padding:0 13mm;display:flex;justify-content:space-between"><span>${this.title}</span><span>Seite <span class="pageNumber"></span> / <span class="totalPages"></span></span></div>` };
    const run = async pages => {
      fs.writeFileSync(tmp, this.render(pages));
      await pg.goto('file://' + tmp, { waitUntil: 'load' });
      await pg.evaluate(async () => { await Promise.all([...document.fonts].map(f => f.load().catch(() => null))); await document.fonts.ready; });
      await pg.pdf(opts);
    };
    await run(null);
    // Seitenzahlen der Kapitel aus dem PDF lesen (Python/pymupdf) und zweiten Durchlauf drucken
    const { execFileSync } = require('child_process');
    const titles = this.chapters.map(k => k.id + '\t' + k.num + '\t' + k.text);
    const py = `import sys,pymupdf,json\nd=pymupdf.open(sys.argv[1]);res={}\nfor line in sys.stdin.read().splitlines():\n  i,n,t=line.split('\\t');key=(n+' ').strip()\n  for p in range(2,len(d)):\n    tx=d[p].get_text()\n    if t[:25] in tx and (n=='' or tx.lstrip().startswith(n) or ('\\n'+n+'\\n') in ('\\n'+tx)):\n      res[i]=p+1;break\nprint(json.dumps(res))`;
    const pages = JSON.parse(execFileSync('python3', ['-c', py, file], { input: titles.join('\n') }).toString());
    await run(pages);
    await br.close(); fs.unlinkSync(tmp);
  }
}
module.exports = { Book };
