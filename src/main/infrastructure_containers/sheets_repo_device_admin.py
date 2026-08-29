# /src/main/infrastructure_containers/sheets_repo_device_admin.py

from dataclasses import dataclass

from src.application.ports.sensing.device_ports import (
    DeviceAdministrationRepositoryPort,
)

from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)
from src.infrastructure.config.settings_model import (
    Settings,
)
from src.infrastructure.persistence.google_sheets.mappers.device.device_profile_row_mapper import (
    DeviceAdministrationProfileRowMapper,
)

from src.infrastructure.persistence.google_sheets.repos.device.device_profile_repository import (
    GoogleSheetsDeviceAdministrationProfileRepository,
)

from src.main.infrastructure_containers.utils_sheets_composition_root import (
    build_google_sheets_query_service,
    build_google_sheet_catalog,
)


@dataclass(frozen=True, slots=True)
class GoogleSheetsDeviceAdminRepositories:
    device_admin_profile_repository: DeviceAdministrationRepositoryPort


def build_google_sheets_device_admin_repositories(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> GoogleSheetsDeviceAdminRepositories:
    query_service = build_google_sheets_query_service(
        settings=settings,
    )

    catalog = build_google_sheet_catalog(
        settings=settings,
        app_config=app_config,
    )

    device_profile_repo: DeviceAdministrationRepositoryPort = (
        GoogleSheetsDeviceAdministrationProfileRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=DeviceAdministrationProfileRowMapper(),
        ))

    return GoogleSheetsDeviceAdminRepositories(
        device_admin_profile_repository=device_profile_repo,
    )
