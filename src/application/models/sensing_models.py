# /src/application/models/sensing_models.py

# these are returned from infrastructure-firebase-repos

from dataclasses import dataclass

from src.domain.entities.sensing.device_entities import (
    GatewayProfile,
    GatewaySensorLink,
    # SensorSystemProfile,
)

from src.domain.entities.sensing.user_sensing_entities import (
    UserSensingAccount,
    UserSensorLink,
    UserGatewayLink,
    UserSensorProfile,
    UserAdlSensorLink,
    UserAlertaRoutineLink,
)


@dataclass(frozen=True, slots=True)
class UserSensingDomainObjects:
    user_profile: UserSensingAccount
    user_sensor_links: tuple[UserSensorLink, ...]
    user_gateway_links: tuple[UserGatewayLink, ...]
    user_sensor_profiles: tuple[UserSensorProfile, ...]
    adl_sensor_links: tuple[UserAdlSensorLink, ...]
    alerta_routine_links: tuple[UserAlertaRoutineLink, ...]


@dataclass(frozen=True, slots=True)
class GatewayDomainObjects:
    gateway_profile: GatewayProfile
    gateway_sensor_links: tuple[GatewaySensorLink, ...]
    gateway_user_links: tuple[UserGatewayLink, ...]


"""
@dataclass(frozen=True, slots=True)
class SensorDomainObjects:
    sensor_system_profiles: tuple[SensorSystemProfile, ...]
"""
