"""Inspect Docling JSON for selected ESG indicators and provenance."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

INDICATORS = {
    "Scope 1 emissions": r"Scope\s+1(?:\s+and\s+Scope\s+2)?\s+emissions",
    "Scope 2 emissions": r"Scope\s+2\s+emissions",
    "energy consumption": r"energy\s+consumption",
    "water consumption": r"water\s+consumption",
    "total employees": r"total\s+employees",
}


def matching_text(element: dict[str, Any], pattern: str) -> dict[str, Any] | None:
    text = element.get("text", "")
    if not isinstance(text, str) or not re.search(pattern, text, re.IGNORECASE):
        return None
    return {"content": text}


def matching_table(element: dict[str, Any], pattern: str) -> dict[str, Any] | None:
    cells = element.get("data", {}).get("table_cells", [])
    rows: dict[int, list[dict[str, Any]]] = {}
    for cell in cells:
        row_number = cell.get("start_row_offset_idx", 0)
        rows.setdefault(row_number, []).append(cell)

    matching_rows: list[dict[str, Any]] = []
    for row_number, row in sorted(rows.items()):
        row.sort(key=lambda cell: cell.get("start_col_offset_idx", 0))
        row_text = [cell.get("text", "") for cell in row]
        if re.search(pattern, " ".join(row_text), re.IGNORECASE):
            matching_rows.append({"row": row_number, "cells": row_text})
    if not matching_rows:
        return None
    return {
        "matching_rows": matching_rows,
        "num_rows": element.get("data", {}).get("num_rows"),
        "num_cols": element.get("data", {}).get("num_cols"),
    }


def inspect(document: dict[str, Any]) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []
    for element_type in ("texts", "tables"):
        for element in document.get(element_type, []):
            for indicator, pattern in INDICATORS.items():
                content = (
                    matching_text(element, pattern)
                    if element_type == "texts"
                    else matching_table(element, pattern)
                )
                if content is None:
                    continue
                matches.append(
                    {
                        "indicator": indicator,
                        "element_type": element_type[:-1],
                        "label": element.get("label"),
                        "self_ref": element.get("self_ref"),
                        "content_layer": element.get("content_layer"),
                        "provenance": element.get("prov", []),
                        **content,
                    }
                )
    return matches


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_file", type=Path, help="Generated Docling JSON file")
    args = parser.parse_args()

    document = json.loads(args.json_file.read_text(encoding="utf-8"))
    matches = inspect(document)
    print(f"Document: {document.get('origin', {}).get('filename', args.json_file.name)}")
    print(f"Matches: {len(matches)}")
    for number, match in enumerate(matches, start=1):
        print(f"\n--- Match {number}: {match['indicator']} ---")
        print(json.dumps(match, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
