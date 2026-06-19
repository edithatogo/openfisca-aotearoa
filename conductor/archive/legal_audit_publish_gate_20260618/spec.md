# Specification: Legal Audit and Publish Readiness Gates

## Purpose

Close the roadmap gap between implementation and release by defining auditable
legal-review and publish-readiness gates for each completed legislation track.

## Requirements

- Define a checklist for legislation traceability, citations, parameters,
  formulas, situation tests, and manual verification.
- Define release criteria for when a Conductor track can be archived or marked
  publish-ready.
- Add a machine-readable readiness manifest that can summarize track status.
- Add a human-readable report for policy/legal reviewers.
- Include unresolved-risk sections rather than overstating completion.
- Add validation tests for manifest schema and report generation.

## Non-Goals

- Providing legal advice.
- Requiring external legal sign-off to run local tests.
- Publishing packages or docs automatically before readiness gates pass.
