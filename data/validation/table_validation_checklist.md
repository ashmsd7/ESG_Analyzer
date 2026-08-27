# BRSR Table Validation Checklist

Source: `BRSR_CBI_2024_2025.md` and `BRSR_CBI_2024_2025.json`

Purpose: one-time manual comparison of every extracted Docling table against the original BRSR PDF. This checklist is diagnostic only; it does not alter preprocessing or extraction.

Data type key: **Numeric** = counts, amounts, percentages, rates, years, or measurements. **Categorical** = yes/no, nil/NA, classifications, names, locations, or enumerated categories. **Qualitative** = narrative descriptions, explanations, rationale, policy text, or links. **Mixed** combines two or more of these.

## Coverage Summary

- Extracted tables: 63 (`#/tables/0` through `#/tables/62`)
- PDF provenance range: pages 1-31
- Environmental coverage: Principles 2 and 6, plus environmental disclosures in Principle 1 and Section A
- Social coverage: Principles 3, 4, 5, and 8, plus social disclosures in Section A
- Governance coverage: Principles 1, 7, and 9, plus governance disclosures in Section A
- For each row, compare table headings, row/column alignment, values, units, `Nil`/`NA` values, narrative text, and page boundaries against the PDF.

## Section A: General Disclosures

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 1 | Company identity, registered/corporate office, contact, reporting year, assurance | Section A, I. Details | `#/tables/0`, p. 1 | Mixed | [ ] |
| 2 | Main business activities and turnover share | Section A, II.16 | `#/tables/1`, p. 1 | Mixed | [ ] |
| 3 | Products/services, NIC code, turnover contribution | Section A, II.17 | `#/tables/2`, p. 1 | Mixed | [ ] |
| 4 | Operating locations, offices, plants, national/international totals | Section A, III.18 | `#/tables/3`, p. 1 | Mixed | [ ] |
| 5 | Markets served by location | Section A, III.19(a) | `#/tables/4`, p. 2 | Mixed | [ ] |
| 6 | Employee counts by employment type and gender | Section A, IV.20(a) | `#/tables/5`, p. 2 | Numeric + categorical | [ ] |
| 7 | Differently abled employee counts by employment type and gender | Section A, IV.20(b) | `#/tables/6`, p. 2 | Numeric + categorical | [ ] |
| 8 | Women participation in Board and key management | Section A, IV.21 | `#/tables/7`, p. 2 | Numeric + categorical | [ ] |
| 9 | Permanent employee turnover rate by gender and financial year | Section A, IV.22 | `#/tables/8`, p. 2 | Numeric | [ ] |
| 10 | Subsidiaries, associates, joint venture status and shareholding | Section A, V.23(a) | `#/tables/9`, p. 3 | Mixed | [ ] |
| 11 | Complaints/grievances by stakeholder group, mechanism, filed and pending | Section A, VII.25 | `#/tables/10`, p. 3 | Mixed | [ ] |
| 12 | Continued complaints/grievances by stakeholder group | Section A, VII.25 (continued) | `#/tables/11`, p. 4 | Mixed | [ ] |
| 13 | Material responsible-business issues, risks/opportunities, rationale and mitigation | Section A, VII.26 | `#/tables/12`, p. 4 | Qualitative + categorical | [ ] |
| 14 | Continued material responsible-business issues and implications | Section A, VII.26 (continued) | `#/tables/13`, p. 5 | Qualitative + categorical | [ ] |

## Section B: Management and Process Disclosures

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 15 | Policy coverage of NGRBC Principles P1-P9 | Section B, policy and management processes | `#/tables/14`, p. 5 | Categorical | [ ] |
| 16 | Board approval, policy links, translation into procedures and value-chain coverage | Section B, policy and management processes | `#/tables/15`, p. 6 | Mixed | [ ] |
| 17 | Highest authority and Board committee responsible for BR oversight | Section B, governance, leadership and oversight | `#/tables/16`, p. 6 | Qualitative + categorical | [ ] |
| 18 | Review of NGRBC policies, performance follow-up and statutory compliance | Section B, governance, leadership and oversight | `#/tables/17`, p. 7 | Qualitative | [ ] |

## Section C: Principle 1 - Ethics, Transparency and Accountability

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 19 | Training and awareness programme coverage by employee category | Principle 1, Essential Indicator 1 | `#/tables/18`, p. 7 | Mixed | [ ] |
| 20 | Fines, penalties, settlements, compounding fees and appeals | Principle 1, Essential Indicators 2-3 | `#/tables/19`, p. 8 | Mixed | [ ] |
| 21 | Directors, KMPs, employees and workers subject to disciplinary action | Principle 1, Essential Indicator 5 | `#/tables/20`, p. 9 | Numeric + categorical | [ ] |
| 22 | Complaints relating to conflict of interest of Directors and KMPs | Principle 1, Essential Indicator 6 | `#/tables/21`, p. 9 | Mixed | [ ] |
| 23 | Accounts payable days | Principle 1, Essential Indicator 8 | `#/tables/22`, p. 9 | Numeric | [ ] |
| 24 | Purchase/sales concentration with trading houses, dealers and related parties | Principle 1, Essential Indicator 9 | `#/tables/23`, p. 10 | Mixed | [ ] |
| 25 | Value-chain partner awareness programmes and coverage | Principle 1, Leadership Indicator 1 | `#/tables/24`, p. 10 | Mixed | [ ] |

## Section C: Principle 2 - Sustainable and Safe Products/Services

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 26 | R&D and capex spending and environmental/social impact improvements | Principle 2, Essential Indicator 1 | `#/tables/25`, p. 11 | Mixed | [ ] |
| 27 | Life Cycle Assessment scope, agency and public communication | Principle 2, Leadership Indicator 1 | `#/tables/26`, p. 11 | Mixed | [ ] |

## Section C: Principle 3 - Employee Well-being

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 28 | Employee well-being coverage: health, accident, maternity, paternity and daycare | Principle 3, Essential Indicator 1(a) | `#/tables/27`, p. 12 | Numeric + categorical | [ ] |
| 29 | Spending on employee and worker well-being | Principle 3, Essential Indicator 1(c) | `#/tables/28`, p. 12 | Numeric | [ ] |
| 30 | Retirement benefits coverage and deposits: PF, gratuity, ESI, pension, NPS | Principle 3, Essential Indicator 2 | `#/tables/29`, p. 12 | Mixed | [ ] |
| 31 | Return-to-work and retention rates after parental leave | Principle 3, Essential Indicator 5 | `#/tables/30`, p. 13 | Numeric + categorical | [ ] |
| 32 | Employee and worker grievance mechanism | Principle 3, Essential Indicator 6 | `#/tables/31`, p. 13 | Categorical + qualitative | [ ] |
| 33 | Employee/worker association and union membership | Principle 3, Essential Indicator 7 | `#/tables/32`, p. 14 | Numeric + categorical | [ ] |
| 34 | Training on health, safety and skill upgradation | Principle 3, Essential Indicator 8 | `#/tables/33`, p. 14 | Numeric + categorical | [ ] |
| 35 | Performance and career development reviews | Principle 3, Essential Indicator 9 | `#/tables/34`, p. 14 | Numeric + categorical | [ ] |
| 36 | Safety incidents, LTIFR, injuries, fatalities and high-consequence harm | Principle 3, Essential Indicator 11 | `#/tables/35`, p. 15 | Numeric + categorical | [ ] |
| 37 | Employee/worker complaints on working conditions and health/safety | Principle 3, Essential Indicator 13 | `#/tables/36`, p. 16 | Mixed | [ ] |
| 38 | Assessment coverage for health and safety practices and working conditions | Principle 3, Essential Indicator 14 | `#/tables/37`, p. 16 | Numeric + categorical | [ ] |
| 39 | Rehabilitation and suitable employment after high-consequence injury | Principle 3, Leadership Indicator 3 | `#/tables/38`, p. 17 | Numeric + categorical | [ ] |
| 40 | Value-chain partner assessment coverage for health and safety and working conditions | Principle 3, Leadership Indicators 5-6 | `#/tables/39`, p. 17 | Numeric + categorical | [ ] |

## Section C: Principle 4 - Stakeholder Responsiveness

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 41 | Key stakeholder group, vulnerability, communication channels and engagement | Principle 4, Leadership Indicator 2 | `#/tables/40`, p. 17 | Categorical + qualitative | [ ] |
| 42 | Continued stakeholder groups, channels, frequency and engagement purpose | Principle 4, Leadership Indicator 2 | `#/tables/41`, p. 18 | Categorical + qualitative | [ ] |

## Section C: Principle 5 - Human Rights

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 43 | Human-rights training coverage for employees and workers | Principle 5, Essential Indicator 1 | `#/tables/42`, p. 19 | Numeric + categorical | [ ] |
| 44 | Minimum-wage coverage for employees and workers | Principle 5, Essential Indicator 2 | `#/tables/43`, p. 20 | Numeric + categorical | [ ] |
| 45 | Remuneration, salary/wage counts and median remuneration | Principle 5, Essential Indicator 3(a) | `#/tables/44`, p. 20 | Numeric + categorical | [ ] |
| 46 | Gross wages paid to females as a percentage of total wages | Principle 5, Essential Indicator 3(b) | `#/tables/45`, p. 20 | Numeric | [ ] |
| 47 | Complaints on sexual harassment, discrimination, child labour, wages and human rights | Principle 5, Essential Indicators 6-7 | `#/tables/46`, p. 21 | Mixed | [ ] |
| 48 | POSH complaints, percentage of female workforce and complaints upheld | Principle 5, Essential Indicator 7 | `#/tables/47`, p. 21 | Numeric + categorical | [ ] |
| 49 | Assessment coverage for labour, forced labour, harassment, discrimination and wages | Principle 5, Essential Indicator 10 | `#/tables/48`, p. 21 | Numeric + categorical | [ ] |
| 50 | Value-chain partner assessment coverage for human-rights topics | Principle 5, Leadership Indicators 4-5 | `#/tables/49`, p. 22 | Numeric + categorical | [ ] |

## Section C: Principle 6 - Environment

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 51 | Electricity, fuel, other-source and total energy consumption/intensity | Principle 6, Essential Indicator 1 | `#/tables/50`, p. 22 | Numeric | [ ] |
| 52 | Waste generated: plastic, e-waste, biomedical, battery, hazardous and other waste | Principle 6, Essential Indicator 8 | `#/tables/51`, p. 23 | Mixed | [ ] |
| 53 | Renewable and non-renewable energy consumption | Principle 6, Leadership Indicator 1 | `#/tables/52`, p. 24 | Numeric + categorical | [ ] |
| 54 | Water discharge by destination and treatment level | Principle 6, Leadership Indicators 2-3 | `#/tables/53`, p. 24 | Numeric + categorical | [ ] |

## Section C: Principle 7 - Public Policy

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 55 | Trade and industry chamber/association affiliations | Principle 7, Essential Indicator 1 | `#/tables/54`, p. 25 | Categorical + numeric | [ ] |
| 56 | Adverse orders for anticompetitive conduct and corrective action | Principle 7, Essential Indicator 2 | `#/tables/55`, p. 26 | Qualitative + categorical | [ ] |
| 57 | Public policy positions, advocacy method, disclosure and Board review | Principle 7, Leadership Indicator 1 | `#/tables/56`, p. 26 | Mixed | [ ] |

## Section C: Principle 8 - Inclusive Growth

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 58 | Job creation and wages paid in rural, semi-urban, urban and metropolitan locations | Principle 8, Essential Indicator 5 | `#/tables/57`, p. 27 | Numeric + categorical | [ ] |
| 59 | CSR beneficiaries, implementing NGO/institute, purpose and amount | Principle 8, CSR project disclosures | `#/tables/58`, p. 28 | Mixed | [ ] |
| 60 | Continued CSR beneficiaries and project amounts | Principle 8, CSR project disclosures | `#/tables/59`, p. 29 | Mixed | [ ] |
| 61 | Continued CSR beneficiaries and project amounts, including total | Principle 8, CSR project disclosures | `#/tables/60`, p. 30 | Mixed | [ ] |

## Section C: Principle 9 - Consumer Responsibility

| Check | Indicator / disclosure topic | Principle 9, Essential Indicator 2 | `#/tables/61`, p. 31 | Categorical + qualitative | [ ] |
| 62 | Consumer complaints: data privacy, advertising, cyber-security, essential services and other | Principle 9, Essential Indicator 3 | `#/tables/62`, p. 31 | Mixed | [ ] |

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

### Findings

| Checklist item | PDF page | Finding | Severity | Resolved |
|---|---:|---|---|:---:|
| | | | | [ ] |
