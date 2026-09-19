import argparse
import sys
from pathlib import Path

from markdown_pdf import MarkdownPdf, Section


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Generate a professional PDF resume from a Markdown file.",
    )
    p.add_argument(
        "-i",
        "--input",
        type=Path,
        default=Path("marek_dohnal_resume.md"),
        help="Input Markdown file (default: marek_dohnal_resume.md)",
    )
    p.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Output PDF path (default: same stem as input with .pdf)",
    )
    return p


def load_styles() -> str:
    with open("styles.css", "r", encoding="utf-8") as f:
        return f.read()


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    input_path: Path = args.input
    if not input_path.exists():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        return 1

    output_path: Path = args.output or input_path.with_suffix(".pdf")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    md_text = input_path.read_text(encoding="utf-8")

    # Single continuous section (no forced page breaks between MD sections)
    # borders: (left, top, right, bottom) in points; negative right/bottom = from edge
    pdf = MarkdownPdf(toc_level=0, optimize=True)
    pdf.meta["title"] = "Marek Dohnal – Resume"
    pdf.meta["author"] = "Marek Dohnal"

    section = Section(
        md_text,
        toc=False,
        paper_size="A4",
        borders=(50, 45, -50, -45),  # ~18mm margins
    )
    pdf.add_section(section, user_css=load_styles())
    pdf.save(str(output_path))

    return 0


if __name__ == "__main__":
    main()
