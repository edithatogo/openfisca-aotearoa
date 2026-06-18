# Legal Audit and Publish Readiness Criteria

## Readiness Statuses

- `draft`: no completed Conductor implementation evidence is present.
- `implemented`: implementation tasks are complete, but test or manual-review
  evidence is incomplete.
- `tested`: automated situation or test evidence is present, but manual
  checkpoints or required evidence remain incomplete.
- `legally_reviewed`: all discovered manual Conductor checkpoints are marked
  `work_done`, but one or more required publish-readiness evidence classes are
  still missing.
- `publish_ready`: required evidence is complete, manual checkpoints are done,
  and unresolved risks are empty.
- `archived`: the track has already been moved to the Conductor archive.

## Required Evidence Classes

The local gate expects evidence for:

- `traceability`;
- `citations`;
- `parameters`;
- `formulas`;
- `situation_tests`;
- `manual_verification`.

The gate is intentionally conservative. It records missing evidence and
unresolved risks rather than treating implementation work as legal advice or
external legal sign-off.

## Archive Criteria

A track can be archived when:

- implementation tasks are complete;
- relevant automated tests pass;
- manual Conductor checkpoints are marked `work_done`;
- the readiness report records no unresolved publish-blocking risks, or the
  archive explicitly records why residual risks are accepted.

## Publish-Ready Criteria

A track can be marked publish-ready only when:

- `readiness_status` is `publish_ready`;
- `missing_evidence` is empty;
- `unresolved_risks` is empty;
- the generated Markdown report is available for policy or legal review.

Use the non-interactive command:

```powershell
.venv\Scripts\python.exe scripts\check_publish_readiness.py `
  conductor\tracks\codify_social_security_core_20260615
```

The command exits with a non-zero status when required readiness evidence is
missing. Use `--allow-not-ready --report <path>` only to generate an audit report
without enforcing the gate.
