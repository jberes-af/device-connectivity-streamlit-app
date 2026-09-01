# /src/application/use_cases/tenant/tenant_profiles_uc_dtos.py

from dataclasses import dataclass

from src.domain.enums.tenant.tenant_enums import TenantTypeEnum


@dataclass(frozen=True)
class TenantProfileDTO:
    tenant_id: str
    tenant_name: str
    tenant_type: TenantTypeEnum
    tenant_street: str
    tenant_city: str
    tenant_state: str
    tenant_postal_code: str
    tenant_telephone: str
    tenant_manager: str
    timezone: str | None = None


"""
@dataclass(frozen=True)
class GetTenantProfilesRequestDTO:
    tenant_id: str | None = None
"""


@dataclass(frozen=True)
class GetTenantProfilesResultDTO:
    tenant_profiles: tuple[TenantProfileDTO, ...]
