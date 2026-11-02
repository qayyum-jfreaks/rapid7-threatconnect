from insightconnect_plugin_runtime.exceptions import PluginException

DATE_OUT_OF_RANGE = "DATE_OUT_OF_RANGE"
FEED_NOT_ENTITLED = "FEED_NOT_ENTITLED"
STATUS_UNAVAILABLE = "STATUS_UNAVAILABLE"
RATE_LIMITED = "RATE_LIMITED"
PARTIAL_RUN = "PARTIAL_RUN"
INVALID_CREDENTIALS = "INVALID_CREDENTIALS"
INVALID_DATE_FORMAT = "INVALID_DATE_FORMAT"
FEED_NOT_AVAILABLE = "FEED_NOT_AVAILABLE"


class FeedNotAvailable(PluginException):
    """Raised when the status endpoint reports a feed as Not Available.

    Subclasses PluginException to follow the SDK exception hierarchy. Caught
    separately in trigger.run() before the generic PluginException handler
    so it results in a long sleep and retry, not a workflow failure.
    """

    def __init__(self, feed: str, reason: str):
        self.feed = feed
        self.reason = reason
        super().__init__(
            cause=f"Feed '{feed}' is not available: {reason}",
            assistance=(
                f"The WhoisFreaks status endpoint currently reports feed '{feed}' as Not Available. "
                "This usually means the feed has not been published for the current cycle, or the "
                "WhoisFreaks side is still building it. The trigger will retry automatically on its "
                "next cycle"
            ),
            data={
                "code": FEED_NOT_AVAILABLE,
                "feed": feed,
                "reason": reason,
            },
        )


def entitlement_exception(feed: str, api_message: str) -> PluginException:
    """Returns a PluginException for a feed entitlement error."""
    return PluginException(
        cause=f"Feed '{feed}' is not entitled: {api_message}",
        assistance=(
            f"The WhoisFreaks account associated with this API key does not have access to feed '{feed}'. "
            "Newly registered domain feeds, threat feeds, and lookup endpoints are sold as separate "
            "subscriptions. Verify your WhoisFreaks subscription includes this feed, or contact "
            "WhoisFreaks support to enable it"
        ),
        data={
            "code": FEED_NOT_ENTITLED,
            "feed": feed,
            "api_message": api_message,
        },
    )


def date_out_of_range(date: str, available_from: str, last_update: str) -> PluginException:
    return PluginException(
        cause=f"Date {date} is outside the allowed range for this feed",
        assistance=(
            f"Allowed range is [{available_from}, {last_update}]. "
            "Pick a date between available_from and last_update for this feed, or omit the date input "
            "to start from the latest available date"
        ),
        data={
            "code": DATE_OUT_OF_RANGE,
            "date": date,
            "available_from": available_from,
            "last_update": last_update,
        },
    )


def status_unavailable(reason: str) -> PluginException:
    return PluginException(
        cause=f"Status endpoint is unavailable: {reason}",
        assistance=(
            "The WhoisFreaks status endpoint https://files.whoisfreaks.com/v3.4/status did not return a "
            "valid response. Check network connectivity from the plugin container, and verify the base_url "
            "connection input. The trigger will retry automatically on its next cycle"
        ),
        data={
            "code": STATUS_UNAVAILABLE,
            "reason": reason,
        },
    )


def rate_limited(feed: str) -> PluginException:
    return PluginException(
        cause=f"Rate limited while querying feed '{feed}'",
        assistance=(
            "The WhoisFreaks API returned HTTP 429. Reduce batch_size, increase poll_interval_minutes, "
            "or verify the API key has remaining credits. The trigger will retry automatically on its "
            "next cycle"
        ),
        data={
            "code": RATE_LIMITED,
            "feed": feed,
        },
    )


def partial_run(feed: str, reason: str) -> PluginException:
    return PluginException(
        cause=f"Partial run on feed '{feed}': {reason}",
        assistance=(
            "The current date was not fully ingested. The trigger will retry from offset 0 on its next "
            "cycle. Because delivery is at-least-once, duplicate events are possible for the rows already "
            "emitted. Deduplicate downstream on the domain field if exact-once is required"
        ),
        data={
            "code": PARTIAL_RUN,
            "feed": feed,
            "reason": reason,
        },
    )


def invalid_credentials(api_message: str) -> PluginException:
    return PluginException(
        cause=f"Invalid API credentials: {api_message}",
        assistance=(
            "Verify the api_key connection input. Confirm the WhoisFreaks account is active and the "
            "API key has remaining credits. A 401 response from any endpoint indicates the key is "
            "invalid, deactivated, or out of credits"
        ),
        data={
            "code": INVALID_CREDENTIALS,
            "api_message": api_message,
        },
    )


def invalid_date_format(date: str) -> PluginException:
    return PluginException(
        cause=f"Invalid date format: {date}",
        assistance=("The date input must be a valid calendar date in YYYY-MM-DD format. " "Example: 2026-09-14"),
        data={
            "code": INVALID_DATE_FORMAT,
            "date": date,
        },
    )
