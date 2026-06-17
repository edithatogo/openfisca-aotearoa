"""Tests for the high-performance ASGI app."""

import asyncio

import orjson

from openfisca_aotearoa.api.app import app


async def call_app(method: str, path: str, body: bytes = b"") -> dict:
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
            "query_string": b"",
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
