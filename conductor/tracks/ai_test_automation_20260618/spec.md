# Specification: AI-Assisted Test Automation

## Purpose

Implement the roadmap's AI-driven test automation requirement in a controlled,
reviewable way that improves coverage without allowing generated tests to become
unreviewed source-of-truth legislation.

## Requirements

- Evaluate TestSprite availability, licensing, local execution model, and CI
  suitability.
- Define a safe workflow for generating candidate tests from specs, plans, and
  legislation references.
- Store generated candidates separately from accepted tests until reviewed.
- Require human or Conductor review before generated tests enter the main test
  suite.
- Add metadata tying generated tests back to the source spec and prompt.
- Add CI checks that accepted generated tests are deterministic.

## Non-Goals

- Allowing AI tools to modify legislation variables without review.
- Depending on network-only AI services in default CI.
- Treating generated tests as authoritative legal interpretations.
