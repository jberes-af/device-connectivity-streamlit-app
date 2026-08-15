# /src/domain/entities/person/resident_entities.py

from dataclasses import dataclass

from src.domain.entities.person.tenant_entities import TenantProfile
from src.domain.enums.person.resident_enums import ResidentAccessLevelEnum


@dataclass(frozen=True)
class ResidentSensorLink:
    resident_id: str
    sensor_id: str
    tenant_id: str | None
    active_from_iso: str | None = None
    active_to_iso: str | None = None


@dataclass(frozen=True)
class ResidentGatewayLink:
    resident_id: str
    gateway_id: str
    tenant_id: str | None
    active_from_iso: str | None = None
    active_to_iso: str | None = None


@dataclass(frozen=True)
class ResidentContactInformation:
    resident_id: str
    resident_name: str
    primary_contact_name: str
    primary_contact_email: str
    primary_contact_telephone: str
    primary_contact_address: str


@dataclass(frozen=True)
class UserResidentAccess:
    user_id: str
    tenant_id: str | None
    resident_id: str
    access_level: ResidentAccessLevelEnum
    granted_by_user_id: str
    granted_at_iso: str
    active: bool | None


@dataclass(frozen=True)
class ResidentProfile:
    resident_id: str
    tenant_id: str | None
    name: str
    preferred_name: str
    contact_information: ResidentContactInformation
    tenant_facility_profile: TenantProfile
    room_reference: str | None = None
    active_status: bool = True
