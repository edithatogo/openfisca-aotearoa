"""ASGI application for the high-performance API."""

from collections.abc import Awaitable, Callable
from http import HTTPStatus
from typing import Any

import orjson

from openfisca_aotearoa.api.models import ErrorEnvelope, ErrorPayload

Receive = Callable[[], Awaitable[dict[str, Any]]]
Send = Callable[[dict[str, Any]], Awaitable[None]]
Scope = dict[str, Any]


async def app(scope: Scope, receive: Receive, send: Send) -> None:
    """Serve the OpenFisca Aotearoa high-performance API."""
    if scope["type"] != "http":
        raise ValueError("Only HTTP ASGI scopes are supported")

    await _send_json(
        send,
        HTTPStatus.NOT_FOUND,
        ErrorEnvelope(
            error=ErrorPayload(
                code="not_found",
                message="Endpoint not found.",
            ),
        ).model_dump(),
    )


async def _send_json(
    send: Send,
    status: HTTPStatus,
    payload: dict[str, Any],
) -> None:
    """Send a JSON ASGI response."""
    body = orjson.dumps(payload)
    await send(
        {
            "type": "http.response.start",
            "status": status.value,
            "headers": [(b"content-type", b"application/json")],
        },
    )
    await send(
        {
            "type": "http.response.body",
            "body": body,
        },
    )
