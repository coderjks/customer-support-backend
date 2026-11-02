"""AI-002: authorization on ticket access."""

import pytest


@pytest.mark.skip(reason="implement in AI-002")
def test_owner_can_read_own_ticket(client):
    created = client.post("/tickets", json={"title": "t", "body": "b"}).json()
    assert client.get(f"/tickets/{created['id']}").status_code == 200


@pytest.mark.skip(reason="implement in AI-002")
def test_non_owner_denied(client):
    created = client.post("/tickets", json={"title": "t", "body": "b"}).json()
    res = client.get(f"/tickets/{created['id']}", headers={"X-User-Id": "someone-else"})
    assert res.status_code in (403, 404)
