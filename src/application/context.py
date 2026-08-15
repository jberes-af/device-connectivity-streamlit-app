# /src/application/context.py

from dataclasses import dataclass

from src.domain.enums.person.tenant_enums import UserRoleEnum

@dataclass(frozen=True)
class UserContext:
    user_id: str
    tenant_id: str
    role: UserRoleEnum



@dataclass
class SessionContext:
    user_context: UserContext | None = None

    @property
    def is_authenticated(self) -> bool:
        return self.user_context is not None