# Manual Verification

Manual checkpoints completed:

- Microsimulation contract review.
- Analytics adapters smoke test.

Implemented boundary:

- canonical Pydantic cohort input and simulation output contracts.
- bounded batch runner with explicit cohort-size protection.
- deterministic JSON and CSV export through existing `BatchSimulator` export
  support.
- offline fixture cohort for local tests.
- optional adapter status and clear missing-dependency errors for
  `open_social_data`, `voiage`, `mars`, and `innovate`.

Non-goals remain unchanged: no vendored large datasets, no reimplementation of
external analytics packages, and no policy conclusions from synthetic fixtures.
