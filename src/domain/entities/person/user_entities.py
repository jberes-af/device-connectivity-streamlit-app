# /src/domain/entities/person/user_entities.py

from dataclasses import dataclass

from src.domain.enums.person.tenant_enums import (
    PermissionEnum,
    UserRoleEnum,
)

from src.domain.enums.care.adl_enums import AdlCategorySensorLinkEnum


@dataclass(frozen=True)
class UserProfile:
    user_id: str
    user_name: str
    user_telephone: str
    user_email_address: str
    user_image: str
    color_scheme: str


@dataclass(frozen=True)
class UserAccount:
    user_id: str
    user_profile: UserProfile


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
class UserResidentAccess:
    tenant_id: str
    user_id: str
    resident_id: str


@dataclass(frozen=True)
class UserSensorLink:
    tenant_id: str
    user_id: str
    sensor_id: str


@dataclass(frozen=True)
class UserGatewayLink:
    tenant_id: str
    user_id: str
    gateway_id: str


@dataclass(slots=True)
class SensorUserProfile:
    sensor_id: str
    name: str = ""
    location: str = ""
    zone: str = ""
    image: str | None = None
    exists: bool = False


@dataclass(frozen=True)
class UserAdlSensorLink:
    user_id: str
    activity: AdlCategorySensorLinkEnum
    sensor_id: str


@dataclass(frozen=True)
class UserAlertaRoutineLink:
    user_id: str
    routine_id: str


"""
@dataclass(frozen=True)
class UserSettingsDTO:
    notifications: UserNotificationSettingEnum
    units_of_measure: UserUoMSettingEnum
"""
