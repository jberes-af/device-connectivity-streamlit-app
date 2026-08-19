# /src/domain/entities/person/resident_entities.py

from dataclasses import dataclass
from datetime import date

from src.domain.entities.person.tenant_entities import TenantProfile
from src.domain.enums.person.resident_enums import ResidentAccessLevelEnum


@dataclass(frozen=True)
class ResidentSensorLink:
    resident_id: str
    sensor_id: str
    tenant_id: str | None
    active_from_date: date | None = None
    active_to_date: date | None = None
    setup_date: date | None = None
    removed_date: date | None = None


@dataclass(frozen=True)
class ResidentGatewayLink:
    resident_id: str
    gateway_id: str
    tenant_id: str | None
    active_from_date: date | None = None
    active_to_date: date | None = None
    setup_date: date | None = None
    removed_date: date | None = None


@dataclass(frozen=True)
class UserResidentAccess:
    user_id: str
    tenant_id: str | None
    resident_id: str
    access_level: ResidentAccessLevelEnum
    granted_by_user_id: str
    granted_at_date: date
    active: bool | None


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
