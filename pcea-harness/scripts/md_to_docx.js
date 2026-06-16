#!/usr/bin/env node
/*
 * md_to_docx.js — PCEA 보고서 변환기 (docx 스킬 docx-js 방식)
 *
 * work/output 의 patent_claims_report.md 를 Word(.docx) 로 변환한다.
 * 설계 의도:
 *   - [VERBATIM] 청구항(``` 코드블록)은 모노스페이스 + 음영 블록으로 렌더해
 *     분석 산문과 시각적으로 분리한다(청구항 원문 불변 원칙의 시각화).
 *   - 표지에 분석 대상 약물/특허 수/검증 통과·미검증 수/생성일을 넣는다.
 *   - 텍스트는 변형하지 않는다 — 마크다운 구조만 docx 구조로 매핑.
 *
 * 사용법: node scripts/md_to_docx.js <input.md> <output.docx>
 */
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType,
  PageBreak, LevelFormat, TableOfContents,
} = require("docx");

const [, , inPath, outPath] = process.argv;
if (!inPath || !outPath) {
  console.error("usage: node md_to_docx.js <input.md> <output.docx>");
  process.exit(2);
}
const md = fs.readFileSync(inPath, "utf8");
const lines = md.split(/\r?\n/);

const CONTENT_WIDTH = 9360; // US Letter, 1" margins

// ---- inline parsing: **bold** and `code` ----
function parseInline(text, baseOpts = {}) {
  const runs = [];
  // tokenize on ** and `
  const re = /(\*\*[^*]+\*\*|`[^`]+`)/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) runs.push(new TextRun({ text: text.slice(last, m.index), ...baseOpts }));
    const tok = m[0];
    if (tok.startsWith("**")) {
      runs.push(new TextRun({ text: tok.slice(2, -2), bold: true, ...baseOpts }));
    } else {
      runs.push(new TextRun({ text: tok.slice(1, -1), font: "Courier New", ...baseOpts }));
    }
    last = re.lastIndex;
  }
  if (last < text.length) runs.push(new TextRun({ text: text.slice(last), ...baseOpts }));
  if (runs.length === 0) runs.push(new TextRun({ text: "", ...baseOpts }));
  return runs;
}

function makeTable(rows) {
  // rows: array of arrays of cell strings; first row is header
  const ncol = Math.max(...rows.map((r) => r.length));
  // proportional column widths based on max content length (so long cells get room)
  const colMax = Array(ncol).fill(1);
  for (const r of rows) {
    for (let ci = 0; ci < ncol; ci++) {
      const len = (r[ci] !== undefined ? r[ci] : "").length;
      if (len > colMax[ci]) colMax[ci] = len;
    }
  }
  // cap weight so one column can't fully starve others, but long text still dominates
  const weights = colMax.map((l) => Math.min(l, 140) + 4);
  const tot = weights.reduce((a, b) => a + b, 0);
  let colWidths = weights.map((w) => Math.round((CONTENT_WIDTH * w) / tot));
  const MIN = 760;
  // enforce minimum width by borrowing from the widest column
  let widest = colWidths.indexOf(Math.max(...colWidths));
  for (let i = 0; i < ncol; i++) {
    if (i !== widest && colWidths[i] < MIN) {
      colWidths[widest] -= MIN - colWidths[i];
      colWidths[i] = MIN;
    }
  }
  // fix rounding so widths sum exactly to CONTENT_WIDTH
  widest = colWidths.indexOf(Math.max(...colWidths));
  colWidths[widest] += CONTENT_WIDTH - colWidths.reduce((a, b) => a + b, 0);
  const border = { style: BorderStyle.SINGLE, size: 1, color: "BBBBBB" };
  const borders = { top: border, bottom: border, left: border, right: border };
  const trows = rows.map((cells, ri) =>
    new TableRow({
      children: Array.from({ length: ncol }, (_, ci) => {
        const txt = cells[ci] !== undefined ? cells[ci] : "";
        return new TableCell({
          borders,
          width: { size: colWidths[ci], type: WidthType.DXA },
          shading: ri === 0
            ? { fill: "D5E8F0", type: ShadingType.CLEAR }
            : { fill: "FFFFFF", type: ShadingType.CLEAR },
          margins: { top: 60, bottom: 60, left: 100, right: 100 },
          children: [new Paragraph({ children: parseInline(txt, { size: 18 }) })],
        });
      }),
    })
  );
  return new Table({
    width: { size: CONTENT_WIDTH, type: WidthType.DXA },
    columnWidths: colWidths,
    rows: trows,
  });
}

const children = [];

// ---------- Cover page ----------
function coverLine(text, opts = {}) {
  return new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 }, children: [new TextRun({ text, ...opts })] });
}
children.push(new Paragraph({ spacing: { before: 2400 } }));
children.push(coverLine("특허 청구항 추출·검증·분석 보고서", { bold: true, size: 44 }));
children.push(coverLine("Patent Claim Extraction & Analysis Report (PCEA)", { size: 24, color: "555555" }));
children.push(new Paragraph({ spacing: { before: 480 } }));
children.push(coverLine("분석 대상: ICOTYDE™ / icotrokinra / JNJ-2113 / PN-235", { bold: true, size: 28 }));
children.push(coverLine("경구용 IL-23 수용체 길항 거대고리 펩타이드 (Protagonist Therapeutics + Janssen / J&J)", { size: 20, color: "555555" }));
children.push(new Paragraph({ spacing: { before: 480 } }));
children.push(coverLine("분석 후보 특허: 27건 (진짜 패밀리 18 · 오귀속/무관 8, US11180535B2 이중분류)", { size: 22 }));
children.push(coverLine("✅ 검증 통과: 1건 (US11939361B2)   ·   ⚠ 미검증/부분/검증불가: 다수", { size: 22 }));
children.push(coverLine("핵심 물질: icotrokinra = SEQ ID NO: 1 (조성물 특허 US11939361B2)", { size: 22 }));
children.push(new Paragraph({ spacing: { before: 360 } }));
children.push(coverLine("생성일: 2026-06-15", { size: 22, bold: true }));
children.push(coverLine("소스 제약: WIPO/Espacenet/Google Patents 차단 — FreePatentsOnline 단일 소스 (cross_source=false)", { size: 16, color: "888888", italics: true }));
children.push(coverLine("청구항 원문은 어떤 단계에서도 번역·교정·재배열되지 않았습니다 (verbatim).", { size: 16, color: "888888", italics: true }));
children.push(new Paragraph({ children: [new PageBreak()] }));

// ---------- Body parsing ----------
let i = 0;
let tableBuf = null;

function flushTable() {
  if (tableBuf && tableBuf.length) {
    // drop the separator row (---)
    const rows = tableBuf.filter((r) => !/^[-:\s|]+$/.test(r.join("")));
    if (rows.length) children.push(makeTable(rows));
    children.push(new Paragraph({ spacing: { after: 80 } }));
  }
  tableBuf = null;
}

while (i < lines.length) {
  const line = lines[i];

  // fenced code block (verbatim)
  if (/^```/.test(line)) {
    flushTable();
    i++;
    const code = [];
    while (i < lines.length && !/^```/.test(lines[i])) { code.push(lines[i]); i++; }
    i++; // closing fence
    for (const cl of code) {
      children.push(new Paragraph({
        shading: { fill: "F0F0F0", type: ShadingType.CLEAR },
        spacing: { after: 0 },
        border: { left: { style: BorderStyle.SINGLE, size: 12, color: "8AB4D8", space: 6 } },
        children: [new TextRun({ text: cl === "" ? " " : cl, font: "Courier New", size: 17 })],
      }));
    }
    children.push(new Paragraph({ spacing: { after: 80 } }));
    continue;
  }

  // table rows
  if (/^\s*\|.*\|\s*$/.test(line)) {
    if (!tableBuf) tableBuf = [];
    tableBuf.push(line.trim().replace(/^\|/, "").replace(/\|$/, "").split("|").map((c) => c.trim()));
    i++;
    continue;
  } else if (tableBuf) {
    flushTable();
  }

  // headings
  let mh;
  if ((mh = line.match(/^#\s+(.*)/))) {
    children.push(new Paragraph({ heading: HeadingLevel.HEADING_1, children: parseInline(mh[1]) }));
  } else if ((mh = line.match(/^##\s+(.*)/))) {
    children.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: parseInline(mh[1]) }));
  } else if ((mh = line.match(/^###\s+(.*)/))) {
    children.push(new Paragraph({ heading: HeadingLevel.HEADING_3, children: parseInline(mh[1]) }));
  } else if ((mh = line.match(/^####\s+(.*)/))) {
    children.push(new Paragraph({ heading: HeadingLevel.HEADING_4, children: parseInline(mh[1]) }));
  } else if (/^---+\s*$/.test(line) || /^___+\s*$/.test(line)) {
    children.push(new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "2E75B6", space: 1 } }, spacing: { after: 80 } }));
  } else if ((mh = line.match(/^>\s?(.*)/))) {
    children.push(new Paragraph({ indent: { left: 480 }, shading: { fill: "FBF6E8", type: ShadingType.CLEAR }, children: parseInline(mh[1], { italics: true }) }));
  } else if ((mh = line.match(/^\s*[-*]\s+(.*)/))) {
    children.push(new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: parseInline(mh[1]) }));
  } else if ((mh = line.match(/^\s*(\d+)\.\s+(.*)/))) {
    children.push(new Paragraph({ numbering: { reference: "numbers", level: 0 }, children: parseInline(mh[2]) }));
  } else if (line.trim() === "") {
    children.push(new Paragraph({ spacing: { after: 60 } }));
  } else {
    children.push(new Paragraph({ spacing: { after: 60 }, children: parseInline(line) }));
  }
  i++;
}
flushTable();

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 20 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, font: "Arial", color: "1F3864" },
        paragraph: { spacing: { before: 280, after: 160 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: "Arial", color: "2E5496" },
        paragraph: { spacing: { before: 220, after: 120 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, font: "Arial", color: "2E5496" },
        paragraph: { spacing: { before: 180, after: 100 }, outlineLevel: 2 } },
      { id: "Heading4", name: "Heading 4", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 22, bold: true, font: "Arial", color: "555555" },
        paragraph: { spacing: { before: 140, after: 80 }, outlineLevel: 3 } },
    ],
  },
  numbering: {
    config: [
      { reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 560, hanging: 280 } } } }] },
      { reference: "numbers", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 560, hanging: 280 } } } }] },
    ],
  },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(outPath, buf); console.log("wrote", outPath, buf.length, "bytes"); });
