# /src/main/infrastructure_containers/sheets_repo_access.py

from dataclasses import dataclass

from src.application.ports.access_repo_ports import (
    UserResidentAccessRepositoryPort,
    UserTenantMembershipRepositoryPort,
    ResidentGatewayLinkRepositoryPort,
    ResidentSensorLinkRepositoryPort,
)

from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)
from src.infrastructure.config.settings_model import (
    Settings,
)

from src.infrastructure.persistence.google_sheets.mappers.access.user_resident_access_row_mapper import (
    UserResidentAccessRowMapper,
)

from src.infrastructure.persistence.google_sheets.mappers.access.user_tenant_membership_row_mapper import (
    UserTenantMembershipRowMapper,
)

from src.infrastructure.persistence.google_sheets.mappers.access.resident_gateway_link_row_mapper import (
    ResidentGatewayLinkRowMapper,
)

from src.infrastructure.persistence.google_sheets.mappers.access.resident_sensor_link_row_mapper import (
    ResidentSensorLinkRowMapper,
)

from src.infrastructure.persistence.google_sheets.repos.access.user_resident_access_repository import (
    GoogleSheetsUserResidentAccessRepository,
)

from src.infrastructure.persistence.google_sheets.repos.access.user_tenant_membership_repository import (
    GoogleSheetsUserTenantMembershipRepository,
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
class GoogleSheetsAccessRepositories:
    resident_gateway_link_repository: ResidentGatewayLinkRepositoryPort
    resident_sensor_link_repository: ResidentSensorLinkRepositoryPort
    user_resident_access_repository: UserResidentAccessRepositoryPort
    user_tenant_membership_repository: UserTenantMembershipRepositoryPort


def build_google_sheets_access_repositories(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> GoogleSheetsAccessRepositories:
    query_service = build_google_sheets_query_service(
        settings=settings,
    )

    catalog = build_google_sheet_catalog(
        settings=settings,
        app_config=app_config,
    )

    user_resident_access_repo: UserResidentAccessRepositoryPort = (
        GoogleSheetsUserResidentAccessRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=UserResidentAccessRowMapper(),
        ))

    user_tenant_membership_repo: UserTenantMembershipRepositoryPort = (
        GoogleSheetsUserTenantMembershipRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=UserTenantMembershipRowMapper(),
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

    return GoogleSheetsAccessRepositories(
        resident_gateway_link_repository=resident_gateway_repo,
        resident_sensor_link_repository=resident_sensor_repo,
        user_resident_access_repository=user_resident_access_repo,
        user_tenant_membership_repository=user_tenant_membership_repo,
    )
