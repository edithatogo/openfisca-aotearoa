# Specification: Una and UV Workspace Integration

## Purpose

Implement the roadmap's workspace requirement by making this package work
cleanly inside the parent `legal-nz` workspace while preserving standalone
development with `uv`.

## Requirements

- Audit current `pyproject.toml`, lockfiles, scripts, and parent workspace
  assumptions.
- Determine whether `una` should be configured in this repository, the parent
  workspace, or both.
- Add workspace metadata that does not break standalone package installation.
- Document commands for local install, test, lint, and docs generation from both
  this repository and the parent workspace.
- Add validation that workspace commands resolve local dependencies correctly.
- Keep parent-repo and nested-repo boundaries explicit.

## Non-Goals

- Moving this repository into a different directory.
- Replacing `uv` with another package manager.
- Making broad parent workspace changes without a separate parent-repo commit.
