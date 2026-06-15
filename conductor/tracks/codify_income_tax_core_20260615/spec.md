# Specification: Codify Income Tax Act 2007 Core Rules

## Purpose

Audit and codify missing Income Tax Act 2007 rules so core individual tax, family scheme, Working for Families, and tax credit logic can be traced from legislation to OpenFisca variables and parameters.

## Requirements

- Reconcile existing `openfisca_aotearoa/variables/acts/income_tax/` modules with Income Tax Act 2007 structure.
- Reconcile existing income tax parameters with current and historical legislative schedules.
- Separate core Income Tax Act rules from Tax Administration Act compliance and filing-date rules.
- Add explicit legislation.govt.nz citations to new or changed variables and parameters.
- Add situation tests for representative tax, credit, and family scheme calculations.
