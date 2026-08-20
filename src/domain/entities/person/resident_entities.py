# /src/domain/entities/person/resident_entities.py

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class ResidentContactInformation:
    resident_id: str
    # resident_name: str
    contact_name: str
    contact_email: str
    contact_telephone: str
    contact_address: str


@dataclass(frozen=True)
class ResidentProfile:
    resident_id: str
    tenant_id: str | None
    full_name: str
    preferred_name: str
    # contact_info: ResidentContactInformation
    date_of_birth: date | None
    # tenant_facility_profile: TenantProfile
    room_reference: str | None = None
    active_status: bool = True
