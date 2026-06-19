# Formula Evidence

Track 12 adds ACC earners' levy variables.

Formula artifacts:

- `acc__earners_levy_liable_income`: caps annual gross income at the configured
  maximum liable income threshold.
- `acc__earners_levy`: multiplies liable income by the configured levy rate.

Implementation file:

- `openfisca_aotearoa/variables/acts/acc/earners_levy.py`
