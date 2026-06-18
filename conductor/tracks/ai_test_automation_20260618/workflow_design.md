# AI Test Workflow Design

## Storage Locations

- Quarantined candidates:
  `conductor/ai_test_candidates/quarantine/`
- Accepted generated tests:
  `openfisca_aotearoa/tests/ai_generated/accepted/`
- Metadata fixtures for contract tests:
  `openfisca_aotearoa/tests/fixtures/ai_test_automation/`

## Candidate Files

Each candidate has two side-by-side JSON files:

- `<candidate_id>.scenario.json`
- `<candidate_id>.metadata.json`

The metadata sidecar must include:

- `candidate_id`;
- `source_track`;
- `source_document`;
- `prompt`;
- `generator`;
- `generated_at`;
- `review_status`;
- `reviewer`;
- `reviewed_at`;
- `notes`.

Candidates start as `quarantined`. A candidate can enter the normal pytest suite
only when `review_status` is `accepted` and both `reviewer` and `reviewed_at`
are present.

## Candidate Generation Command

Use the offline generator for default local and CI-safe candidate generation:

```powershell
.venv\Scripts\python.exe scripts\generate_ai_test_candidates.py `
  --candidate-id age_boundary_2025 `
  --source-track ai_test_automation_20260618 `
  --source-document openfisca_aotearoa/variables/demographics/ages.py `
  --prompt "Generate a deterministic boundary test for age on 2025-01-01."
```

The script writes candidate files into
`conductor/ai_test_candidates/quarantine/` unless `--output-dir` is supplied.

## Review Gates

The review gate is implemented by
`openfisca_aotearoa.ai_test_automation.require_accepted_candidate`.
Quarantined, rejected, or needs-changes candidates fail before execution.
