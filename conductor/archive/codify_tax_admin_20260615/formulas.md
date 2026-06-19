# Formula Evidence

Track 11 adds Tax Administration Act compliance variables.

Formula artifacts:

- `tax_admin__automatic_tax_assessment`: default automatic assessment flag.
- `tax_admin__filing_deadline_months_after_year_end`: returns `0` for
  automatic assessment and `3` for manual filing.

Implementation file:

- `openfisca_aotearoa/variables/acts/tax_admin/compliance.py`
