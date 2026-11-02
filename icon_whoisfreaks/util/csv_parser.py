import csv
import io
from datetime import datetime

BOOL_FIELDS = {"is_seed", "is_extrapolated", "is_dropped", "is_parked"}
TIMESTAMP_FIELDS = {"first_seen", "last_seen", "query_time", "create_date", "update_date", "expiry_date"}


def parse_csv(content: bytes, has_header: bool, offset: int) -> list[dict]:
    """Parse a WhoisFreaks CSV page into a list of typed dictionaries.

    Args:
        content: raw response body bytes from requests
        has_header: True if every page of this feed includes a header row
        offset: current offset (for logging only; header is dropped on every
                page when has_header=True, regardless of offset)

    Returns:
        List of dicts, one per data row, with bool and timestamp fields coerced.

    Notes:
        - whois=false NRD pages have NO header on any page (has_header=False)
        - whois=true NRD and all threat feed pages have a header on EVERY page
          (has_header=True), including offset>0 pages so the header must be
          dropped on every page, not just the first.
        - csv.reader handles quoted commas and embedded newlines correctly;
          split(",") or iter_lines() will corrupt these rows.
        - utf-8-sig strips the BOM if present.
    """
    if not content:
        return []

    text = content.decode("utf-8-sig")
    if not text.strip():
        return []

    reader = csv.reader(io.StringIO(text))
    raw_rows = [row for row in reader if row]
    if not raw_rows:
        return []

    if has_header:
        header = raw_rows[0]
        data_rows = raw_rows[1:]
    else:
        header = ["domain_name"]
        data_rows = raw_rows

    result: list[dict] = []
    for raw_row in data_rows:
        # Pad short rows, truncate long rows so zip aligns with header
        if len(raw_row) < len(header):
            raw_row = raw_row + [""] * (len(header) - len(raw_row))
        elif len(raw_row) > len(header):
            raw_row = raw_row[: len(header)]

        row_dict = dict(zip(header, raw_row))
        _coerce(row_dict)
        result.append(row_dict)

    return result


def _coerce(row: dict) -> None:
    """In-place type coercion for known boolean and timestamp fields.

    Non-coercible values are preserved verbatim ("", "N/A",
    "REDACTED FOR PRIVACY" remain distinct).
    """
    for key, value in row.items():
        if key in BOOL_FIELDS and isinstance(value, str):
            lowered = value.strip().lower()
            if lowered == "t":
                row[key] = True
            elif lowered == "f":
                row[key] = False
        elif key in TIMESTAMP_FIELDS and isinstance(value, str) and value.strip():
            stripped = value.strip()
            if stripped.endswith("+00"):
                try:
                    row[key] = datetime.fromisoformat(stripped[:-3] + "+00:00").isoformat()
                except ValueError:
                    # Preserve verbatim if not parseable
                    pass
