# Validation

## Focused tests

PASS: .venv\Scripts\python.exe scripts\run_openfisca_yaml_tests.py openfisca_aotearoa\tests\acc\earners_levy.yaml

The focused ACC YAML suite collected 5 tests and all passed.

## uv validation

uv run python scripts\run_openfisca_yaml_tests.py openfisca_aotearoa\tests\acc\earners_levy.yaml was attempted first. It was blocked by uv cache Access is denied errors in the Scoop cache, C:\tmp cache, and a workspace-local cache. This is an environment/cache write blocker, not a model assertion failure.

## Manual review

Official source values were checked against New Zealand Legislation pages for Pae Ora, Public and Community Housing Management, and ACC earners levy. Tax Administration was reviewed against the existing official-source freshness record because the current page challenged this session with JavaScript verification.

## Full local suite

PASS: .venv\Scripts\python.exe -m pytest --cov=openfisca_aotearoa --cov-report=xml --strict-markers --strict-config -W error
Result: 65 passed, 1 skipped; coverage.xml written.

Additional focused suites passed:
- .venv\Scripts\python.exe scripts\run_openfisca_yaml_tests.py openfisca_aotearoa\tests\pae_ora\health_services.yaml (3 passed)
- .venv\Scripts\python.exe scripts\run_openfisca_yaml_tests.py openfisca_aotearoa\tests\housing_restructuring\social_housing.yaml (2 passed)
- .venv\Scripts\python.exe scripts\run_openfisca_yaml_tests.py openfisca_aotearoa\tests\tax_admin\compliance.yaml (2 passed)
