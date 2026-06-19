# Situation-Test Evidence

Focused validation:

```text
uv run python scripts\run_openfisca_yaml_tests.py openfisca_aotearoa\tests\acc\earners_levy.yaml
```

Covered scenarios:

- ACC earners levy applies the current rate below the cap.
- ACC earners levy liable income is capped at the maximum threshold.
