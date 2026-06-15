# Target Legislation Audit Report

## Scope

Track 4 reviewed the Conductor roadmap, current `openfisca_aotearoa` structure, and track registry for legislation areas that need separate codification work.

## Command Availability

- `nz-legislation`: not available in the current local shell during review-fix verification.
- Follow-up: rerun the fetch and text-change checks with `nz-legislation` before each codification track begins implementation.

## Repository Inventory

- Social Security Act 2018: existing variables and parameters are present under `openfisca_aotearoa/variables/acts/social_security/` and `openfisca_aotearoa/parameters/social_security/`, but core Act coverage needs a dedicated gap map and follow-up track.
- Income Tax Act 2007: existing variables and parameters are present under `openfisca_aotearoa/variables/acts/income_tax/` and income-tax parameter folders, but core Act coverage needs a dedicated gap map separate from Tax Administration Act compliance work.
- Pae Ora (Healthy Futures) Act 2022: generated as `codify_pae_ora_20260615`.
- Housing Restructuring and Tenancy Matters Act 1992: generated as `codify_housing_restructuring_20260615`.
- Tax Administration Act 1994: generated as `codify_tax_admin_20260615`.
- Accident Compensation (Earners' Levy) Regulations: generated as `codify_acc_levy_regs_20260615`.

## Gap-to-Track Mapping

| Legislation area | Track | Status |
| --- | --- | --- |
| Social Security Act 2018 core entitlements and income tests | `codify_social_security_core_20260615` | pending |
| Income Tax Act 2007 core tax and family scheme rules | `codify_income_tax_core_20260615` | pending |
| Pae Ora (Healthy Futures) Act 2022 | `codify_pae_ora_20260615` | pending |
| Housing Restructuring and Tenancy Matters Act 1992 | `codify_housing_restructuring_20260615` | generated |
| Tax Administration Act 1994 | `codify_tax_admin_20260615` | generated |
| Accident Compensation (Earners' Levy) Regulations | `codify_acc_levy_regs_20260615` | generated |

## Residual Risk

This report records the Conductor audit result and scaffolded work queue. It does not replace a live `nz-legislation` text-change transcript; each implementation track should refresh its cited legislation text before coding rules.
