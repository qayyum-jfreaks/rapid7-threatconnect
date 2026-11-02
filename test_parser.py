import requests
from icon_whoisfreaks.util.csv_parser import parse_csv

BASE = "http://localhost:8001"
H = {"X-API-KEY": "test"}


def check(name, fn):
    fn()
    print(f"OK {name}")


def whois_false_headerless():
    r = requests.get(f"{BASE}/v3.3/stream/domainer/gtld?date=2026-09-14&limit=3&offset=0&whois=false", headers=H)
    rows = parse_csv(r.content, has_header=False, offset=0)
    assert len(rows) == 3
    assert rows[0] == {"domain_name": "newly0-gtld.com"}
    assert rows[2] == {"domain_name": "newly2-gtld.com"}


def whois_false_offset_nonzero():
    r = requests.get(f"{BASE}/v3.3/stream/domainer/gtld?date=2026-09-14&limit=3&offset=3&whois=false", headers=H)
    rows = parse_csv(r.content, has_header=False, offset=3)
    assert rows[0] == {"domain_name": "newly3-gtld.com"}


def whois_true_offset_zero():
    r = requests.get(f"{BASE}/v3.3/stream/domainer/gtld?date=2026-09-14&limit=3&offset=0&whois=true", headers=H)
    rows = parse_csv(r.content, has_header=True, offset=0)
    assert rows[0]["num"] == "1"
    assert rows[0]["domain_name"] == "sample0-gtld.com"
    assert rows[0]["name_server_1"] == "ns1.example.com"


def whois_true_offset_nonzero():
    r = requests.get(f"{BASE}/v3.3/stream/domainer/gtld?date=2026-09-14&limit=3&offset=5&whois=true", headers=H)
    rows = parse_csv(r.content, has_header=True, offset=5)
    assert rows[0]["num"] == "6"
    assert rows[0]["domain_name"] == "sample5-gtld.com"
    assert rows[0]["name_server_1"] == "ns1.example.com"


def threat_quoted_commas():
    r = requests.get(f"{BASE}/v3.4/stream/threat-feed/phishing?date=2026-10-12&limit=3&offset=0", headers=H)
    rows = parse_csv(r.content, has_header=True, offset=0)
    assert rows[0]["domain"] == "tricky0.com"
    assert rows[0]["matched_pivots"] == "email:a@b.com | org:Example, Inc."


def threat_bool_coercion():
    r = requests.get(f"{BASE}/v3.4/stream/threat-feed/phishing?date=2026-10-12&limit=3&offset=0", headers=H)
    rows = parse_csv(r.content, has_header=True, offset=0)
    assert rows[0]["is_seed"] is True
    assert rows[0]["is_extrapolated"] is False
    assert rows[0]["is_dropped"] is False
    # is_parked is empty in the fixture must stay empty, NOT become False
    assert rows[0]["is_parked"] == ""


def threat_timestamp():
    r = requests.get(f"{BASE}/v3.4/stream/threat-feed/phishing?date=2026-10-12&limit=3&offset=0", headers=H)
    rows = parse_csv(r.content, has_header=True, offset=0)
    assert rows[0]["first_seen"].startswith("2026-10-01T00:16:16")
    assert rows[0]["first_seen"].endswith("+00:00")


def empty_body():
    assert parse_csv(b"", has_header=True, offset=0) == []
    assert parse_csv(b"   \n  \n", has_header=True, offset=0) == []


def bom_stripped():
    bom_content = b"\xef\xbb\xbfdomain,threat_type\nx.com,phishing\n"
    rows = parse_csv(bom_content, has_header=True, offset=0)
    assert rows == [{"domain": "x.com", "threat_type": "phishing"}]


def redacted_preserved():
    r = requests.get(f"{BASE}/v3.3/stream/domainer/gtld?date=2026-09-14&limit=1&offset=1&whois=true", headers=H)
    rows = parse_csv(r.content, has_header=True, offset=1)
    assert rows[0]["registrant_email"] == "REDACTED FOR PRIVACY"
    assert rows[0]["registrant_email"] != "N/A"
    assert rows[0]["registrant_email"] != ""


if __name__ == "__main__":
    check("whois=false headerless", whois_false_headerless)
    check("whois=false offset>0 headerless", whois_false_offset_nonzero)
    check("whois=true offset=0 header dropped", whois_true_offset_zero)
    check("whois=true offset>0 header still dropped", whois_true_offset_nonzero)
    check("threat feed quoted commas preserved", threat_quoted_commas)
    check("bool coercion", threat_bool_coercion)
    check("timestamp normalization", threat_timestamp)
    check("empty body", empty_body)
    check("BOM stripped", bom_stripped)
    check("REDACTED preserved", redacted_preserved)
    print("ALL PASS")
