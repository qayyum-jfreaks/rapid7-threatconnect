import os

os.environ.setdefault("WHOISFREAKS_BASE_URL", "http://localhost:8001")

from icon_whoisfreaks.util.http_client import stream_request, probe_entitlement

KEY = "test"
NRD_PATH = "/v3.3/stream/domainer/gtld"
THREAT_PATH = "/v3.4/stream/threat-feed/phishing"

BASE_NRD_PARAMS = {"date": "2026-09-14", "limit": "1", "offset": "0", "whois": "false"}
BASE_THREAT_PARAMS = {"date": "2026-10-12", "limit": "1", "offset": "0"}


def check(name, fn):
    fn()
    print(f"OK {name}")


def stream_request_returns_response():
    resp = stream_request(NRD_PATH, BASE_NRD_PARAMS, KEY)
    assert resp.status_code == 200
    assert resp.content
    assert resp.headers["content-type"].startswith("text/plain")


def probe_ok():
    kind, msg = probe_entitlement(NRD_PATH, BASE_NRD_PARAMS, KEY)
    assert kind == "ok" and msg is None


def probe_empty():
    params = dict(BASE_NRD_PARAMS)
    params["force"] = "empty"
    kind, msg = probe_entitlement(NRD_PATH, params, KEY)
    assert kind == "empty" and msg is None


def probe_not_entitled():
    params = dict(BASE_NRD_PARAMS)
    params["auth"] = "fail"
    kind, msg = probe_entitlement(NRD_PATH, params, KEY)
    assert kind == "not_entitled"
    assert msg == "Please buy domainer package."


def probe_global_auth_fail():
    params = dict(BASE_NRD_PARAMS)
    params["auth"] = "global_fail"
    kind, msg = probe_entitlement(NRD_PATH, params, KEY)
    assert kind == "not_entitled"
    assert msg == "Provided API key is invalid"


def probe_server_error():
    params = dict(BASE_NRD_PARAMS)
    params["force"] = "503"
    kind, msg = probe_entitlement(NRD_PATH, params, KEY)
    assert kind == "server_error"
    assert msg == 503


def probe_client_error_bad_date():
    params = dict(BASE_NRD_PARAMS)
    params["force"] = "bad_date"
    kind, msg = probe_entitlement(NRD_PATH, params, KEY)
    assert kind == "client_error"
    assert "HTTP 400" in msg


def probe_network_error():
    os.environ["WHOISFREAKS_BASE_URL"] = "http://localhost:9999"
    try:
        kind, msg = probe_entitlement(NRD_PATH, BASE_NRD_PARAMS, KEY)
    finally:
        os.environ["WHOISFREAKS_BASE_URL"] = "http://localhost:8001"
    assert kind == "network_error"
    assert msg


def probe_threat_ok():
    kind, msg = probe_entitlement(THREAT_PATH, BASE_THREAT_PARAMS, KEY)
    assert kind == "ok" and msg is None


if __name__ == "__main__":
    check("stream_request returns 200 with text/plain", stream_request_returns_response)
    check("probe ok", probe_ok)
    check("probe empty", probe_empty)
    check("probe not_entitled", probe_not_entitled)
    check("probe global_auth_fail (still 401)", probe_global_auth_fail)
    check("probe server_error 503", probe_server_error)
    check("probe client_error 400", probe_client_error_bad_date)
    check("probe network_error", probe_network_error)
    check("probe threat ok", probe_threat_ok)
    print("ALL PASS")
