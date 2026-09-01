# /src/interface_adapters/view_models/sensing/device_admin_view_models.py

from dataclasses import dataclass

from src.domain.enums.tenant.tenant_enums import TenantTypeEnum


@dataclass(frozen=True)
class SensingSummaryViewModel:
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
class TenantOptionViewModel:
    tenant_id: str
    tenant_name: str
    tenant_name_label: str
    # tenant_type: TenantTypeEnum
    # tenant_street: str
    # tenant_city: str
    # tenant_state: str
    # tenant_postal_code: str
    # tenant_display_state_zip: str
    # tenant_telephone: str
    # tenant_manager: str
    # timezone: str | None = None


@dataclass(frozen=True)
class SensingAdministrationViewModel:
    title: str
    tenants: tuple[TenantOptionViewModel, ...]
    selected_tenant_name: str | None
    summary: SensingSummaryViewModel
    sensors: tuple[SensorOverviewRowViewModel, ...]
    gateways: tuple[GatewayOverviewRowViewModel, ...]
