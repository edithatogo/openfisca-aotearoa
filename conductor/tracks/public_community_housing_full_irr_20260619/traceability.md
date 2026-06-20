# Traceability

| Decision surface | Source | Implementation | Status |
| --- | --- | --- | --- |
| Current Act title and citation | Public and Community Housing Management Act 1992 | Variable references and evidence artifacts use current title and latest legislation.govt.nz URL | implemented |
| Eligibility/application gate | Act s104 | `housing_restructuring__social_housing_eligible`; insufficient information handled by `housing_restructuring__income_related_rent_information_sufficient` | implemented |
| Notice/update boundary | Act s106 | Market-rent and discrepancy outputs are modelled as calculation outputs; provider notification workflow remains outside OpenFisca | implemented for amount, out-of-scope for notification workflow |
| Weekly calculation period | Act s107(1) | `housing_restructuring__income_related_rent_weekly` | implemented |
| Income up to threshold | Act s107(2)(a), regs 5-6 | `housing_restructuring__income_formula_rent_weekly`; `thresholds.yaml`; `proportions.yaml` | implemented |
| Income above threshold | Act s107(2)(b), reg 7 | `housing_restructuring__income_formula_rent_weekly` | implemented |
| Family tax credit component | Act s107(2)(c), s107(3)(b), regs 8-9 | `housing_restructuring__weekly_family_tax_credit_entitlement`; `family_tax_credit_cap.yaml` | implemented |
| Additional resident contributions | Act s107(2)(d), s107(3)(c) | `housing_restructuring__additional_resident_contributions`; 62% parameter | implemented |
| Benefit-floor higher-rent test | Act s107(3), reg 10 | `housing_restructuring__benefit_floor_rent_weekly`; `housing_restructuring__jobseeker_support_floor` input | implemented |
| Assessable income agency estimate | Act ss108-112 | `housing_restructuring__assessable_income` input with annual gross fallback; deprivation and asset-imputation decisions remain agency-input surfaces | implemented as input surface |
| Reviews and other rent | Act s116 | `housing_restructuring__pre_2026_amendment_calculation` preserves excluded calculations; discretionary review outcomes are out of scope unless represented through inputs | partially implemented, explicit input |
| Discrepancy/market rent | Act s118A and guidance | `housing_restructuring__income_related_rent_discrepancy_unresolved`; market-rent cap/input | implemented |
| Market-rent cap | Guidance and Act notification boundaries | `_cap_at_market_rent`; `housing_restructuring__weekly_market_rent` | implemented |
| Minimum rent | Work and Income guidance | `housing_restructuring__minimum_weekly_rent`; `minimum_weekly_rent.yaml` | implemented |
| 2 March 2026 transition | Act Schedule 4 Part 6; regulations Schedule Part 4 | `formula_2026_03_02`; `housing_restructuring__pre_2026_amendment_calculation`; `transition_date.yaml` | implemented |

No remaining publish-readiness gap is known for the implemented amount
calculation. Live agency notification, authenticated information collection,
review adjudication, and direct asset-deprivation determinations are out of
scope for this OpenFisca formula track and are represented as explicit inputs
where they affect the calculated amount.
