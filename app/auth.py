"""Request identity stub.

AI-002: replace this with real authentication (e.g. JWT) and use it
in the ticket routes for ownership checks.
"""


def get_current_user_id() -> str:
    # TODO(AI-002): authenticate the caller; never trust a client header.
    raise NotImplementedError("not implemented: AI-002")
