import os

DEFAULT_BASE_URL = "https://files.whoisfreaks.com"
DEFAULT_API_URL = "https://api.whoisfreaks.com"
STATUS_PATH = "/v3.4/status"
TIMEOUT_SECONDS = 30


def get_base_url() -> str:
    """Base URL for stream and status endpoints.

    Production value is fixed. Environment variable override exists only for
    local testing against the mock server; it is never exposed to end users
    through connection inputs.
    """
    return os.environ.get("WHOISFREAKS_BASE_URL", DEFAULT_BASE_URL).rstrip("/")


def get_api_url() -> str:
    """Base URL for lookup endpoints.

    Same override rules as get_base_url().
    """
    return os.environ.get("WHOISFREAKS_API_URL", DEFAULT_API_URL).rstrip("/")
