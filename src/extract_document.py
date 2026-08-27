"""Extract one PDF into Markdown and Docling's structured JSON representation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from docling.document_converter import DocumentConverter


def extract_document(pdf_path: Path, output_dir: Path) -> tuple[Path, Path]:
    converter = DocumentConverter()
    result = converter.convert(pdf_path)
    document = result.document

    output_dir.mkdir(parents=True, exist_ok=True)
    markdown_path = output_dir / f"{pdf_path.stem}.md"
    json_path = output_dir / f"{pdf_path.stem}.json"

    markdown_path.write_text(document.export_to_markdown(), encoding="utf-8")
    json_path.write_text(
        json.dumps(document.export_to_dict(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return markdown_path, json_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, help="PDF file to process")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/processed"),
        help="Directory for Markdown and JSON output",
    )
    args = parser.parse_args()

    markdown_path, json_path = extract_document(args.pdf, args.output_dir)
    print(f"Markdown: {markdown_path}")
    print(f"JSON: {json_path}")


if __name__ == "__main__":
    main()
