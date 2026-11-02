"""Safe order lookup tool (AI-005).

Every lookup must check caller permission, validate input, record an
audit event, and never return another customer's orders.
"""

from __future__ import annotations

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["tools"])

AUDIT_LOG: list[dict] = []


class OrderLookupOut(BaseModel):
    order_id: str
    status: str


@router.get("/tools/orders/{order_id}", response_model=OrderLookupOut)
def lookup_order(order_id: str) -> OrderLookupOut:
    # TODO(AI-005): permission check + validation + audit event.
    from fastapi import HTTPException

    raise HTTPException(status_code=501, detail="not implemented: AI-005")
