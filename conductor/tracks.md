# Project Tracks

This file tracks all major tracks for the project. Each track has its own detailed plan in its respective folder.

---

## [x] Track 1: Migrate project configuration to UV-compatible pyproject metadata, consolidate linting under Ruff, and set up a passable Basedpyright baseline
*Archived: [./conductor/archive/modernize_tooling_20260615/](./conductor/archive/modernize_tooling_20260615/)*

---

## [x] Track 2: Upstream Governance Alignment and Active Fork Designation
*Archived: [./conductor/archive/upstream_governance_20260615/](./conductor/archive/upstream_governance_20260615/)*
*Description:* Document status of this repository as the definitive active fork of OpenFisca Aotearoa, updating README files to reference legacy repos (`BetterRules` / `digitalaotearoa`) as dormant upstream references.

---

## [x] Track 3: Integrate and Map Historical/Current Tax Rules from nztaxmicrosim
*Archived: [./conductor/archive/integrate_nztaxmicrosim_20260615/](./conductor/archive/integrate_nztaxmicrosim_20260615/)*
*Description:* Import and map all existing historical tax rules and brackets from `nztaxmicrosim` into OpenFisca Aotearoa parameters, and update with newer NZ tax rules.

---

## [x] Track 4: Target Legislation Audit and New Legislation Track Scaffolding
*Archived: [./conductor/archive/legislation_audit_20260615/](./conductor/archive/legislation_audit_20260615/)*
*Description:* Map and audit target NZ legislation using the `nz-legislation` CLI tool, identify gaps, and automatically generate individual feature tracks to explore and codify each target Act/Regulation.

---

## [x] Track 5: GitHub CI/CD Automation & Multi-Tier Testing
*Archived: [./conductor/archive/github_actions_20260615/](./conductor/archive/github_actions_20260615/)*
*Description:* Scaffold GitHub Actions workflows to install project dependencies with `uv`, automate Ruff linting via `ruff-action`, run the current Basedpyright baseline, enforce Complexipy complexity checks, and run Pytest coverage checks with warnings-as-errors and Hypothesis-backed property tests.

---

## [x] Track 6: Automated Documentation and Exploration Publishing via Astro on GitHub Pages
*Link: [./conductor/tracks/github_pages_20260615/](./conductor/tracks/github_pages_20260615/)*
*Description:* Deploy an automated documentation page and parameter explorer built with **Astro** to GitHub Pages, ensuring policy analysts can search laws and parameter changes visually.

---

## [x] Track 7: Release, Tagging, and Dependency Lifecycle Automation
*Link: [./conductor/tracks/release_lifecycle_20260615/](./conductor/tracks/release_lifecycle_20260615/)*
*Description:* Configure Dependabot to maintain bleeding-edge Rust tooling, and configure `hatch-vcs` for dynamic semantic tagging and auto-release builds.

---

## [x] Track 8: Decisional Simulation Analytics & Policy Diffusion
*Link: [./conductor/tracks/simulation_analytics_20260615/](./conductor/tracks/simulation_analytics_20260615/)*
*Description:* Implement simulation analytics using `voiage` (Value of Information), `mars` regression, and `innovate` (policy diffusion and uptake modelling) over `open_social_data`.

---

## [x] Track 9: Codify Pae Ora (Healthy Futures) Act 2022 (Primary Care Funding Integration)
*Link: [./conductor/tracks/codify_pae_ora_20260615/](./conductor/tracks/codify_pae_ora_20260615/)*
*Description:* Explores and codifies primary care funding structures under the Pae Ora (Healthy Futures) Act 2022, integrating parameters and logic derived from `gtpcnz`.

---

## [x] Track 10: Codify Housing Restructuring and Tenancy Matters Act 1992
*Link: [./conductor/tracks/codify_housing_restructuring_20260615/](./conductor/tracks/codify_housing_restructuring_20260615/)*
*Description:* Codify social housing income-related rent calculators governed under the Housing Restructuring and Tenancy Matters Act 1992.

---

## [x] Track 11: Codify Tax Administration Act 1994 & WFF amendments
*Link: [./conductor/tracks/codify_tax_admin_20260615/](./conductor/tracks/codify_tax_admin_20260615/)*
*Description:* Codify WFF adjustments and administrative compliance timelines under the Tax Administration Act 1994.

---

## [x] Track 12: Codify ACC Earners' Levy Regulations
*Link: [./conductor/tracks/codify_acc_levy_regs_20260615/](./conductor/tracks/codify_acc_levy_regs_20260615/)*
*Description:* Codify Acc Earner's Levy rate changes and maximum caps under the Accident Compensation (Earners' Levy) Regulations.

---

## [ ] Track 13: Codify Social Security Act 2018 Core Entitlements and Income Tests
*Link: [./conductor/tracks/codify_social_security_core_20260615/](./conductor/tracks/codify_social_security_core_20260615/)*
*Description:* Audit and codify missing Social Security Act 2018 entitlement, income-test, and assistance rules, reconciling existing benefit modules with current legislative structure.

---

## [~] Track 14: Codify Income Tax Act 2007 Core Tax and Family Scheme Rules
*Link: [./conductor/tracks/codify_income_tax_core_20260615/](./conductor/tracks/codify_income_tax_core_20260615/)*
*Description:* Audit and codify missing Income Tax Act 2007 core tax, family scheme, and Working for Families rules, separating core Act coverage from Tax Administration Act compliance work.
