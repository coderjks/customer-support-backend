"""LLM ticket summarization behind a typed interface (AI-003).

Rules: structured JSON output only; provider timeouts degrade to
502/503; never include prompts, keys, or raw provider errors in
responses.
"""

from __future__ import annotations

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["summarization"])


class SummaryOut(BaseModel):
    ticket_id: str
    summary: str
    key_points: list[str]


class Summarizer:
    """Typed LLM boundary. AI-003 provides a real implementation."""

    def summarize(self, title: str, body: str) -> SummaryOut:  # pragma: no cover
        raise NotImplementedError("not implemented: AI-003")


@router.post("/tickets/{ticket_id}/summary", response_model=SummaryOut)
def summarize_ticket(ticket_id: str) -> SummaryOut:
    # TODO(AI-003): load the ticket, call Summarizer, map failures to 502/503.
    from fastapi import HTTPException

    raise HTTPException(status_code=501, detail="not implemented: AI-003")
