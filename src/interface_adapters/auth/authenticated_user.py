# /src/interface_adapters/google_sheets/authenticated_user.py

from dataclasses import dataclass


@dataclass(frozen=True)
class AuthenticatedUser:
    user_id: str
    email: str | None = None
    is_development_user: bool = False