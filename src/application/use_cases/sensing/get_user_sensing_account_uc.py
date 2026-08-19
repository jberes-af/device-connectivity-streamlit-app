# /src/application/use_cases/sensing/get_user_sensing_account_uc.py

from collections import defaultdict

from src.domain.entities.sensing.device_entities import (
    SensorSystemProfile,
)

from src.domain.entities.sensing.user_sensing_entities import (
    UserSensorProfile,
)

from src.application.models.sensing_models import (
    GatewayDomainObjects,
    UserSensingDomainObjects,
)

from src.application.ports.sensing.user_sensing_port import (
    UserSensingRepositoryPort,
)

from src.application.ports.sensing.device_ports import (
    GatewayRepositoryPort,
    SensorRepositoryPort,
)

from src.application.use_cases.sensing.user_sensing_account_uc_dtos import (
    SensorProfileDTO,
    GatewayProfileDTO,
    UserSensingAccountRequestDTO,
    UserSensingAccountResultDTO,
)


class GetUserSensingAccountUseCase:
    def __init__(
            self,
            user_sensing_repository: UserSensingRepositoryPort,
            gateway_repository: GatewayRepositoryPort,
            sensor_repository: SensorRepositoryPort,
    ) -> None:
        self._user_sensing_repo = user_sensing_repository
        self._gateway_repo = gateway_repository
        self._sensor_repo = sensor_repository

    def execute(
            self,
            request: UserSensingAccountRequestDTO,
    ) -> UserSensingAccountResultDTO:
        uid: str = request.user_id

        _TENANT_ID_DEV = "larry"

        user_objects: UserSensingDomainObjects = (
            self._user_sensing_repo.get(user_id=uid,
                                        tenant_id=_TENANT_ID_DEV))

        sensor_ids: list[str] = [
            r.sensor_id for r in user_objects.user_sensor_links
        ]

        sensor_profiles: list[SensorProfileDTO] = (
            self._build_sensor_profiles(
                tenant_id=_TENANT_ID_DEV,
                sensor_ids=sensor_ids,
                user_sensor_profiles=user_objects.user_sensor_profiles
            ))

        gateway_ids: list[str] = [
            r.gateway_id for r in user_objects.user_gateway_links
        ]

        gateway_profiles: tuple[GatewayProfileDTO, ...] = (
            self._build_gateway_profiles(
                tenant_id=_TENANT_ID_DEV,
                gateway_ids=gateway_ids,
            ))

        return UserSensingAccountResultDTO(
            user_id=uid,
            sensor_ids=tuple(sensor_ids),
            sensor_profiles=tuple(sensor_profiles),
            gateway_ids=tuple(gateway_ids),
            gateway_profiles=gateway_profiles,
        )

    def _build_sensor_profiles(
            self,
            tenant_id: str,
            sensor_ids: list[str],
            user_sensor_profiles: tuple[UserSensorProfile, ...],
    ) -> list[SensorProfileDTO]:

        user_profiles_by_id: dict[str, UserSensorProfile] = {
            profile.sensor_id: profile
            for profile in user_sensor_profiles
        }

        profiles: list[SensorProfileDTO] = []

        for sensor_id in sensor_ids:
            system_profile: SensorSystemProfile = self._sensor_repo.get(
                sensor_id=sensor_id,
                tenant_id=tenant_id,
            )

            if system_profile is None:
                continue

            profiles.append(
                SensorProfileDTO(
                    sensor_id=sensor_id,
                    tenant_id=tenant_id,
                    system_config=system_profile,
                    user_config=user_profiles_by_id.get(sensor_id),
                )
            )

        return profiles

    def _build_gateway_profiles(
            self,
            tenant_id: str,
            gateway_ids: list[str],
    ) -> tuple[GatewayProfileDTO, ...]:

        paired_sensors: dict[str, list[str]] = defaultdict(list)

        for gateway_id in gateway_ids:
            gateway: GatewayDomainObjects = self._gateway_repo.get(
                gateway_id=gateway_id,
                tenant_id=tenant_id,
            )

            if gateway is None:
                continue

            for link in gateway.gateway_sensor_links:
                paired_sensors[link.gateway_id].append(link.sensor_id)

        return tuple(
            GatewayProfileDTO(
                gateway_id=gateway_id,
                tenant_id=tenant_id,
                paired_sensor_ids=tuple(paired_sensors[gateway_id]),
            )
            for gateway_id in gateway_ids
        )
