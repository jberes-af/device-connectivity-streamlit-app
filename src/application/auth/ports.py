# src/application/auth/ports.py

from typing import Protocol

from src.application.auth.dto import AuthenticatedUserDTO


class AuthenticationPort(Protocol):
    def authenticate(
            self,
            email: str,
            password: str) -> AuthenticatedUserDTO:
        ...
