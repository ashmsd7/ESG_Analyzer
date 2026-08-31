# BRSR Table Validation Checklist

Source: `BRSR_Reliance_2024_2025.md` and `BRSR_Reliance_2024_2025.json`

Purpose: one-time manual comparison of every extracted Docling table against the original BRSR PDF. This checklist is diagnostic only; it does not alter preprocessing or extraction.

Data type key: **Numeric** = counts, amounts, percentages, rates, years, or measurements. **Categorical** = yes/no, nil/NA, classifications, names, locations, or enumerated categories. **Qualitative** = narrative descriptions, explanations, rationale, policy text, or links. **Mixed** combines two or more of these.

## Coverage Summary

- Extracted tables: 102 (`#/tables/0` through `#/tables/101`)
- PDF provenance range: pages 4-50
- Environmental coverage: Principle 6 (full essential + leadership indicator set: energy, water, air emissions, GHG, waste, environmental compliance), plus environmental disclosures in Principle 2 (R&D/capex, life-cycle assessment, recycled input material, reclaimed products)
- Social coverage: Principles 3, 4, 5, and 8 (employee/worker well-being, safety, human rights, stakeholder engagement, community/CSR), plus social/workforce disclosures in Section A
- Governance coverage: Principles 1, 7, and 9, plus governance, policy and CSR-applicability disclosures in Section A and Section B
- Reliance is a diversified conglomerate (O2C, retail, digital services, exploration & production), so Section A's holding/subsidiary/associate/joint-venture disclosure (Section A, V.23(a)) is unusually large — it spans 7 extracted tables (`#/tables/10`-`#/tables/16`) listing roughly 300+ group entities, versus a small table for a single-entity bank such as CBI.
- Unlike the CBI report, this filing includes a separate Independent Practitioner's Reasonable Assurance Report with an Appendix I "BRSR Core Indicators subject to Reasonable Assurance" list; these 4 tables (`#/tables/98`-`#/tables/101`, pages 49-50) are captured in a dedicated section below since they are not part of Section A/B/C.
- For each row, compare table headings, row/column alignment, values, units, `Nil`/`NA` values, narrative text, and page boundaries against the PDF.

## Section A: General Disclosures

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 1 | Main business activity description and % of turnover (O2C business) | Section A, II.16 | `#/tables/0`, p. 4 | Mixed | [ ] |
| 2 | Products/services sold, NIC code, % of total turnover contributed | Section A, II.17 | `#/tables/1`, p. 4 | Mixed | [ ] |
| 3 | Number of plants and offices, national/international totals | Section A, III.18 | `#/tables/2`, p. 4 | Numeric | [ ] |
| 4 | Markets served by the entity: number of locations (national/international) | Section A, III.19(a) | `#/tables/3`, p. 4 | Numeric + categorical | [ ] |
| 5 | Employee counts by employment type and gender | Section A, IV.20(a) | `#/tables/4`, p. 5 | Numeric + categorical | [ ] |
| 6 | Worker counts by employment type and gender | Section A, IV.20(b) | `#/tables/5`, p. 5 | Numeric + categorical | [ ] |
| 7 | Differently abled employee counts by employment type and gender | Section A, IV.20(c) | `#/tables/6`, p. 5 | Numeric + categorical | [ ] |
| 8 | Differently abled worker counts by employment type and gender | Section A, IV.20(d) | `#/tables/7`, p. 5 | Numeric + categorical | [ ] |
| 9 | Women participation in Board and key management personnel | Section A, IV.21 | `#/tables/8`, p. 5 | Numeric + categorical | [ ] |
| 10 | Turnover rate for permanent employees and workers (3-year trend) | Section A, IV.22 | `#/tables/9`, p. 5 | Numeric | [ ] |
| 11 | Holding/subsidiary/associate/JV list: name, type, % shareholding, BR participation (entries approx. 1-45) | Section A, V.23(a) | `#/tables/10`, p. 6 | Mixed | [ ] |
| 12 | Continued holding/subsidiary/associate/JV list (entries starting approx. 46) | Section A, V.23(a) (continued) | `#/tables/11`, p. 6 | Mixed | [ ] |
| 13 | Continued holding/subsidiary/associate/JV list (entries starting approx. 91) | Section A, V.23(a) (continued) | `#/tables/12`, p. 7 | Mixed | [ ] |
| 14 | Continued holding/subsidiary/associate/JV list (entries starting approx. 139) | Section A, V.23(a) (continued) | `#/tables/13`, p. 7 | Mixed | [ ] |
| 15 | Continued holding/subsidiary/associate/JV list (entries starting approx. 187) | Section A, V.23(a) (continued) | `#/tables/14`, p. 8 | Mixed | [ ] |
| 16 | Continued holding/subsidiary/associate/JV list (entries starting approx. 237) | Section A, V.23(a) (continued) | `#/tables/15`, p. 8 | Mixed | [ ] |
| 17 | Continued holding/subsidiary/associate/JV list, final entries (starting approx. 286) | Section A, V.23(a) (continued) | `#/tables/16`, p. 9 | Mixed | [ ] |
| 18 | CSR applicability, turnover and net worth | Section A, VI.24 | `#/tables/17`, p. 9 | Mixed | [ ] |
| 19 | Complaints/grievances by stakeholder group, mechanism, filed and pending (FY 2024-25 and FY 2023-24) | Section A, VII.25 | `#/tables/18`, p. 9 | Mixed | [ ] |
| 20 | Material responsible-business issues, rationale and mitigation approach (topics 1-3) | Section A, VII.26 | `#/tables/19`, p. 10 | Qualitative + categorical | [ ] |
| 21 | Continued material issues (topics starting at 4, e.g. Sustainable Supply Chain) | Section A, VII.26 (continued) | `#/tables/20`, p. 10 | Qualitative + categorical | [ ] |
| 22 | Continued material issues (topics starting at 6, e.g. Community Development) | Section A, VII.26 (continued) | `#/tables/21`, p. 11 | Qualitative + categorical | [ ] |
| 23 | Continued material issues (topics starting at 9, e.g. Talent Management) | Section A, VII.26 (continued) | `#/tables/22`, p. 11 | Qualitative + categorical | [ ] |
| 24 | Material topic interlinkages: mapping to `<IR>` framework capitals, stakeholders and SDGs | Section A, VII.26 (topic interlinkages) | `#/tables/23`, p. 14 | Qualitative + categorical | [ ] |

## Section B: Management and Process Disclosures

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 25 | Policy and management process coverage matrix for NGRBC Principles P1-P9 (part 1) | Section B, policy and management processes | `#/tables/24`, p. 15 | Categorical | [ ] |
| 26 | Continued policy and management process coverage matrix (Board approval, value-chain extension, procedures, part 2) | Section B, policy and management processes | `#/tables/25`, p. 16 | Categorical | [ ] |
| 27 | Continued policy coverage matrix with decarbonisation/Net Carbon Zero narrative (part 3) | Section B, policy and management processes | `#/tables/26`, p. 16 | Categorical + qualitative | [ ] |
| 28 | Review of NGRBC policies by Director/Committee of the Board, frequency of review | Section B, Q10 (Review of NGRBCs) | `#/tables/27`, p. 16 | Qualitative + categorical | [ ] |
| 29 | Independent external assessment/evaluation of policies by principle (P1-P9 header row; verify against PDF for possible missing/embedded Yes-No values) | Section B, Q11 (independent assessment of policies) | `#/tables/28`, p. 16 | Categorical | [ ] |
| 30 | Reasons why NGRBC principles are not covered by policy (all principles marked NA) | Section B, Q12 (reasons for non-coverage) | `#/tables/29`, p. 16 | Categorical | [ ] |

## Section C: Principle 1 - Ethics, Transparency and Accountability

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 31 | Training and awareness programme coverage by segment (Board, KMP, employees, workers) | Principle 1, Essential Indicator 1 | `#/tables/30`, p. 18 | Mixed | [ ] |
| 32 | Fines/penalties/settlement amounts - monetary proceedings | Principle 1, Essential Indicator 2 | `#/tables/31`, p. 18 | Mixed | [ ] |
| 33 | Fines/penalties - non-monetary proceedings | Principle 1, Essential Indicator 2 (continued) | `#/tables/32`, p. 18 | Mixed | [ ] |
| 34 | Appeal/revision details for monetary or non-monetary actions | Principle 1, Essential Indicator 3 | `#/tables/33`, p. 18 | Qualitative + categorical | [ ] |
| 35 | Directors/KMPs/employees/workers subject to disciplinary action for bribery/corruption | Principle 1, Essential Indicator 5 | `#/tables/34`, p. 18 | Numeric + categorical | [ ] |
| 36 | Complaints relating to conflict of interest (Directors and KMPs) | Principle 1, Essential Indicator 6 | `#/tables/35`, p. 19 | Mixed | [ ] |
| 37 | Number of days of accounts payable | Principle 1, Essential Indicator 8 | `#/tables/36`, p. 19 | Numeric | [ ] |
| 38 | Concentration of purchases/sales with trading houses, dealers and related parties | Principle 1, Essential Indicator 9 | `#/tables/37`, p. 19 | Mixed | [ ] |
| 39 | Value-chain partner awareness programmes on Principles | Principle 1, Leadership Indicator 1 | `#/tables/38`, p. 19 | Mixed | [ ] |

## Section C: Principle 2 - Sustainable and Safe Products/Services

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 40 | R&D and capex investment % for environmental/social impact improvement | Principle 2, Essential Indicator 1 | `#/tables/39`, p. 21 | Mixed | [ ] |
| 41 | Life Cycle Assessment (LCA): products assessed, boundary, external agency, public disclosure | Principle 2, Leadership Indicator 1 | `#/tables/40`, p. 22 | Mixed | [ ] |
| 42 | Risks/concerns identified from LCA and action taken | Principle 2, Leadership Indicator 2 | `#/tables/41`, p. 22 | Qualitative | [ ] |
| 43 | Recycled or re-used input material as % of total material used | Principle 2, Leadership Indicator 3 | `#/tables/42`, p. 22 | Numeric | [ ] |
| 44 | Products/packaging reclaimed at end of life: reused, recycled, safely disposed (metric tonnes) | Principle 2, Leadership Indicator 4 | `#/tables/43`, p. 22 | Numeric | [ ] |
| 45 | Reclaimed products and packaging as % of products sold, by product category | Principle 2, Leadership Indicator 5 | `#/tables/44`, p. 22 | Numeric | [ ] |

## Section C: Principle 3 - Employee Well-being

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 46 | Employee well-being coverage: health, accident, maternity, paternity, day-care | Principle 3, Essential Indicator 1(a) | `#/tables/45`, p. 24 | Numeric + categorical | [ ] |
| 47 | Worker well-being coverage: health, accident, maternity, paternity, day-care | Principle 3, Essential Indicator 1(b) | `#/tables/46`, p. 24 | Numeric + categorical | [ ] |
| 48 | Cost incurred on well-being measures as % of total revenue | Principle 3, Essential Indicator 1(c) | `#/tables/47`, p. 24 | Numeric | [ ] |
| 49 | Retirement benefits coverage and deposits: PF, gratuity, ESI, etc. | Principle 3, Essential Indicator 2 | `#/tables/48`, p. 24 | Mixed | [ ] |
| 50 | Return-to-work and retention rates after parental leave | Principle 3, Essential Indicator 5 | `#/tables/49`, p. 24 | Numeric + categorical | [ ] |
| 51 | Grievance redressal mechanism for employees and workers | Principle 3, Essential Indicator 6 | `#/tables/50`, p. 25 | Categorical + qualitative | [ ] |
| 52 | Employee/worker association or union membership | Principle 3, Essential Indicator 7 | `#/tables/51`, p. 25 | Numeric + categorical | [ ] |
| 53 | Training on health & safety and skill upgradation | Principle 3, Essential Indicator 8 | `#/tables/52`, p. 25 | Numeric + categorical | [ ] |
| 54 | Performance and career development reviews | Principle 3, Essential Indicator 9 | `#/tables/53`, p. 25 | Numeric + categorical | [ ] |
| 55 | Safety incidents: LTIFR, injuries, fatalities, high-consequence harm | Principle 3, Essential Indicator 11 | `#/tables/54`, p. 26 | Numeric + categorical | [ ] |
| 56 | Complaints on working conditions and health/safety | Principle 3, Essential Indicator 13 | `#/tables/55`, p. 26 | Mixed | [ ] |
| 57 | Assessment coverage for health & safety practices and working conditions | Principle 3, Essential Indicator 14 | `#/tables/56`, p. 26 | Numeric + categorical | [ ] |
| 58 | Rehabilitation/suitable employment after high-consequence work-related injury | Principle 3, Leadership Indicator 3 | `#/tables/57`, p. 27 | Numeric + categorical | [ ] |
| 59 | Value-chain partner assessment coverage: health & safety practices and working conditions | Principle 3, Leadership Indicator 5 | `#/tables/58`, p. 27 | Numeric + categorical | [ ] |

## Section C: Principle 4 - Stakeholder Responsiveness

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 60 | Key stakeholder groups: vulnerability, communication channels, frequency and purpose of engagement | Principle 4, Essential Indicator 2 | `#/tables/59`, p. 29 | Categorical + qualitative | [ ] |

## Section C: Principle 5 - Human Rights

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 61 | Material topic interlinkages for Human Rights, Health/Safety and Employee Well-being | Principle 5, introduction (topic interlinkages) | `#/tables/60`, p. 31 | Qualitative + categorical | [ ] |
| 62 | Human-rights training coverage for employees and workers | Principle 5, Essential Indicator 1 | `#/tables/61`, p. 32 | Numeric + categorical | [ ] |
| 63 | Minimum-wage coverage for employees | Principle 5, Essential Indicator 2 | `#/tables/62`, p. 32 | Numeric + categorical | [ ] |
| 64 | Minimum-wage coverage for workers | Principle 5, Essential Indicator 2 (continued) | `#/tables/63`, p. 32 | Numeric + categorical | [ ] |
| 65 | Median remuneration/salary/wages by gender and category | Principle 5, Essential Indicator 3(a) | `#/tables/64`, p. 32 | Numeric + categorical | [ ] |
| 66 | Gross wages paid to females as % of total wages | Principle 5, Essential Indicator 3(b) | `#/tables/65`, p. 32 | Numeric | [ ] |
| 67 | Complaints: sexual harassment, discrimination, child labour, wages, human rights | Principle 5, Essential Indicator 6 | `#/tables/66`, p. 33 | Mixed | [ ] |
| 68 | POSH complaints filed/pending | Principle 5, Essential Indicator 7 | `#/tables/67`, p. 33 | Numeric + categorical | [ ] |
| 69 | Assessment coverage for child labour, forced labour, sexual harassment, discrimination, wages | Principle 5, Essential Indicator 10 | `#/tables/68`, p. 33 | Numeric + categorical | [ ] |
| 70 | Value-chain partner assessment coverage for human-rights topics | Principle 5, Leadership Indicator 4 | `#/tables/69`, p. 33 | Numeric + categorical | [ ] |

## Section C: Principle 6 - Environment

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 71 | Total energy consumption (renewable/non-renewable) and energy intensity | Principle 6, Essential Indicator 1 | `#/tables/70`, p. 35 | Numeric | [ ] |
| 72 | Water withdrawal by source and water intensity | Principle 6, Essential Indicator 3 | `#/tables/71`, p. 35 | Numeric | [ ] |
| 73 | Water discharge by destination and level of treatment | Principle 6, Essential Indicator 4 | `#/tables/72`, p. 36 | Numeric | [ ] |
| 74 | Air emissions (NOx, SOx, PM, POP, VOC, HAP) other than GHG | Principle 6, Essential Indicator 6 | `#/tables/73`, p. 36 | Numeric | [ ] |
| 75 | Greenhouse gas emissions (Scope 1 and Scope 2) and intensity | Principle 6, Essential Indicator 7 | `#/tables/74`, p. 36 | Numeric | [ ] |
| 76 | Waste generated by category (plastic, e-waste, hazardous, etc.) and waste recovered | Principle 6, Essential Indicator 9 | `#/tables/75`, p. 37 | Numeric | [ ] |
| 77 | Waste recycled/re-used/recovered intensity and waste disposed by method | Principle 6, Essential Indicator 9 (continued) | `#/tables/76`, p. 37 | Numeric | [ ] |
| 78 | Locations near ecologically sensitive areas and environmental-approval compliance | Principle 6, Essential Indicator 13 | `#/tables/77`, p. 38 | Categorical | [ ] |
| 79 | Environmental impact assessment (EIA) details for projects | Principle 6, Essential Indicator 12 | `#/tables/78`, p. 38 | Mixed | [ ] |
| 80 | Environmental law non-compliance details (none reported) | Principle 6, Essential Indicator 13 (continued) | `#/tables/79`, p. 38 | Categorical + qualitative | [ ] |
| 81 | Water withdrawal, consumption and discharge in water-stressed area (Rewari) | Principle 6, Leadership Indicator 1(c) | `#/tables/80`, p. 38 | Numeric | [ ] |
| 82 | Resource-efficiency/circular-economy initiatives and outcomes | Principle 6, Leadership Indicator 4 | `#/tables/81`, p. 39 | Qualitative | [ ] |

## Section C: Principle 7 - Public Policy

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 83 | Trade and industry chamber/association affiliations (top 10 by membership) | Principle 7, Essential Indicator 1(b) | `#/tables/82`, p. 41 | Categorical | [ ] |
| 84 | Corrective action on anticompetitive conduct (none reported) | Principle 7, Essential Indicator 2 | `#/tables/83`, p. 41 | Qualitative + categorical | [ ] |
| 85 | Public policy positions advocated, method, disclosure and Board review frequency | Principle 7, Leadership Indicator 1 | `#/tables/84`, p. 41 | Mixed | [ ] |

## Section C: Principle 8 - Inclusive Growth

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 86 | Social Impact Assessment (SIA) details for projects | Principle 8, Essential Indicator 1 | `#/tables/85`, p. 43 | Mixed | [ ] |
| 87 | Rehabilitation and Resettlement (R&R) project details | Principle 8, Essential Indicator 2 | `#/tables/86`, p. 43 | Mixed | [ ] |
| 88 | % of input material sourced from suppliers (directly sourced) | Principle 8, Essential Indicator 4 | `#/tables/87`, p. 43 | Numeric | [ ] |
| 89 | Job creation and wages paid by location (rural/semi-urban/urban/metropolitan) | Principle 8, Essential Indicator 5 | `#/tables/88`, p. 43 | Numeric | [ ] |
| 90 | Negative social impacts identified and corrective action (not applicable) | Principle 8, Leadership Indicator 1 | `#/tables/89`, p. 44 | Qualitative | [ ] |
| 91 | CSR spend in government-identified aspirational districts by state | Principle 8, Leadership Indicator 2 | `#/tables/90`, p. 44 | Mixed | [ ] |
| 92 | Intellectual property based on traditional knowledge: ownership and benefit sharing | Principle 8, Leadership Indicator 4 | `#/tables/91`, p. 44 | Categorical + qualitative | [ ] |
| 93 | Corrective action on traditional-knowledge disputes (none reported) | Principle 8, Leadership Indicator 5 | `#/tables/92`, p. 44 | Qualitative | [ ] |
| 94 | CSR project beneficiaries: persons benefitted and % from vulnerable/marginalised groups | Principle 8, Leadership Indicator 6 | `#/tables/93`, p. 44 | Mixed | [ ] |

## Section C: Principle 9 - Consumer Responsibility

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 95 | % of turnover from products/services carrying environmental, social and safe-usage information | Principle 9, Essential Indicator 2 | `#/tables/94`, p. 46 | Mixed | [ ] |
| 96 | Consumer complaints: data privacy, advertising, cyber-security, essential services, other | Principle 9, Essential Indicator 3 | `#/tables/95`, p. 46 | Mixed | [ ] |
| 97 | Product recall instances (voluntary/forced) and reasons | Principle 9, Essential Indicator 4 | `#/tables/96`, p. 46 | Categorical + qualitative | [ ] |
| 98 | Channels/web portals where product and service information can be accessed | Principle 9, Leadership Indicator 1 | `#/tables/97`, p. 47 | Categorical | [ ] |

## Assurance Statement and Appendices

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 99 | Independent Practitioner's Reasonable Assurance Report - auditor signatory block (Deloitte Haskins & Sells LLP) | Assurance Statement | `#/tables/98`, p. 49 | Qualitative | [ ] |
| 100 | Appendix I: Identified Sustainability Information subject to Reasonable Assurance - BRSR Core indicators list (part 1) | Appendix I | `#/tables/99`, p. 49 | Mixed | [ ] |
| 101 | Continued Appendix I indicator list, incl. GHG emissions boundary (part 2) | Appendix I (continued) | `#/tables/100`, p. 50 | Mixed | [ ] |
| 102 | Continued Appendix I indicator list, incl. Section A general disclosures boundary (part 3) | Appendix I (continued) | `#/tables/101`, p. 50 | Mixed | [ ] |

## Manual Review Notes

For every checked table, record discrepancies here rather than editing the generated outputs:

- [ ] Page boundaries and repeated continuation headers are correct.
- [ ] Table row and column order matches the PDF.
- [ ] Numeric values, percentages, units, and financial years match the PDF.
- [ ] `Nil`, `NA`, blank, and `Not Applicable` values are preserved correctly.
- [ ] Categorical labels and organization names are correct.
- [ ] Qualitative text, URLs, footnotes, and explanatory notes are complete.
- [ ] Tables split across pages are treated as one disclosure where applicable.
- [ ] Image-only or OCR-dependent content is separately compared with the PDF.
- [ ] Check #29 (`#/tables/28`) in particular: this table has only a header row (P1-P9) with no visible data row extracted; confirm whether the underlying Yes/No answers exist in the PDF as text/image content that Docling did not capture as a table cell.

### Findings

| Checklist item | PDF page | Finding | Severity | Resolved |
|---|---:|---|---|:---:|
| | | | | [ ] |
