# /src/domain/entities/contact/access_entities.py

from dataclasses import dataclass
from datetime import date

from src.domain.enums.person.resident_enums import ResidentAccessLevelEnum
from src.domain.enums.person.tenant_enums import UserRoleEnum, PermissionEnum


@dataclass(frozen=True)
class UserTenantMembership:
    user_id: str
    tenant_id: str
    role: UserRoleEnum
    is_active: bool = True


@dataclass(frozen=True)
class UserLoginCredentials:
    user_id: str
    user_login_id: str
    user_password: str


@dataclass(frozen=True)
class UserPermissionOverride:
    user_id: str
    tenant_id: str
    permission: PermissionEnum
    is_granted: bool


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
class ResidentSensorLink:
    resident_id: str
    sensor_id: str
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
