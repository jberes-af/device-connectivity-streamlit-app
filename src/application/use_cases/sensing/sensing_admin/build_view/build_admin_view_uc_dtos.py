# /src/application/use_cases/sensing/sensing_admin/build_view/build_admin_view_uc_dtos.py

from dataclasses import dataclass

from src.application.use_cases.tenant.tenant_profiles_uc_dtos import (
    TenantProfileDTO
)

from src.application.use_cases.sensing.sensing_admin.admin_profiles.device_admin_uc_dtos import (
    GatewayProfileDTO,
    SensorProfileDTO,
)

from src.application.use_cases.sensing.live_status.sensor_connectivity_uc_dtos import (
    SensorLastSeenDTO,
    MostRecentSensorEventDTO,
)

@dataclass(frozen=True)
class BuildSensingAdminViewRequestDTO:
    selected_tenant_name: str | None = None


@dataclass(frozen=True)
class BuildSensingAdminViewResultDTO:
    tenant_profiles: tuple[TenantProfileDTO, ...]
    selected_tenant_id: str | None
    selected_tenant_name: str | None
    sensor_profiles: tuple[SensorProfileDTO, ...]
    gateway_profiles: tuple[GatewayProfileDTO, ...]
    sensor_online_statuses: tuple[SensorLastSeenDTO, ...]
    most_recent_events: tuple[MostRecentSensorEventDTO, ...]

