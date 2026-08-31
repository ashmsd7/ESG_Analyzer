# BRSR Table Validation Checklist

Source: `BRSR_TataELXSI_2025_2026.md` and `BRSR_TataELXSI_2025_2026.json`

Purpose: one-time manual comparison of every extracted Docling table against the original BRSR PDF. This checklist is diagnostic only; it does not alter preprocessing or extraction.

Data type key: **Numeric** = counts, amounts, percentages, rates, years, or measurements. **Categorical** = yes/no, nil/NA, classifications, names, locations, or enumerated categories. **Qualitative** = narrative descriptions, explanations, rationale, policy text, or links. **Mixed** combines two or more of these.

## Coverage Summary

- Extracted tables: 91 (`#/tables/0` through `#/tables/90`)
- PDF provenance range: pages 3-59
- Environmental coverage: Principles 2 and 6, plus environmental disclosures in Section A and the assurance annexure
- Social coverage: Principles 3, 4, 5, and 8, plus social disclosures in Section A
- Governance coverage: Principles 1, 7, and 9, plus governance and policy disclosures in Section A and Section B
- Additional coverage not present in other companies' filings: an Independent Assurance Statement with a "Verified Key Performance Indicators" annexure (`#/tables/84` - `#/tables/90`, pages 53-59) issued by ISOQAR, consolidating assured ESG metrics across all nine principles. Tata Elxsi is an ER&D/design and technology services company (not a manufacturer or a bank), so several Principle 2 and Principle 6 disclosures that are typically populated for manufacturing/financial entities (EPR, LCA, effluent treatment, PAT scheme) are reported as Nil/NA/Not Applicable rather than populated with figures - this is expected given the business model and is not an extraction defect.
- For each row, compare table headings, row/column alignment, values, units, `Nil`/`NA` values, narrative text, and page boundaries against the PDF.

## Section A: General Disclosures

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 1 | Entity identity: CIN, incorporation year, registered/corporate office, email, phone, website, reporting FY, stock exchanges, paid-up capital, BRSR contact person, reporting boundary, assurance provider and type | Section A, I. Details of the Listed Entity | `#/tables/0`, p. 3 | Mixed | [ ] |
| 2 | Main business activities and % of turnover (Software Development & Services; Systems Integration & Support) | Section A, II.16 | `#/tables/1`, p. 3 | Mixed | [ ] |
| 3 | Products/services sold, NIC code, % turnover contribution | Section A, II.17 | `#/tables/2`, p. 4 | Mixed | [ ] |
| 4 | Number of plants/offices - national vs. international totals | Section A, III.18 | `#/tables/3`, p. 4 | Mixed | [ ] |
| 5 | Markets served - number of states/UT and countries | Section A, III.19(a) | `#/tables/4`, p. 4 | Mixed | [ ] |
| 6 | Employees and workers by category (permanent/other than permanent) and gender | Section A, IV.20(a) | `#/tables/5`, p. 4 | Numeric + categorical | [ ] |
| 7 | Differently abled employees and workers by category and gender | Section A, IV.20(b) | `#/tables/6`, p. 5 | Numeric + categorical | [ ] |
| 8 | Women participation - Board of Directors and Key Managerial Personnel | Section A, IV.21 | `#/tables/7`, p. 5 | Numeric + categorical | [ ] |
| 9 | Turnover rate for permanent employees by gender, FY 2025-26 / FY 2024-25 / FY 2023-24 | Section A, IV.22 | `#/tables/8`, p. 5 | Numeric | [ ] |
| 10 | Complaints/grievances by stakeholder group - communities, investors, shareholders (filed/pending) | Section A, VII.25 | `#/tables/9`, p. 6 | Mixed | [ ] |
| 11 | Continued complaints/grievances - employees & workers, customers, value chain partners, other | Section A, VII.25 (continued) | `#/tables/10`, p. 7 | Mixed | [ ] |
| 12 | Material issue 1 - Employee Engagement and Well-Being: risk/opportunity, rationale, mitigation, financial implication | Section A, VII.26 | `#/tables/11`, p. 8 | Qualitative + categorical | [ ] |
| 13 | Material issues 2-3 - Data Privacy, Cyber Security | Section A, VII.26 (continued) | `#/tables/12`, p. 9 | Qualitative + categorical | [ ] |
| 14 | Material issue 4 - Climate Change (risk and opportunity) | Section A, VII.26 (continued) | `#/tables/13`, p. 10 | Qualitative + categorical | [ ] |
| 15 | Material issues 5-6 - Talent Management & DEI, Innovation & IP Protection | Section A, VII.26 (continued) | `#/tables/14`, p. 11 | Qualitative + categorical | [ ] |
| 16 | Material issue 7 - Risk Management | Section A, VII.26 (continued) | `#/tables/15`, p. 12 | Qualitative + categorical | [ ] |
| 17 | Material issues 8-9 - Community Engagement (CSR), Product and Service Stewardship | Section A, VII.26 (continued) | `#/tables/16`, p. 13 | Qualitative + categorical | [ ] |

## Section B: Management and Process Disclosures

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 18 | Policy coverage matrix Q1(a-c): policy coverage of each NGRBC principle P1-P9, Board approval, policy weblink | Section B, policy and management processes, Q1 | `#/tables/17`, p. 14 | Categorical | [ ] |
| 19 | Q5: specific commitments, goals and targets by principle (N across P1-P5/P7-P9, Y* for P6) | Section B, policy and management processes, Q5 | `#/tables/18`, p. 14 | Categorical | [ ] |
| 20 | Header fragment for Q6 disclosure table (Disclosure Questions / P1-P9), no populated data rows | Section B, policy and management processes, Q6 (header) | `#/tables/19`, p. 15 | Categorical | [ ] |
| 21 | Q6: performance against commitments/targets, reasons if not met (NA across all principles) | Section B, policy and management processes, Q6 | `#/tables/20`, p. 15 | Categorical | [ ] |
| 22 | Q8-9: highest authority for BR policy oversight (CEO & MD) and Board committee responsible for sustainability decisions | Section B, governance, leadership and oversight, Q8-9 | `#/tables/21`, p. 15 | Qualitative + categorical | [ ] |
| 23 | Q10: review of NGRBC performance/compliance by director or committee, and frequency, by principle P1-P9 | Section B, governance, leadership and oversight, Q10 | `#/tables/22`, p. 16 | Categorical + qualitative | [ ] |
| 24 | Q11: independent external assessment of policies by principle (Y for P1, P3-P9) | Section B, governance, leadership and oversight, Q11 | `#/tables/23`, p. 16 | Categorical | [ ] |
| 25 | Q12: reasons principles are not covered by a policy (NA throughout, since all nine are covered) | Section B, policy and management processes, Q12 | `#/tables/24`, p. 16 | Categorical | [ ] |

## Section C: Principle 1 - Ethics, Transparency and Accountability

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 26 | Training and awareness programme coverage by segment - BoD, KMP, employees, workers | Principle 1, Essential Indicator 1 | `#/tables/25`, p. 18 | Mixed | [ ] |
| 27 | Monetary fines/penalties/settlements/compounding fees (Nil across all categories) | Principle 1, Essential Indicator 2 | `#/tables/26`, p. 18 | Numeric + categorical | [ ] |
| 28 | Non-monetary fines - imprisonment/punishment (Nil) | Principle 1, Essential Indicator 2 (continued) | `#/tables/27`, p. 19 | Categorical | [ ] |
| 29 | Appeal/revision details on Q2 monetary/non-monetary instances (NA) | Principle 1, Essential Indicator 3 | `#/tables/28`, p. 19 | Categorical | [ ] |
| 30 | Conflict of interest complaints by Directors/KMPs/Employees/Workers (Nil) | Principle 1, Essential Indicator 6 | `#/tables/29`, p. 19 | Categorical | [ ] |
| 31 | Continued conflict of interest complaints - number and remarks by financial year | Principle 1, Essential Indicator 6 (continued) | `#/tables/30`, p. 19 | Numeric + categorical | [ ] |
| 32 | Accounts payable days (16 vs. 7) | Principle 1, Essential Indicator 8 | `#/tables/31`, p. 20 | Numeric | [ ] |
| 33 | Openness of business - concentration of purchases/sales with trading houses, dealers, related parties | Principle 1, Essential Indicator 9 | `#/tables/32`, p. 20 | Numeric + categorical | [ ] |
| 34 | Value-chain partner awareness programme coverage on principles (100% across P1-P9) | Principle 1, Leadership Indicator 1 | `#/tables/33`, p. 21 | Numeric + categorical | [ ] |

## Section C: Principle 2 - Sustainable and Safe Products/Services

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 35 | R&D and capex spend (% of total) and environmental/social impact improvements | Principle 2, Essential Indicator 1 | `#/tables/34`, p. 21 | Mixed | [ ] |
| 36 | Life Cycle Assessment (LCA) scope, NIC code, boundary, external agency, public disclosure (Nil/NA) | Principle 2, Leadership Indicator 1 | `#/tables/35`, p. 23 | Mixed | [ ] |
| 37 | Reclaimed products/packaging - reused, recycled, safely disposed by category (Nil throughout) | Principle 2, Leadership Indicator 4 | `#/tables/36`, p. 23 | Numeric + categorical | [ ] |

## Section C: Principle 3 - Employee Well-being

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 38 | Employee well-being coverage: health, accident, maternity, paternity, day care insurance | Principle 3, Essential Indicator 1(a) | `#/tables/37`, p. 24 | Numeric + categorical | [ ] |
| 39 | Worker well-being coverage: same benefit categories | Principle 3, Essential Indicator 1(b) | `#/tables/38`, p. 24 | Numeric + categorical | [ ] |
| 40 | Retirement benefits coverage and deposit status - PF, Gratuity, ESI | Principle 3, Essential Indicator 2 | `#/tables/39`, p. 25 | Numeric + categorical | [ ] |
| 41 | Return-to-work and retention rates after parental leave, permanent employees and workers | Principle 3, Essential Indicator 5 | `#/tables/40`, p. 26 | Mixed | [ ] |
| 42 | Employee/worker association and union membership | Principle 3, Essential Indicator 7 | `#/tables/41`, p. 26 | Numeric + categorical | [ ] |
| 43 | Training given to employees and workers - health & safety and skill upgradation | Principle 3, Essential Indicator 8 | `#/tables/42`, p. 27 | Numeric + categorical | [ ] |
| 44 | Performance and career development reviews of employees and workers | Principle 3, Essential Indicator 9 | `#/tables/43`, p. 27 | Numeric + categorical | [ ] |
| 45 | Safety incidents - LTIFR, recordable injuries, fatalities, high-consequence harm | Principle 3, Essential Indicator 11 | `#/tables/44`, p. 28 | Numeric + categorical | [ ] |
| 46 | Employee/worker complaints on working conditions and health & safety | Principle 3, Essential Indicator 13 | `#/tables/45`, p. 29 | Mixed | [ ] |
| 47 | Assessment coverage - health & safety practices and working conditions (100%) | Principle 3, Essential Indicator 14 | `#/tables/46`, p. 29 | Numeric + categorical | [ ] |
| 48 | Rehabilitation and suitable employment after high-consequence injury (0 affected) | Principle 3, Leadership Indicator 4 | `#/tables/47`, p. 30 | Numeric + categorical | [ ] |
| 49 | Value-chain partner assessment coverage - health & safety practices, working conditions (100%) | Principle 3, Leadership Indicator 5 | `#/tables/48`, p. 30 | Numeric + categorical | [ ] |

## Section C: Principle 4 - Stakeholder Responsiveness

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 50 | Key stakeholder groups (shareholders, employees, customers) - vulnerability, communication channels, frequency, purpose | Principle 4, Essential Indicator 2 | `#/tables/49`, p. 31 | Categorical + qualitative | [ ] |
| 51 | Continued stakeholder groups (academic institutions, suppliers/vendors/partners, communities, regulatory bodies) | Principle 4, Essential Indicator 2 (continued) | `#/tables/50`, p. 32 | Categorical + qualitative | [ ] |

## Section C: Principle 5 - Human Rights

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 52 | Human-rights training coverage - column header structure (employees/workers, current vs. previous FY) | Principle 5, Essential Indicator 1 | `#/tables/51`, p. 33 | Categorical | [ ] |
| 53 | Continued - permanent and other-than-permanent employees trained (100%) | Principle 5, Essential Indicator 1 (continued) | `#/tables/52`, p. 33 | Numeric + categorical | [ ] |
| 54 | Continued - workers trained (narrative: mandatory Tata Code of Conduct orientation) | Principle 5, Essential Indicator 1 (continued) | `#/tables/53`, p. 33 | Mixed | [ ] |
| 55 | Minimum wage coverage - employees (equal to / more than minimum wage) | Principle 5, Essential Indicator 2 | `#/tables/54`, p. 33 | Numeric + categorical | [ ] |
| 56 | Continued minimum wage coverage - workers | Principle 5, Essential Indicator 2 (continued) | `#/tables/55`, p. 34 | Numeric + categorical | [ ] |
| 57 | Complaints - sexual harassment, discrimination, child/forced labour, wages, other human-rights issues | Principle 5, Essential Indicator 6 | `#/tables/56`, p. 35 | Numeric + categorical | [ ] |
| 58 | POSH complaints - total filed, % of female workforce, upheld | Principle 5, Essential Indicator 7 | `#/tables/57`, p. 36 | Numeric + categorical | [ ] |
| 59 | Assessment coverage - child labour, forced labour, sexual harassment, discrimination, wages (100%) | Principle 5, Essential Indicator 10 | `#/tables/58`, p. 36 | Numeric + categorical | [ ] |
| 60 | Value-chain partner assessment coverage for human-rights topics (100%) | Principle 5, Leadership Indicator 4 | `#/tables/59`, p. 37 | Numeric + categorical | [ ] |

## Section C: Principle 6 - Environment

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 61 | Energy consumption (renewable vs. non-renewable) and energy intensity metrics | Principle 6, Essential Indicator 1 | `#/tables/60`, p. 38 | Numeric | [ ] |
| 62 | Water withdrawal by source, total consumption and intensity | Principle 6, Essential Indicator 3 | `#/tables/61`, p. 39 | Numeric | [ ] |
| 63 | Water discharge by destination and level of treatment | Principle 6, Essential Indicator 4 | `#/tables/62`, p. 40 | Numeric | [ ] |
| 64 | Air emissions (NOx, SOx, PM, POP, VOC, HAP) - not measured/immaterial | Principle 6, Essential Indicator 6 | `#/tables/63`, p. 41 | Categorical | [ ] |
| 65 | Scope 1 and Scope 2 GHG emissions and intensity per turnover | Principle 6, Essential Indicator 7 | `#/tables/64`, p. 41 | Numeric | [ ] |
| 66 | Continued - PPP-adjusted and per-employee GHG emission intensity | Principle 6, Essential Indicator 7 (continued) | `#/tables/65`, p. 42 | Numeric | [ ] |
| 67 | Waste generated by category (plastic, e-waste, biomedical, battery, hazardous, other) and intensity | Principle 6, Essential Indicator 9 | `#/tables/66`, p. 43 | Numeric | [ ] |
| 68 | Environmental impact assessment (EIA) of projects - empty template, not applicable | Principle 6, Essential Indicator 12 | `#/tables/67`, p. 44 | Categorical | [ ] |
| 69 | Non-compliance with environmental law/regulations - empty template, not applicable | Principle 6, Essential Indicator 13 | `#/tables/68`, p. 44 | Categorical | [ ] |
| 70 | Scope 3 emissions and intensity (employee commuting and air travel) | Principle 6, Leadership Indicator 2 | `#/tables/69`, p. 45 | Numeric | [ ] |

## Section C: Principle 7 - Public Policy

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 71 | Trade and industry chamber/association affiliations (Nil) | Principle 7, Essential Indicator 1(b) | `#/tables/70`, p. 46 | Categorical | [ ] |
| 72 | Corrective action on anticompetitive-conduct adverse orders (NA) | Principle 7, Essential Indicator 2 | `#/tables/71`, p. 46 | Categorical | [ ] |
| 73 | Public policy positions advocated, method, public disclosure, Board review frequency (Nil) | Principle 7, Leadership Indicator 1 | `#/tables/72`, p. 47 | Qualitative + categorical | [ ] |

## Section C: Principle 8 - Inclusive Growth

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 74 | Social Impact Assessment (SIA) of projects - empty template, not applicable | Principle 8, Essential Indicator 1 | `#/tables/73`, p. 47 | Categorical | [ ] |
| 75 | Rehabilitation and Resettlement (R&R) ongoing projects - empty template, not applicable | Principle 8, Essential Indicator 2 | `#/tables/74`, p. 47 | Categorical | [ ] |
| 76 | Job creation in smaller towns - sourcing from MSMEs and within India, % of wage cost | Principle 8, Essential Indicator 5 | `#/tables/75`, p. 48 | Numeric | [ ] |
| 77 | Continued - wages by location (rural/semi-urban/urban/metropolitan) | Principle 8, Essential Indicator 5 (continued) | `#/tables/76`, p. 48 | Numeric + categorical | [ ] |
| 78 | Negative social impact identified and corrective action (NA) | Principle 8, Leadership Indicator 3 | `#/tables/77`, p. 48 | Categorical | [ ] |
| 79 | CSR spend in aspirational districts (Karnataka - Raichur, Rs 60,00,000) | Principle 8, Leadership Indicator 2 | `#/tables/78`, p. 48 | Numeric + categorical | [ ] |
| 80 | Intellectual property benefit-sharing from traditional knowledge (Nil) | Principle 8, Leadership Indicator 4 | `#/tables/79`, p. 49 | Categorical | [ ] |
| 81 | Corrective action on adverse IP-related traditional-knowledge disputes (Nil) | Principle 8, Leadership Indicator 5 | `#/tables/80`, p. 49 | Categorical | [ ] |
| 82 | CSR project beneficiaries and % from vulnerable/marginalised groups | Principle 8, Leadership Indicator 6 | `#/tables/81`, p. 49 | Categorical | [ ] |

## Section C: Principle 9 - Consumer Responsibility

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 83 | Consumer complaints - data privacy, advertising, cybersecurity, essential services, trade practices (Nil across) | Principle 9, Essential Indicator 3 | `#/tables/82`, p. 50 | Numeric + categorical | [ ] |
| 84 | Product recall instances - voluntary/forced (not applicable, B2B contractual delivery model) | Principle 9, Essential Indicator 4 | `#/tables/83`, p. 50 | Qualitative + categorical | [ ] |

## Independent Assurance Statement: Verified Key Performance Indicators

ISOQAR's reasonable-assurance annexure. It restates assured ESG figures already disclosed above, organised by attribute number (1-22) rather than by BRSR principle, and is split into 7 Docling tables purely by page break within one continuous PDF table.

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 85 | Attributes 1-2: GHG footprint (Scope 1/2 emissions, intensity) and Water footprint (consumption, discharge, intensity) | Independent Assurance Statement, Verified KPIs | `#/tables/84`, p. 53 | Numeric | [ ] |
| 86 | Attributes 3-4: Energy footprint (consumption, % renewable, intensity) and circularity/waste management, recovery and disposal breakdown | Independent Assurance Statement, Verified KPIs (continued) | `#/tables/85`, p. 54 | Numeric | [ ] |
| 87 | Attributes 5-8: employee well-being/safety spend and incidents, gender diversity and POSH complaints, inclusive-development sourcing, data/cybersecurity breach and accounts-payable metrics | Independent Assurance Statement, Verified KPIs (continued) | `#/tables/86`, p. 55 | Numeric + categorical | [ ] |
| 88 | Attributes 9-12: openness of business (RPT/trading house concentration), business-activity turnover split, operations/markets served, employee & worker headcount details | Independent Assurance Statement, Verified KPIs (continued) | `#/tables/87`, p. 56 | Numeric + categorical | [ ] |
| 89 | Attributes 13-18 (partial): women representation on Board/KMP, employee turnover rates, financial details (net worth, turnover), Principle 1-3 KPIs (training coverage, R&D spend, employee benefit coverage) | Independent Assurance Statement, Verified KPIs (continued) | `#/tables/88`, p. 57 | Numeric + categorical | [ ] |
| 90 | Attributes 18-19 (continued): Principle 3 performance reviews/training/complaints/assessments, Principle 5 human-rights training, minimum wage, median remuneration, assessment and complaint KPIs | Independent Assurance Statement, Verified KPIs (continued) | `#/tables/89`, p. 58 | Numeric + categorical | [ ] |
| 91 | Attributes 20-22: Principle 6 air emissions and Scope 3 GHG KPIs, CSR aspirational-district spend, Principle 9 consumer-complaint KPIs | Independent Assurance Statement, Verified KPIs (continued) | `#/tables/90`, p. 59 | Numeric + categorical | [ ] |

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
- [ ] Empty/near-empty template tables (checklist items 20, 68, 69, 74, 75) are confirmed as genuinely blank in the source PDF, not a Docling extraction failure.

### Findings

| Checklist item | PDF page | Finding | Severity | Resolved |
|---|---:|---|---|:---:|
| | | | | [ ] |
