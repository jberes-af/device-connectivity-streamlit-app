# /src/application/use_cases/access/access_scope_uc_dtos.py

from dataclasses import dataclass

from src.application.context import AccessScope


@dataclass(frozen=True, slots=True)
class BuildAccessScopeRequestDTO:
    user_id: str
    tenant_id: str


@dataclass(frozen=True, slots=True)
class BuildAccessScopeResultDTO:
    access_scope: AccessScope
