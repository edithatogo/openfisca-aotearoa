# Formula Evidence

Track 15 changed one formula output contract:

- `openfisca_aotearoa/variables/acts/social_security/accommodation_supplement/situation.py`

`accommodation_supplement__situation.formula_2018_11_26` now returns integer
enum indices from `numpy.select` for all choices, instead of mixing enum member
objects with an integer fallback. OpenFisca Core 44.7.0 can encode the resulting
integer array as `AccommodationSupplement__Situation` enum values.

The family tax credit group-to-person aggregation issue is already fixed in the
current branch by using `populations.ADD` in
`openfisca_aotearoa/variables/acts/income_tax/family_scheme/family_tax_credit.py`.
