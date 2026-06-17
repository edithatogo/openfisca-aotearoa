"""ASGI application for the high-performance API."""

from collections.abc import Awaitable, Callable
from http import HTTPStatus
from importlib import metadata
from typing import Any

import orjson
from pydantic import ValidationError

from openfisca_aotearoa.api.models import (
    CalculationRequest,
    CalculationResponse,
    ErrorEnvelope,
    ErrorPayload,
    HealthResponse,
    MetadataResponse,
)
from openfisca_aotearoa.simulation import BatchSimulator

Receive = Callable[[], Awaitable[dict[str, Any]]]
Send = Callable[[dict[str, Any]], Awaitable[None]]
Scope = dict[str, Any]


async def app(scope: Scope, receive: Receive, send: Send) -> None:
    """Serve the OpenFisca Aotearoa high-performance API."""
    if scope["type"] != "http":
        raise ValueError("Only HTTP ASGI scopes are supported")

    method = scope["method"]
    path = scope["path"]

    if method == "GET" and path == "/health":
        await _send_json(send, HTTPStatus.OK, HealthResponse().model_dump())
        return

    if method == "GET" and path == "/metadata":
        await _send_json(send, HTTPStatus.OK, _metadata().model_dump())
        return

    if method == "POST" and path == "/calculate":
        await _handle_calculate(receive, send)
        return

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


async def _handle_calculate(receive: Receive, send: Send) -> None:
    """Validate a calculation request and return OpenFisca results."""
    try:
        payload = orjson.loads(await _read_body(receive))
        request = CalculationRequest.model_validate(payload)
    except orjson.JSONDecodeError as error:
        await _send_error(
            send,
            HTTPStatus.BAD_REQUEST,
            "invalid_json",
            "Request body must be valid JSON.",
            [{"message": str(error)}],
        )
        return
    except ValidationError as error:
        await _send_error(
            send,
            HTTPStatus.UNPROCESSABLE_ENTITY,
            "validation_error",
            "Request body is invalid.",
            error.errors(),
        )
        return

    try:
        cohort = [
            {"id": person.id, **person.variables}
            for person in request.persons
        ]
        result = BatchSimulator().run(
            cohort,
            request.period,
            request.variables,
        )
    except Exception as error:
        await _send_error(
            send,
            HTTPStatus.BAD_REQUEST,
            "calculation_error",
            str(error),
        )
        return

    await _send_json(
        send,
        HTTPStatus.OK,
        CalculationResponse(
            period=request.period,
            results=result.to_dicts(),
        ).model_dump(),
    )


def _metadata() -> MetadataResponse:
    """Return package metadata without constructing the tax-benefit system."""
    return MetadataResponse(
        country_package="openfisca-aotearoa",
        model="AotearoaLegislationModel",
        openfisca_core_version=metadata.version("openfisca-core"),
    )


async def _read_body(receive: Receive) -> bytes:
    """Read the full ASGI request body."""
    chunks = []
    while True:
        message = await receive()
        if message["type"] == "http.disconnect":
            break
        chunks.append(message.get("body", b""))
        if not message.get("more_body", False):
            break
    return b"".join(chunks)


async def _send_error(
    send: Send,
    status: HTTPStatus,
    code: str,
    message: str,
    details: list[Any] | None = None,
) -> None:
    """Send a structured JSON error envelope."""
    await _send_json(
        send,
        status,
        ErrorEnvelope(
            error=ErrorPayload(
                code=code,
                message=message,
                details=details or [],
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
