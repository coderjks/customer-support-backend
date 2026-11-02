"""Ticket endpoints.

AI-001: implement create_ticket (POST /tickets, 201 + persisted row,
invalid payload -> 422 via schema validation).
AI-002: implement get_ticket / update_ticket with ownership checks
(non-owner -> 403 or 404) and add the auth dependency in app/auth.py.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Ticket
from app.schemas import TicketCreate, TicketOut

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.post("", response_model=TicketOut, status_code=201)
def create_ticket(payload: TicketCreate, db: Session = Depends(get_db)) -> TicketOut:
    # TODO(AI-001): persist and return the created ticket.
    raise HTTPException(status_code=501, detail="not implemented: AI-001")


@router.get("/{ticket_id}", response_model=TicketOut)
def get_ticket(ticket_id: str, db: Session = Depends(get_db)) -> TicketOut:
    # TODO(AI-002): owner-only read; non-owner -> 403 or 404.
    raise HTTPException(status_code=501, detail="not implemented: AI-002")


@router.patch("/{ticket_id}", response_model=TicketOut)
def update_ticket(ticket_id: str, payload: TicketCreate, db: Session = Depends(get_db)) -> TicketOut:
    # TODO(AI-002): owner-only update; non-owner -> 403 or 404.
    raise HTTPException(status_code=501, detail="not implemented: AI-002")
