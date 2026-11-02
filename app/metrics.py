"""Evaluation + monitoring endpoint (AI-006).

GET /metrics evaluates data/golden.json, reports quality counts and
latency p50/p95 derived from persisted evidence (no invented numbers).
"""

from __future__ import annotations

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["monitoring"])


class MetricsOut(BaseModel):
    golden_total: int
    golden_passed: int
    latency_p50_ms: float
    latency_p95_ms: float


@router.get("/metrics", response_model=MetricsOut)
def get_metrics() -> MetricsOut:
    # TODO(AI-006): run the golden dataset, compute real latency stats.
    from fastapi import HTTPException

    raise HTTPException(status_code=501, detail="not implemented: AI-006")
