# /src/application/use_cases/sensing/sensing_admin/device_admin_uc_dtos.py

from dataclasses import dataclass
from datetime import date

from src.domain.enums.sensing.device_enums import (
    SensorPurposeEnum,
)

from src.domain.enums.sensing.device_enums import (
    SensorTypeEnum,
)


@dataclass(frozen=True)
class SensorProfileDTO:
    sensor_id: str
    sensor_type: SensorTypeEnum
    tenant_id: str | None = None
    name: str | None = None
    location: str | None = None
    zone: str | None = None
    firmware_version: str | None = None
    hardware_version: str | None = None
    paired_gateway_id: str | None = None
    attached_user_ids: tuple[str, ...] = ()
    attached_adl_names: tuple[str, ...] = ()
    used_in_routine_ids: tuple[str, ...] = ()
    sensor_purpose: SensorPurposeEnum | None = None
    install_date: date | None = None
    removed_date: date | None = None
    owned_from_date: date | None = None
    owned_to_date: date | None = None


@dataclass(frozen=True)
class GatewayProfileDTO:
    gateway_id: str
    tenant_id: str | None = None
    attached_user_ids: tuple[str, ...] = ()
    paired_sensor_ids: tuple[str, ...] = ()
    firmware_version_mcu: str | None = None
    firmware_version_cellular: str | None = None
    hardware_version: str | None = None
    install_date: date | None = None
    removed_date: date | None = None
    owned_from_date: date | None = None
    owned_to_date: date | None = None


@dataclass(frozen=True)
class GetDevicesAdministrationRequestDTO:
    tenant_ids: tuple[str, ...]


@dataclass(frozen=True)
class GetDeviceAdministrationResultDTO:
    sensor_profiles: tuple[SensorProfileDTO, ...]
    gateway_profiles: tuple[GatewayProfileDTO, ...]
