# /src/application/use_cases/sensing/sensing_admin/build_admin_view/build_sensing_admin_view_use_case.py

import logging

from src.application.use_cases.sensing.sensing_admin.admin_profiles.device_admin_uc_dtos import (
    GetDevicesAdministrationRequestDTO,
    GetDeviceAdministrationResultDTO
)

from src.application.use_cases.tenant.tenant_profiles_uc_dtos import (
    TenantProfileDTO,
    GetTenantProfilesResultDTO
)

from src.application.use_cases.sensing.sensing_admin.build_view.build_admin_view_uc_dtos import (
    BuildSensingAdminViewRequestDTO,
    BuildSensingAdminViewResultDTO,
)

from src.application.use_cases.tenant.get_tenant_profiles_uc import (
    GetTenantProfilesUseCase
)

from src.application.use_cases.sensing.sensing_admin.admin_profiles.get_device_admin_uc import (
    GetDeviceAdministrationUseCase
)

logger = logging.getLogger(__name__)

_TENANTS_TO_EXCLUDE: list[str] = ["Alerta Family"]


class BuildSensingAdministrationViewUseCase:

    def __init__(
            self,
            get_tenant_profiles_use_case: GetTenantProfilesUseCase,
            get_device_admin_profiles_use_case: GetDeviceAdministrationUseCase,
    ) -> None:
        self._get_tenant_profiles_uc = get_tenant_profiles_use_case
        self._get_device_admin_uc = get_device_admin_profiles_use_case

    def execute(
            self,
            request: BuildSensingAdminViewRequestDTO,
    ) -> BuildSensingAdminViewResultDTO:

        exclude_alerta_family: bool = True

        tenants_result: GetTenantProfilesResultDTO = (
            self._get_tenant_profiles_uc.execute())

        if exclude_alerta_family:
            available_tenant_profiles: tuple[TenantProfileDTO, ...] = tuple([
                p
                for p in tenants_result.tenant_profiles
                if p.tenant_name not in _TENANTS_TO_EXCLUDE
            ])
        else:
            available_tenant_profiles: tuple[TenantProfileDTO, ...] = (
                tenants_result.tenant_profiles)

        if not available_tenant_profiles:
            return BuildSensingAdminViewResultDTO(
                tenant_profiles=(),
                selected_tenant_id=None,
                selected_tenant_name=None,
                sensor_profiles=(),
                gateway_profiles=()
            )

        """
        valid_tenant_ids: set[str] = {
            item.tenant_id
            for item in available_tenant_profiles
        }
        """

        valid_tenant_names: set[str] = {
            item.tenant_name
            for item in available_tenant_profiles
        }

        selected_name = request.selected_tenant_name

        if selected_name not in valid_tenant_names:
            selected_name = available_tenant_profiles[0].tenant_name

        tenant_name_to_id_mapping = {
            r.tenant_name: r.tenant_id
            for r in available_tenant_profiles
        }

        selected_id = tenant_name_to_id_mapping.get(selected_name)

        detail_result: GetDeviceAdministrationResultDTO = self._get_device_admin_uc.execute(
            GetDevicesAdministrationRequestDTO(
                tenant_ids=(selected_id,),
            )
        )

        return BuildSensingAdminViewResultDTO(
            tenant_profiles=available_tenant_profiles,
            selected_tenant_id=selected_id,
            selected_tenant_name=selected_name,
            sensor_profiles=detail_result.sensor_profiles,
            gateway_profiles=detail_result.gateway_profiles,
        )
