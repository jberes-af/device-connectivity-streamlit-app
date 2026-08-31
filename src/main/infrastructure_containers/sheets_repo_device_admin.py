# /src/main/infrastructure_containers/sheets_repo_device_admin.py

from dataclasses import dataclass

from src.application.ports.sensing.device_ports import (
    DeviceAdministrationRepositoryPort,
)

from src.application.ports.sensing.device_ports import (
    ResidentGatewayLinkRepositoryPort,
    ResidentSensorLinkRepositoryPort
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

from src.infrastructure.persistence.google_sheets.mappers.access.resident_gateway_link_row_mapper import (
    ResidentGatewayLinkRowMapper,
)

from src.infrastructure.persistence.google_sheets.mappers.access.resident_sensor_link_row_mapper import (
    ResidentSensorLinkRowMapper,
)

from src.infrastructure.persistence.google_sheets.repos.device.device_profile_repository import (
    GoogleSheetsDeviceAdministrationProfileRepository,
)

from src.infrastructure.persistence.google_sheets.repos.access.resident_gateway_link_repository import (
    GoogleSheetsResidentGatewayLinkRepository,
)

from src.infrastructure.persistence.google_sheets.repos.access.resident_sensor_link_repository import (
    GoogleSheetsResidentSensorLinkRepository,
)

from src.main.infrastructure_containers.utils_sheets_composition_root import (
    build_google_sheets_query_service,
    build_google_sheet_catalog,
)


@dataclass(frozen=True, slots=True)
class GoogleSheetsDeviceAdminRepositories:
    device_admin_profile_repository: DeviceAdministrationRepositoryPort
    resident_gateway_link_repository: ResidentGatewayLinkRepositoryPort
    resident_sensor_link_repository: ResidentSensorLinkRepositoryPort


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

    resident_gateway_repo: ResidentGatewayLinkRepositoryPort = (
        GoogleSheetsResidentGatewayLinkRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=ResidentGatewayLinkRowMapper(),
        )
    )

    resident_sensor_repo: ResidentSensorLinkRepositoryPort = (
        GoogleSheetsResidentSensorLinkRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=ResidentSensorLinkRowMapper(),

        )
    )

    return GoogleSheetsDeviceAdminRepositories(
        device_admin_profile_repository=device_profile_repo,
        resident_gateway_link_repository=resident_gateway_repo,
        resident_sensor_link_repository=resident_sensor_repo,
    )
