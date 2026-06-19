# Legislative Freshness Review 2026-06-19

This is a separate freshness review from the Track 21 readiness gate. The
readiness gate proves that required evidence artifacts exist for publish review;
it does not prove that every recent New Zealand legislative amendment has been
incorporated into model code, parameters, citations, and tests.

## Method

- Scope: recent official-source freshness check for the currently modelled Track
  9-14 legislation surfaces and the Track 19 evidence pipeline boundary.
- Sources: read-only checks against legislation.govt.nz pages surfaced by the
  Track 19 citation/evidence workflow.
- Boundary: no authenticated `fyi-cli` work, no OIA requests, and no automatic
  legal conclusion beyond identifying model-refresh risks.

## Local Surfaces Reviewed

- `openfisca_aotearoa/variables/acts/pae_ora/health_services.py`
- `openfisca_aotearoa/parameters/entitlements/health/pae_ora/primary_care_copayment_amount.yaml`
- `openfisca_aotearoa/variables/acts/housing_restructuring/social_housing.py`
- `openfisca_aotearoa/variables/acts/tax_admin/compliance.py`
- `openfisca_aotearoa/variables/acts/acc/earners_levy.py`
- `openfisca_aotearoa/parameters/acc/earners_levy.yaml`
- `conductor/tracks/codify_pae_ora_20260615/`
- `conductor/tracks/codify_housing_restructuring_20260615/`
- `conductor/tracks/codify_tax_admin_20260615/`
- `conductor/tracks/codify_acc_levy_regs_20260615/`

## Findings

### Pae Ora

Official source:
<https://www.legislation.govt.nz/act/public/2022/0030/latest/whole.html>

The latest official Pae Ora page is current as at 15 January 2026. It includes
section 46A, inserted by the Pae Ora (Healthy Futures) (Improving Mental Health
Outcomes) Amendment Act 2024, requiring the Minister to prepare and determine a
Mental Health and Wellbeing Strategy.

Freshness risk: the local model remains a narrow primary-care copayment scaffold
under the `pae_ora` namespace and does not record a review of section 46A or
other 2024-2026 Pae Ora changes. Recent parliamentary material also indicates a
Healthy Futures (Pae Ora) naming change is in flight, so title/namespace/citation
freshness should be checked before claiming current coverage.

### Public and Community Housing Management

Official source:
<https://www.legislation.govt.nz/act/public/1992/0076/latest/whole.html>

The official current Act title is Public and Community Housing Management Act
1992, latest version as at 2 March 2026. The official text records amendments to
sections 106 and 107, and transitional provisions applying amendments to weeks
starting on or after 2 March 2026, from the Social Assistance Legislation
(Accommodation Supplement and Income-related Rent) Amendment Act 2025.

Freshness risk: the local model and track names still use the older Housing
Restructuring and Tenancy Matters framing. The local formula is a simplified
monthly 25 percent gross-income calculation and does not yet demonstrate
coverage of the current weekly calculation structure, higher-rent tests, market
rent caps, or transitional rules from the 2025 Amendment Act.

### Tax Administration

Official source:
<https://www.legislation.govt.nz/act/public/1994/166/en/latest/>

The official latest Tax Administration Act page reports that some amendments
have not yet been incorporated. The Deposit Takers Act 2023 page includes Tax
Administration Act amendments, including bank account and licensed-bank
definition changes.

Freshness risk: the local Track 11 model only covers automatic assessment and a
manual filing deadline scaffold. It does not include evidence that unincorporated
amendments, Deposit Takers Act 2023 consequential changes, or recent annual tax
amendments were reviewed and ruled out as out-of-scope.

### ACC Earners' Levy

Official sources:

- <https://www.legislation.govt.nz/regulation/public/2022/0030/11.0/whole.html>
- <https://www.legislation.govt.nz/regulation/public/2025/0018/latest/LMS1019211.html>

The 2022 earners' levy regulations include maximum liable earnings for 2022/23,
2023/24, and 2024/25 and later. The 2025 earners' levy regulations set maximum
liable earnings for 2025/26, 2026/27, and 2027/28 and later.

Freshness risk: `openfisca_aotearoa/parameters/acc/earners_levy.yaml` currently
contains rate and maximum-threshold entries only through 2023-04-01, and its
reference points at 2023 regulations. It is missing explicit 2024/25, 2025/26,
2026/27, and 2027/28+ maximum-threshold evidence and likely needs rate/citation
reconciliation against the current instruments.

## Conclusion

Do not treat the roadmap work as proving that all recent New Zealand
legislative amendments have been incorporated. The readiness gate is satisfied
for evidence presence, but legislative freshness remains open for at least Pae
Ora, Public and Community Housing Management, Tax Administration, and ACC
earners' levy surfaces.

## Recommended Follow-up

Create a dedicated Conductor freshness implementation track using Track 19's
pipeline. Acceptance criteria should require:

- a source refresh transcript or manifest for each affected Act or regulation;
- explicit in-scope/out-of-scope determinations for each recent amendment;
- updated citations, parameters, formulas, and situation tests where amendments
  affect modelled behavior;
- an updated readiness report that distinguishes evidence presence from
  legislative-currentness.
