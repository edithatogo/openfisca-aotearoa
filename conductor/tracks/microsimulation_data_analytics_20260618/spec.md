# Specification: Microsimulation Data and Analytics Integrations

## Purpose

Turn the roadmap's population simulation and analytics goals into auditable
interfaces for `open_social_data`, `voiage`, `mars`, and `innovate`.

## Requirements

- Define a stable input schema for population cohorts and household/person
  records imported from `open_social_data`.
- Provide a bounded batch simulation runner that maps input records to
  OpenFisca entities and variables.
- Export reproducible JSON and CSV outputs suitable for downstream analytics.
- Add adapter boundaries for value-of-information, spline regression, and
  policy diffusion workflows without hiding missing external dependencies.
- Add representative fixture datasets and tests that run offline.
- Document which integrations are local, optional, or blocked by missing
  external packages.

## Non-Goals

- Vendoring large datasets into this repository.
- Reimplementing `voiage`, `mars`, or `innovate`.
- Claiming policy conclusions from synthetic test fixtures.
