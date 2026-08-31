# ESG Analyzer – Docling Pipeline Onboarding

**Project**: ESG_Analyzer
**Repository**: https://github.com/ashmsd7/ESG_Analyzer
**Last Updated**: 2026-09-01
**Status**: Stage 1-4 pipeline complete, piloted end-to-end on one document per company

---

## Project Overview

This project extracts **Business Responsibility and Sustainability Report (BRSR)** data from Indian companies' annual report PDFs into structured, machine-usable form, matched against a fixed set of ESG indicators.

**Current Scope**: One (usually the latest) filing year processed per company, as a deliberate pilot to validate output quality before running the rest of the corpus. Companies piloted: Central Bank of India, Infosys, Reliance, Tata Steel, Tata Elxsi, HDFC Bank.

**Additional PDFs already present but not yet processed** (older filing years, awaiting the full-corpus run once the pilot is validated): `BRSR_Infosys_2022_2023.pdf`, `BRSR_Infosys_2023_2024.pdf`, `BRSR_TataSteel_2022_2023.pdf`, `BRSR_TataSteel_2023_2024.pdf`, `BRSR_TataELXSI_2024_2025.pdf`, `BRSR_HDFCBank_2021_2022.pdf`.

---

## Directory Structure

```
Major_Project/
├── .git/                              # Version control
├── .gitattributes                     # Git LFS config for model weights
├── .gitignore                         # Excludes PDFs, venv, model weights
├── requirements.txt                   # Python dependencies (Docling 2.0+)
├── run_pipeline.bat                   # Windows batch launcher (Stage 1 only)
│
├── src/
│   ├── extract_document.py            # Stage 1: Docling PDF → Markdown + JSON
│   ├── inspect_docling_json.py        # Diagnostic: search JSON for ESG indicators
│   ├── extract_indicators.py          # Stage 3: match indicator dictionary against Stage 1 JSON
│   └── parse_indicator_values.py      # Stage 4: parse numeric values from Stage 3 matches
│
├── data/
│   ├── docling-models/                # Pre-downloaded Docling model weights (local only)
│   ├── processed/                     # Stage 1 output: <stem>.md, <stem>.json (committed)
│   ├── reference/
│   │   └── indicator_dictionary.json  # Master list of 20 ESG indicators (7E/7S/6G)
│   ├── indicators/                    # Stage 3 & 4 output (committed)
│   │   ├── <stem>_indicators.json     # Stage 3: raw matched content + provenance, per company
│   │   ├── <stem>_parsed_values.json  # Stage 4: parsed numeric values, per company
│   │   └── esg_indicators_summary.csv # One row per indicator per company, accumulates across runs
│   └── validation/
│       └── *_validation_checklist.md  # Manual table-by-table verification checklists (see below)
│
├── BRSR_*.pdf                         # Source documents (local only, not in repo)
├── .venv/                             # Python virtual environment (local only)
└── pip-install.log                    # Installation log (local only)
```

---

## Pipeline Architecture (4 stages)

```
PDF Input
    ↓
[Stage 1] extract_document.py — Docling DocumentConverter
    ├─ Layout Detection (docling-layout-heron)
    ├─ Table Recognition (tableformer)
    └─ export_to_markdown() / export_to_dict()
    ↓
data/processed/<stem>.md + <stem>.json
    ↓
[Stage 2] data/reference/indicator_dictionary.json — hand-curated, not code
    (20 ESG indicators: search_terms, expected_data type, units, BRSR principle/section)
    ↓
[Stage 3] extract_indicators.py
    Regex word-boundary match of each indicator's search_terms against every
    text block and table row in the Stage 1 JSON. NOT fuzzy/Levenshtein matching.
    ↓
data/indicators/<stem>_indicators.json + esg_indicators_summary.csv
    ↓
[Stage 4] parse_indicator_values.py
    For indicators tagged "expected_data": "numeric" only — regex-scans Stage 3's
    matched snippets for a number+unit, or an explicit Not Applicable / Nil signal.
    Qualitative indicators are left untouched at this stage (no Stage 4 equivalent yet).
    ↓
data/indicators/<stem>_parsed_values.json
```

**Notes**:
- No data preprocessing or cleanup applied at Stage 1; tables remain as extracted, OCR artifacts preserved.
- Provenance metadata (page number, bounding box, `self_ref`) is carried through Stage 1 → 3 for traceability back to the source PDF.
- Stage 3/4 output for a company overwrites/replaces (not appends) that company's prior rows in `esg_indicators_summary.csv`, keyed by the derived company label.

## Key Concepts

### Docling (PDF Processing Framework)
Converts PDFs to structured documents using vision models, extracting text, tables, images, and layout with full provenance (page numbers, bounding boxes). Used because BRSR PDFs contain complex, often nested/multi-column tables that plain text extraction mangles.

### `indicator_dictionary.json` (Stage 2)
One entry per ESG indicator, keyed by a short id (e.g. `scope_1_emissions`). Fields:
- `search_terms` — phrases Stage 3 searches for
- `expected_data` — `"numeric"` or otherwise (gates whether Stage 4 attempts parsing)
- `possible_units`, `unit_notes` — known unit quirks per company (e.g. CBI reports energy in "lakh kWh", not the BRSR-mandated Joules — a naive parser would misparse this by 100,000x)
- `principle`, `indicator_type`, `brsr_core` — BRSR taxonomy metadata (P1-P9, essential/leadership)
- `sources_reviewed` — **documentation only, not read by any script.** A manual audit trail of which company reports were actually read when that indicator's `search_terms`/`unit_notes` were written or last refined. Currently stale for most indicators (mostly lists only `BRSR_CBI_2024_2025`); should be updated as more companies are reviewed per indicator.

### Validation Checklists (`data/validation/`)
**Purpose**: a one-time, manual, table-by-table inventory of everything Docling extracted from a company's filing, meant to be checked by eye against the original PDF. For every table Docling found, it records: what the table actually contains, which BRSR section/principle it belongs to, its Docling reference (`#/tables/N`) and PDF page, and its data type (numeric/categorical/qualitative/mixed) — plus a checkbox to mark once verified.

**Why it exists**: Stage 1 (Docling) and Stage 3 (regex matching) can both silently fail in ways that are hard to notice from the JSON alone — a table row misaligned, a heading dropped, a numeric value OCR'd wrong, or an indicator's `search_terms` missing a phrasing the document actually uses. The checklist is the mechanism for catching those errors by hand: someone works through it row by row with the source PDF open, ticking off each table once its content is confirmed correct. It doesn't feed back into any code — it's purely a human QA pass over the pipeline's output.

**Status**: previously only existed for CBI (63 tables). Being extended to cover the other 5 piloted companies.

---

## Setup Instructions

### 1. Clone and Install
```bash
git clone https://github.com/ashmsd7/ESG_Analyzer.git
cd Major_Project
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Download Models (One-Time)
Docling auto-downloads models from Hugging Face on first use; pre-download to `data/docling-models/` to avoid repeated downloads. Excluded from Git via `.gitignore`/`.gitattributes`.

### 3. Add Source PDFs
Place BRSR/annual-report PDFs in the project root (ignored by Git):
```
BRSR_CompanyName_Year.pdf
```

---

## Running the Pipeline

### Stage 1 — via batch launcher (Windows)
```bash
run_pipeline.bat BRSR_Infosys_2024_2025.pdf
```
Creates `.venv` if missing, installs dependencies, runs `extract_document.py`, outputs to `data/processed/`.

### Stage 1 — direct invocation
```bash
.venv\Scripts\python.exe src\extract_document.py BRSR_Infosys_2024_2025.pdf --output-dir data\processed
```

### Stage 3 — indicator matching
```bash
.venv\Scripts\python.exe src\extract_indicators.py data\processed\BRSR_Infosys_2024_2025.json
```
Optional flags: `--dictionary` (default `data/reference/indicator_dictionary.json`), `--output-dir` (default `data/indicators`), `--company` (override the auto-derived company label).

### Stage 4 — value parsing
```bash
.venv\Scripts\python.exe src\parse_indicator_values.py data\indicators\BRSR_Infosys_2024_2025_indicators.json
```

### Diagnostic — `inspect_docling_json.py`
Read-only scanner that regex-searches a Stage 1 JSON for five hardcoded ESG indicators (Scope 1/2 emissions, energy consumption, water consumption, total employees) and prints matches with provenance. Predates and is superseded by Stage 3/4 for anything beyond quick manual spot-checks.

---

## Git Workflow

### Committed to Repository
- `src/*.py`, `requirements.txt`, `run_pipeline.bat`, `ONBOARDING.md`
- `data/processed/*.json` and `*.md`
- `data/reference/indicator_dictionary.json`
- `data/indicators/*.json` and `esg_indicators_summary.csv`
- `data/validation/*.md`

### Excluded from Repository
- `data/docling-models/` (model weights, auto-downloaded)
- `.venv/`, `*.pdf` (source documents), `pip-install.log`

---

## Known Gaps / Next Steps

1. **Qualitative indicators have no Stage 4 equivalent.** `parse_indicator_values.py` only processes `"expected_data": "numeric"` indicators; qualitative ones stop at Stage 3's raw matched text.
2. **No consolidated cross-company dataset.** Each company's `_parsed_values.json` is separate; nothing joins them into one table for comparison/scoring yet.
3. **No unit normalization.** Known unit mismatches (e.g. CBI's "lakh kWh") are documented in `unit_notes` but not automatically converted — Stage 4 records whatever unit it finds as-is.
4. **`sources_reviewed` is stale** for most indicators in the dictionary — needs a pass now that 5 more companies have been matched.
5. **Validation checklist coverage** is being extended from CBI-only to all 6 piloted companies (in progress).
6. **Remaining corpus** (the 6 older-year PDFs listed above under Current Scope) still needs to go through all 4 stages once the pilot output is trusted.
7. **HDFC Bank's pilot document was initially a manually-trimmed 52-page excerpt** of the true 585-page filing (undocumented at the time it was made). Being reprocessed against the full native PDF for consistency with the other 5 companies.

---

## Configuration & Environment

**Python Version**: 3.11.5
**OS**: Windows (batch launcher provided; adapt for Linux/macOS)
**Git**: LFS configured for `*.safetensors` and `*.onnx`
**Current HEAD**: `48a1900` — see `git log` for full history rather than relying on this doc.

---

## References
- Docling GitHub: https://github.com/docling-project/docling
- BRSR Guidelines: https://www.mca.gov.in/
- Docling JSON Schema: `origin.schema_name` in generated `*.json` files (v1.10.0)
