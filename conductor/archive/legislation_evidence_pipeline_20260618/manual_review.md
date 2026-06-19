# Manual Review Steps

## Evidence Manifest Schema Review

1. Confirm the manifest fields are sufficient to trace each variable or
   parameter reference back to source text.
2. Confirm `verification_status` values distinguish unverified local extraction
   from tool-verified, failed, unavailable, and manual-review evidence.
3. Confirm `fyi-cli` remains manual for live or authenticated OIA activity.

## Evidence Pipeline Smoke Test

1. Run the offline evidence tests:

   ```powershell
   .venv\Scripts\python.exe -m pytest openfisca_aotearoa\tests\test_evidence.py
   ```

2. Optionally build a manifest in a Python shell:

   ```python
   from openfisca_aotearoa.evidence import build_manifest

   manifest = build_manifest(
       "legislation_evidence_pipeline_20260618",
       ["openfisca_aotearoa/variables", "openfisca_aotearoa/parameters"],
   )
   ```

3. If external tools are installed, compare their exported JSON reports against
   the manifest. Do not run live `fyi-cli` activity without explicit operator
   approval and credentials.
