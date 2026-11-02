"""AI-005: safe order lookup tool."""

import pytest


@pytest.mark.skip(reason="implement in AI-005")
def test_lookup_denied_without_permission(client):
    res = client.get("/tools/orders/ord-1")
    assert res.status_code in (401, 403)
