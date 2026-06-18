# Generated Test Review Checklist

Before accepting a generated test:

- Confirm the source document and prompt are recorded in the metadata sidecar.
- Confirm the generated scenario is deterministic and does not call live AI,
  legislation, OIA, or external data services.
- Confirm expected outputs are independently reviewed against source code,
  hand-written tests, or legislation references.
- Confirm the test does not change variables, parameters, or legal rules.
- Set `review_status` to `accepted`.
- Set `reviewer` and `reviewed_at`.
- Move the scenario and metadata files into
  `openfisca_aotearoa/tests/ai_generated/accepted/`.
- Run:

```powershell
.venv\Scripts\python.exe -m pytest openfisca_aotearoa\tests\test_ai_test_automation.py
```

Reject or mark `needs_changes` when the generated scenario is ambiguous,
duplicates existing coverage without value, lacks traceable source metadata, or
contains unsupported legal interpretation.
