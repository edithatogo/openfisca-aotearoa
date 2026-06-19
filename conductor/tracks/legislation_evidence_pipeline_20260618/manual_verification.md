# Manual Verification

Manual checkpoints completed:

- Evidence manifest schema review.
- Evidence pipeline smoke test.

Verified boundaries:

- `fyi-cli` live or authenticated OIA activity remains manual and requires
  operator approval.
- `nz-legislation`, `sourceright`, and `nlp-policy-nz` are optional live tools;
  default tests use offline fixtures and local manifests.
- Generated LLM or policy mappings are not treated as legal advice.
- Network access is not required for the default evidence tests.
