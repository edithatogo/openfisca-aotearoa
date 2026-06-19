# Manual Verification

Manual checkpoints completed:

- Readiness model review.
- Publish readiness gate review.

Verified boundaries:

- The readiness model distinguishes draft, implemented, tested,
  legally-reviewed, publish-ready, and archived tracks.
- Publish-ready manifests cannot declare missing evidence or unresolved risks.
- The Markdown report includes evidence details and unresolved risks.
- The non-interactive gate exits non-zero when required evidence is missing.
- Residual gaps for Tracks 9-12 remain visible instead of being marked complete.
- Tracks 13 and 14 are reported as publish-ready based on their current evidence
  artifacts and completed manual checkpoints.

Focused validation rerun on 2026-06-19:

```text
uv run pytest openfisca_aotearoa\tests\test_readiness.py --strict-markers --strict-config -W error
```

Result:

```text
8 passed
```
