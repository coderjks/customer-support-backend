# Ticket map — one branch/PR per ticket

## PR naming convention (required)

The evaluation pipeline maps a PR to a ticket by the `AI-NNN` key in
the PR title, body, or branch name (case-insensitive, first match wins).

- Branch: `ai-001-ticket-api`
- PR title: `[AI-001] Ticket creation API`
- Body: mention the key again (e.g. `Implements AI-001.`)

A PR with no key is acknowledged and ignored — it never counts.

## Tickets

| Ticket | Title | Implement in | Acceptance |
|---|---|---|---|
| AI-001 | Ticket creation REST API | `app/tickets.py` (`create_ticket`) | `POST /tickets` validates title/body; 201 with persisted ticket; invalid payload 422 |
| AI-002 | Authorization on ticket access | `app/tickets.py` (`get_ticket`, `update_ticket`) + `app/auth.py` | Owner reads own ticket; non-owner gets 403/404; negative-access tests pass |
| AI-003 | LLM ticket summarization | `app/summarize.py` (+ wire into `app/main.py`) | Structured summary JSON; provider timeout → 502/503; no prompt/key leaks |
| AI-004 | Retrieval over knowledge base | `app/retrieval.py` (+ `data/articles.json`) | Top-k relevant passages; relevance fixture passes; empty query handled |
| AI-005 | Safe order lookup tool | `app/tools.py` | Permission checks; audit event per lookup; no cross-customer exposure |
| AI-006 | Evaluation and monitoring | `app/metrics.py` (+ `data/golden.json`), `GET /metrics` | Golden dataset evaluated; latency p50/p95; metrics from persisted evidence |

Dependencies: AI-002 and AI-003 need AI-001; AI-004 needs AI-003;
AI-005 needs AI-002; AI-006 needs AI-004. Open PRs in dependency
order so each evaluation runs against its prerequisites.
