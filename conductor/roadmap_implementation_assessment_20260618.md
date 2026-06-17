# Roadmap Implementation Assessment 2026-06-18

## Verdict

The scheduled roadmap tracks 1-8 have implementation artifacts and are marked
complete or archived in `conductor/tracks.md`.

The full roadmap is not yet fully implemented. The roadmap combines the
scheduled tracks with a broader product vision, MoSCoW requirements, legislation
codification pipeline, and testing/integration strategy. Several of those
broader requirements remain partial or unimplemented.

## Completed Scheduled Tracks

- Track 1: Modernize Tooling.
- Track 2: Upstream Governance Alignment.
- Track 3: Map Historical/Current Tax Rules.
- Track 4: Legislation Audit & Scaffolding.
- Track 5: GitHub CI/CD Automation & Multi-Tier Testing.
- Track 6: Documentation Pages Explorer.
- Track 7: Release & Dependabot Lifecycle.
- Track 8: Simulation Analytics & Policy Diffusion.

## Open Conductor Tracks Beyond The Roadmap Schedule

- Track 13, Social Security Act 2018 Core Entitlements and Income Tests, is
  still pending tests and manual verification.
- Track 14, Income Tax Act 2007 Core Tax and Family Scheme Rules, is still in
  progress and has pending implementation, tests, and manual verification.

## Remaining Roadmap Gaps

- The roadmap calls for strict type safety, but `pyproject.toml` currently uses
  a basic `basedpyright` baseline rather than strict settings.
- The roadmap calls for `uv` workspaces and `una` monorepo tooling. The current
  repository has `uv` metadata, but `una` workspace integration is not evident
  in this repository.
- The roadmap calls for high-performance web serving with `granian` or `robyn`.
  Neither runtime is declared in the current project dependencies.
- The roadmap calls for population simulations over `open_social_data` and
  analytics integrations with `voiage`, `mars`, and `innovate`. Track 8 now
  provides a tested batch simulation helper and JSON/CSV export path, but those
  external integrations are not implemented in this repository.
- The roadmap calls for `sourceright`, `nlp-policy-nz`, and `fyi-cli`
  integration in the legislation-to-code pipeline. These are referenced in
  roadmap documentation, but no end-to-end local integration is evident here.
- The roadmap calls for TestSprite AI-driven tests. No TestSprite integration is
  evident in the current project.
- The roadmap calls for legal-audit completion before publish. Tracks 13 and 14
  show core legal codification work remains open.

## Verification Snapshot

The following checks were run during the Tracks 6-8 remediation and archive
pass:

- `python docs-site\generate_parameters.py`.
- `python -m ruff check docs-site\generate_parameters.py`.
- `npm run docs:check`.
- `npm run docs:build`.
- `bash -n .github/has-functional-changes.sh .github/is-version-number-acceptable.sh .github/publish-git-tag.sh`.
- `DRY_RUN=true RELEASE_VERSION=0.1.0 .github/publish-git-tag.sh`.
- `GITHUB_REF=refs/heads/main .github/is-version-number-acceptable.sh`.
- `GITHUB_REF=refs/heads/review .github/is-version-number-acceptable.sh`.
- GitHub workflow YAML parsing.
- `uv run python -m pytest -q openfisca_aotearoa\tests\test_simulation.py`.
- `python -m ruff check openfisca_aotearoa\simulation.py openfisca_aotearoa\tests\test_simulation.py`.

## Recommended Next Tracks

- Complete Track 13 tests and manual verification for Social Security Act core
  rules.
- Complete Track 14 implementation, tests, and manual verification for Income
  Tax Act core rules.
- Track 15: Upgrade OpenFisca Core compatibility and strict quality gates.
- Track 16: Add `una` and `uv` workspace integration.
- Track 17: Add high-performance Web API serving with Granian or Robyn.
- Track 18: Integrate microsimulation data and analytics adapters for
  `open_social_data`, `voiage`, `mars`, and `innovate`.
- Track 19: Integrate the legislation evidence pipeline for `nz-legislation`,
  `sourceright`, `nlp-policy-nz`, and `fyi-cli`.
- Track 20: Add AI-assisted test automation with safe review gates.
- Track 21: Create legal audit and publish readiness gates.
