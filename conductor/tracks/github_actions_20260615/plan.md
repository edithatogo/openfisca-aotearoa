# Plan: GitHub CI/CD Automation & Quality Gates

## Phase 1: Workflow Scaffolding and Quality Gates
- [x] Task: Integrate Astral's `setup-uv` Action for cache-optimized dependency installs
- [x] Task: Implement `ruff-action` to run strict linting and formatting gates
- [x] Task: Configure `basedpyright` for strict static type checking
- [x] Task: Add `complexipy` to check and restrict cognitive complexity to <= 15
- [x] Task: Integrate multi-tier testing via `pytest` with warnings-as-errors (`-W error`), `hypothesis` fuzzing, and `pytest-gremlins`
- [x] Task: Set up a comprehensive PR template with a quality gates verification checklist
- [x] Task: Conductor - User Manual Verification 'Verify CI workflow passes on PR/Push' [checkpoint: work_done]
