"""Retrieval over the support knowledge base (AI-004).

Corpus lives in data/articles.json. Return top-k passages with
relevance scores; an empty query is a 422, never an exception.
"""

from __future__ import annotations

from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(tags=["retrieval"])


class Passage(BaseModel):
    article_id: str
    title: str
    score: float


class RetrievalOut(BaseModel):
    query: str
    passages: list[Passage] = Field(default_factory=list)


@router.get("/retrieval", response_model=RetrievalOut)
def retrieve(q: str = "", k: int = 3) -> RetrievalOut:
    # TODO(AI-004): index data/articles.json, score, return top-k.
    from fastapi import HTTPException

    raise HTTPException(status_code=501, detail="not implemented: AI-004")
