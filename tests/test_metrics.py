"""AI-006: evaluation and monitoring."""

import pytest


@pytest.mark.skip(reason="implement in AI-006")
def test_metrics_reports_golden_and_latency(client):
    res = client.get("/metrics")
    assert res.status_code == 200
    data = res.json()
    assert data["golden_total"] > 0
    assert data["latency_p95_ms"] >= data["latency_p50_ms"] >= 0
