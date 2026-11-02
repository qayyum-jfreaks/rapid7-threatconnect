import datetime
from typing import Any

import requests

from icon_whoisfreaks.util import config, errors


def fetch_status() -> dict:
    """Fetch the WhoisFreaks status endpoint and return parsed JSON.

    The status endpoint is public and requires no API key.

    Raises:
        PluginException (STATUS_UNAVAILABLE) on network error, non-200, or non-JSON.
    """
    url = f"{config.get_base_url()}{config.STATUS_PATH}"
    try:
        resp = requests.get(url, timeout=config.TIMEOUT_SECONDS)
    except requests.RequestException as exc:
        raise errors.status_unavailable(f"network error: {exc}") from exc

    if resp.status_code != 200:
        raise errors.status_unavailable(f"HTTP {resp.status_code} from {url}: {resp.text[:200]}")

    try:
        data = resp.json()
    except ValueError as exc:
        raise errors.status_unavailable(f"non-JSON response from {url}: {resp.text[:200]}") from exc

    if not isinstance(data, dict):
        raise errors.status_unavailable(f"unexpected response shape from {url}: {type(data).__name__}")

    return data


def navigate_status_node(status: dict, path: list[str]) -> dict:
    """Walk the status JSON to the leaf node for a feed.

    Args:
        status: the parsed status response
        path: key path, e.g. ["newly", "gtld"] or ["threat_feed", "phishing"]

    Returns:
        The leaf dict containing last_update and available_from.

    Raises:
        FeedNotAvailable if any path key is missing, the leaf is not a dict,
        or last_update / available_from is "Not Available" or empty.
    """
    feed_id = ".".join(path)
    node: Any = status

    for key in path:
        if not isinstance(node, dict) or key not in node:
            raise errors.FeedNotAvailable(
                feed=feed_id,
                reason=f"path not found in status response: missing key '{key}'",
            )
        node = node[key]

    if not isinstance(node, dict):
        raise errors.FeedNotAvailable(
            feed=feed_id,
            reason=f"status node is not a dict: {type(node).__name__}",
        )

    last_update = node.get("last_update")
    available_from = node.get("available_from")

    if not last_update or last_update == "Not Available":
        raise errors.FeedNotAvailable(
            feed=feed_id,
            reason=f"last_update is '{last_update}'",
        )
    if not available_from or available_from == "Not Available":
        raise errors.FeedNotAvailable(
            feed=feed_id,
            reason=f"available_from is '{available_from}'",
        )

    return node


def validate_date(user_date: str, node: dict) -> str:
    """Validate the user-supplied date against the feed's allowed range.

    Args:
        user_date: YYYY-MM-DD string from the date input
        node: the leaf dict from navigate_status_node

    Returns:
        The same user_date string (normalized by successful parse).

    Raises:
        PluginException (INVALID_DATE_FORMAT) if user_date is not a valid calendar date
        PluginException (DATE_OUT_OF_RANGE) if user_date is outside [available_from, last_update]
    """
    try:
        parsed = datetime.datetime.strptime(user_date, "%Y-%m-%d").date()
    except (ValueError, TypeError) as exc:
        raise errors.invalid_date_format(str(user_date)) from exc

    available_from = datetime.date.fromisoformat(node["available_from"])
    last_update = datetime.date.fromisoformat(node["last_update"])

    if parsed < available_from or parsed > last_update:
        raise errors.date_out_of_range(
            user_date,
            node["available_from"],
            node["last_update"],
        )

    return user_date
