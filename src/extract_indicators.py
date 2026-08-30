"""Extract ESG indicator matches from a Docling JSON using the indicator dictionary.

Produces two outputs per run:
  1. A per-company detail file (data/indicators/<stem>_indicators.json) with every
     matched text/table element per indicator, including provenance, for manual
     verification against the source PDF.
  2. A consolidated summary row per indicator (data/indicators/esg_indicators_summary.csv)
     appended/replaced for this company so multiple companies can accumulate over time.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Any

DEFAULT_DICTIONARY = Path("data/reference/indicator_dictionary.json")
DEFAULT_OUTPUT_DIR = Path("data/indicators")
SUMMARY_FILENAME = "esg_indicators_summary.csv"
SUMMARY_FIELDS = [
    "company",
    "source_document",
    "indicator_key",
    "canonical_name",
    "category",
    "principle",
    "indicator_type",
    "brsr_core",
    "expected_data",
    "found",
    "match_count",
    "sample_snippet",
]


def compile_pattern(search_terms: list[str]) -> re.Pattern[str]:
    term_patterns = [
        r"\W+".join(re.escape(word) for word in re.findall(r"\w+", term))
        for term in search_terms
    ]
    return re.compile("|".join(term_patterns), re.IGNORECASE)


def matching_text(element: dict[str, Any], pattern: re.Pattern[str]) -> dict[str, Any] | None:
    text = element.get("text", "")
    if not isinstance(text, str) or not pattern.search(text):
        return None
    return {"content": text}


def matching_table(element: dict[str, Any], pattern: re.Pattern[str]) -> dict[str, Any] | None:
    cells = element.get("data", {}).get("table_cells", [])
    rows: dict[int, list[dict[str, Any]]] = {}
    for cell in cells:
        row_number = cell.get("start_row_offset_idx", 0)
        rows.setdefault(row_number, []).append(cell)

    all_rows: list[dict[str, Any]] = []
    matched_row_indices: list[int] = []
    for row_number, row in sorted(rows.items()):
        row.sort(key=lambda cell: cell.get("start_col_offset_idx", 0))
        row_text = [cell.get("text", "") for cell in row]
        all_rows.append({"row": row_number, "cells": row_text})
        if pattern.search(" ".join(row_text)):
            matched_row_indices.append(row_number)

    if not matched_row_indices:
        return None
    return {
        "matched_row_indices": matched_row_indices,
        "rows": all_rows,
        "num_rows": element.get("data", {}).get("num_rows"),
        "num_cols": element.get("data", {}).get("num_cols"),
    }


def find_matches(document: dict[str, Any], pattern: re.Pattern[str]) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []
    for element_type in ("texts", "tables"):
        for element in document.get(element_type, []):
            content = (
                matching_text(element, pattern)
                if element_type == "texts"
                else matching_table(element, pattern)
            )
            if content is None:
                continue
            matches.append(
                {
                    "element_type": element_type[:-1],
                    "label": element.get("label"),
                    "self_ref": element.get("self_ref"),
                    "provenance": element.get("prov", []),
                    **content,
                }
            )
    return matches


def snippet_for(matches: list[dict[str, Any]]) -> str:
    if not matches:
        return ""
    first = matches[0]
    if "content" in first:
        text = first["content"]
    else:
        first_matched_row = first["matched_row_indices"][0]
        row = next(r for r in first["rows"] if r["row"] == first_matched_row)
        text = " | ".join(row["cells"])
    text = " ".join(text.split())
    return text[:200]


def derive_company_label(stem: str) -> str:
    tokens = [t for t in stem.split("_") if t.upper() != "BRSR"]
    tokens = [t for t in tokens if not re.fullmatch(r"\d{4}", t)]
    tokens = [t for t in tokens if t.lower() not in ("brsronly", "only")]
    return "_".join(tokens) if tokens else stem


def extract_for_company(
    document: dict[str, Any], indicator_dict: dict[str, Any]
) -> dict[str, Any]:
    results: dict[str, Any] = {}
    for key, spec in indicator_dict.items():
        pattern = compile_pattern(spec["search_terms"])
        matches = find_matches(document, pattern)
        results[key] = {
            "canonical_name": spec["canonical_name"],
            "category": spec["category"],
            "principle": spec["principle"],
            "indicator_type": spec["indicator_type"],
            "brsr_core": spec["brsr_core"],
            "expected_data": spec["expected_data"],
            "found": bool(matches),
            "match_count": len(matches),
            "matches": matches,
        }
    return results


def update_summary_csv(
    summary_path: Path, company: str, source_document: str, results: dict[str, Any]
) -> None:
    existing_rows: list[dict[str, str]] = []
    if summary_path.exists():
        with summary_path.open("r", encoding="utf-8", newline="") as fh:
            existing_rows = [row for row in csv.DictReader(fh) if row["company"] != company]

    new_rows = [
        {
            "company": company,
            "source_document": source_document,
            "indicator_key": key,
            "canonical_name": result["canonical_name"],
            "category": result["category"],
            "principle": ";".join(result["principle"]),
            "indicator_type": result["indicator_type"],
            "brsr_core": result["brsr_core"],
            "expected_data": result["expected_data"],
            "found": result["found"],
            "match_count": result["match_count"],
            "sample_snippet": snippet_for(result["matches"]),
        }
        for key, result in results.items()
    ]

    summary_path.parent.mkdir(parents=True, exist_ok=True)
    with summary_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=SUMMARY_FIELDS)
        writer.writeheader()
        writer.writerows(existing_rows + new_rows)


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_file", type=Path, help="Docling JSON file from data/processed/")
    parser.add_argument("--dictionary", type=Path, default=DEFAULT_DICTIONARY)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--company", help="Override the derived company label")
    args = parser.parse_args()

    document = json.loads(args.json_file.read_text(encoding="utf-8"))
    indicator_dict = json.loads(args.dictionary.read_text(encoding="utf-8"))

    company = args.company or derive_company_label(args.json_file.stem)
    source_document = document.get("origin", {}).get("filename", args.json_file.name)

    results = extract_for_company(document, indicator_dict)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    detail_path = args.output_dir / f"{args.json_file.stem}_indicators.json"
    detail_path.write_text(
        json.dumps(
            {"company": company, "source_document": source_document, "indicators": results},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    summary_path = args.output_dir / SUMMARY_FILENAME
    update_summary_csv(summary_path, company, source_document, results)

    found_count = sum(1 for r in results.values() if r["found"])
    print(f"Company: {company} ({source_document})")
    print(f"Indicators found: {found_count}/{len(results)}")
    print(f"Detail written to: {detail_path}")
    print(f"Summary updated at: {summary_path}")
    for key, result in results.items():
        status = "FOUND" if result["found"] else "missing"
        print(f"  [{status:7}] {key}: {result['match_count']} match(es)")


if __name__ == "__main__":
    main()
