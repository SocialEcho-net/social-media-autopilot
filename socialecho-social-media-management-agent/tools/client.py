from __future__ import annotations

from typing import Any

import requests

PRODUCTION_BASE_URL = "https://api.socialecho.net"
SUCCESS_CODES = {0, 200}


def _build_headers(credentials: dict[str, Any]) -> dict[str, str]:
    api_key = str(credentials.get("api_key", "")).strip()
    if not api_key:
        raise ValueError("Missing required credential: api_key")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    x_lang = str(credentials.get("x_lang", "")).strip()
    if x_lang:
        headers["X-Lang"] = x_lang

    return headers


def request_socialecho(
    credentials: dict[str, Any],
    path: str,
    body: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    Call SocialEcho external API.

    Most v1 routes use **GET** with a **JSON body** (not query string), per:
    `socialEchoApidocs_cn.md` / help-center OpenAPI.
    """
    base_url = PRODUCTION_BASE_URL.rstrip("/")
    clean = {k: v for k, v in (body or {}).items() if v is not None}

    response = requests.get(
        url=f"{base_url}{path}",
        json=clean,
        headers=_build_headers(credentials),
        timeout=30,
    )

    try:
        payload: Any = response.json()
    except Exception as e:
        raise ValueError(
            f"Invalid JSON response. HTTP {response.status_code}, body={response.text[:500]}"
        ) from e

    if response.status_code != 200:
        raise ValueError(f"HTTP {response.status_code} error: {payload}")

    if not isinstance(payload, dict):
        raise ValueError(f"Unexpected response body type: {type(payload)}")

    code = payload.get("code")
    if code not in SUCCESS_CODES:
        raise ValueError(
            f"Business error: code={payload.get('code')}, message={payload.get('message')}"
        )

    return payload


def parse_account_ids_csv(raw: str | None) -> list[int] | None:
    """Turn CSV '1,2,3' into [1, 2, 3]. Empty/whitespace -> None (omit field)."""
    if raw is None:
        return None
    s = str(raw).strip()
    if not s:
        return None
    out: list[int] = []
    for part in s.split(","):
        p = part.strip()
        if not p:
            continue
        out.append(int(p))
    return out or None
