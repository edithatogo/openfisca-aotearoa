# Plan: Legislative Freshness Refresh

## Phase 1: Source Refresh and Scope Decisions

- [x] Task: Build a Track 19 source refresh manifest for Pae Ora, Public and Community Housing Management, Tax Administration, and ACC earners' levy instruments.
- [x] Task: Capture official URLs, version dates, amendment notices, and extraction status in track evidence artifacts.
- [x] Task: Create an amendment decision table classifying each recent amendment as implemented, no model impact, out-of-scope, or blocked pending official incorporation.
- [x] Task: Record tool-boundary notes for unavailable live tools and confirm no authenticated `fyi-cli` or OIA activity was run.

## Phase 2: Pae Ora Refresh

- [x] Task: Review Pae Ora section 46A and 2024-2026 amendments against the local primary-care funding module.
- [x] Task: Reconcile current Act title, pending or enacted naming changes, local `pae_ora` namespace usage, labels, and citations.
- [x] Task: Update Pae Ora variables, parameters, and evidence artifacts for any in-scope model impact.
- [x] Task: Add or update Pae Ora situation tests covering changed or explicitly unchanged behavior.

## Phase 3: Public and Community Housing Management Refresh

- [x] Task: Rename or document the older Housing Restructuring track/module framing against the current Public and Community Housing Management Act title.
- [x] Task: Review sections 106 and 107, market-rent caps, higher-rent tests, weekly calculation rules, and 2 March 2026 transitional provisions.
- [x] Task: Update housing variables, formulas, labels, citations, and tests for the current income-related rent structure, or document a partial-coverage blocker with explicit tests.
- [x] Task: Add evidence artifacts tracing each housing formula and parameter decision to official source text.

## Phase 4: Tax Administration Refresh

- [x] Task: Review official Tax Administration Act unincorporated-amendment notices and recent consequential amendments.
- [x] Task: Determine whether Deposit Takers Act 2023 and recent annual tax amendments affect local automatic-assessment or filing-deadline variables.
- [x] Task: Update Tax Administration variables, citations, tests, and evidence artifacts for any in-scope model impact.
- [x] Task: Record out-of-scope or no-model-impact decisions for amendments that do not affect the current compliance scaffold.

## Phase 5: ACC Earners' Levy Refresh

- [x] Task: Reconcile ACC earners' levy citations against the current 2022 and 2025 regulations.
- [x] Task: Update rate and maximum-threshold parameters for 2024/25, 2025/26, 2026/27, and 2027/28+ where official instruments provide values.
- [x] Task: Review low-earner or self-employed formulas and decide whether they affect the current wage-earner levy model.
- [x] Task: Add ACC YAML tests for threshold capping and levy calculations across the refreshed years.

## Phase 6: Currentness Gate and Closeout

- [x] Task: Generate a legislative-currentness report that distinguishes evidence presence from amendment incorporation.
- [x] Task: Run focused YAML tests for Pae Ora, housing, Tax Administration, and ACC.
- [x] Task: Run readiness/currentness checks and update Track 9-12 evidence artifacts where required.
- [x] Task: Run the broad CI-equivalent suite: `uv run pytest --cov=openfisca_aotearoa --cov-report=xml --strict-markers --strict-config -W error`.
- [x] Task: Conductor - User Manual Verification 'Confirm legislative freshness decisions and remaining legal/currentness risks' [checkpoint: work_done]
