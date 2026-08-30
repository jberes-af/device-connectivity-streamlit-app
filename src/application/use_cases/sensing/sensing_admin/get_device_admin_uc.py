# /src/application/use_cases/sensing/sensing_admin/get_device_admin_uc.py

import logging

from src.application.services.tenant.get_tenant_service import FetchTenantAdminService
from src.domain.entities.tenant.tenant_entities import TenantProfile
from src.domain.enums.sensing.device_enums import (
    DeviceTypeEnum,
)

from src.domain.entities.sensing.device_entities import (
    DeviceAdministrationProfile,
)

from src.domain.entities.sensing.device_entities import (
    SensorSystemProfile,
)

from src.domain.entities.sensing.user_sensing_entities import (
    UserSensorProfile,
)

from src.application.models.sensing_models import (
    GatewayDomainObjects,
    UserSensorProfiles,
)

from src.application.ports.sensing.user_sensing_port import (
    UserSensingRepositoryPort,
)

from src.application.ports.sensing.device_ports import (
    GatewayRepositoryPort,
    SensorDeviceRepositoryPort,
)

from src.application.services.sensing.get_device_admin_service import (
    FetchDeviceAdminService,
)

from src.application.use_cases.sensing.sensing_admin.device_admin_uc_dtos import (
    SensorProfileDTO,
    GatewayProfileDTO,
    GetDevicesAdministrationRequestDTO,
    GetDeviceAdministrationResultDTO
)

logger = logging.getLogger(__name__)


class GetDeviceAdministrationUseCase:

    def __init__(
            self,
            *,
            fetch_device_admin_service: FetchDeviceAdminService,
            fetch_tenant_service: FetchTenantAdminService,
            gateway_repository: GatewayRepositoryPort,
            sensor_repository: SensorDeviceRepositoryPort,
            user_sensing_repository: UserSensingRepositoryPort,
    ):
        self._fetch_device_admin_service = fetch_device_admin_service
        self._fetch_tenant_service = fetch_tenant_service
        self._gateway_repo = gateway_repository
        self._sensor_repo = sensor_repository
        self._user_sensing_repo = user_sensing_repository

    def execute(
            self,
            request: GetDevicesAdministrationRequestDTO,
    ) -> GetDeviceAdministrationResultDTO:

        if request.tenant_id is None:
            device_admin_profiles: tuple[DeviceAdministrationProfile, ...] = (
                self._fetch_device_admin_service.fetch_all_device_admin_profiles(
                ))

            tenant_profiles: tuple[TenantProfile, ...] = (
                self._fetch_tenant_service.fetch_all_tenant_profiles()
            )

        else:
            device_admin_profiles: tuple[DeviceAdministrationProfile, ...] = (
                self._fetch_device_admin_service.fetch_device_admin_profiles_for_tenant_id(
                    tenant_id=request.tenant_id,
                ))
            tenant_profiles: tuple[TenantProfile] = (
                self._fetch_tenant_service.get_by_id(request.tenant_id),
            )

        gateway_profiles: tuple[GatewayProfileDTO, ...] = (
            self._build_gateway_profiles(
                admin_profiles=device_admin_profiles,
            ))

        sensor_profiles: tuple[SensorProfileDTO, ...] = (
            self._build_sensor_profiles(
                admin_profiles=device_admin_profiles,
                gateway_profiles=gateway_profiles,
            ))

        return GetDeviceAdministrationResultDTO(
            tenant_profiles=tenant_profiles,
            sensor_profiles=sensor_profiles,
            gateway_profiles=gateway_profiles,
        )

    def _build_device_admin_profiles(
            self) -> tuple[DeviceAdministrationProfile, ...]:  # tuple[DeviceAdminProfileDTO, ...]:

        return (self._fetch_device_admin_service
                .fetch_all_device_admin_profiles()
                )

    def _build_sensor_profiles(
            self,
            admin_profiles: tuple[DeviceAdministrationProfile, ...],
            gateway_profiles: tuple[GatewayProfileDTO, ...],
    ) -> tuple[SensorProfileDTO, ...]:
        # --- BUILD SENSOR TO GATEWAY MAPPING

        gateway_to_sensor_mapping = {
            profile.gateway_id: profile.paired_sensor_ids
            for profile in gateway_profiles
        }

        sensor_to_gateway_mapping: dict[str, str] = {}
        for gateway_id, paired_sensors in gateway_to_sensor_mapping.items():
            for sensor_id in paired_sensors:
                sensor_to_gateway_mapping[sensor_id] = gateway_id

        # --- BUILD SENSOR ADMIN PROFILES

        sensor_admin_records = {
            profile.device_id: profile
            for profile in admin_profiles
            if profile.device_type == DeviceTypeEnum.SENSOR
        }

        # --- FETCH SENSOR SYSTEM RECORDS (FROM FIREBASE RTDB; IMMUTABLE)

        sensor_system_records: dict[str, SensorSystemProfile] = {}

        for sensor_id in sensor_admin_records:
            system_profile = self._sensor_repo.get(
                sensor_id=sensor_id,
            )

            if system_profile is not None:
                sensor_system_records[sensor_id] = system_profile

        # --- FETCH & BUILD SENSOR USER RECORDS (MUTABLE)

        user_ids: tuple[str, ...] = self._user_sensing_repo.get_all_user_ids()
        user_sensor_profiles: dict[str, UserSensorProfiles] = {}

        for user_id in user_ids:
            user_sensor_profile: UserSensorProfiles = (
                self._user_sensing_repo
                .get_sensor_profiles_by_user_id(
                    user_id=user_id,
                )
            )

            if user_sensor_profile is not None:
                user_sensor_profiles[user_id] = user_sensor_profile

        sensor_user_mapping: dict[
            str,
            list[tuple[str, UserSensorProfile]],
        ] = {}

        for user_id, user_profiles in user_sensor_profiles.items():
            for profile in user_profiles.sensor_profiles:
                sensor_user_mapping.setdefault(
                    profile.sensor_id,
                    [],
                ).append(
                    (user_id, profile)
                )

        # --- BUILD SENSOR PROFILE DTO

        profiles: list[SensorProfileDTO] = []

        for sensor_id, admin_profile in sensor_admin_records.items():

            system_profile = sensor_system_records.get(sensor_id)

            if system_profile is None:
                continue

            associated_profiles: list[tuple[str, UserSensorProfile]] = (
                sensor_user_mapping.get(sensor_id, [],
                                        ))

            attached_user_ids: tuple[str, ...] = tuple(
                user_id
                for user_id, _ in associated_profiles
            )

            primary_user_profile: UserSensorProfile = (
                associated_profiles[0][1]
                if associated_profiles
                else None
            )

            profiles.append(

                SensorProfileDTO(
                    sensor_id=sensor_id,
                    sensor_type=system_profile.sensor_type,
                    tenant_id=admin_profile.tenant_id,

                    name=(
                        primary_user_profile.name
                        if primary_user_profile
                        else None
                    ),
                    location=(
                        primary_user_profile.location
                        if primary_user_profile
                        else None
                    ),
                    zone=(
                        primary_user_profile.zone
                        if primary_user_profile
                        else None
                    ),

                    firmware_version=(
                        admin_profile.firmware_version_sensor
                    ),
                    hardware_version=admin_profile.hardware_version,

                    paired_gateway_id=sensor_to_gateway_mapping[sensor_id],

                    attached_user_ids=attached_user_ids,

                    attached_adl_names=(),
                    used_in_routine_ids=(),

                    sensor_purpose=admin_profile.sensor_purpose,

                    install_date=admin_profile.install_date,
                    removed_date=admin_profile.removed_date,
                    owned_from_date=admin_profile.owned_from_date,
                    owned_to_date=admin_profile.owned_to_date,
                )
            )

        return tuple(profiles)

    def _build_gateway_profiles(
            self,
            admin_profiles: tuple[DeviceAdministrationProfile, ...],
    ) -> tuple[GatewayProfileDTO, ...]:
        gateway_admin_records: dict[str, DeviceAdministrationProfile] = {
            profile.device_id: profile
            for profile in admin_profiles
            if profile.device_type == DeviceTypeEnum.GATEWAY
        }

        profiles: list[GatewayProfileDTO] = []

        for gateway_id, admin_profile in gateway_admin_records.items():

            gateway: GatewayDomainObjects | None = (
                self._gateway_repo.get(
                    gateway_id=gateway_id,
                )
            )

            if gateway is None:
                continue

            paired_sensor_ids: tuple[str, ...] = tuple(
                link.sensor_id
                for link in gateway.gateway_sensor_links
                if link.gateway_id == gateway_id
            )

            attached_user_ids: tuple[str, ...] = tuple(
                link.user_id
                for link in gateway.gateway_user_links
                if link.gateway_id == gateway_id
            )

            profiles.append(
                GatewayProfileDTO(
                    gateway_id=gateway_id,
                    tenant_id=admin_profile.tenant_id,

                    attached_user_ids=attached_user_ids,

                    paired_sensor_ids=paired_sensor_ids,

                    firmware_version_mcu=(
                        admin_profile.firmware_version_gateway
                    ),
                    firmware_version_cellular=(
                        admin_profile.firmware_version_cellular
                    ),
                    hardware_version=(
                        admin_profile.hardware_version
                    ),

                    install_date=admin_profile.install_date,
                    removed_date=admin_profile.removed_date,

                    owned_from_date=admin_profile.owned_from_date,
                    owned_to_date=admin_profile.owned_to_date,
                )
            )

        return tuple(profiles)
