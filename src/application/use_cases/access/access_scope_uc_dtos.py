# /src/application/use_cases/access/access_scope_uc_dtos.py

from dataclasses import dataclass

from src.domain.entities.person.tenant_entities import TenantProfile

# --- USE CASE

@dataclass(frozen=True)
class AccessScopeRequestDTO:
    user_id: str
    tenant_id: str


@dataclass(frozen=True, slots=True)
class AccessScopeResultDTO:
    resident_ids: tuple[str, ...]
    sensor_ids: tuple[str, ...]
    gateway_ids: tuple[str, ...]
    tenant_profile: TenantProfile
