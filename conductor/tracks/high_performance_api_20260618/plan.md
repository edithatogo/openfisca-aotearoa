# Plan: High-Performance Web API Serving

## Phase 1: Runtime Selection and API Contract

- [x] Task: Compare Granian and Robyn against project requirements, Windows support, dependency size, and CI behaviour. (`c4aae06`)
- [x] Task: Define endpoint contract for `/health`, `/metadata`, `/calculate`, and `/parameters`. (`62d62c7`)
- [x] Task: Create Pydantic request and response schemas for calculation requests and validation errors. (`64e451f`)
- [x] Task: Conductor - User Manual Verification 'API runtime and contract review' [checkpoint: work_done]. (`c4aae06`, `62d62c7`, `64e451f`)

## Phase 2: Server Implementation

- [x] Task: Add selected runtime dependency and minimal application module. (`0b53edf`)
- [x] Task: Implement health and metadata endpoints without loading unnecessary state. (`33775d4`)
- [x] Task: Implement calculation endpoint using the OpenFisca tax-benefit system. (`90b45a8`)
- [x] Task: Implement parameter inspection endpoint with bounded output and clear errors. (`fc3c232`)
- [x] Task: Add non-interactive local run command and environment configuration. (`b7f8f0c`)

## Phase 3: Tests, Smoke Checks, and Docs

- [x] Task: Add unit tests for Pydantic models and validation errors. (`64e451f`)
- [x] Task: Add API smoke tests for health, metadata, and a representative calculation. (`33775d4`, `90b45a8`)
- [x] Task: Add CI-safe server startup/shutdown validation. (`a122e68`)
- [x] Task: Document API usage, example payloads, and limitations. (`e7a6b90`)
- [ ] Task: Conductor - User Manual Verification 'High-performance API smoke test' [checkpoint: pending].
