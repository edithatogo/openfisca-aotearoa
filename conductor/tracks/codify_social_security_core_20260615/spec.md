# Specification: Codify Social Security Act 2018 Core Rules

## Purpose

Audit and codify missing Social Security Act 2018 rules so benefit entitlement, income-test, asset-test, and payment-rate logic can be traced from legislation to OpenFisca variables and parameters.

## Requirements

- Reconcile existing `openfisca_aotearoa/variables/acts/social_security/` modules with Social Security Act 2018 structure.
- Reconcile existing `openfisca_aotearoa/parameters/social_security/` files with Act and Regulation schedules.
- Identify missing rules before implementation and record the gap map in the track plan or a supporting report.
- Add explicit legislation.govt.nz citations to new or changed variables and parameters.
- Add situation tests for representative eligibility and payment calculations.
