# Specification: Legislative Freshness Refresh

## Purpose

Implement the open legislative freshness work identified in
`conductor/legislative_freshness_review_20260619.md`. This track is separate
from publish-readiness evidence checks: it must prove whether recent New Zealand
legislative amendments have been incorporated into OpenFisca variables,
parameters, citations, formulas, and situation tests.

## Scope

The implementation must refresh and reconcile these model surfaces:

- Pae Ora (Healthy Futures) Act 2022, including the latest official text current
  as at 15 January 2026, section 46A, and any enacted title or naming changes
  affecting local citations or namespaces.
- Public and Community Housing Management Act 1992, including the title change
  from the older Housing Restructuring and Tenancy Matters framing and the 2025
  Social Assistance Legislation amendments applying from 2 March 2026.
- Tax Administration Act 1994, including official unincorporated-amendment
  notices and recent consequential amendments such as Deposit Takers Act 2023
  changes that affect modelled compliance variables or should be ruled
  out-of-scope with evidence.
- Accident Compensation earners' levy regulations, including 2024/25, 2025/26,
  2026/27, and 2027/28+ rate and maximum-liable-earnings instruments.

## Requirements

- Use Track 19's evidence pipeline boundaries for source refreshes. Offline or
  fixture-backed evidence is acceptable for automated tests; live tool outputs
  must be captured as local artifacts when available.
- Do not run authenticated `fyi-cli` or send OIA requests automatically. Any
  such work remains manual and out-of-band unless explicitly approved.
- Produce a per-instrument source refresh artifact recording official URLs,
  version dates, amendment notices, extraction status, and in-scope or
  out-of-scope decisions.
- Update local citations, parameters, formulas, variable names, labels, tests,
  and track evidence artifacts where recent amendments affect modelled behavior.
- Preserve backwards-compatible OpenFisca variable names unless a migration plan
  and alias/deprecation strategy is documented.
- Add or update YAML situation tests for every changed formula or parameter.
- Update the readiness report or add a legislative-currentness report that
  distinguishes evidence presence from amendment incorporation.

## Acceptance Criteria

- A source refresh manifest exists for Pae Ora, Public and Community Housing
  Management, Tax Administration, and ACC earners' levy instruments.
- Each recent amendment identified in the freshness review has an explicit
  decision: implemented, no model impact, out-of-scope, or blocked pending
  official incorporation.
- ACC earners' levy parameters include current official maximum-liable-earnings
  and rate evidence for 2024/25 through 2027/28+ where available.
- Housing income-related rent logic is either updated for the current weekly
  calculation structure or documented as intentionally partial with failing or
  skipped tests that define the remaining work.
- Tax Administration unincorporated amendments are reviewed against the local
  compliance variables and recorded with source evidence.
- Pae Ora current-title, section 46A, and naming/citation impacts are reconciled
  against the local primary-care funding module.
- Focused tests, readiness/currentness checks, and the broad CI-equivalent suite
  pass locally before archive or release.
