"""AI-001: ticket creation REST API."""

import pytest


def test_health(client):
    assert client.get("/health").json() == {"status": "ok"}


@pytest.mark.skip(reason="implement in AI-001")
def test_create_ticket_returns_201(client):
    res = client.post("/tickets", json={"title": "Login fails", "body": "SSO loop since Tuesday"})
    assert res.status_code == 201
    data = res.json()
    assert data["id"] and data["created_at"]


@pytest.mark.skip(reason="implement in AI-001")
def test_create_ticket_rejects_invalid_payload(client):
    assert client.post("/tickets", json={"title": "", "body": ""}).status_code == 422
