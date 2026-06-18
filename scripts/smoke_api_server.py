"""Smoke test the Granian ASGI API server from the packaged entry point."""

from __future__ import annotations

import json
import os
import socket
import subprocess
import sys
import time
from contextlib import closing
from urllib.error import URLError
from urllib.request import Request, urlopen


def main() -> None:
    """Start the API server, probe it, and shut it down."""
    host = "127.0.0.1"
    port = _free_port()
    process = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "openfisca_aotearoa.api.cli",
            "--host",
            host,
            "--port",
            str(port),
            "--workers",
            "1",
            "--no-log",
        ],
        env=_server_env(),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    try:
        base_url = f"http://{host}:{port}"
        _wait_for_health(process, f"{base_url}/health")
        calculation = _post_json(
            f"{base_url}/calculate",
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
        )
        if calculation["results"] != [{"id": "person_a", "age": 30}]:
            raise RuntimeError(f"Unexpected calculation: {calculation!r}")
    finally:
        _stop(process)


def _server_env() -> dict[str, str]:
    """Return environment variables suitable for deterministic smoke checks."""
    env = os.environ.copy()
    env.setdefault("OPENBLAS_NUM_THREADS", "1")
    env.setdefault("OMP_NUM_THREADS", "1")
    env.setdefault("GRANIAN_WORKERS", "1")
    return env


def _free_port() -> int:
    """Reserve and release an ephemeral TCP port for the smoke server."""
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def _wait_for_health(process: subprocess.Popen[str], url: str) -> None:
    """Wait until the health endpoint responds or the server exits."""
    deadline = time.monotonic() + 30
    last_error: Exception | None = None
    while time.monotonic() < deadline:
        if process.poll() is not None:
            output = process.stdout.read() if process.stdout else ""
            raise RuntimeError(
                f"API server exited with {process.returncode}: {output}",
            )
        try:
            health = _get_json(url)
        except (TimeoutError, URLError) as error:
            last_error = error
            time.sleep(0.25)
            continue
        if health == {
            "status": "ok",
            "service": "openfisca-aotearoa-api",
        }:
            return
        raise RuntimeError(f"Unexpected health payload: {health!r}")
    raise TimeoutError(f"API server did not become healthy: {last_error!r}")


def _get_json(url: str) -> dict:
    """Fetch JSON from a URL."""
    with urlopen(url, timeout=2) as response:
        return json.loads(response.read().decode("utf-8"))


def _post_json(url: str, payload: dict) -> dict:
    """Post a JSON payload and parse the JSON response."""
    request = Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"content-type": "application/json"},
        method="POST",
    )
    with urlopen(request, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def _stop(process: subprocess.Popen[str]) -> None:
    """Terminate the smoke server without leaving a process behind."""
    if process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=10)


if __name__ == "__main__":
    main()
