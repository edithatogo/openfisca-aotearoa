PYTHON ?= python
UV ?= uv
OPENFISCA_YAML_TESTS ?= openfisca_aotearoa/tests

COMPATIBILITY_YAML_TESTS = \
	openfisca_aotearoa/tests/social_security/accommodation_supplement/2018/situation.yaml \
	openfisca_aotearoa/tests/income_tax/family_scheme/family_tax_credit.yaml

all: quality

uninstall:
	pip freeze | grep -v "^-e" | sed "s/@.*//" | xargs pip uninstall -y

clean:
	rm -rf build dist
	find . -name '*.pyc' -exec rm \{\} \;

deps:
	pip install --upgrade pip build twine setuptools

install: deps
	@# Install OpenFisca-Aotearoa for development.
	@# `make install` installs the editable version of OpenFisca-Aotearoa.
	@# This allows contributors to test as they code.
	pip install --editable .[dev] --upgrade

build: clean deps
	@# Install OpenFisca-Extension-Template for deployment and publishing.
	@# `make build` allows us to be be sure tests are run against the packaged version
	@# of OpenFisca-Extension-Template, the same we put in the hands of users and reusers.
	python -m build
	find dist -name "*.whl" -exec pip install --force-reinstall {}[dev] \;

check-syntax-errors:
	$(PYTHON) -m compileall -q .

format:
	$(UV) run ruff format .
	$(UV) run ruff check --fix .

lint:
	$(UV) run ruff check .
	$(UV) run basedpyright openfisca_aotearoa
	$(UV) run python scripts/run_complexity_gate.py

quality: lint test compatibility-yaml

test: clean check-syntax-errors pytest

full-test: test qtest

pytest:
	$(UV) run pytest --cov=openfisca_aotearoa --cov-report=term-missing

qtest:
ifdef yaml
	$(UV) run python scripts/run_openfisca_yaml_tests.py openfisca_aotearoa/tests/$(yaml)
else
	$(UV) run python scripts/run_openfisca_yaml_tests.py $(OPENFISCA_YAML_TESTS)
endif

compatibility-yaml:
	$(UV) run python scripts/run_openfisca_yaml_tests.py $(COMPATIBILITY_YAML_TESTS)

serve: build
	$(UV) run openfisca serve --country-package openfisca_aotearoa -b 0.0.0.0:5000 --reload
