#!/usr/bin/env python3
"""Build AFM_Complete_Exam_Notes.pdf from AFM_Exam_Notes.md.

The builder is deliberately single-file and deterministic. It performs no network
access and uses only ReportLab plus fonts already installed on the system.
"""

from __future__ import annotations

import hashlib
import html
import os
import re
import sys
from functools import partial
from pathlib import Path

# ReportLab honours SOURCE_DATE_EPOCH when creating metadata and document IDs.
# A fixed value makes byte-for-byte rebuilds deterministic.
os.environ["SOURCE_DATE_EPOCH"] = "946684800"

try:
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (
        BaseDocTemplate,
        Frame,
        KeepTogether,
        ListFlowable,
        ListItem,
        LongTable,
        NextPageTemplate,
        PageBreak,
        PageTemplate,
        Paragraph,
        Spacer,
        Table,
        TableStyle,
    )
    from reportlab.platypus.tableofcontents import TableOfContents
    from reportlab.pdfgen import canvas
except ImportError as exc:  # pragma: no cover - clear local setup error
    raise SystemExit(
        "ReportLab is required. Install it in the active Python environment with "
        "'python -m pip install reportlab'."
    ) from exc

ROOT = Path(__file__).resolve().parent
MARKDOWN_PATH = ROOT / "AFM_Exam_Notes.md"
OUTPUT_PATH = ROOT / "AFM_Complete_Exam_Notes.pdf"
TITLE = "Advanced Financial Management — Complete Exam Notes"
AUTHOR = "Prepared from uploaded course materials"
SHORT_TITLE = "AFM — Complete Exam Notes"
PAGE_WIDTH, PAGE_HEIGHT = A4
BLACK = colors.Color(0, 0, 0)
WHITE = colors.Color(1, 1, 1)


def find_font(candidates: list[str]) -> Path:
    for candidate in candidates:
        path = Path(candidate)
        if path.is_file():
            return path
    raise FileNotFoundError("No suitable Unicode TrueType font was found on this system.")


def register_fonts() -> None:
    regular = find_font(
        [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/google-noto/NotoSans-Regular.ttf",
            "/usr/share/fonts/google-noto-vf/NotoSans[wght].ttf",
        ]
    )
    bold = find_font(
        [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/google-noto/NotoSans-Bold.ttf",
            "/usr/share/fonts/google-noto-vf/NotoSans[wght].ttf",
        ]
    )
    italic = find_font(
        [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf",
            "/usr/share/fonts/google-noto/NotoSans-Italic.ttf",
            str(regular),
        ]
    )
    bold_italic = find_font(
        [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf",
            "/usr/share/fonts/google-noto/NotoSans-BoldItalic.ttf",
            str(bold),
        ]
    )
    pdfmetrics.registerFont(TTFont("AFMSans", str(regular)))
    pdfmetrics.registerFont(TTFont("AFMSans-Bold", str(bold)))
    pdfmetrics.registerFont(TTFont("AFMSans-Italic", str(italic)))
    pdfmetrics.registerFont(TTFont("AFMSans-BoldItalic", str(bold_italic)))
    pdfmetrics.registerFontFamily(
        "AFMSans",
        normal="AFMSans",
        bold="AFMSans-Bold",
        italic="AFMSans-Italic",
        boldItalic="AFMSans-BoldItalic",
    )


class HeadingParagraph(Paragraph):
    """Paragraph carrying TOC and bookmark metadata."""

    def __init__(self, text: str, style: ParagraphStyle, level: int, key: str):
        super().__init__(text, style)
        self.toc_level = level
        self.bookmark_key = key
        self.plain_heading = re.sub(r"<[^>]+>", "", text)


class AFMDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str):
        super().__init__(
            filename,
            pagesize=A4,
            leftMargin=23.5 * mm,
            rightMargin=23.5 * mm,
            topMargin=23 * mm,
            bottomMargin=22 * mm,
            title=TITLE,
            author=AUTHOR,
            subject="Exam-ready Advanced Financial Management notes based on uploaded course materials",
            creator="Deterministic ReportLab AFM notes builder",
            keywords="AFM, finance, capital structure, investment appraisal, risk, working capital, mergers",
        )
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="body",
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        self.addPageTemplates(
            [PageTemplate(id="normal", frames=[frame], onPage=self.draw_header_footer)]
        )

    def draw_header_footer(self, canv: canvas.Canvas, doc: "AFMDocTemplate") -> None:
        canv.saveState()
        canv.setFillColor(BLACK)
        canv.setStrokeColor(BLACK)
        canv.setLineWidth(0.45)
        canv.setFont("AFMSans", 7.8)
        header_y = PAGE_HEIGHT - 11.5 * mm
        canv.drawString(self.leftMargin, header_y, SHORT_TITLE)
        canv.line(self.leftMargin, header_y - 2.2 * mm, PAGE_WIDTH - self.rightMargin, header_y - 2.2 * mm)
        footer_y = 9.5 * mm
        canv.line(self.leftMargin, footer_y + 3.5 * mm, PAGE_WIDTH - self.rightMargin, footer_y + 3.5 * mm)
        page_label = f"Page {doc.page}"
        canv.drawRightString(PAGE_WIDTH - self.rightMargin, footer_y, page_label)
        canv.restoreState()

    def afterFlowable(self, flowable) -> None:  # noqa: N802 (ReportLab API)
        if not isinstance(flowable, HeadingParagraph):
            return
        level = flowable.toc_level
        key = flowable.bookmark_key
        text = flowable.plain_heading
        self.canv.bookmarkPage(key)
        # Bookmarks are useful for the six modules and end matter, while TOC uses H1/H2.
        if level == 0:
            self.canv.addOutlineEntry(text, key, level=0, closed=False)
        if level <= 1:
            self.notify("TOCEntry", (level, text, self.page, key))


def make_styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    styles: dict[str, ParagraphStyle] = {}
    styles["body"] = ParagraphStyle(
        "AFMBody",
        parent=base["BodyText"],
        fontName="AFMSans",
        fontSize=10.2,
        leading=15.8,
        textColor=BLACK,
        spaceAfter=6.2,
        alignment=TA_LEFT,
        splitLongWords=True,
        allowWidows=0,
        allowOrphans=0,
    )
    styles["title"] = ParagraphStyle(
        "AFMTitle",
        parent=styles["body"],
        fontName="AFMSans-Bold",
        fontSize=20,
        leading=24,
        spaceBefore=3 * mm,
        spaceAfter=5 * mm,
        keepWithNext=True,
    )
    styles["h1"] = ParagraphStyle(
        "AFMH1",
        parent=styles["body"],
        fontName="AFMSans-Bold",
        fontSize=15,
        leading=18,
        spaceBefore=5 * mm,
        spaceAfter=2.5 * mm,
        keepWithNext=True,
        borderWidth=0,
    )
    styles["h2"] = ParagraphStyle(
        "AFMH2",
        parent=styles["body"],
        fontName="AFMSans-Bold",
        fontSize=12.2,
        leading=15,
        spaceBefore=3.5 * mm,
        spaceAfter=1.6 * mm,
        keepWithNext=True,
    )
    styles["h3"] = ParagraphStyle(
        "AFMH3",
        parent=styles["body"],
        fontName="AFMSans-Bold",
        fontSize=10.5,
        leading=13.1,
        spaceBefore=2.5 * mm,
        spaceAfter=1.0 * mm,
        keepWithNext=True,
    )
    styles["small"] = ParagraphStyle(
        "AFMSmall",
        parent=styles["body"],
        fontSize=8.5,
        leading=10.7,
    )
    styles["table"] = ParagraphStyle(
        "AFMTable",
        parent=styles["body"],
        fontSize=9.4,
        leading=12.4,
        spaceAfter=0,
        allowWidows=1,
        allowOrphans=1,
    )
    styles["table_header"] = ParagraphStyle(
        "AFMTableHeader",
        parent=styles["table"],
        fontName="AFMSans-Bold",
    )
    styles["box"] = ParagraphStyle(
        "AFMBox",
        parent=styles["body"],
        borderColor=BLACK,
        borderWidth=0.65,
        borderPadding=6,
        spaceBefore=2,
        spaceAfter=5,
        keepTogether=True,
    )
    styles["toc_title"] = ParagraphStyle(
        "AFMTOCTitle",
        parent=styles["h1"],
        fontSize=15,
        leading=18,
    )
    styles["toc0"] = ParagraphStyle(
        "AFMTOC0",
        parent=styles["body"],
        fontName="AFMSans-Bold",
        fontSize=9.2,
        leading=11.5,
        leftIndent=0,
        firstLineIndent=0,
        spaceBefore=2,
    )
    styles["toc1"] = ParagraphStyle(
        "AFMTOC1",
        parent=styles["body"],
        fontSize=8.7,
        leading=10.8,
        leftIndent=11 * mm,
        firstLineIndent=0,
        spaceBefore=0.5,
    )
    return styles


INLINE_CODE_RE = re.compile(r"`([^`]+)`")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
ITALIC_RE = re.compile(r"(?<!\*)\*([^*]+?)\*(?!\*)")


def inline_markup(text: str) -> str:
    """Convert the deliberately small inline-Markdown subset to ReportLab XML."""
    placeholders: list[str] = []

    def keep_code(match: re.Match[str]) -> str:
        placeholders.append(html.escape(match.group(1), quote=False))
        return f"\x00CODE{len(placeholders) - 1}\x00"

    protected = INLINE_CODE_RE.sub(keep_code, text)
    escaped = html.escape(protected, quote=False)
    escaped = BOLD_RE.sub(r"<b>\1</b>", escaped)
    escaped = ITALIC_RE.sub(r"<i>\1</i>", escaped)
    for idx, value in enumerate(placeholders):
        escaped = escaped.replace(
            html.escape(f"\x00CODE{idx}\x00", quote=False),
            f'<font name="AFMSans">{value}</font>',
        )
    return escaped


def heading_key(text: str, serial: int) -> str:
    digest = hashlib.sha1(text.encode("utf-8")).hexdigest()[:10]
    return f"h-{serial}-{digest}"


def is_table_separator(line: str) -> bool:
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def parse_table(lines: list[str], start: int, styles: dict[str, ParagraphStyle], width: float):
    rows: list[list[str]] = []
    i = start
    while i < len(lines) and lines[i].strip().startswith("|"):
        line = lines[i].strip()
        if not is_table_separator(line):
            rows.append([cell.strip() for cell in line.strip("|").split("|")])
        i += 1
    if not rows:
        return None, i
    columns = max(len(row) for row in rows)
    for row in rows:
        row.extend([""] * (columns - len(row)))
    # Estimate useful widths from content, then constrain them to the available frame.
    weights: list[float] = []
    for col in range(columns):
        longest = max(min(len(re.sub(r"[*`]", "", row[col])), 42) for row in rows)
        weights.append(max(7.0, float(longest)))
    total = sum(weights)
    col_widths = [width * weight / total for weight in weights]
    # Avoid unusably narrow columns; equal widths are safer for many-column numerical tables.
    if min(col_widths) < 19 * mm:
        col_widths = [width / columns] * columns
    data = []
    for row_idx, row in enumerate(rows):
        style = styles["table_header"] if row_idx == 0 else styles["table"]
        data.append([Paragraph(inline_markup(cell), style) for cell in row])
    table = LongTable(data, colWidths=col_widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.45, BLACK),
                ("BOX", (0, 0), (-1, -1), 0.7, BLACK),
                ("BACKGROUND", (0, 0), (-1, -1), WHITE),
                ("TEXTCOLOR", (0, 0), (-1, -1), BLACK),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 3.5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3.5),
                ("TOPPADDING", (0, 0), (-1, -1), 3.0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3.0),
                ("LINEBELOW", (0, 0), (-1, 0), 0.8, BLACK),
            ]
        )
    )
    return table, i


def parse_markdown(text: str, styles: dict[str, ParagraphStyle], frame_width: float):
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    story = []
    paragraph_lines: list[str] = []
    heading_serial = 0
    first_heading = True
    in_module_body = False
    module_h2_seen = False
    content_since_h2 = False

    def flush_paragraph() -> None:
        nonlocal paragraph_lines, content_since_h2
        if not paragraph_lines:
            return
        joined = " ".join(line.strip() for line in paragraph_lines).strip()
        paragraph_lines = []
        if not joined:
            return
        style = styles["body"]
        if joined.startswith("**COMMON MISTAKES:**") or joined.startswith("**Memory aid:**"):
            style = styles["box"]
        story.append(Paragraph(inline_markup(joined), style))
        if in_module_body:
            content_since_h2 = True

    i = 0
    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()
        if not stripped:
            flush_paragraph()
            i += 1
            continue
        if stripped == "\\pagebreak":
            flush_paragraph()
            story.append(PageBreak())
            i += 1
            continue
        if stripped == "[TOC]":
            flush_paragraph()
            toc = TableOfContents()
            toc.levelStyles = [styles["toc0"], styles["toc1"]]
            toc.dotsMinLevel = 0
            story.append(toc)
            i += 1
            continue
        heading_match = re.match(r"^(#{1,3})\s+(.+)$", stripped)
        if heading_match:
            flush_paragraph()
            level = len(heading_match.group(1)) - 1
            heading_text = heading_match.group(2)
            if level == 0 and heading_text.startswith("MODULE "):
                in_module_body = True
                module_h2_seen = False
            elif level == 0 and heading_text.startswith("SIX-MODULE"):
                in_module_body = False
            elif level == 1 and in_module_body:
                # Major examinable groups start cleanly, improving navigation and
                # preventing dense run-on pages. Keep each module title with its
                # first group rather than creating a title-only page.
                if module_h2_seen:
                    story.append(PageBreak())
                module_h2_seen = True
                content_since_h2 = False
            heading_serial += 1
            key = heading_key(heading_text, heading_serial)
            style_name = "title" if first_heading else f"h{level + 1}"
            first_heading = False
            story.append(
                HeadingParagraph(
                    inline_markup(heading_text), styles[style_name], level, key
                )
            )
            i += 1
            continue
        if stripped.startswith("|"):
            flush_paragraph()
            table, i = parse_table(lines, i, styles, frame_width)
            if table is not None:
                story.extend([table, Spacer(1, 4)])
                if in_module_body:
                    content_since_h2 = True
            continue
        bullet_match = re.match(r"^-\s+(.*)$", stripped)
        numbered_match = re.match(r"^\d+\.\s+(.*)$", stripped)
        checkbox_match = re.match(r"^-\s+\[([ xX])\]\s+(.*)$", stripped)
        if bullet_match or numbered_match:
            flush_paragraph()
            ordered = numbered_match is not None
            items = []
            while i < len(lines):
                current = lines[i].strip()
                check = re.match(r"^-\s+\[([ xX])\]\s+(.*)$", current)
                match = (
                    re.match(r"^\d+\.\s+(.*)$", current)
                    if ordered
                    else re.match(r"^-\s+(.*)$", current)
                )
                if not match:
                    break
                item_text = match.group(1)
                if check:
                    mark = "☑" if check.group(1).lower() == "x" else "□"
                    item_text = f"{mark} {check.group(2)}"
                items.append(
                    ListItem(
                        Paragraph(inline_markup(item_text), styles["body"]),
                        leftIndent=10,
                    )
                )
                i += 1
            story.append(
                ListFlowable(
                    items,
                    bulletType="1" if ordered else "bullet",
                    start="1",
                    leftIndent=14,
                    bulletFontName="AFMSans",
                    bulletFontSize=8.5,
                    spaceAfter=4,
                )
            )
            if in_module_body:
                content_since_h2 = True
            continue
        paragraph_lines.append(stripped)
        i += 1

    flush_paragraph()
    return story


def build() -> Path:
    if not MARKDOWN_PATH.is_file():
        raise FileNotFoundError(f"Markdown source not found: {MARKDOWN_PATH}")
    register_fonts()
    styles = make_styles()
    doc = AFMDocTemplate(str(OUTPUT_PATH))
    markdown = MARKDOWN_PATH.read_text(encoding="utf-8")
    story = parse_markdown(markdown, styles, doc.width)
    deterministic_canvas = partial(canvas.Canvas, invariant=1, pageCompression=1)
    doc.multiBuild(story, canvasmaker=deterministic_canvas)
    return OUTPUT_PATH


if __name__ == "__main__":
    try:
        result = build()
    except Exception as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        raise
    print(f"Built {result}")
