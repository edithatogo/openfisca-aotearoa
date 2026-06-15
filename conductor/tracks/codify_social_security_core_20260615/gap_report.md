# Gap Analysis: Social Security Act 2018 Coverage

Generated: 2026-06-15T21:00:00Z

## Legend

| Status | Meaning |
|--------|---------|
| COVERED | Variable(s) fully implement the section requirements |
| PARTIAL | Some aspects covered but gaps remain |
| MISSING | No implementation exists |
| SKELETON | Variable defined but formula not implemented |
| ADMIN | Administrative or obligations rules (low priority) |

---

## Part 1: General Provisions (s 1-14)

| Section | Description | Status | Notes |
|---------|-------------|--------|-------|
| s 3-4 | Purpose, Principles | ADMIN | Discretionary/guiding principle |
| s 6 | Definitions (Schedule 2) | PARTIAL | Dictionary variables in `interpretation/` |
| s 8 | Single/de facto relationship | COVERED | `social_security__in_a_relationship` |
| s 9-14 | Interpretation, transitional | ADMIN | Administrative/transitional |

---

## Part 2: Assistance

### Subpart 1: Introduction (s 15-19)

| Section | Description | Status | Notes |
|---------|-------------|--------|-------|
| s 16 | Residential requirement | COVERED | `social_security__residential_requirement` |
| s 17 | Rates (Schedule 4) | PARTIAL | Parts 1 & 3 done; Parts 2, 4-12 missing |
| s 18 | Limitation: >1 benefit | PARTIAL | Combined with s 19 |
| s 19 | Unlawfully resident / temp visa | COVERED | `social_security__general_limitation` |

### Subpart 2: Jobseeker Support - s 20-28

| Section | Description | Status | Notes |
|---------|-------------|--------|-------|
| s 20 | Requirements | COVERED | `jobseeker_support__entitled` |
| s 21 | Work gap | COVERED | `jobseeker_support__work_gap` |
| s 22 | Available for work | COVERED | `jobseeker_support__available_for_work` |
| s 23 | Age requirement | COVERED | `jobseeker_support__age_requirement` |
| s 24 | No/minimum income | COVERED | `jobseeker_support__minimum_income` |
| s 25 | Discretionary grant hardship | MISSING | Not coded |
| s 26 | Ineligibility | MISSING | TODO: full-time student (a), strike (b), training (c) |
| s 27-28 | Medical certificate/examination | MISSING | Not coded |

### Subpart 3: Sole Parent Support - s 29-33

| Section | Description | Status | Notes |
|---------|-------------|--------|-------|
| s 29 | Requirements | COVERED | `sole_parent_support__entitled` |
| s 30 | Sole parent requirement | COVERED | `sole_parent_support__requirement` |
| s 31 | Dependent child as applicant's | COVERED | `sole_parent_support__dependent_child_requirement` |
| s 32 | Split care | COVERED | `sole_parent_support__split_care` |
| s 33 | Expiry when youngest turns 14 | MISSING | Not coded |

### Subpart 4: Supported Living Payment - s 34-42

| Section | Description | Status | Notes |
|---------|-------------|--------|-------|
| s 34 | SLP: restricted work/blindness | COVERED | `supported_living_payment__disabled_or_blind` |
| s 35 | Restricted work capacity | COVERED | `supported_living_payment__restricted_work_capacity` |
| s 36 | Self-inflicted exclusion | COVERED | `supported_living_payment__disability_self_inflicted` |
| s 37-39 | Medical exam, apportionment, open emp. | MISSING | Not coded |
| s 40 | SLP: caring for another | COVERED | `supported_living_payment__carer` |
| s 41-42 | Certificate/examination (carer) | MISSING | Not coded |

### Subpart 5-6: Orphan's & Unsupported Child's - s 43-48

| Section | Description | Status | Notes |
|---------|-------------|--------|-------|
| s 43-45 | Orphan's Benefit | PARTIAL | `orphans_benefit.py` exists - verify s 44 |
| s 46-48 | Unsupported Child's Benefit | PARTIAL | `unsupported_child.py` exists - verify s 47 |

### Subpart 7-8: Youth Payment & Young Parent - s 49-62

| Section | Description | Status | Notes |
|---------|-------------|--------|-------|
| s 49-55 | Youth Payment | PARTIAL | `youth_payment/` exists - needs review |
| s 56-62 | Young Parent Payment | PARTIAL | `young_parent_payment/` exists - needs review |

### Subpart 9: Emergency Benefit - s 63-64

| Section | Description | Status | Notes |
|---------|-------------|--------|-------|
| s 63 | Discretionary grant hardship | PARTIAL | `emergency_benefit.py` exists |
| s 64 | Grant during epidemic | MISSING | Not coded |

### Subpart 10: Accommodation Supplement - s 65-69

| Section | Description | Status | Notes |
|---------|-------------|--------|-------|
| s 65 | Requirements | COVERED | `accommodation_supplement__entitled` |
| s 66 | Social housing exclusion | COVERED | `accommodation_supplement__social_housing_exclusion` |
| s 67 | Other funding exclusion | COVERED | `accommodation_supplement__other_funding_exclusion` |
| s 68 | Joint tenants in relationship | MISSING | Not coded |
| s 69 | Refusal, reduction, cancellation | MISSING | Not coded |

### Subpart 11: Winter Energy Payment - s 70-75

| Section | Description | Status | Notes |
|---------|-------------|--------|-------|
| s 70-75 | Winter Energy Payment | MISSING | Entire subpart not implemented |

### Subpart 12-14: Childcare, Disability, Child Disability - s 76-89

| Section | Description | Status | Notes |
|---------|-------------|--------|-------|
| s 76-77 | Childcare Assistance | PARTIAL | Parameters exist, variables need review |
| s 78-83 | Child Disability Allowance | PARTIAL | `child_disability_allowance/` exists |
| s 84-88 | Disability Allowance | PARTIAL | `disability_allowance/` exists |
| s 89 | Special Disability Allowance | MISSING | Not coded |

### Subpart 15-18: Remaining Assistance - s 90-103

| Section | Description | Status | Notes |
|---------|-------------|--------|-------|
| s 90-94 | Funeral Grants | MISSING | Entire subpart not implemented |
| s 95-98 | Hardship Assistance (TAS) | MISSING | Not coded |
| s 99-102 | Special Assistance | MISSING | Low priority |
| s 103 | Extended payment children 18+ | MISSING | Not coded |

---

## Part 3: Obligations (s 104-182)

*Obligations and sanctions are primarily administrative/enforcement rules. Low priority for Phase 1.*

---

## Part 4: Factors Affecting Benefits (s 183-230)

| Section | Description | Status | Notes |
|---------|-------------|--------|-------|
| s 186 | Insurance recovery | MISSING | |
| s 187-191 | Overseas pensions | MISSING | |
| s 195-196 | Shared care | PARTIAL | In sole_parent_support split care |
| s 197-198 | Compensation/damages | MISSING | |
| s 199-200 | Veteran's entitlement | MISSING | |
| s 202-203 | Maintenance/family protection | MISSING | |
| s 204 | Not ordinarily resident | MISSING | |
| s 205 | Refugee/protected person | COVERED | `social_security__refugee_or_protected_person` |
| s 206-207 | Hospitalisation | MISSING | |
| s 208 | Alcohol/drug treatment | MISSING | |
| s 209-216 | Warrant for arrest | MISSING | |
| s 217-218 | Custody in prison/remand | MISSING | |
| s 219-220 | Absence from NZ | MISSING | |
| s 225-229 | Voluntary unemployment | MISSING | |
| s 230 | Stand down | MISSING | |

---

## Part 5: Enforcement (s 231-295)

| Section | Description | Status | Notes |
|---------|-------------|--------|-------|
| s 231-295 | Sanctions, offences, penalties | ADMIN | Administrative/enforcement |

---

## Part 6: Administration (s 296-end)

| Section | Description | Status | Notes |
|---------|-------------|--------|-------|
| s 296+ | Applications, reviews, commencement | ADMIN | Administrative - low priority |

---

## Schedules

### Schedule 2: Dictionary Definitions

| Term | Status | Notes |
|------|--------|-------|
| Beneficiary | COVERED | `social_security__beneficiary` |
| Child | COVERED | `social_security__child` |
| Dependent child | COVERED | `social_security__dependent_child` |
| Employment | COVERED | `social_security__employment` |
| Full employment | COVERED | `social_security__full_employment` |
| Income | SKELETON | `social_security__income` - formula not implemented |
| Principal caregiver | COVERED | `social_security__principal_caregiver` |
| Parent | COVERED | `social_security__parent` |
| Remaining terms | PARTIAL | Many not yet mapped |

### Schedule 4: Rates of Benefits

| Part | Benefit | Status | Notes |
|------|---------|--------|-------|
| Part 1 | Jobseeker Support | COVERED | `schedule_4/part1.py` |
| Part 2 | Sole Parent Support | MISSING | Not yet implemented |
| Part 3 | Supported Living Payment | COVERED | `schedule_4/part3.py` |
| Part 4 | Orphan's Benefit | MISSING | Not yet implemented |
| Part 5 | Unsupported Child's Benefit | MISSING | Not yet implemented |
| Part 6 | Youth Payment | MISSING | Not yet implemented |
| Part 7 | Young Parent Payment | MISSING | Not yet implemented |
| Part 8 | Emergency Benefit | MISSING | Not yet implemented |
| Part 9 | Childcare Assistance | MISSING | Parameters exist |
| Part 10 | Disability Allowance | MISSING | Not yet implemented |
| Part 11 | Child Disability Allowance | MISSING | Not yet implemented |
| Part 12 | Funeral Grants | MISSING | Not yet implemented |

### Schedule 5: Means, Asset, and Income Limits

| Clause | Status | Notes |
|--------|--------|-------|
| Asset limits 1-4 | COVERED | `schedule_5/asset_limits_1-4.yml` |
| Income limits 5-9 | COVERED | `schedule_5/income_limits_5-9.yml` |

---

## Income Tests

| Test | Status | Notes |
|------|--------|-------|
| Income Test 1 | COVERED | Single no children - 30% to threshold, then 70% |
| Income Test 2 | COVERED | Single with children - 15% then 35% |
| Income Test 3a | COVERED | Single (certain rates) - 70% over threshold |
| Income Test 3b | COVERED | Partnered - 70% over threshold |
| Income Test 4 | COVERED | Partnered (other) - 35% over threshold |

---

## Summary of Missing Items (Priority Order)

### High Priority (Phase 1 - core benefit entitlements)

1. s 26 Jobseeker ineligibility - full-time student, strike, training (TODO)
2. Schedule 4, Part 2 - Sole Parent Support rates
3. Schedule 4, Part 4 - Orphan's Benefit rates
4. Schedule 4, Part 5 - Unsupported Child's Benefit rates
5. Schedule 4, Part 6 - Youth Payment rates
6. Schedule 4, Part 7 - Young Parent Payment rates
7. Schedule 4, Part 8 - Emergency Benefit rates
8. s 33 Sole Parent Support expiry when youngest turns 14

### Medium Priority (Phase 1 - supplementary assistance)

9. Subpart 11: Winter Energy Payment (s 70-75) - entire subpart
10. Subpart 15: Funeral Grants (s 90-94) - entire subpart
11. s 89 Special Disability Allowance
12. Subpart 16: Temporary Additional Support (s 95-98)
13. Schedule 4, Parts 9-12 - remaining rate schedules

### Low Priority (Phase 2+)

14. Part 3: Obligations - administrative/enforcement
15. Part 5: Sanctions and Offences - administrative/enforcement
16. Part 6: Administration - application/commencement/ending
17. Part 4 factors - hospitalisation, arrest warrants, overseas pensions, etc.
