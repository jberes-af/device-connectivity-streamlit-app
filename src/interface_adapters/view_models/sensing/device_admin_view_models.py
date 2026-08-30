# /src/interface_adapters/view_models/sensing/device_admin_view_models.py

from dataclasses import dataclass


@dataclass(frozen=True)
class DeviceSummaryViewModel:
    sensor_count: int
    gateway_count: int
    assigned_sensor_count: int
    unassigned_sensor_count: int


@dataclass(frozen=True)
class SensorOverviewRowViewModel:
    sensor_id: str
    sensor_type: str
    name: str
    location: str
    zone: str

    paired_gateway_id: str
    attached_user_count: int
    attached_users: str

    sensor_purpose: str

    firmware_version: str
    hardware_version: str

    install_date: str
    removed_date: str

    ownership_start_date: str
    ownership_end_date: str


@dataclass(frozen=True)
class GatewayOverviewRowViewModel:
    gateway_id: str

    attached_user_count: int
    attached_users: str

    paired_sensor_count: int
    paired_sensors: str

    firmware_version_mcu: str
    firmware_version_cellular: str
    hardware_version: str

    install_date: str
    removed_date: str

    ownership_start_date: str
    ownership_end_date: str


@dataclass(frozen=True)
class DevicesAdministrationViewModel:
    title: str

    summary: DeviceSummaryViewModel

    sensors: tuple[SensorOverviewRowViewModel, ...]
    gateways: tuple[GatewayOverviewRowViewModel, ...]
