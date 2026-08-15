# device_entities.py

from dataclasses import dataclass

from src.domain.enums.sensing.notification_enums import NotificationMessageStatusEnum
from src.domain.enums.sensing.device_enums import SensorStateDefinitionEnum

from src.domain.entities.person.user_entities import SensorUserProfile


# --- GENERAL

@dataclass(frozen=True)
class DeviceOwnershipDTO:
    device_id: str
    device_type: str
    owned_from_iso: str
    ownership_id: str
    tenant_id: str
    owned_to_iso: str | None = None


# --- GATEWAY

@dataclass(frozen=True)
class GatewayProfileDTO:
    gateway_id: str
    tenant_id: str | None = None
    timezone: str | None = None
    firmware_version: str | None = None
    hardware_version: str | None = None
    last_seen_at_iso: str | None = None
    is_online: bool = False


# --- SENSORS


@dataclass(frozen=True)
class SensorSystemProfile:
    brand: str
    sensor_id: str
    sensor_type: str
    firmware_version: str | None = None
    hardware_version: str | None = None
    icon: str | None = None


@dataclass(frozen=True)
class SensorProfile:
    sensor_id: str
    system_configuration: SensorSystemProfile
    state: SensorStateDefinitionEnum | None = None
    tenant_id: str | None = None
    user_configuration: SensorUserProfile | None = None


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
    install_date: str | None = None
    last_seen_at: str | None = None
    signal_strength: float | None = None


@dataclass(frozen=True)
class SensorEvent:
    current_state: SensorStateDefinitionEnum
    event_id: str
    sensor_id: str
    tenant_id: str
    timestamp: str


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
    sensor_end: SensorProfile
    sensor_start: SensorProfile
    time_end: str
    time_start: str
