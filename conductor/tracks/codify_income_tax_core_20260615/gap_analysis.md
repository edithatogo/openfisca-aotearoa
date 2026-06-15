# Gap Analysis: Income Tax Act 2007 → OpenFisca Aotearoa

## Purpose

Map existing OpenFisca variables and parameters against the Income Tax Act 2007 (ITA07) structure, identify gaps in coverage, and prioritise Phase 2 implementation work. This report separates core ITA07 rules from Tax Administration Act 1994 rules (Track 11) and Social Security Act 2018 rules.

---

## 1. Existing Code → ITA07 Structure Mapping

### Part A — Interpretation / Part YA — Definitions / Part YB — Family scheme / Part YC — Working for Families

| Subpart / Topic | ITA07 Reference | Existing Code | Status |
|---|---|---|---|
| **Part A / YA — Interpretation & Definitions** | YA 1 | None | ❌ Missing |
| **Part YB — Family scheme definitions** | YB 1–4 | Partial: `income_tax__dependent_child`, `income_tax__principal_caregiver` in `interpretation.py` | ⚠️ Partial |
| **Part YC — Working for Families definitions** | YC 1 | None | ❌ Missing |
| **Schedule 1 — Tax rates** | Sch 1, Parts A–C | Individual progressive rates in `individual_income_tax_rate.yaml` | ⚠️ Partial |

### Part B — Core Provisions

| Subpart / Topic | ITA07 Reference | Existing Code | Status |
|---|---|---|---|
| **Subpart BC — Core provisions** | BC 1–9 | `income_tax__annual_gross_income`, `income_tax__annual_total_deduction`, `income_tax__net_income`, `income_tax__net_loss`, `income_tax__available_tax_loss`, `income_tax__taxable_income` in `individual.py` | ⚠️ Partial (definitions present, constituent income/deduction types absent) |

### Part C — Income (Specific Types)

| Subpart / Topic | ITA07 Reference | Existing Code | Status |
|---|---|---|---|
| **CA — Income** | CA 1–2 | None | ❌ Missing |
| **CB — Business income** | CB 1–32 | None | ❌ Missing |
| **CC — Government grants** | CC 1–12 | None | ❌ Missing |
| **CE — Employment income** | CE 1–13 | None (but `salary`/`wages` may be input variables) | ❌ Missing |
| **CF — Fringe benefits** | CF 1–4 | None | ❌ Missing |
| **CG — Trading stock** | CG 1–13 | None | ❌ Missing |
| **CH — Disposal of land** | CH 1–4 | None | ❌ Missing |
| **CQ — Foreign-sourced income** | CQ 1–9 | None | ❌ Missing |
| **CT — PIE income** | CT 1–11 | None | ❌ Missing |
| **CU — Retirement scheme income** | CU 1–2 | None | ❌ Missing |
| **CV — Other income** | CV 1–18 | None | ❌ Missing |
| **CZ — Transitional** | CZ 1–40 | None | ❌ Missing |

### Part D — Deductions (Specific Types)

| Subpart / Topic | ITA07 Reference | Existing Code | Status |
|---|---|---|---|
| **DA — General rules** | DA 1–5 | None | ❌ Missing |
| **DB — Business/employment/investment** | DB 1–70 | None | ❌ Missing |
| **DC — Residential rental** | DC 1–16 | None | ❌ Missing |
| **DD — Motor vehicle** | DD 1–6 | None | ❌ Missing |
| **DE — Entertainment** | DE 1–12 | None | ❌ Missing |
| **DF — Low-value assets** | DF 1–8 | None | ❌ Missing |
| **DG — Research & development** | DG 1–17 | None | ❌ Missing |
| **DH — Charitable donations** | DH 1–6 | None | ❌ Missing |
| **DJ — Other deductions** | DJ 1–28 | None | ❌ Missing |
| **DZ — Transitional** | DZ 1–12 | None | ❌ Missing |

### Part E (Timing), Part F (Apportionment), Part G (Avoidance), Part H (Exemptions)

**All subparts EA–HZ:** No existing code. ❌ Missing entirely.

### Part I — Tax Credits

| Subpart / Topic | ITA07 Reference | Existing Code | Status |
|---|---|---|---|
| **IA — General rules** | IA 1–8 | `income_tax__individual_income_tax` (rate scale calc) | ⚠️ Partial |
| **IC — Credits for certain payments** | IC 1–10 | None | ❌ Missing |
| **ID — Refundable credits** | ID 1–7 | None | ❌ Missing |
| **IE — Independent earner tax credit** | IE 1–2 | None | ❌ Missing |
| **IF — Payroll giving** | IF 1–3 | None | ❌ Missing |
| **IG — R&D tax credits** | IG 1–13 | None | ❌ Missing |
| **IK — Film production** | IK 1–3 | None | ❌ Missing |
| **IL — International tax-sharing** | IL 1–10 | None | ❌ Missing |
| **IP — Related-party** | IP 1–3 | None | ❌ Missing |
| **IQ — Māori authority** | IQ 1–10 | None | ❌ Missing |
| **IR — Supplementary** | IR 1–17 | None | ❌ Missing |
| **IT — Other credits (donations)** | IT 1–5 | None | ❌ Missing |
| **IW — Withholding tax credits** | IW 1–7 | None | ❌ Missing |
| **IZ — Transitional** | IZ 1–29 | None | ❌ Missing |

### Part YB — Family Scheme (Subparts MA–MJ, MZ)

| Subpart / Topic | ITA07 Reference | Existing Code | Status |
|---|---|---|---|
| **MA — Family scheme income** | MA 1–10 | `family_scheme__assessable_income` (commented-out formula, no logic), `family_scheme__assessable_income_for_month` | ⚠️ Stub only |
| **MB — Base eligibility** | MB 1–14 | `family_scheme__base_qualifies`, `family_scheme__caregiver_age_qualifies`, `family_scheme__qualifies_as_principal_carer` in `family_scheme.py` | ✅ Partial |
| **MC — Dependent children** | MC 1–4 | `family_scheme__dependent_children`, `income_tax__dependent_child` | ⚠️ Partial |
| **MD — Family tax credit** | MD 1–18 | `family_tax_credit`, `family_tax_credit__eligible`, `family_tax_credit__base`, `family_tax_credit__eldest`, `family_tax_credit__not_eldest`, `family_tax_credit__dependent_child`, `family_scheme__qualifies_for_family_tax_credit`, `family_scheme__family_tax_credit_income_under_threshold`, `family_scheme__family_tax_credit_entitlement` | ⚠️ Partial (abatement missing, entitlement stubbed) |
| **ME — In-work tax credit** | ME 1–10 | `family_scheme__qualifies_for_in_work_tax_credit`, `family_scheme__in_work_tax_credit_income_under_threshold` (proxy), `family_scheme__in_work_tax_credit_entitlement` (stub) | ⚠️ Stub only |
| **MF — Minimum family tax credit** | MF 1–10 | `family_scheme__qualifies_for_minimum_family_tax_credit` | ⚠️ Partial (entitlement missing) |
| **MG — Parental tax credit** | MG 1–8 | `family_scheme__qualifies_for_parental_tax_credit`, `family_scheme__parental_tax_credit_entitlement` (stub) | ⚠️ Stub only |
| **MJ — Best start tax credit** | MJ 1–14 | `best_start__eligibility`, `best_start__family_has_children_eligible`, `best_start__year_of_child`, `best_start__tax_credit_per_child`, `best_start__entitlement` | ✅ Most complete — abatement may need review |
| **MZ — Transitional** | MZ 1–9 | None | ❌ Missing |

### Part YC — Working for Families

| Subpart / Topic | ITA07 Reference | Existing Code | Status |
|---|---|---|---|
| **Part YC — Entitlement aggregation** | YC 1–5 | `family_scheme__qualifies_for_working_for_families`, `family_scheme__working_for_families_entitlement` (stub) | ⚠️ Stub only |

### Part L — Administration (Boundary: Tax Administration Act 1994)

| Subpart / Topic | ITA07 Reference | Existing Code | Status |
|---|---|---|---|
| **Part L** — ITA07 residual admin | LA–LZ | None in ITA07 | ✅ Belongs in TAA94 |
| _Tax Administration Act 1994_ | TAA94 | `tax_admin/compliance.py` with `tax_admin__automatic_tax_assessment`, `tax_admin__filing_deadline_months_after_year_end` | ✅ Track 11 (concluded) |

### Part M (Special), Part R (General), Part Z (Transitional)

All subparts MA–RZ, ZA–ZZ: No existing code. ❌ Missing entirely.

---

## 2. Missing Core Individual Tax Rules

### 2.1 Part C — Specific Income Types

| # | Missing Rule | ITA07 Reference | Priority |
|---|---|---|---|
| 1 | **Employment income** (salary, wages, bonuses) | CE 1–5 | High |
| 2 | **Business income** | CB 1–32 | High |
| 3 | **Investment income** (interest, dividends) | CD 1–14 | High |
| 4 | **Foreign-sourced income** | CQ 1–9 | Medium |
| 5 | **Fringe benefit values** | CF 1–4 | Medium |
| 6 | **PIE income** | CT 1–11 | Medium |

### 2.2 Part D — Specific Deduction Types

| # | Missing Rule | ITA07 Reference | Priority |
|---|---|---|---|
| 1 | **Employment-related deductions** | DB 1–10 | High |
| 2 | **Business deductions** | DB 11–50 | High |
| 3 | **Residential rental property deductions** | DC 1–16 | Medium |
| 4 | **Charitable donations** | DH 1–6 | Medium |
| 5 | **Motor vehicle expenditure** | DD 1–6 | Low |
| 6 | **Low-value asset write-offs** | DF 1–8 | Low |

### 2.3 Part I — Tax Credits

| # | Missing Rule | ITA07 Reference | Priority |
|---|---|---|---|
| 1 | **Independent earner tax credit (IETC)** | IE 1–2 | High |
| 2 | **PAYE / withholding tax credits** | IW 1–7 | High |
| 3 | **Charitable donation tax credits** | IT 1 / DH 1–6 | Medium |
| 4 | **R&D tax credits** | IG 1–13 | Low |
| 5 | **Māori authority credits** | IQ 1–10 | Low |
| 6 | **Payroll giving credits** | IF 1–3 | Low |

### 2.4 Schedule 1 — Tax Rate Tables

| # | Missing Aspect | Reference | Priority |
|---|---|---|---|
| 1 | **Trust tax rate** | Sch 1, Part A | High |
| 2 | **PIE prescribed investor rates** | Sch 1, Part A (table 4) | Medium |
| 3 | **ESCT rates** | Sch 1, Part A (table 3) | Low |
| 4 | **RWT rates** | Sch 1, Part A (table 2) | Low |
| 5 | **NRWT rates** | Sch 1, Part A | Low |
| 6 | **Bracket structure review** | Sch 1, Part A (table 1) | Medium |

---

## 3. Missing Family Scheme / Working for Families Rules

### 3.1 Family Scheme Income (Subpart MA) — CRITICAL

| # | Missing Rule | ITA07 Reference | Detail |
|---|---|---|---|
| 1 | **Family scheme income definition** | MA 1–10 | `family_scheme__assessable_income` has no formula |
| 2 | **Income add-backs** | MA 4–6 | Exempt income, NZ super, veterans pension, ACC |
| 3 | **Income deductions** | MA 7–10 | Child support payments |

### 3.2 Family Tax Credit (Subpart MD) — CRITICAL

| # | Missing Rule | ITA07 Reference | Detail |
|---|---|---|---|
| 1 | **FTC abatement formula** | MD 8–14 | `family_scheme__family_tax_credit_entitlement` stubbed |
| 2 | **Income threshold check** | MD 8 | `income_under_threshold` is manual boolean, no logic |
| 3 | **Age-banded rate deduplication** | MD 3 | Duplicated under `family_scheme/` and `working_for_families/` |

### 3.3 In-Work Tax Credit (Subpart ME)

| # | Missing Rule | ITA07 Reference | Detail |
|---|---|---|---|
| 1 | **IWTC calculation** | ME 3–5 | `entitlement` returns `persons` — completely stubbed |
| 2 | **IWTC abatement** | ME 6–8 | No abatement logic |
| 3 | **Full-time earner param source** | ME 1 | References `social_security` instead of ITA07 |

### 3.4-3.6 Remaining Credits

| Credit | Subpart | Status |
|---|---|---|
| Minimum family tax credit | MF | Only qualification exists; no entitlement formula |
| Parental tax credit | MG | Only qualification exists; no entitlement or parameters |
| Best start tax credit | MJ | Most complete; abatement may need review |
| Working for Families aggregation | YC 1–5 | Stub with hard-coded `5 * -1` abatement |
| Child tax credit | MC 5–10 / MD 2 | Stub — returns `persons` |

---

## 4. Act Boundary Map: ITA07 vs. TAA94 vs. SSA18

| Legislation | Track | Coverage |
|---|---|---|
| **ITA07 — Parts B, C, D, E** | This track | ❌ Phase 2 |
| **ITA07 — Schedule 1** | This track | ⚠️ Partial |
| **ITA07 — Part I (tax credits)** | This track | ❌ Phase 2 |
| **ITA07 — Part YB (family scheme)** | This track | ⚠️ Partial |
| **ITA07 — Part YC (WFF)** | This track | ❌ Phase 2 |
| **TAA94 — Compliance (Track 11)** | `codify_tax_admin_20260615` | ✅ Concluded |
| **SSA18 — Income-tested benefits** | `codify_social_security_core_20260615` | ✅ Implemented |

---

## 5. Parameter Issues

| Issue | Location | Action |
|---|---|---|
| **Duplicate FTC rates** | `family_scheme/` and `working_for_families/` | Deduplicate |
| **Full-time earner uses SSA params** | `family_scheme.py:57-58` | Fix reference |
| **Placeholder dates** | Multiple param files | Research effective dates |
| **Brackets 2&3 identical 2000-2009** | `individual_income_tax_rate.yaml` | Verify structure |
| **Best Start single date** | `best_start/*.yaml` | Verify rate changes |

---

## 6. Priority Gaps for Phase 2

### P0 — Critical (Blocks all WFF calculation)
| # | Gap | Effort |
|---|---|---|
| 1 | `family_scheme__assessable_income` — implement MA 1–10 formula | Medium |
| 2 | `family_scheme__family_tax_credit_entitlement` — wire abatement | Medium |
| 3 | `family_scheme__in_work_tax_credit_entitlement` — implement calc | Medium |
| 4 | `family_scheme__working_for_families_entitlement` — aggregate + abate | Medium |
| 5 | `family_scheme__family_tax_credit_income_under_threshold` — replace proxy | Small |

### P1 — High (Individual tax completeness)
| # | Gap | Effort |
|---|---|---|
| 6 | Independent earner tax credit (IE 1–2) | Small |
| 7 | PAYE/withholding credits (IW 1–7) | Medium |
| 8 | Donation tax credit (IT 1 / DH 1–6) | Small |
| 9 | Trust tax rate (Schedule 1, Part A) | Small |
| 10 | PIE prescribed investor rates | Small |
| 11 | Employment income distinction (CE 1) | Small |

### P2 — Medium (Family scheme completeness)
| # | Gap | Effort |
|---|---|---|
| 12 | Minimum family tax credit (MF 1–10) — entitlement | Small |
| 13 | Parental tax credit (MG 1–8) — entitlement + params | Small |
| 14 | Child tax credit (MD 2 / MC 5–10) — historical | Small |
| 15 | Dependent child definition — financial independence tests | Medium |
| 16 | Child support deduction (MA 7–10) | Small |
| 17 | Parameter deduplication | Small |

### P3 — Low (Simulation edge cases)
| # | Gap |
|---|---|
| 18 | Detailed residence rules (183-day, permanent place of abode) |
| 19 | Transitional provisions (Part Z) |
| 20 | Tax avoidance provisions (Part G) |
| 21 | Fringe benefit tax (CF 1–4) |
| 22 | Full Part C income subpart coverage |
| 23 | Full Part D deduction subpart coverage |

---

## Appendix A: Variable Name Cleanup Opportunities

| Current Name | Issue | Suggestion |
|---|---|---|
| `income_tax__residence` | Ambiguous | `income_tax__resident_in_new_zealand` |
| `family_scheme__assessable_income` | Not ITA07 term | `family_scheme__income` (matching MA 1) |
| `family_scheme__full_time_earner` | Returns int, wrong param ref | `family_scheme__full_time_earner_hours` |
| `family_tax_credit__dependent_child` | Confusing vs `income_tax__dependent_child` | Clarify docs re 1/3 care test |

## Appendix B: Test Coverage Gaps

| Area | Existing | Needed |
|---|---|---|
| Individual tax rate calc | ✅ Basic | More bracket edge cases |
| FTC eligibility | ✅ Basic | Abatement scenarios |
| FTC base (eldest/not-eldest) | ✅ | None |
| In-work TC eligibility | ✅ Basic | Abatement + entitlement tests |
| Minimum FTC eligibility | ✅ Basic | ❌ No entitlement tests |
| Parental TC | ❌ No tests | ❌ Needs full suite |
| Best Start | ✅ Complex | None |
| Family scheme income | ❌ No tests | ❌ Needs full suite |
| WFF aggregation | ❌ No tests | ❌ Needs full suite |
| Independent earner TC | ❌ No tests | ❌ Needs full suite |
| Donation tax credit | ❌ No tests | ❌ Needs suite |
| PAYE credits | ❌ No tests | ❌ Needs suite |
| Dependent child definition | ✅ Age check | ❌ Needs financial independence tests |

## Appendix C: Parameter Files Inventory

### Present
| Path | Status |
|---|---|
| `taxes/income_tax/individual_income_tax_rate.yaml` | ✅ 8 brackets, historical rates |
| `taxes/income_tax/family_tax_credit/prescribed_amount.yaml` | ✅ MD 3(4)(a) & (b) |
| `entitlements/income_tax/family_scheme/best_start/*.yaml` | ✅ 3 files |
| `entitlements/income_tax/family_scheme/family_tax_credit/*.yaml` | ✅ 4 files |
| `entitlements/income_tax/family_scheme/principal_caregiver_*.yaml` | ✅ 2 files |
| `entitlements/income_tax/family_scheme/dependent_children_minimum.yaml` | ✅ value=1 |
| `entitlements/income_tax/working_for_families/*.yaml` | ✅ 2 files (duplicates) |

### Missing
| Path | Priority |
|---|---|
| `taxes/income_tax/independent_earner_tax_credit/` | High |
| `taxes/income_tax/trustee_income_rate.yaml` | High |
| `taxes/income_tax/prescribed_investor_rate.yaml` | Medium |
| `taxes/income_tax/esct_rate.yaml` | Low |
| `taxes/income_tax/rwt_rate.yaml` | Low |
| `entitlements/income_tax/family_scheme/minimum_family_tax_credit/` | Medium |
| `entitlements/income_tax/family_scheme/parental_tax_credit/` | Medium |

---

## Appendix D: Recommended File Structure for Phase 2

```
variables/acts/income_tax/
├── __init__.py
├── individual.py               # Existing — residence, net income, taxable income, individual tax
├── interpretation.py           # Existing — dependent_child, principal_caregiver
├── part_c_income.py            # NEW — employment, business, investment income
├── part_d_deductions.py        # NEW — employment costs, donations, rental deductions
├── part_i_tax_credits.py       # NEW — IETC, donation credits, PAYE credits
├── schedule_1_rates.py         # NEW — trust, PIE, ESCT, RWT rates
├── family_scheme/
│   ├── __init__.py
│   ├── family_scheme.py        # Existing — UPDATE: wire assessable_income formula
│   ├── family_tax_credit.py    # Existing — UPDATE: wire abatement
│   ├── in_work_tax_credit.py   # Existing — UPDATE: wire entitlement + abatement
│   ├── minimum_family_tax_credit.py  # Existing — UPDATE: wire entitlement
│   ├── parental_tax_credit.py  # Existing — UPDATE: wire entitlement
│   ├── child_tax_credit.py     # Existing — UPDATE: wire entitlement
│   ├── best_start.py           # Existing — most complete
│   └── working_for_families.py # Existing — UPDATE: wire aggregation + abatement
```
