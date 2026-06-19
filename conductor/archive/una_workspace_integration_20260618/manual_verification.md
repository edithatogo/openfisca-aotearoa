# Manual Verification

Manual checkpoints completed:

- Workspace boundary and Una design review.
- Una workspace commands pass.

The current boundary remains explicit:

- Nested repository owns `pyproject.toml`, `uv.lock`, `docs/workspace.md`, and
  `scripts/smoke_workspace.py`.
- Parent `legal-nz` root is read-only for this track, except for documented
  `uv --directory openfisca-aotearoa ...` invocation examples.
- Parent submodule pointer updates remain a parent-repository follow-up.
