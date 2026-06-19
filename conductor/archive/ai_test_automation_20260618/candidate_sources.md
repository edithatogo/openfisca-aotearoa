# Candidate Source Documents

The first generated-test sources are deliberately narrow and deterministic:

| Source | Reason |
| --- | --- |
| `openfisca_aotearoa/variables/demographics/ages.py` | Stable age calculation with existing hand-written coverage and a clear boundary date. |
| `conductor/tracks/ai_test_automation_20260618/spec.md` | Source of the review-gated AI automation requirements. |
| `conductor/product-guidelines.md` | Ensures generated tests remain traceable and reviewable rather than authoritative legal interpretation. |

Future candidate generation should prefer tracks with:

- a reviewed spec or gap report;
- explicit legislative references;
- existing hand-written tests to compare against;
- small deterministic scenarios before broader generated coverage.
