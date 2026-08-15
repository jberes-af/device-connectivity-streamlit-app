# /src/main/infrastructure_containers/sheets_repo_tenant.py

from dataclasses import dataclass

from src.application.ports.tenant_repo_ports import (
    TenantProfileRepositoryPort,
)

from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)
from src.infrastructure.config.settings_model import (
    Settings,
)
from src.infrastructure.persistence.google_sheets.mappers.tenant.tenant_profile_row_mapper import (
    TenantProfileRowMapper,
)

from src.infrastructure.persistence.google_sheets.repos.tenant.tenant_profile_repository import (
    GoogleSheetsTenantProfileRepository,
)

from src.main.infrastructure_containers.utils_sheets_composition_root import (
    build_google_sheets_query_service,
    build_google_sheet_catalog,
)


@dataclass(frozen=True, slots=True)
class GoogleSheetsTenantRepositories:
    tenant_profile_repository: TenantProfileRepositoryPort


def build_google_sheets_tenant_repositories(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> GoogleSheetsTenantRepositories:
    query_service = build_google_sheets_query_service(
        settings=settings,
    )

    catalog = build_google_sheet_catalog(
        settings=settings,
        app_config=app_config,
    )

    tenant_profile_repository: TenantProfileRepositoryPort = (
        GoogleSheetsTenantProfileRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=TenantProfileRowMapper(),
        ))

    return GoogleSheetsTenantRepositories(
        tenant_profile_repository=tenant_profile_repository,
    )
