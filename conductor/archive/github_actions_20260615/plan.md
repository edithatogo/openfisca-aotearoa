# Plan: GitHub CI/CD Automation & Quality Gates

## Phase 1: Workflow Scaffolding and Quality Gates
- [x] Task: Integrate Astral's `setup-uv` Action for cache-optimized dependency installs
- [x] Task: Install project and dev dependencies with `uv sync --extra dev`
- [x] Task: Implement `ruff-action` to run lint gates
- [x] Task: Configure `basedpyright` for the current type-checking baseline
- [x] Task: Add `complexipy` to check and restrict cognitive complexity to <= 15
- [x] Task: Integrate `pytest` with warnings-as-errors (`-W error`) and Hypothesis property-based test coverage
- [x] Task: Set up a comprehensive PR template with a quality gates verification checklist
- [x] Task: Conductor - User Manual Verification 'Verify CI workflow passes on PR/Push' [checkpoint: work_done]
