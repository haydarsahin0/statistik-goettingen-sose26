// Gemeinsame Bausteine für die Word-Formelsammlungen (docx-js)
const fs = require('fs');
const D = require('docx');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType,
  BorderStyle, AlignmentType, LevelFormat, Footer, PageNumber, HeadingLevel, PageBreak } = D;

const PAGE_W = 11906, MARGIN = 850, CONTENT_W = PAGE_W - 2 * MARGIN; // A4, 1.5 cm Rand
const PALETTE = ['1F4E79', '7030A0', 'C55A11', '2E7D32', 'AD1457', '00838F', '6A1B9A', 'B71C1C', '283593', '00695C', '8D6E00', '4E342E', '1565C0', '558B2F', '880E4F', '37474F'];
const BOXES = {
  retter: { fill: 'FFF4CC', line: 'E0A800', label: '★ PUNKTE-RETTER: ' },
  satz:   { fill: 'E8F5E9', line: '2E7D32', label: '✎ ANTWORTSATZ: ' },
  falle:  { fill: 'FDECEA', line: 'C62828', label: '⚠ FALLE: ' },
  tr:     { fill: 'E0F2F1', line: '00796B', label: 'TR: ' },
  tipp:   { fill: 'E3F2FD', line: '1565C0', label: '➜ REZEPT: ' },
};

// **fett** und `code` im Text
function runs(text, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|`[^`]+`|\^\{[^}]*\}|_\{[^}]*\})/g;
  let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    const t = m[0];
    if (t.startsWith('**')) out.push(new TextRun({ text: t.slice(2, -2), bold: true, ...base }));
    else if (t.startsWith('^{')) out.push(new TextRun({ text: t.slice(2, -1), superScript: true, ...base }));
    else if (t.startsWith('_{')) out.push(new TextRun({ text: t.slice(2, -1), subScript: true, ...base }));
    else out.push(new TextRun({ text: t.slice(1, -1), font: 'Consolas', size: 19, color: '0B3D2E', ...base }));
    last = m.index + t.length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), ...base }));
  return out;
}

class Book {
  constructor(title) { this.title = title; this.kids = []; this.ch = 0; this.color = PALETTE[0]; }
  h1(text) {
    this.color = PALETTE[this.ch % PALETTE.length]; this.ch++;
    this.kids.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: this.ch > 1 && this.breakEach !== false,
      shading: { type: ShadingType.CLEAR, fill: this.color, color: 'auto' }, spacing: { before: 120, after: 160 },
      children: [new TextRun({ text: ' ' + text, bold: true, color: 'FFFFFF', size: 32, font: 'Calibri' })] }));
  }
  h2(text) {
    this.kids.push(new Paragraph({ heading: HeadingLevel.HEADING_2, keepNext: true, spacing: { before: 200, after: 80 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: this.color, space: 2 } },
      children: runs(text, { bold: true, color: this.color, size: 25, font: 'Calibri' }) }));
  }
  h3(text) {
    this.kids.push(new Paragraph({ keepNext: true, spacing: { before: 120, after: 40 },
      children: [new TextRun({ text, bold: true, color: this.color, size: 21 })] }));
  }
  p(text) { this.kids.push(new Paragraph({ spacing: { after: 70 }, children: runs(text) })); }
  // Formelblock: jede Zeile eigener Absatz, Cambria Math, schattiert
  f(...lines) {
    lines.forEach((l, i) => this.kids.push(new Paragraph({ keepNext: i < lines.length - 1, keepLines: true,
      shading: { type: ShadingType.CLEAR, fill: 'F3F4F8', color: 'auto' }, indent: { left: 200, right: 200 },
      border: { left: { style: BorderStyle.SINGLE, size: 18, color: this.color, space: 6 } },
      spacing: { before: i ? 0 : 60, after: i === lines.length - 1 ? 90 : 0, line: 300 },
      children: runs(l, { font: 'Cambria Math', size: 22 }) })));
  }
  ul(items) { items.forEach(t => this.kids.push(new Paragraph({ numbering: { reference: 'bul', level: 0 }, spacing: { after: 30 }, children: runs(t) }))); }
  ol(items) {
    const ref = 'num' + (this.numCount = (this.numCount || 0) + 1);
    (this.numRefs = this.numRefs || []).push(ref);
    items.forEach(t => this.kids.push(new Paragraph({ numbering: { reference: ref, level: 0 }, spacing: { after: 30 }, children: runs(t) })));
  }
  box(type, ...lines) {
    const b = BOXES[type];
    lines.forEach((l, i) => this.kids.push(new Paragraph({ keepNext: i < lines.length - 1, keepLines: true,
      shading: { type: ShadingType.CLEAR, fill: b.fill, color: 'auto' }, indent: { left: 120, right: 120 },
      border: { left: { style: BorderStyle.SINGLE, size: 24, color: b.line, space: 6 } },
      spacing: { before: i ? 0 : 80, after: i === lines.length - 1 ? 100 : 0 },
      children: [...(i === 0 ? [new TextRun({ text: b.label, bold: true, color: b.line })] : []), ...runs(l, type === 'tr' ? { italics: true } : {})] })));
  }
  code(lines) {
    lines.forEach((l, i) => this.kids.push(new Paragraph({ keepLines: true, keepNext: i < lines.length - 1,
      shading: { type: ShadingType.CLEAR, fill: '1E293B', color: 'auto' }, indent: { left: 120, right: 120 },
      spacing: { before: i ? 0 : 60, after: i === lines.length - 1 ? 100 : 0, line: 260 },
      children: [new TextRun({ text: l || ' ', font: 'Consolas', size: 18, color: l.trim().startsWith('#') ? '94A3B8' : (l.trim().startsWith('[') || l.trim().startsWith('##') ? 'A7F3D0' : 'F1F5F9') })] })));
  }
  table(head, rows, widths) {
    const tot = widths.reduce((a, b) => a + b, 0);
    const w = widths.map(x => Math.round(x / tot * CONTENT_W));
    w[w.length - 1] += CONTENT_W - w.reduce((a, b) => a + b, 0);
    const border = { style: BorderStyle.SINGLE, size: 4, color: 'C9CED6' };
    const borders = { top: border, bottom: border, left: border, right: border };
    const cell = (t, i, hdr, alt) => new TableCell({ width: { size: w[i], type: WidthType.DXA }, borders,
      shading: { type: ShadingType.CLEAR, fill: hdr ? this.color : (alt ? 'F7F8FB' : 'FFFFFF'), color: 'auto' },
      margins: { top: 50, bottom: 50, left: 90, right: 90 },
      children: String(t).split('\n').map(line => new Paragraph({ children: runs(line, hdr ? { bold: true, color: 'FFFFFF', size: 20 } : { size: 20 }) })) });
    this.kids.push(new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: w,
      rows: [new TableRow({ tableHeader: true, children: head.map((h, i) => cell(h, i, true)) }),
        ...rows.map((r, ri) => new TableRow({ cantSplit: true, children: r.map((c, i) => cell(c, i, false, ri % 2)) }))] }));
    this.kids.push(new Paragraph({ spacing: { after: 60 }, children: [] }));
  }
  pagebreak() { this.kids.push(new Paragraph({ children: [new PageBreak()] })); }
  cover(title, sub, lines) {
    this.kids.push(new Paragraph({ spacing: { before: 1800, after: 200 }, alignment: AlignmentType.LEFT,
      children: [new TextRun({ text: title, bold: true, size: 64, color: PALETTE[0] })] }));
    this.kids.push(new Paragraph({ spacing: { after: 400 }, children: [new TextRun({ text: sub, size: 28, color: '555555' })] }));
    lines.forEach(l => this.kids.push(new Paragraph({ spacing: { after: 80 }, children: runs(l, { size: 22 }) })));
  }
  toc(entries) {
    this.kids.push(new Paragraph({ spacing: { before: 200, after: 120 }, children: [new TextRun({ text: 'Inhaltsverzeichnis', bold: true, size: 30, color: PALETTE[0] })] }));
    entries.forEach((e, i) => this.kids.push(new Paragraph({ spacing: { after: 40 },
      children: [new TextRun({ text: e, size: 22, color: PALETTE[(i + 1) % PALETTE.length], bold: !/^\s/.test(e) })] })));
  }
  async save(file) {
    const numbering = { config: [
      { reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 460, hanging: 260 } } } }] },
      ...(this.numRefs || []).map(r => ({ reference: r, levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 460, hanging: 300 } } } }] }))] };
    const doc = new Document({
      creator: 'Lernpaket', title: this.title,
      styles: { default: { document: { run: { font: 'Calibri', size: 21 } } },
        paragraphStyles: [
          { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 32, bold: true }, paragraph: { outlineLevel: 0 } },
          { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 25, bold: true }, paragraph: { outlineLevel: 1 } }] },
      numbering,
      sections: [{ properties: { page: { size: { width: PAGE_W, height: 16838 }, margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN } } },
        footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT,
          children: [new TextRun({ text: this.title + '  ·  Seite ', size: 16, color: '888888' }), new TextRun({ children: [PageNumber.CURRENT], size: 16, color: '888888' })] })] }) },
        children: this.kids }] });
    fs.writeFileSync(file, await Packer.toBuffer(doc));
  }
}
module.exports = { Book };
