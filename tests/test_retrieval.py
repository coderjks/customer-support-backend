"""AI-004: retrieval over the knowledge base."""

import pytest


@pytest.mark.skip(reason="implement in AI-004")
def test_retrieval_returns_ranked_passages(client):
    res = client.get("/retrieval", params={"q": "reset my password", "k": 2})
    assert res.status_code == 200
    assert len(res.json()["passages"]) <= 2


@pytest.mark.skip(reason="implement in AI-004")
def test_retrieval_rejects_empty_query(client):
    assert client.get("/retrieval", params={"q": ""}).status_code == 422
