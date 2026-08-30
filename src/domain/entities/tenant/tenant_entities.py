# tenant_entities.py

from dataclasses import dataclass

from src.domain.enums.tenant.tenant_enums import TenantTypeEnum


@dataclass(frozen=True)
class TenantProfile:
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
