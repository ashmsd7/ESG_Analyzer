# ESG Analyzer – Docling Pipeline Onboarding

**Project**: ESG_Analyzer  
**Repository**: https://github.com/ashmsd7/ESG_Analyzer  
**Last Updated**: 2026-08-30  
**Status**: Stage 1 pipeline complete – single-document extraction validated

---

## Project Overview

This project extracts **Business Responsibility and Sustainability Report (BRSR)** documents using **Docling**, an AI-powered document conversion framework. The output is structured Markdown and JSON representations of PDF content for ESG indicator analysis.

**Current Scope**: Processing BRSR reports from Indian companies (Central Bank of India, Infosys, Reliance, TataSteel, TataELXSI, HDFC Bank).

---

## Directory Structure

```
Major_Project/
├── .git/                              # Version control
├── .gitattributes                     # Git LFS config for model weights
├── .gitignore                         # Excludes PDFs, venv, model weights
├── requirements.txt                   # Python dependencies (Docling 2.0+)
├── run_pipeline.bat                   # Windows batch launcher
│
├── src/
│   ├── extract_document.py            # Stage 1: Docling PDF → Markdown + JSON
│   └── inspect_docling_json.py        # Diagnostic: Search JSON for ESG indicators
│
├── data/
│   ├── docling-models/                # Pre-downloaded Docling model weights (local only)
│   │   ├── docling-project--docling-layout-heron/          # Layout detection model
│   │   ├── docling-project--docling-layout-heron-onnx/     # ONNX variant
│   │   └── docling-project--docling-models/tableformer/    # Table extraction models
│   ├── processed/                     # Generated outputs (committed to repo)
│   │   ├── BRSR_CBI_2024_2025.md      # Markdown extraction
│   │   └── BRSR_CBI_2024_2025.json    # Docling structured JSON
│   └── validation/
│       └── table_validation_checklist.md  # Table inventory for manual verification
│
├── BRSR_*.pdf                         # Source documents (local only, not in repo)
├── .venv/                             # Python virtual environment (local only)
└── pip-install.log                    # Installation log (local only)
```

---

## Key Concepts

### Docling (PDF Processing Framework)

**What it does**:
- Converts PDFs to structured documents using vision models
- Extracts text, tables, images, and layout information
- Produces JSON with full provenance metadata (page numbers, bounding boxes)

**Why we use it**:
- Accurately captures complex BRSR tables (often nested, multi-column)
- Preserves document structure and page references
- Enables downstream validation and ESG indicator extraction

**Current Models**:
- **docling-layout-heron**: Layout detection (text vs. table vs. image regions)
- **tableformer**: Table cell detection and content extraction

### Generated Outputs

**Markdown** (`BRSR_CBI_2024_2025.md`):
- Human-readable formatted text
- Markdown tables from extracted BRSR data
- Section headings preserved from PDF structure
- ~192 KB uncompressed

**JSON** (`BRSR_CBI_2024_2025.json`):
- Docling's native `DoclingDocument` schema (version 1.10.0)
- Full-fidelity structured representation
- Elements indexed by type: `texts`, `tables`, `pictures`
- Each element includes:
  - `label`: Element classification (e.g., `text`, `table`, `heading`, `list_item`)
  - `text` / `data.table_cells`: Extracted content
  - `prov`: Provenance metadata (page number, bounding box, character span)
  - `self_ref`: Internal reference ID (e.g., `#/texts/123`, `#/tables/42`)
- ~2.9 MB uncompressed

### Validation Checklist

**File**: `data/validation/table_validation_checklist.md`  
**Content**: Inventory of all 63 extracted tables with:
- Table reference (#/tables/N)
- BRSR section and principle
- PDF page number
- Data type classification (numeric, categorical, qualitative, mixed)
- Verification checkbox

**Purpose**: Enable manual comparison against original PDF to catch OCR errors or layout misinterpretation.

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

Docling automatically downloads models from Hugging Face on first use. You can pre-download to `data/docling-models/` to avoid repeated downloads. Models are excluded from Git via `.gitignore` and `.gitattributes`.

### 3. Add Source PDFs

Place BRSR PDF files in the project root. They are ignored by Git (see `.gitignore`):

```
BRSR_CompanyName_Year.pdf
```

---

## Running the Pipeline

### Using the Batch Launcher (Windows)

**Default** (processes `BRSR_CBI_2024_2025.pdf`):
```bash
run_pipeline.bat
```

**Custom PDF**:
```bash
run_pipeline.bat BRSR_Infosys_2024_2025.pdf
```

**What it does**:
1. Creates `.venv` if missing
2. Installs dependencies from `requirements.txt`
3. Runs `extract_document.py` on the specified PDF
4. Outputs Markdown and JSON to `data/processed/`

### Direct Python Invocation

```bash
.venv\Scripts\python.exe src\extract_document.py BRSR_CBI_2024_2025.pdf --output-dir data\processed
```

### Running the Inspector (Diagnostic)

Searches the generated JSON for five ESG indicators and prints matching content + provenance:

```bash
.venv\Scripts\python.exe src\inspect_docling_json.py data\processed\BRSR_CBI_2024_2025.json
```

**Indicators searched**:
- Scope 1 emissions
- Scope 2 emissions
- Energy consumption
- Water consumption
- Total employees

**Output format** (JSON):
```json
{
  "indicator": "energy consumption",
  "element_type": "text",
  "label": "list_item",
  "self_ref": "#/texts/398",
  "provenance": [
    {
      "page_no": 22,
      "bbox": { "l": 53.86, "t": 228.54, "r": 521.30, "b": 220.61 }
    }
  ],
  "content": "Details of total energy consumption (in Joules or multiples)..."
}
```

---

## Pipeline Architecture (Stage 1)

```
PDF Input
    ↓
[Docling DocumentConverter]
    ├─ Layout Detection (docling-layout-heron)
    ├─ Text Extraction
    ├─ Table Recognition (tableformer)
    └─ Image/Shape Detection
    ↓
[Docling Document object]
    ├─ export_to_markdown() → Markdown file
    └─ export_to_dict() → JSON file
    ↓
Output: Markdown + JSON (both committed to repo)
```

**Notes**:
- No data preprocessing or cleanup applied
- Tables remain as extracted; OCR artifacts are preserved
- Provenance metadata allows traceability back to original PDF

---

## Code Files

### `src/extract_document.py`

**Purpose**: Single-file Docling extraction wrapper  
**Input**: PDF file path (CLI argument)  
**Output**: Markdown and JSON in `data/processed/`

**Key function**:
```python
extract_document(pdf_path: Path, output_dir: Path) -> tuple[Path, Path]
```

**No preprocessing applied** – output is raw Docling conversion.

### `src/inspect_docling_json.py`

**Purpose**: Read-only diagnostic scanner for ESG indicators  
**Input**: Generated Docling JSON file  
**Output**: Matching elements with provenance

**Key features**:
- Regex-based pattern matching for five ESG indicators
- Groups table cells by row offset index
- Reports full provenance (page, bounding box, character span)
- Does NOT modify pipeline or extraction code

**Usage**: Allows manual verification against original PDF before feeding to downstream ESG analysis.

---

## Git Workflow

### Committed to Repository

- `src/*.py` – Python extraction and diagnostic scripts
- `requirements.txt` – Dependency specification
- `run_pipeline.bat` – Windows launcher
- `data/processed/*.json` and `data/processed/*.md` – Generated outputs (Stage 1)
- `data/validation/table_validation_checklist.md` – Validation inventory
- `.gitattributes` – Git LFS config

### Excluded from Repository

- `data/docling-models/` – Model weights (too large; auto-downloaded via Docling)
- `.venv/` – Virtual environment
- `*.pdf` – Source documents (declared in `.gitignore`)
- `pip-install.log` – Installation artifacts

### Recent Commit

**Hash**: `425f297`  
**Message**: `28AugCommit_Docling`  
**Contents**: Initial Docling pipeline setup with Stage 1 extraction and diagnostics

---

## Validation Summary (One Document Tested)

**Document**: BRSR_CBI_2024_2025.pdf  
**Extracted**: 63 tables, 404 text blocks, 10+ images  
**Extracted Indicators**:
- **Scope 1 emissions**: Page 23 (text)
- **Scope 2 emissions**: Page 23 (text)
- **Energy consumption**: Pages 22, 24 (text + table)
- **Total employees**: Pages 2, 12, 14, 19 (tables)
- **Water consumption**: Not found in extracted output

**Table Validation**: See `data/validation/table_validation_checklist.md` for complete inventory (Section A–C, Principles 1–9).

---

## Next Steps for Agents

1. **Expand to Multiple Documents**: Run `run_pipeline.bat BRSR_<name>_<year>.pdf` on remaining PDFs
2. **Validate Extraction Quality**: Manually spot-check high-value tables against originals using checklist
3. **Build ESG Indicator Pipeline**: Parse extracted JSON for domain-specific indicators (greenhouse gas, water stress, employee diversity, etc.)
4. **Implement Data Cleaning**: Handle OCR artifacts, standardize numeric formats, reconcile table continuations
5. **Create Downstream Models**: Feed cleaned data to ML/analytics for ESG scoring or anomaly detection

---

## Common Issues & Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| `ModuleNotFoundError: docling` | Dependency not installed | Run `.venv\Scripts\python.exe -m pip install -r requirements.txt` |
| Model download hangs | First-time Hugging Face download | Set `HF_TOKEN` env var if rate-limited; retry with internet connection |
| "RapidOCR returned empty result" | OCR model timeout or PDF format | Retry; inspect original PDF for corruption |
| JSON too large to view | 2.9 MB uncompressed | Use `grep` or Python JSON parser; don't open in text editor directly |
| `pip-install.log` pollutes Git status | Installation artifact | Intentionally excluded; safe to delete locally |

---

## Dependencies

```
docling>=2.0,<3.0
  └─ docling-slim (core functionality)
     ├─ torch (model inference)
     ├─ transformers (NLP models)
     ├─ pypdfium2 (PDF rendering)
     ├─ rapidocr (optical character recognition)
     └─ [+50 transitive deps]
```

Full dependency tree available via `pip freeze`.

---

## Configuration & Environment

**Python Version**: 3.11.5  
**OS**: Windows (batch launcher provided; adapt shebang for Linux/macOS)  
**Git**: LFS configured for `*.safetensors` and `*.onnx`

---

## Contacts & History

- **Project Lead**: [Your name/team]
- **Initial Setup**: 2026-08-25
- **Docling Integration**: 2026-08-26
- **Validation & Commit**: 2026-08-30

---

## References

- Docling GitHub: https://github.com/docling-project/docling
- BRSR Guidelines: https://www.mca.gov.in/
- Docling JSON Schema: Refer to `origin.schema_name` in generated `*.json` files (v1.10.0)

