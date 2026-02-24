"""
External API integration layer.
Stub for email, analytics, or third-party volleyball APIs.
"""
import logging
from django.conf import settings
import requests

logger = logging.getLogger(__name__)


def call_external_api(path: str, method: str = "GET", json_data: dict | None = None) -> dict | None:
    """Call configured external API. Returns JSON or None on failure."""
    base = (getattr(settings, "EXTERNAL_API_BASE_URL") or "").rstrip("/")
    if not base:
        logger.debug("EXTERNAL_API_BASE_URL not set, skipping external call")
        return None
    url = f"{base}/{path.lstrip('/')}"
    try:
        if method.upper() == "GET":
            r = requests.get(url, timeout=10)
        elif method.upper() == "POST":
            r = requests.post(url, json=json_data or {}, timeout=10)
        else:
            return None
        r.raise_for_status()
        return r.json() if r.content else {}
    except requests.RequestException as e:
        logger.warning("External API call failed: %s", e)
        return None
