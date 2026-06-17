"""Tests for the high-performance ASGI app."""

import asyncio

import orjson

from openfisca_aotearoa.api.app import app


async def call_app(
    method: str,
    path: str,
    body: bytes = b"",
    query_string: bytes = b"",
) -> dict:
    """Call the ASGI app in-process and return status/body data."""
    messages = []
    request_sent = False

    async def receive() -> dict:
        nonlocal request_sent
        if request_sent:
            return {"type": "http.disconnect"}
        request_sent = True
        return {"type": "http.request", "body": body, "more_body": False}

    async def send(message: dict) -> None:
        messages.append(message)

    await app(
        {
            "type": "http",
            "method": method,
            "path": path,
            "query_string": query_string,
            "headers": [],
        },
        receive,
        send,
    )

    start = messages[0]
    response = messages[1]
    return {
        "status": start["status"],
        "body": orjson.loads(response["body"]),
    }


def test_unknown_route_returns_json_error() -> None:
    response = asyncio.run(call_app("GET", "/missing"))

    assert response == {
        "status": 404,
        "body": {
            "error": {
                "code": "not_found",
                "message": "Endpoint not found.",
                "details": [],
            },
        },
    }


def test_health_returns_liveness_payload() -> None:
    response = asyncio.run(call_app("GET", "/health"))

    assert response == {
        "status": 200,
        "body": {
            "status": "ok",
            "service": "openfisca-aotearoa-api",
        },
    }


def test_metadata_returns_package_and_model_details() -> None:
    response = asyncio.run(call_app("GET", "/metadata"))

    assert response["status"] == 200
    assert response["body"]["country_package"] == "openfisca-aotearoa"
    assert response["body"]["model"] == "AotearoaLegislationModel"
    assert response["body"]["api_version"] == "1"
    assert response["body"]["openfisca_core_version"]


def test_calculate_returns_openfisca_results() -> None:
    response = asyncio.run(
        call_app(
            "POST",
            "/calculate",
            orjson.dumps(
                {
                    "period": "2025-01-01",
                    "variables": ["age"],
                    "persons": [
                        {
                            "id": "person_a",
                            "date_of_birth": {"ETERNITY": "1995-01-01"},
                        },
                    ],
                },
            ),
        ),
    )

    assert response == {
        "status": 200,
        "body": {
            "period": "2025-01-01",
            "results": [{"id": "person_a", "age": 30}],
        },
    }


def test_calculate_returns_validation_error() -> None:
    response = asyncio.run(
        call_app(
            "POST",
            "/calculate",
            orjson.dumps(
                {
                    "period": "2025",
                    "variables": [],
                    "persons": [{"id": "person_a"}],
                },
            ),
        ),
    )

    assert response["status"] == 422
    assert response["body"]["error"]["code"] == "validation_error"
    assert response["body"]["error"]["details"]


def test_calculate_returns_calculation_error() -> None:
    response = asyncio.run(
        call_app(
            "POST",
            "/calculate",
            orjson.dumps(
                {
                    "period": "2025",
                    "variables": ["missing_variable"],
                    "persons": [{"id": "person_a"}],
                },
            ),
        ),
    )

    assert response["status"] == 400
    assert response["body"]["error"]["code"] == "calculation_error"


def test_parameters_returns_root_children() -> None:
    response = asyncio.run(call_app("GET", "/parameters"))

    assert response["status"] == 200
    assert response["body"]["path"] == "root"
    assert "taxes" in response["body"]["children"]
    assert response["body"]["truncated"] is False


def test_parameters_returns_nested_children() -> None:
    response = asyncio.run(
        call_app("GET", "/parameters", query_string=b"path=taxes"),
    )

    assert response["status"] == 200
    assert response["body"]["path"] == "taxes"
    assert "income_tax" in response["body"]["children"]


def test_parameters_applies_limit() -> None:
    response = asyncio.run(
        call_app("GET", "/parameters", query_string=b"limit=1"),
    )

    assert response["status"] == 200
    assert len(response["body"]["children"]) == 1
    assert response["body"]["truncated"] is True


def test_parameters_returns_not_found_for_missing_path() -> None:
    response = asyncio.run(
        call_app("GET", "/parameters", query_string=b"path=missing.path"),
    )

    assert response["status"] == 404
    assert response["body"]["error"]["code"] == "parameter_not_found"
