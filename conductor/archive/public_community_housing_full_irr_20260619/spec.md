# Specification: Public and Community Housing Full Income-Related Rent Coverage

## Purpose

Implement the remaining full income-related rent coverage for public and community housing under the current Public and Community Housing Management Act 1992 framework. Track 22 closed the freshness and currentness gap by reconciling recent amendments and documenting partial coverage; this track turns that documented follow-up into a scoped implementation lane.

## Scope

The implementation must cover the current weekly income-related rent structure and related decision points that were intentionally left as follow-up scope:

- Current Act title and citation framing for the Public and Community Housing Management Act 1992.
- Sections 104, 106, and 107 rent-calculation concepts, including assessment persons, weekly income, and higher-rent tests.
- Market-rent caps and notification boundaries where modelled outputs must not exceed the applicable market rent.
- Additional resident and household composition rules where they affect the rent payable by the tenant or household.
- 2 March 2026 Social Assistance Legislation amendment effects and transitional provisions that alter current or future calculation behavior.
- Prescribed proportions, thresholds, and supporting parameters from current regulations or official guidance.

## Requirements

- Preserve backwards-compatible OpenFisca variable names where possible; add aliases or deprecation notes if public variables need to be renamed.
- Use Track 19 evidence-pipeline conventions for source manifests, citations, formulas, and traceability artifacts.
- Keep unsupported legal surfaces explicit with not_implemented evidence rows or skipped situation tests that name the missing source dependency.
- Add YAML situation tests for every new formula branch and parameter period.
- Maintain the readiness/currentness distinction: evidence presence alone does not prove full current-law coverage.
- Do not perform live authenticated information requests or external submissions as part of this implementation.

## Acceptance Criteria

- The housing module exposes a full current-law income-related rent calculation with assessment-person, household, income, prescribed-proportion, higher-rent, and market-rent-cap branches covered by tests.
- Parameters include effective-dated values for all implemented prescribed proportions, caps, thresholds, and transition dates, with official citations.
- Evidence artifacts include traceability, citations, parameters, formulas, and situation-test coverage for each implemented housing decision.
- The readiness gate reports the housing surface as publish-ready or reports only clearly documented out-of-scope items.
- Focused housing tests, readiness/currentness checks, and the broad CI-equivalent pytest command pass before this track is archived.
