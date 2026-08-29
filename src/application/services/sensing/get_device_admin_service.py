# /src/application/services/sensing/get_device_admin_service.py


from src.domain.entities.sensing.device_entities import (
    DeviceAdministrationProfile,
)

from src.application.ports.sensing.device_ports import (
    DeviceAdministrationRepositoryPort,
)


class FetchDeviceAdminService:

    def __init__(
            self,
            *,
            device_admin_repository: DeviceAdministrationRepositoryPort,
    ) -> None:
        self._device_admin_repo = device_admin_repository

    def fetch_all_device_admin_profiles(
            self) -> tuple[DeviceAdministrationProfile, ...]:
        return self._device_admin_repo.list_device_admin_profiles()

    def fetch_device_admin_profiles_for_tenant_id(
            self,
            tenant_id: str,
    ) -> tuple[DeviceAdministrationProfile, ...]:
        return self._device_admin_repo.list_devices_for_tenant_id(
            tenant_id=tenant_id
        )
