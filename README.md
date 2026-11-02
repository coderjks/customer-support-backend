# AI-Powered Customer Support Backend (starter)

Sprint starter repo for the DevSpace AI Applied AI Engineering project
(Sprint 1 — Support Backend Foundations, tickets AI-001 through AI-006).

Endpoints start as documented stubs. Implement one ticket per
branch/PR; see [TICKETS.md](./TICKETS.md) for the ticket-to-file map
and the PR naming convention.

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8100
```

Health: http://localhost:8100/health — API docs: http://localhost:8100/docs

Postgres (optional; SQLite is the default):

```bash
DATABASE_URL=postgresql+psycopg://devspace:devspace@localhost:5432/support \
  uvicorn app.main:app --reload --port 8100
```

## Tests

```bash
pytest -q
```

Skipped tests mark work for later tickets — implement the ticket to
unskip them. Do not commit secrets; the evaluation pipeline fails any
diff containing secret patterns.
