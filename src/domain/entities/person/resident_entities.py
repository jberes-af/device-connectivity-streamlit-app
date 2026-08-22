# /src/domain/entities/person/resident_entities.py

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class ResidentProfile:
    resident_id: str
    tenant_id: str | None
    full_name: str
    preferred_name: str
    # contact_info: ResidentContactInformation
    date_of_birth: date | None
    # tenant_facility_profile: TenantProfile
    telephone: str | None
    email: str | None
    address_line_1: str | None
    address_line_2: str | None
    city: str | None
    state: str | None
    postal_code: str | None
    room_reference: str | None = None
    active_status: bool = True


@dataclass(frozen=True)
class ResidentInCaseOfNeedContact:
    resident_id: str
    # resident_name: str
    contact_name: str
    contact_email: str
    contact_telephone: str
    contact_address: str
    contact_relationship: str
