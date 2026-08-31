# BRSR Table Validation Checklist

Source: `BRSR_Infosys_2024_2025.md` and `BRSR_Infosys_2024_2025.json`

Purpose: one-time manual comparison of every extracted Docling table against the original BRSR PDF. This checklist is diagnostic only; it does not alter preprocessing or extraction.

Data type key: **Numeric** = counts, amounts, percentages, rates, years, or measurements. **Categorical** = yes/no, nil/NA, classifications, names, locations, or enumerated categories. **Qualitative** = narrative descriptions, explanations, rationale, policy text, or links. **Mixed** combines two or more of these.

## Coverage Summary

- Extracted tables: 81 (`#/tables/0` through `#/tables/80`)
- PDF provenance range: pages 2-49
- Environmental coverage: Principles 2 and 6, plus environmental disclosures in Section A (material responsible-business issues, item VII.26)
- Social coverage: Principles 3, 4, 5, and 8, plus social disclosures in Section A (employee counts, women participation, grievances)
- Governance coverage: Principles 1, 7, and 9, plus governance disclosures in Section A and Section B (company details, policy coverage matrix, review mechanisms)
- Unlike a bank, Infosys (an IT/services company) has no manufacturing-related Principle 2 leadership disclosures (LCA, recycled input material, EPR are all marked "Not applicable" with no tables) and a much larger Principle 8 CSR footprint (112 aspirational districts, ~80 named CSR projects split across several continuation tables).
- Note: tables 30-31 (`#/tables/30`, `#/tables/31`, page 17, employee/worker well-being coverage and spend) are content-wise Principle 3 Essential Indicator 1(a) and 1(c). In the extracted markdown they appear directly after Principle 2's Leadership Indicators text and before the "PRINCIPLE 3" section heading itself — an apparent page-layout/reading-order artifact from Docling extraction. They are classified below by their actual content (Principle 3), not by their position relative to the heading text.
- Note: `#/tables/35` (Principle 3, Essential Indicator 8, training) and `#/tables/77` (Principle 8, CSR beneficiaries continuation, page 47) hold intact structured cell data in the JSON (9x7 and 20x4 respectively), but the markdown export renders them as a disjointed sequence of single-value lines rather than a clean pipe table. Verify these two directly against the PDF and JSON `table_cells`, not the markdown rendering.
- For each row, compare table headings, row/column alignment, values, units, `Nil`/`NA` values, narrative text, and page boundaries against the PDF.

## Section A: General Disclosures

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 1 | Company identity (CIN, registered/corporate office, contact, financial year, assurance provider) | Section A, I. Company details | `#/tables/0`, p. 2 | Mixed | [ ] |
| 2 | Main business activity description and % of turnover | Section A, II.16 | `#/tables/1`, p. 3 | Mixed | [ ] |
| 3 | Products/services sold, NIC code, % of turnover contributed | Section A, II.17 | `#/tables/2`, p. 3 | Mixed | [ ] |
| 4 | Number of plants/offices, national vs. international, totals | Section A, III.18 | `#/tables/3`, p. 3 | Mixed | [ ] |
| 5 | Number of locations served (national states / international countries) | Section A, III.19(a) | `#/tables/4`, p. 3 | Numeric + categorical | [ ] |
| 6 | Employees and workers by employment type and gender | Section A, IV.20(a) | `#/tables/5`, p. 4 | Numeric + categorical | [ ] |
| 7 | Differently-abled employees and workers by employment type and gender | Section A, IV.20(b) | `#/tables/6`, p. 4 | Numeric + categorical | [ ] |
| 8 | Women participation in Board of Directors and Key Management Personnel | Section A, IV.21 | `#/tables/7`, p. 5 | Numeric + categorical | [ ] |
| 9 | Turnover rate for permanent employees, 3-year trend by gender | Section A, IV.22 | `#/tables/8`, p. 5 | Numeric | [ ] |
| 10 | CSR applicability, turnover, and net worth | Section A, VI.24 | `#/tables/9`, p. 5 | Mixed | [ ] |
| 11 | Complaints/grievances by stakeholder group, mechanism, filed and pending | Section A, VII.25 | `#/tables/10`, p. 6 | Mixed | [ ] |
| 12 | Material responsible-business issue 1 (climate change risk), rationale and mitigation | Section A, VII.26 | `#/tables/11`, p. 6 | Qualitative + categorical | [ ] |
| 13 | Continued material issues 2-4 (climate opportunity, employee experience, Tech for Good) | Section A, VII.26 (continued) | `#/tables/12`, p. 7 | Qualitative + categorical | [ ] |
| 14 | Continued material issues 5-6 (data privacy/information management, cybersecurity leadership) | Section A, VII.26 (continued) | `#/tables/13`, p. 8 | Qualitative + categorical | [ ] |

## Section B: Management and Process Disclosures

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 15 | Policy coverage matrix for P1-P9: policy/board approval, weblinks, codes and certifications adopted | Section B, policy and management processes | `#/tables/14`, p. 9 | Mixed | [ ] |
| 16 | Performance against ESG commitments, goals and targets (narrative reference) | Section B, policy and management processes, item 6 | `#/tables/15`, p. 10 | Qualitative | [ ] |
| 17 | Highest authority responsible for implementation/oversight of BR policies (4 policies) | Section B, governance, leadership and oversight, item 8 | `#/tables/16`, p. 10 | Mixed | [ ] |
| 18 | ESG Committee of the Board: directors, designation, DIN | Section B, governance, leadership and oversight, item 9 | `#/tables/17`, p. 10 | Categorical | [ ] |
| 19 | Review of NGRBC policies across P1-P9: performance follow-up, statutory compliance review, independent external assessment | Section B, governance, leadership and oversight, items 10-12 | `#/tables/18`, p. 11 | Mixed | [ ] |

## Section C: Principle 1 - Ethics, Transparency and Accountability

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 20 | Training and awareness programme coverage by category (Board, KMP, employees, workers) | Principle 1, Essential Indicator 1 | `#/tables/19`, p. 12 | Mixed | [ ] |
| 21 | Monetary fines/penalties: principle, regulator, amount, case, appeal status | Principle 1, Essential Indicator 2 | `#/tables/20`, p. 12 | Mixed | [ ] |
| 22 | Settlement and compounding fee details (SEBI settlement order) | Principle 1, Essential Indicator 2 (continued) | `#/tables/21`, p. 13 | Mixed | [ ] |
| 23 | Non-monetary imprisonment/punishment actions | Principle 1, Essential Indicator 2 (continued) | `#/tables/22`, p. 13 | Categorical | [ ] |
| 24 | Appeal/revision of fines and penalties (not applicable) | Principle 1, Essential Indicator 3 | `#/tables/23`, p. 13 | Categorical | [ ] |
| 25 | Disciplinary action against Directors/KMPs/employees/workers for bribery/corruption | Principle 1, Essential Indicator 5 | `#/tables/24`, p. 13 | Numeric + categorical | [ ] |
| 26 | Complaints regarding conflict of interest of Directors and KMPs | Principle 1, Essential Indicator 6 | `#/tables/25`, p. 13 | Mixed | [ ] |
| 27 | Number of days of accounts payable | Principle 1, Essential Indicator 8 | `#/tables/26`, p. 14 | Numeric | [ ] |
| 28 | Concentration of purchases/sales with trading houses, dealers and related parties | Principle 1, Essential Indicator 9 | `#/tables/27`, p. 14 | Numeric | [ ] |
| 29 | Value-chain partner awareness programme coverage | Principle 1, Leadership Indicator 1 | `#/tables/28`, p. 15 | Mixed | [ ] |

## Section C: Principle 2 - Sustainable and Safe Products/Services

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 30 | R&D and capex spend (%) and environmental/social impact improvements | Principle 2, Essential Indicator 1 | `#/tables/29`, p. 15 | Mixed | [ ] |

## Section C: Principle 3 - Employee Well-being

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 31 | Employee well-being coverage by gender: health, accident, maternity, paternity, daycare | Principle 3, Essential Indicator 1(a) | `#/tables/30`, p. 17 | Numeric + categorical | [ ] |
| 32 | Spending on employee/worker well-being as % of total revenue | Principle 3, Essential Indicator 1(c) | `#/tables/31`, p. 17 | Numeric | [ ] |
| 33 | Retirement benefits coverage and deposit status: PF, gratuity, ESI, NPS, superannuation | Principle 3, Essential Indicator 2 | `#/tables/32`, p. 18 | Mixed | [ ] |
| 34 | Return-to-work and retention rates after parental leave, by gender | Principle 3, Essential Indicator 5 | `#/tables/33`, p. 18 | Numeric | [ ] |
| 35 | Employee/worker membership in associations or unions | Principle 3, Essential Indicator 7 | `#/tables/34`, p. 19 | Numeric + categorical | [ ] |
| 36 | Training on health/safety measures and skill upgradation (markdown rendering is broken; verify against JSON/PDF) | Principle 3, Essential Indicator 8 | `#/tables/35`, p. 20 | Numeric + categorical | [ ] |
| 37 | Safety incidents: LTIFR, recordable injuries, fatalities, high-consequence injuries | Principle 3, Essential Indicator 11 | `#/tables/36`, p. 21 | Numeric + categorical | [ ] |
| 38 | Employee/worker complaints on working conditions and health/safety | Principle 3, Essential Indicator 13 | `#/tables/37`, p. 22 | Mixed | [ ] |
| 39 | Assessment coverage for health and safety practices and working conditions | Principle 3, Essential Indicator 14 | `#/tables/38`, p. 22 | Numeric | [ ] |
| 40 | Rehabilitation/suitable employment after high-consequence work-related injury | Principle 3, Leadership Indicator 3 | `#/tables/39`, p. 23 | Numeric | [ ] |
| 41 | Value-chain partner assessment coverage: working conditions and health/safety | Principle 3, Leadership Indicators 5-6 | `#/tables/40`, p. 23 | Numeric | [ ] |

## Section C: Principle 4 - Stakeholder Responsiveness

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 42 | Key stakeholder groups (Investors, Employees): vulnerability, channels, frequency, purpose of engagement | Principle 4, Leadership Indicator 2 | `#/tables/41`, p. 24 | Categorical + qualitative | [ ] |
| 43 | Continued stakeholder groups (Clients, Government/regulatory bodies, Communities, Suppliers) | Principle 4, Leadership Indicator 2 (continued) | `#/tables/42`, p. 25 | Categorical + qualitative | [ ] |

## Section C: Principle 5 - Human Rights

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 44 | Human-rights training coverage for employees and workers | Principle 5, Essential Indicator 1 | `#/tables/43`, p. 26 | Numeric + categorical | [ ] |
| 45 | Minimum-wage compliance: equal to / more than minimum wage, by gender | Principle 5, Essential Indicator 2 | `#/tables/44`, p. 27 | Numeric + categorical | [ ] |
| 46 | Median remuneration: Board, KMP, employee levels, by gender | Principle 5, Essential Indicator 3(a) | `#/tables/45`, p. 27 | Numeric + categorical | [ ] |
| 47 | Gross wages paid to females as % of total wages | Principle 5, Essential Indicator 3(b) | `#/tables/46`, p. 28 | Numeric | [ ] |
| 48 | Complaints: sexual harassment, discrimination, child/forced labor, wages, other human rights | Principle 5, Essential Indicator 6 | `#/tables/47`, p. 28 | Mixed | [ ] |
| 49 | POSH complaints: total, % of female workforce, complaints upheld | Principle 5, Essential Indicator 7 | `#/tables/48`, p. 29 | Numeric | [ ] |
| 50 | Assessment coverage: child labor, forced labor, sexual harassment, discrimination, wages | Principle 5, Essential Indicator 10 | `#/tables/49`, p. 29 | Numeric + categorical | [ ] |
| 51 | Value-chain partner assessment coverage for human-rights topics | Principle 5, Leadership Indicators 4-5 | `#/tables/50`, p. 30 | Numeric + categorical | [ ] |

## Section C: Principle 6 - Environment

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 52 | Energy consumption (renewable/non-renewable electricity, fuel) and intensity | Principle 6, Essential Indicator 1 | `#/tables/51`, p. 31 | Numeric | [ ] |
| 53 | Water withdrawal by source and water intensity | Principle 6, Essential Indicator 3 | `#/tables/52`, p. 32 | Numeric | [ ] |
| 54 | Water discharge to surface water, by treatment level | Principle 6, Essential Indicator 4 | `#/tables/53`, p. 32 | Numeric + categorical | [ ] |
| 55 | Continued water discharge: groundwater, seawater, third parties, others, total | Principle 6, Essential Indicator 4 (continued) | `#/tables/54`, p. 33 | Numeric + categorical | [ ] |
| 56 | Air emissions other than GHG (NOx, SOx, particulate matter, POP, VOC, HAP) | Principle 6, Essential Indicator 6 | `#/tables/55`, p. 33 | Numeric + categorical | [ ] |
| 57 | Scope 1 and Scope 2 GHG emissions and intensity | Principle 6, Essential Indicator 7 | `#/tables/56`, p. 34 | Numeric | [ ] |
| 58 | Waste generated, recovered (recycled/reused), and disposed by category | Principle 6, Essential Indicator 9 | `#/tables/57`, p. 35 | Mixed | [ ] |
| 59 | Environmental impact assessments of projects (empty template, Nil) | Principle 6, Essential Indicator 12 | `#/tables/58`, p. 36 | Categorical | [ ] |
| 60 | Water withdrawal/discharge in water-stress areas | Principle 6, Leadership Indicator 1 | `#/tables/59`, p. 37 | Numeric + categorical | [ ] |
| 61 | Continued water discharge in water-stress areas (third parties, total) | Principle 6, Leadership Indicator 1 (continued) | `#/tables/60`, p. 38 | Numeric | [ ] |
| 62 | Scope 3 GHG emissions and intensity | Principle 6, Leadership Indicator 2 | `#/tables/61`, p. 38 | Numeric | [ ] |
| 63 | Resource-efficiency/innovative technology initiatives and outcomes | Principle 6, Leadership Indicator 4 | `#/tables/62`, p. 39 | Qualitative + categorical | [ ] |

## Section C: Principle 7 - Public Policy

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 64 | Top 10 trade and industry chamber/association affiliations | Principle 7, Essential Indicator 1(b) | `#/tables/63`, p. 40 | Categorical | [ ] |
| 65 | Public policy positions advocated: method, disclosure, Board review frequency | Principle 7, Leadership Indicator 1 | `#/tables/64`, p. 41 | Mixed | [ ] |
| 66 | Continued public policy positions advocated | Principle 7, Leadership Indicator 1 (continued) | `#/tables/65`, p. 42 | Mixed | [ ] |

## Section C: Principle 8 - Inclusive Growth

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 67 | Social Impact Assessments of projects (not applicable) | Principle 8, Essential Indicator 1 | `#/tables/66`, p. 43 | Categorical | [ ] |
| 68 | Rehabilitation and Resettlement (R&R) project details (not applicable) | Principle 8, Essential Indicator 2 | `#/tables/67`, p. 43 | Categorical | [ ] |
| 69 | Input material sourced from MSMEs/small producers and within India | Principle 8, Essential Indicator 4 | `#/tables/68`, p. 43 | Numeric | [ ] |
| 70 | Job creation/wages by location: rural, semi-urban, urban, metropolitan | Principle 8, Essential Indicator 5 | `#/tables/69`, p. 44 | Numeric + categorical | [ ] |
| 71 | CSR spend by aspirational district, part 1 (Andhra Pradesh-Bihar) | Principle 8, Leadership Indicator 2 | `#/tables/70`, p. 44 | Numeric + categorical | [ ] |
| 72 | Continued CSR spend by aspirational district, part 2 (Bihar-Gujarat) | Principle 8, Leadership Indicator 2 (continued) | `#/tables/71`, p. 44 | Numeric + categorical | [ ] |
| 73 | Continued CSR spend by aspirational district, part 3 (Jammu & Kashmir-Meghalaya) | Principle 8, Leadership Indicator 2 (continued) | `#/tables/72`, p. 45 | Numeric + categorical | [ ] |
| 74 | Continued CSR spend by aspirational district, part 4 (Odisha-Uttarakhand, including total) | Principle 8, Leadership Indicator 2 (continued) | `#/tables/73`, p. 45 | Numeric + categorical | [ ] |
| 75 | Intellectual property based on traditional knowledge (empty template, not applicable) | Principle 8, item 4 | `#/tables/74`, p. 46 | Categorical | [ ] |
| 76 | Corrective actions on traditional-knowledge IP disputes (empty template, not applicable) | Principle 8, item 5 | `#/tables/75`, p. 46 | Categorical | [ ] |
| 77 | CSR project beneficiaries and % from vulnerable/marginalised groups, part 1 | Principle 8, item 6 | `#/tables/76`, p. 46 | Numeric + categorical | [ ] |
| 78 | Continued CSR project beneficiaries, part 2 (markdown rendering is broken; verify against JSON/PDF) | Principle 8, item 6 (continued) | `#/tables/77`, p. 47 | Numeric + categorical | [ ] |

## Section C: Principle 9 - Consumer Responsibility

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 79 | Turnover share of products/services with environmental/social product information (not applicable, B2B) | Principle 9, Essential Indicator 2 | `#/tables/78`, p. 48 | Categorical | [ ] |
| 80 | Consumer complaints: data privacy, advertising, cybersecurity, essential services, trade practices | Principle 9, Essential Indicator 3 | `#/tables/79`, p. 48 | Mixed | [ ] |
| 81 | Product recalls: voluntary/forced, number and reasons | Principle 9, Essential Indicator 4 | `#/tables/80`, p. 49 | Categorical | [ ] |

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
