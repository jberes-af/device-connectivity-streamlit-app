# src/application/google_sheets/ports.py

from typing import Protocol

from src.application.auth.dto import AuthenticatedUserDTO


class AuthProvider(Protocol):
    def authenticate(self, email: str, password: str) -> AuthenticatedUserDTO:
        ...
