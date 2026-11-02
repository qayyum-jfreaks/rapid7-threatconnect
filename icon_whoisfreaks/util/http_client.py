from typing import Any

import requests

from icon_whoisfreaks.util import config


def stream_request(
    path: str,
    params: dict[str, Any],
    api_key: str,
    timeout: int = None,
) -> requests.Response:
    """Issue a GET request to a WhoisFreaks stream endpoint.

    Base URL is fixed in config. Returns the raw Response object - no status
    mapping, no retries, no exception wrapping. The caller decides how to
    react to non-200 codes.

    All params values MUST be strings - the caller converts bools to
    "true"/"false" and ints to str before calling.
    """
    if timeout is None:
        timeout = config.TIMEOUT_SECONDS
    url = f"{config.get_base_url()}{path}"
    return requests.get(
        url,
        headers={"X-API-KEY": api_key},
        params=params,
        timeout=timeout,
    )


def probe_entitlement(
    path: str,
    params: dict[str, Any],
    api_key: str,
    timeout: int = None,
) -> tuple[str, Any]:
    """Probe a stream endpoint for entitlement without consuming a full page.

    Returns (kind, message) where kind is one of:
        ok, empty, not_entitled, rate_limited, server_error,
        client_error, network_error

    See module docstring for interpretation.
    """
    try:
        resp = stream_request(path, params, api_key, timeout)
    except requests.RequestException as exc:
        return ("network_error", str(exc))

    if resp.status_code == 200:
        if resp.content.strip():
            return ("ok", None)
        return ("empty", None)

    if resp.status_code in (401, 403):
        return ("not_entitled", _extract_message(resp))

    if resp.status_code == 429:
        return ("rate_limited", None)

    if 500 <= resp.status_code < 600:
        return ("server_error", resp.status_code)

    return (
        "client_error",
        f"HTTP {resp.status_code}: {resp.text[:200] or '<empty body>'}",
    )


def _extract_message(resp: requests.Response) -> str:
    """Extract the 'message' field from a JSON error body, or fall back to text."""
    try:
        data = resp.json()
    except ValueError:
        data = None
    if isinstance(data, dict):
        message = data.get("message")
        if message:
            return str(message)
    body = resp.text.strip()[:200]
    if body:
        return body
    return f"HTTP {resp.status_code}"
