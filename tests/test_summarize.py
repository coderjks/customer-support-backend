"""AI-003: LLM ticket summarization."""

import pytest


@pytest.mark.skip(reason="implement in AI-003")
def test_summary_structured_output(client):
    created = client.post("/tickets", json={"title": "t", "body": "b"}).json()
    res = client.post(f"/tickets/{created['id']}/summary")
    assert res.status_code == 200
    assert {"summary", "key_points"} <= set(res.json())
