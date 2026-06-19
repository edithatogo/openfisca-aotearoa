# Manual Verification

Manual checkpoints completed:

- AI test workflow safety review.
- Accepted AI-generated tests pass.

Verified boundaries:

- TestSprite is optional and is not required for default local or CI execution.
- Candidate generation defaults to an offline deterministic template.
- Generated candidates are written to quarantine before review.
- Accepted generated tests require metadata with source track, source document,
  prompt, generator, generated timestamp, reviewer, and reviewed timestamp.
- Quarantined, rejected, and needs-changes candidates fail the review gate.
- Accepted generated tests do not modify variables, parameters, formulas, or
  legal rules.

Focused validation rerun on 2026-06-19:

```text
uv run pytest openfisca_aotearoa\tests\test_ai_test_automation.py --strict-markers --strict-config -W error
```

Result:

```text
6 passed
```
