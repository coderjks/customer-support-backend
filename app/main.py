"""Assemble the FastAPI app. New ticket routers register here."""

from __future__ import annotations

from fastapi import FastAPI

from app import metrics, retrieval, summarize, tickets, tools
from app.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Customer Support Backend (starter)")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


app.include_router(tickets.router)
app.include_router(summarize.router)
app.include_router(retrieval.router)
app.include_router(tools.router)
app.include_router(metrics.router)
