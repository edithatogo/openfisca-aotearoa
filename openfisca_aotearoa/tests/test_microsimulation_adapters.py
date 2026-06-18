"""Tests for optional microsimulation analytics adapter boundaries."""

import pytest

from openfisca_aotearoa.microsimulation import (
    MicrosimulationAdapterError,
    OptionalDependency,
    adapter_statuses,
)


def test_adapter_statuses_report_optional_dependencies(monkeypatch) -> None:
    monkeypatch.setattr(
        "importlib.util.find_spec",
        lambda name: None,
    )

    statuses = adapter_statuses()

    assert [status.name for status in statuses] == [
        "open_social_data",
        "voiage",
        "mars",
        "innovate",
    ]
    assert all(not status.available for status in statuses)
    assert statuses[0].purpose == "population cohort source"


def test_optional_dependency_raises_clear_error_when_absent(
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        "importlib.util.find_spec",
        lambda name: None,
    )
    adapter = OptionalDependency(
        name="voiage",
        import_name="voiage",
        purpose="value-of-information analysis",
    )

    with pytest.raises(MicrosimulationAdapterError, match="not installed"):
        adapter.require()


def test_value_of_information_adapter_boundary(monkeypatch) -> None:
    monkeypatch.setattr(
        "importlib.util.find_spec",
        lambda name: None,
    )
    adapters = {status.name: status for status in adapter_statuses()}

    assert adapters["voiage"].purpose == "value-of-information analysis"


def test_spline_regression_adapter_boundary(monkeypatch) -> None:
    monkeypatch.setattr(
        "importlib.util.find_spec",
        lambda name: None,
    )
    adapters = {status.name: status for status in adapter_statuses()}

    assert adapters["mars"].purpose == "spline-regression summaries"


def test_policy_diffusion_adapter_boundary(monkeypatch) -> None:
    monkeypatch.setattr(
        "importlib.util.find_spec",
        lambda name: None,
    )
    adapters = {status.name: status for status in adapter_statuses()}

    assert adapters["innovate"].purpose == "policy-diffusion modelling"
