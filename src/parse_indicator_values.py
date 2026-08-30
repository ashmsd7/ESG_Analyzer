"""Parse numeric ESG indicator values out of Stage-2 matched content.

Reads a company's data/indicators/<stem>_indicators.json (produced by
extract_indicators.py) and, for indicators tagged "expected_data": "numeric"
in the indicator dictionary, scans the matched text/table content for either
a number+unit or an explicit Not Applicable / Nil signal.

Writes a new file (does not modify the Stage-2 detail file):
  data/indicators/<stem>_parsed_values.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

DEFAULT_DICTIONARY = Path("data/reference/indicator_dictionary.json")
DEFAULT_OUTPUT_DIR = Path("data/indicators")

NOT_APPLICABLE_PATTERN = re.compile(r"\bnot\s+applicable\b|\bn\.?/?a\.?\b", re.IGNORECASE)
NIL_PATTERN = re.compile(r"\bnil\b", re.IGNORECASE)

FALLBACK_UNITS = [
    r"lakh\s*kwh",
    r"kwh",
    r"joules",
    r"kilolitres?",
    r"tonnes?",
    r"kg",
    r"crore",
    r"lakh",
    r"%",
    r"percent",
]


def build_value_pattern(possible_units: list[str]) -> re.Pattern[str]:
    unit_alternatives = [re.escape(u) for u in possible_units] + FALLBACK_UNITS
    unit_group = "|".join(unit_alternatives)
    return re.compile(
        rf"(?<!\w)(\d[\d,]*\.?\d*)\s*({unit_group})?(?!\w)",
        re.IGNORECASE,
    )


def texts_from_match(match: dict[str, Any]) -> list[tuple[str, str]]:
    """Return [(snippet, self_ref)] candidate text pieces from one match."""
    self_ref = match.get("self_ref", "")
    if "content" in match:
        return [(match["content"], self_ref)]
    pieces = []
    for row in match.get("rows", []):
        text = " ".join(cell for cell in row["cells"] if cell)
        if text.strip():
            pieces.append((text, self_ref))
    return pieces


def parse_indicator(spec: dict[str, Any], matches: list[dict[str, Any]]) -> dict[str, Any]:
    value_pattern = build_value_pattern(spec.get("possible_units", []))

    numeric_values: list[dict[str, Any]] = []
    na_snippet: str | None = None
    nil_snippet: str | None = None

    for match in matches:
        for snippet, self_ref in texts_from_match(match):
            for number_str, unit in value_pattern.findall(snippet):
                if not unit:
                    continue
                numeric_values.append(
                    {
                        "value": float(number_str.replace(",", "")),
                        "unit": unit.strip().lower(),
                        "raw_snippet": " ".join(snippet.split())[:200],
                        "self_ref": self_ref,
                    }
                )
            if na_snippet is None and NOT_APPLICABLE_PATTERN.search(snippet):
                na_snippet = " ".join(snippet.split())[:200]
            if nil_snippet is None and NIL_PATTERN.search(snippet):
                nil_snippet = " ".join(snippet.split())[:200]

    if numeric_values:
        status = "parsed"
    elif na_snippet:
        status = "not_applicable"
    elif nil_snippet:
        status = "nil"
    else:
        status = "unparsed"

    return {
        "status": status,
        "numeric_values": numeric_values,
        "not_applicable_snippet": na_snippet,
        "nil_snippet": nil_snippet,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("indicators_file", type=Path, help="A *_indicators.json file from data/indicators/")
    parser.add_argument("--dictionary", type=Path, default=DEFAULT_DICTIONARY)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    detail = json.loads(args.indicators_file.read_text(encoding="utf-8"))
    indicator_dict = json.loads(args.dictionary.read_text(encoding="utf-8"))

    results: dict[str, Any] = {}
    for key, spec in indicator_dict.items():
        indicator_result = detail["indicators"][key]
        if spec["expected_data"] != "numeric":
            results[key] = {
                "status": "not_parsed_this_pass",
                "reason": f"expected_data is '{spec['expected_data']}', numeric parsing only in this pass",
            }
            continue
        results[key] = parse_indicator(spec, indicator_result["matches"])

    stem = args.indicators_file.stem.removesuffix("_indicators")
    output_path = args.output_dir / f"{stem}_parsed_values.json"
    output_path.write_text(
        json.dumps(
            {"company": detail["company"], "source_document": detail["source_document"], "indicators": results},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"Company: {detail['company']}")
    print(f"Written to: {output_path}")
    for key, result in results.items():
        if result["status"] == "not_parsed_this_pass":
            continue
        summary = result["status"]
        if result["numeric_values"]:
            summary += f" ({len(result['numeric_values'])} value(s))"
        print(f"  {key}: {summary}")


if __name__ == "__main__":
    main()
