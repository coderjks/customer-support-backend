"""Pydantic schemas for ticket I/O."""

from __future__ import annotations

import datetime as dt

from pydantic import BaseModel, Field


class TicketCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    body: str = Field(min_length=1)


class TicketOut(BaseModel):
    id: str
    title: str
    body: str
    created_at: dt.datetime
    updated_at: dt.datetime
