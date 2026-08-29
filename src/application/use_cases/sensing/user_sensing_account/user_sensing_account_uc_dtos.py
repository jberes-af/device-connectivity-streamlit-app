# /src/application/use_cases/sensing/user_sensing_account/user_resident_sensing_uc_dtos.py

from dataclasses import dataclass

from src.domain.entities.sensing.device_entities import (
    SensorSystemProfile,
)

from src.domain.entities.sensing.user_sensing_entities import (
    UserSensorProfile,
)


@dataclass(frozen=True)
class SensorProfileDTO:
    sensor_id: str
    tenant_id: str | None
    system_config: SensorSystemProfile
    user_config: UserSensorProfile | None = None


@dataclass(frozen=True)
class GatewayProfileDTO:
    gateway_id: str
    tenant_id: str | None
    paired_sensor_ids: tuple[str, ...]


@dataclass(frozen=True)
class UserSensingAccountRequestDTO:
    user_id: str


@dataclass(frozen=True)
class UserSensingAccountResultDTO:
    user_id: str
    sensor_ids: tuple[str, ...]
    sensor_profiles: tuple[SensorProfileDTO, ...]
    gateway_ids: tuple[str, ...]
    gateway_profiles: tuple[GatewayProfileDTO, ...]
