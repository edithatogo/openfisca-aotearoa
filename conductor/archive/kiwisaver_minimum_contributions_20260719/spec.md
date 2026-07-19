# Specification: KiwiSaver Minimum Contributions

## Overview

Record the completed controlled-fork implementation of minimum employee and
employer KiwiSaver contributions, including dated rates and native scenarios.
This retrospective track binds the implementation to its issue, pull request,
hosted validation, and RaC programme provenance.

## Requirements

1. Employee and employer minimum contribution rates are represented as dated
   OpenFisca parameters.
2. Annual contribution variables select the rate applicable from 1 April.
3. Negative contribution bases are clamped to zero.
4. Native scenarios cover 2025, 2026, 2028, and negative earnings.
5. The implementation remains ordinary controlled-fork adoption and is not
   represented as independently controlled validation.

## Acceptance Criteria

- Issue #1 is closed by merged PR #2.
- PR #2 is merged as `0ee8ac98e5dae08bd061edd0a9bfce564177ceaf`.
- Hosted quality, documentation, package build, lint, YAML, API, and version
  checks pass.
- The issue is included in GitHub Project 19 and links to this track.

## Non-functional Constraints

- Preserve decimal/rate semantics used by OpenFisca Aotearoa.
- Do not claim upstream BetterRules review or independent adoption.
- Historical BetterRules issue #199 and PR #200 are provenance only.

## Authoritative Inputs

- Repository issue: https://github.com/edithatogo/openfisca-aotearoa/issues/1
- Merged implementation: https://github.com/edithatogo/openfisca-aotearoa/pull/2
- Merge revision: `0ee8ac98e5dae08bd061edd0a9bfce564177ceaf`

## External Gates

None. Upstream acceptance is outside this track and is not required.

## Out of Scope

- Other KiwiSaver policy surfaces.
- Publication or release authorization.
- Independent-validation claims.
