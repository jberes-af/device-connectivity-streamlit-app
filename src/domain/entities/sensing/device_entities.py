# /src/domain/entities/sensing/device_entities.py

from dataclasses import dataclass
from datetime import date, datetime

from src.domain.enums.sensing.notification_enums import (
    NotificationMessageStatusEnum)

from src.domain.enums.sensing.device_enums import (
    DeviceTypeEnum,
    SensorPurposeEnum,
)

from src.domain.enums.sensing.device_enums import (
    SensorTypeEnum,
    SensorStateDefinitionEnum,
)


# --- GENERAL

@dataclass(frozen=True)
class DeviceAdministrationProfile:
    device_id: str
    device_type: DeviceTypeEnum
    tenant_id: str
    sensor_purpose: SensorPurposeEnum | None = None
    install_date: date | None = None
    removed_date: date | None = None
    owned_from_date: date | None = None
    owned_to_date: date | None = None
    hardware_version: str | None = None
    firmware_version_sensor: str | None = None
    firmware_version_gateway: str | None = None
    firmware_version_cellular: str | None = None


"""
@dataclass(frozen=True)
class DeviceOwnership:
    device_id: str
    device_type: str
    owned_from_iso: str
    ownership_id: str
    tenant_id: str
    owned_to_iso: str | None = None
"""


# --- GATEWAY

@dataclass(frozen=True)
class GatewayProfile:
    gateway_id: str
    tenant_id: str | None = None
    timezone: str | None = None
    firmware_version_mcu: str | None = None
    firmware_version_cellular: str | None = None
    hardware_version: str | None = None


@dataclass(frozen=True)
class GatewayHealth:
    gateway_id: str
    tenant_id: str
    is_online: bool
    last_seen_at: str | None = None
    signal_strength: float | None = None


# --- SENSORS


@dataclass(frozen=True)
class SensorSystemProfile:
    brand: str
    sensor_id: str
    sensor_type: SensorTypeEnum
    tenant_id: str | None = None
    firmware_version: str | None = None
    hardware_version: str | None = None
    icon: str | None = None


@dataclass(frozen=True)
class SensorStateDefinition:
    definition: str
    display_name: str
    numeric_code: str


@dataclass(frozen=True)
class SensorGroup:
    group_id: str
    tenant_id: str
    sensor_ids: tuple[str, ...]
    name: str | None = None
    color: str | None = None
    image: str | None = None


@dataclass(frozen=True)
class SensorLiveState:
    current_state: SensorStateDefinitionEnum
    last_updated_at: str
    sensor_id: str
    tenant_id: str


@dataclass(frozen=True)
class SensorHealth:
    sensor_id: str
    tenant_id: str
    is_online: bool
    battery_level: float | None = None
    last_seen_at: str | None = None
    signal_strength: float | None = None


@dataclass(frozen=True)
class SensorEvent:
    sensor_id: str
    sensor_state: SensorStateDefinitionEnum
    activated_at_utc: datetime  # UTC
    event_id: str | None = None


@dataclass(frozen=True)
class SensorEventNotificationMessage:
    tenant_id: str
    channel: str
    created_at: str
    message: str
    notification_id: str
    recipient_user_id: str
    source_event_type: str
    status: NotificationMessageStatusEnum
    title: str
    read_at: str | None = None
    sent_at: str | None = None
    source_event_id: str | None = None


# --- ASSOCIATIONS

@dataclass(frozen=True)
class GatewaySensorLink:
    gateway_id: str
    sensor_id: str


@dataclass(frozen=True)
class MovementDTO:
    sensor_end: str
    sensor_start: str
    time_end: str
    time_start: str
