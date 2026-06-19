# Situation-Test Evidence

Focused validation:

```text
uv run python scripts\run_openfisca_yaml_tests.py openfisca_aotearoa\tests\pae_ora\health_services.yaml
```

Covered scenarios:

- Eligible person receives the standard copayment subsidy.
- Ineligible person receives zero subsidy.
- Subsidy reflects the parameter amount for the period.
