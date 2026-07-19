# Specification

## Objective

Make all 23 historical archive tracks discoverable by the current Conductor
validator without changing their plans, specifications, metadata, or evidence.

## Contract

- Each historical archive gains a standard `index.md` entrypoint.
- The registry gains one canonical machine-readable alias per archive.
- Existing legacy headings remain as historical presentation context.
- Track content and status remain unchanged.

## Acceptance

- Full Conductor validation reports no errors or warnings.
- Hosted repository checks pass.
- Every historical archive resolves through exactly one canonical target.
