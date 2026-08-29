# /src/domain/entities/contact/user_sensing_entities.py

from dataclasses import dataclass
from typing import Mapping

from src.domain.enums.care.adl_enums import AdlCategorySensorLinkEnum


@dataclass(frozen=True)
class UserSensingAccount:
    user_id: str
    user_name: str
    telephone: str
    email_address: str


@dataclass(frozen=True)
class UserSensorLink:
    user_id: str
    sensor_id: str


@dataclass(frozen=True)
class UserGatewayLink:
    user_id: str
    gateway_id: str


@dataclass(slots=True)
class UserSensorProfile:
    sensor_id: str
    name: str = ""
    location: str = ""
    zone: str = ""
    # image: str | None = None
    # exists: bool = False


@dataclass(frozen=True)
class UserAdlSensorLink:
    user_id: str
    activity: Mapping[AdlCategorySensorLinkEnum, tuple[str, ...]]  # activity_name: sensor_id


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
