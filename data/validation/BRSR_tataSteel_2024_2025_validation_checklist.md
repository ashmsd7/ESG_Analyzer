# BRSR Table Validation Checklist

Source: `BRSR_tataSteel_2024_2025.md` and `BRSR_tataSteel_2024_2025.json`

Purpose: one-time manual comparison of every extracted Docling table against the original BRSR PDF. This checklist is diagnostic only; it does not alter preprocessing or extraction.

Data type key: **Numeric** = counts, amounts, percentages, rates, years, or measurements. **Categorical** = yes/no, nil/NA, classifications, names, locations, or enumerated categories. **Qualitative** = narrative descriptions, explanations, rationale, policy text, or links. **Mixed** combines two or more of these.

## Coverage Summary

- Extracted tables: 97 (`#/tables/0` through `#/tables/96`)
- PDF provenance range: pages 2-63
- Environmental coverage: Principle 6 (13 tables covering energy, water withdrawal/discharge, air emissions, Scope 1/2/3 GHG emissions, waste management, ecologically sensitive locations, and EIA projects) and Principle 2 (sustainable sourcing, Life Cycle Assessment, recycled/reclaimed material), plus the environmental risk items inside Section A's materiality disclosure (VII.26)
- Social coverage: Principles 3, 4, 5, and 8, plus employee, CSR, and grievance/complaint disclosures in Section A
- Governance coverage: Principles 1, 7, and 9, plus policy and oversight disclosures in Section B and the general/company disclosures in Section A
- Tata Steel is a diversified heavy-manufacturing and mining group (unlike CBI, a bank), so environmental reporting is substantially larger here: Principle 6 alone accounts for 13 of 97 tables (versus 4 of 63 for CBI), reflecting energy, water, air, GHG, and waste data reported across standalone/consolidated boundaries and multiple geographies (India, Netherlands, UK, Thailand). Section A's materiality disclosure is also split across 5 tables (versus CBI's 2) because Tata Steel's issue list runs Strategic/Operational/Social risk categories (GHG, circular economy, water, energy, safety, air quality, biodiversity, R&D, supply chain, employee well-being, community) rather than a short combined list.
- For each row, compare table headings, row/column alignment, values, units, `Nil`/`NA` values, narrative text, and page boundaries against the PDF.

## Section A: General Disclosures

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 1 | Report index / table of contents (Section A, B, C page references) | Section A, front matter | `#/tables/0`, p. 2 | Categorical | [ ] |
| 2 | Company identity: CIN, incorporation year, registered/corporate address, contact, financial year, stock exchanges, paid-up capital | Section A, I. Details (Q1-12) | `#/tables/1`, p. 3 | Mixed | [ ] |
| 3 | Consolidated reporting boundary: parent, Indian subsidiaries, overseas subsidiaries by region | Section A, I.13 Reporting boundary | `#/tables/2`, p. 4 | Categorical | [ ] |
| 4 | Main business activity, NIC code, description, % of turnover | Section A, II.16 | `#/tables/3`, p. 5 | Mixed | [ ] |
| 5 | Products/services sold with turnover and % of turnover, consolidated vs. standalone | Section A, II.17 | `#/tables/4`, p. 5 | Mixed | [ ] |
| 6 | Number of plants and offices, India vs. outside India | Section A, III.18 | `#/tables/5`, p. 5 | Numeric | [ ] |
| 7 | Markets served: national states/UTs and international countries | Section A, III.19(a) | `#/tables/6`, p. 6 | Numeric + categorical | [ ] |
| 8 | Revenue by geography, Tata Steel Consolidated (India/Outside India/Total, 2-year) | Section A, III.19(b) | `#/tables/7`, p. 6 | Numeric | [ ] |
| 9 | Export revenue and % of exports in total revenue, Tata Steel Standalone | Section A, III.19(b) | `#/tables/8`, p. 6 | Numeric | [ ] |
| 10 | Employees and workers by gender (permanent/other than permanent), consolidated | Section A, IV.20(a) | `#/tables/9`, p. 7 | Numeric + categorical | [ ] |
| 11 | Differently abled employees and workers by gender | Section A, IV.20(b) | `#/tables/10`, p. 7 | Numeric + categorical | [ ] |
| 12 | Women participation: Board of Directors, KMP, Senior Leadership Team | Section A, IV.21 | `#/tables/11`, p. 7 | Numeric + categorical | [ ] |
| 13 | Turnover rate for permanent employees and workers, 3-year, by gender | Section A, IV.22 | `#/tables/12`, p. 8 | Numeric | [ ] |
| 14 | Continued turnover data: separation by resignation, 3-year, by gender | Section A, IV.22 (continued) | `#/tables/13`, p. 8 | Numeric | [ ] |
| 15 | CSR applicability, turnover, and net worth | Section A, VI.24 | `#/tables/14`, p. 8 | Mixed | [ ] |
| 16 | Complaints/grievances - Communities: filed and pending, 2-year | Section A, VII.25 | `#/tables/15`, p. 9 | Numeric | [ ] |
| 17 | Complaints/grievances - Investors and Shareholders: filed and pending, 2-year | Section A, VII.25 | `#/tables/16`, p. 9 | Numeric | [ ] |
| 18 | Complaints/grievances - Employees and Workers: filed and pending, 2-year | Section A, VII.25 | `#/tables/17`, p. 9 | Numeric | [ ] |
| 19 | Complaints/grievances - Customers: filed and pending, 2-year | Section A, VII.25 | `#/tables/18`, p. 10 | Numeric | [ ] |
| 20 | Complaints/grievances - Value Chain Partners: Speak-up and Vendor Grievance Redressal Committee, 2-year | Section A, VII.25 | `#/tables/19`, p. 10 | Numeric | [ ] |
| 21 | Complaints/grievances - Others: filed and pending, 2-year | Section A, VII.25 | `#/tables/20`, p. 10 | Numeric | [ ] |
| 22 | Material issues: GHG emissions/climate change, circular economy, water consumption/effluent discharge risk (A1-A3), rationale, mitigation, financial implication | Section A, VII.26 | `#/tables/21`, p. 11 | Qualitative + categorical | [ ] |
| 23 | Continued material issues: energy efficiency (A4), occupational health & safety (B1), air pollution/air quality (B2) | Section A, VII.26 (continued) | `#/tables/22`, p. 12 | Qualitative + categorical | [ ] |
| 24 | Continued material issues: biodiversity risk (B3), R&D/technology innovation (B4), supply chain sustainability risk (C1) | Section A, VII.26 (continued) | `#/tables/23`, p. 13 | Qualitative + categorical | [ ] |
| 25 | Continued material issue: employee well-being and development (C2) | Section A, VII.26 (continued) | `#/tables/24`, p. 14 | Qualitative + categorical | [ ] |
| 26 | Continued material issue: community support / CSR - building thriving communities (C3) | Section A, VII.26 (continued) | `#/tables/25`, p. 15 | Qualitative + categorical | [ ] |

## Section B: Management and Process Disclosures

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 27 | Policy coverage of NGRBC Principles P1-P9, policies 1-29 | Section B, Q1(a) | `#/tables/26`, p. 16 | Categorical | [ ] |
| 28 | Continued policy coverage of NGRBC Principles P1-P9, policies 30-39 | Section B, Q1(a) (continued) | `#/tables/27`, p. 17 | Categorical | [ ] |
| 29 | Policy Board-approval status and web-link to policies | Section B, Q1(b)-(c) | `#/tables/28`, p. 17 | Qualitative + categorical | [ ] |
| 30 | National/international codes, certifications and standards adopted, mapped to P1-P9 | Section B, Q4 | `#/tables/29`, p. 18 | Categorical | [ ] |
| 31 | Review of NGRBC policies: subject, reviewing authority, frequency | Section B, Q10 | `#/tables/30`, p. 20 | Qualitative | [ ] |

## Section C: Principle 1 - Ethics, Transparency and Accountability

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 32 | Training/awareness programme coverage: Board, KMP, employees and workers | Principle 1, Essential Indicator 1 | `#/tables/31`, p. 21 | Mixed | [ ] |
| 33 | Fines/penalties/settlements: regulator, amount, case detail, appeal status | Principle 1, Essential Indicator 2 | `#/tables/32`, p. 22 | Mixed | [ ] |
| 34 | Appeal/revision case details | Principle 1, Essential Indicator 3 | `#/tables/33`, p. 23 | Categorical | [ ] |
| 35 | Directors/KMPs/employees/workers subject to disciplinary action for bribery/corruption | Principle 1, Essential Indicator 5 | `#/tables/34`, p. 23 | Numeric + categorical | [ ] |
| 36 | Complaints on conflict of interest of Directors and KMPs | Principle 1, Essential Indicator 6 | `#/tables/35`, p. 23 | Numeric + categorical | [ ] |
| 37 | Number of days of accounts payable, standalone/consolidated | Principle 1, Essential Indicator 8 | `#/tables/36`, p. 23 | Numeric | [ ] |
| 38 | Purchase/sales concentration with trading houses, dealers, and related-party share | Principle 1, Essential Indicator 9 | `#/tables/37`, p. 24 | Numeric | [ ] |

## Section C: Principle 2 - Sustainable and Safe Products/Services

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 39 | R&D and capex spend % on environmental/social impact improvements, with detail | Principle 2, Essential Indicator 1 | `#/tables/38`, p. 25 | Mixed | [ ] |
| 40 | Life Cycle Assessment summary by product/entity: turnover share, boundary, external verification, public disclosure | Principle 2, Leadership Indicator 1 | `#/tables/39`, p. 27 | Mixed | [ ] |
| 41 | Recycled/re-used input material as % of total material | Principle 2, Leadership Indicator 3 | `#/tables/40`, p. 28 | Numeric | [ ] |
| 42 | Reclaimed products/packaging reused, recycled, safely disposed (plastics, e-waste, hazardous waste) | Principle 2, Leadership Indicator 4 | `#/tables/41`, p. 28 | Numeric + categorical | [ ] |

## Section C: Principle 3 - Employee and Worker Well-being

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 43 | Well-being measure coverage for employees: health/accident insurance, maternity, paternity, day care | Principle 3, Essential Indicator 1(a) | `#/tables/42`, p. 29 | Numeric + categorical | [ ] |
| 44 | Well-being measure coverage for workers: health/accident insurance, maternity, paternity, day care | Principle 3, Essential Indicator 1(b) | `#/tables/43`, p. 29 | Numeric + categorical | [ ] |
| 45 | Spending on well-being measures as % of revenue, standalone/consolidated | Principle 3, Essential Indicator 1(c) | `#/tables/44`, p. 30 | Numeric | [ ] |
| 46 | Retirement benefits coverage by scheme and geography (PF, gratuity, ESI, pension funds, severance) | Principle 3, Essential Indicator 2 | `#/tables/45`, p. 30 | Mixed | [ ] |
| 47 | Return-to-work and retention rates after parental leave, by gender | Principle 3, Essential Indicator 5 | `#/tables/46`, p. 32 | Numeric | [ ] |
| 48 | Union/association membership, Tata Steel Indian entities | Principle 3, Essential Indicator 7 | `#/tables/47`, p. 32 | Numeric + categorical | [ ] |
| 49 | Continued union/association membership, India + overseas entities | Principle 3, Essential Indicator 7 (continued) | `#/tables/48`, p. 32 | Numeric + categorical | [ ] |
| 50 | Training given to employees/workers on health & safety and skill upgradation | Principle 3, Essential Indicator 8 | `#/tables/49`, p. 33 | Numeric + categorical | [ ] |
| 51 | Performance and career development reviews, by gender | Principle 3, Essential Indicator 9 | `#/tables/50`, p. 33 | Numeric + categorical | [ ] |
| 52 | Safety incidents: LTIFR, recordable injuries, fatalities, high-consequence injuries, permanent disabilities | Principle 3, Essential Indicator 11 | `#/tables/51`, p. 35 | Numeric + categorical | [ ] |
| 53 | Complaints from employees/workers on working conditions and health & safety | Principle 3, Essential Indicator 13 | `#/tables/52`, p. 36 | Numeric | [ ] |
| 54 | Assessment coverage: health & safety practices, working conditions | Principle 3, Essential Indicator 14 | `#/tables/53`, p. 36 | Numeric + categorical | [ ] |
| 55 | Rehabilitation and placement after high-consequence injury/fatality | Principle 3, Leadership Indicator 3 | `#/tables/54`, p. 37 | Numeric | [ ] |
| 56 | Value-chain-partner assessment coverage: health & safety, working conditions, by entity | Principle 3, Leadership Indicator 5 | `#/tables/55`, p. 38 | Numeric + categorical | [ ] |

## Section C: Principle 4 - Stakeholder Responsiveness

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 57 | Key stakeholder groups (Investors, Customers, Vendors, Government, Employees, Community), vulnerability, channels, frequency, engagement purpose | Principle 4, Essential Indicator 2 | `#/tables/56`, p. 39 | Categorical + qualitative | [ ] |
| 58 | Continued stakeholder groups: Media, Industry Bodies/Associations, Academic Bodies | Principle 4, Essential Indicator 2 (continued) | `#/tables/57`, p. 40 | Categorical + qualitative | [ ] |

## Section C: Principle 5 - Human Rights

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 59 | Human-rights training coverage for employees and workers | Principle 5, Essential Indicator 1 | `#/tables/58`, p. 41 | Numeric + categorical | [ ] |
| 60 | Minimum-wage coverage for employees, by gender and employment type | Principle 5, Essential Indicator 2 | `#/tables/59`, p. 41 | Numeric + categorical | [ ] |
| 61 | Continued minimum-wage coverage for workers, by gender and employment type | Principle 5, Essential Indicator 2 (continued) | `#/tables/60`, p. 42 | Numeric + categorical | [ ] |
| 62 | Median remuneration/wages: Board of Directors, KMP, employees & workers, by gender | Principle 5, Essential Indicator 3(a) | `#/tables/61`, p. 42 | Numeric + categorical | [ ] |
| 63 | Individual remuneration of Board of Directors (male and female) | Principle 5, Essential Indicator 3(a), Annexure | `#/tables/62`, p. 42 | Numeric + categorical | [ ] |
| 64 | Individual remuneration of Key Managerial Personnel | Principle 5, Essential Indicator 3(a), Annexure | `#/tables/63`, p. 43 | Numeric + categorical | [ ] |
| 65 | Gross wages paid to females as % of total wages, standalone/consolidated | Principle 5, Essential Indicator 3(b) | `#/tables/64`, p. 43 | Numeric | [ ] |
| 66 | Complaints: sexual harassment, discrimination, child labour, forced labour, wages, other human rights | Principle 5, Essential Indicator 6 | `#/tables/65`, p. 43 | Numeric + categorical | [ ] |
| 67 | POSH complaints, % of female workforce, complaints upheld, standalone/consolidated | Principle 5, Essential Indicator 7 | `#/tables/66`, p. 44 | Numeric | [ ] |
| 68 | Assessment for the year: child labour, forced labour, sexual harassment, discrimination, wages, other human rights issues | Principle 5, Essential Indicator 10 | `#/tables/67`, p. 44 | Numeric + categorical | [ ] |
| 69 | Human-rights due-diligence scope: 14 business & human rights principles and 6 rightsholder categories | Principle 5, Leadership Indicator 2 | `#/tables/68`, p. 45 | Categorical | [ ] |
| 70 | Value-chain-partner assessment coverage for human-rights issues | Principle 5, Leadership Indicator 4 | `#/tables/69`, p. 46 | Numeric + categorical | [ ] |

## Section C: Principle 6 - Environment

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 71 | Total energy consumption (renewable/non-renewable, secondary/primary) and energy intensity, standalone/consolidated | Principle 6, Essential Indicator 1 | `#/tables/70`, p. 46 | Numeric | [ ] |
| 72 | Water withdrawal by source (surface, ground, third-party, seawater, other) and water intensity | Principle 6, Essential Indicator 3 | `#/tables/71`, p. 47 | Numeric | [ ] |
| 73 | Water discharge by destination (surface, ground, seawater, third-party, other) and treatment level | Principle 6, Essential Indicator 4 | `#/tables/72`, p. 47 | Numeric | [ ] |
| 74 | Air emissions other than GHG: stack NOx, SOx, particulate matter | Principle 6, Essential Indicator 6 | `#/tables/73`, p. 48 | Numeric | [ ] |
| 75 | Scope 1 and Scope 2 GHG emissions and intensity, standalone/consolidated | Principle 6, Essential Indicator 7 | `#/tables/74`, p. 48 | Numeric | [ ] |
| 76 | Waste generated, recovered (recycled/re-used), and disposed by category, standalone/consolidated | Principle 6, Essential Indicator 9 | `#/tables/75`, p. 49 | Numeric | [ ] |
| 77 | Operations/mines near wildlife sanctuaries, forests, coastal regulation zones: location, type, environmental-clearance compliance | Principle 6, Essential Indicator 11 | `#/tables/76`, p. 51 | Categorical | [ ] |
| 78 | Environmental impact assessment projects: EIA notification, date, external agency, public disclosure, web link | Principle 6, Essential Indicator 12 | `#/tables/77`, p. 52 | Mixed | [ ] |
| 79 | Water withdrawal, consumption, and discharge in areas of water stress | Principle 6, Leadership Indicator 2 | `#/tables/78`, p. 53 | Numeric | [ ] |
| 80 | Scope 3 GHG emissions and intensity, standalone/consolidated | Principle 6, Leadership Indicator 3 | `#/tables/79`, p. 53 | Numeric | [ ] |
| 81 | Resource-efficiency/innovation initiatives: description and outcome, part 1 | Principle 6, Leadership Indicator 5 | `#/tables/80`, p. 54 | Qualitative | [ ] |
| 82 | Continued resource-efficiency/innovation initiatives: description and outcome, part 2 | Principle 6, Leadership Indicator 5 (continued) | `#/tables/81`, p. 55 | Qualitative | [ ] |
| 83 | Value-chain-partner assessment coverage for environmental impact, by entity | Principle 6, Leadership Indicator 8 | `#/tables/82`, p. 56 | Numeric + categorical | [ ] |

## Section C: Principle 7 - Public Policy Advocacy

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 84 | Top trade and industry chambers/associations, reach (state/national/international) | Principle 7, Essential Indicator 1(b) | `#/tables/83`, p. 56 | Categorical | [ ] |
| 85 | Public policy positions advocated, methods, public disclosure, Board review frequency, web link | Principle 7, Leadership Indicator 1 | `#/tables/84`, p. 57 | Mixed | [ ] |

## Section C: Principle 8 - Inclusive Growth

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 86 | Rehabilitation & Resettlement project (Kalinganagar): affected families, % covered, amount paid | Principle 8, Essential Indicator 2 | `#/tables/85`, p. 58 | Numeric + categorical | [ ] |
| 87 | Input material sourced from MSMEs/small producers and directly from within India | Principle 8, Essential Indicator 4 | `#/tables/86`, p. 58 | Numeric | [ ] |
| 88 | Job creation in smaller towns: wages by location type (rural/semi-urban/urban/metropolitan) | Principle 8, Essential Indicator 5 | `#/tables/87`, p. 58 | Numeric | [ ] |
| 89 | Negative social impact identified and corrective action taken | Principle 8, Leadership Indicator 1 | `#/tables/88`, p. 58 | Categorical | [ ] |
| 90 | CSR spend in government-identified aspirational districts, by state/district | Principle 8, Leadership Indicator 2 | `#/tables/89`, p. 59 | Numeric + categorical | [ ] |
| 91 | CSR project beneficiaries by project category and % from vulnerable/marginalised groups | Principle 8, Leadership Indicator 6 | `#/tables/90`, p. 60 | Numeric + categorical | [ ] |

## Section C: Principle 9 - Consumer Responsibility

| Check | Indicator / disclosure topic | BRSR section | Docling table / PDF page | Data type | Verify |
|---:|---|---|---|---|:---:|
| 92 | Turnover % of products/services carrying information on environmental/social parameters, safe usage, recycling/disposal | Principle 9, Essential Indicator 2 | `#/tables/91`, p. 60 | Numeric | [ ] |
| 93 | Consumer complaints: data privacy, advertising, cyber security, essential services, trade practices, other | Principle 9, Essential Indicator 3 | `#/tables/92`, p. 60 | Numeric + categorical | [ ] |
| 94 | Product recalls: voluntary/forced, reason | Principle 9, Essential Indicator 4 | `#/tables/93`, p. 61 | Numeric + categorical | [ ] |
| 95 | Data breaches: instances, % involving customer PII, impact, standalone/consolidated | Principle 9, Essential Indicator 7 | `#/tables/94`, p. 61 | Numeric | [ ] |
| 96 | Websites where product/service information is accessible, by Group entity | Principle 9, Leadership Indicator 1 | `#/tables/95`, p. 61 | Categorical | [ ] |
| 97 | Customer Satisfaction Index trend, 3 calendar years | Principle 9, Leadership Indicator 4 (customer satisfaction survey) | `#/tables/96`, p. 63 | Numeric | [ ] |

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
