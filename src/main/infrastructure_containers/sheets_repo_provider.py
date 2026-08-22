# /src/main/infrastructure_containers/sheets_repo_provider.py

from dataclasses import dataclass

from src.application.ports.provider_repo_ports import (
    ProviderRepositoryPort,
)

from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)
from src.infrastructure.config.settings_model import (
    Settings,
)

from src.infrastructure.persistence.google_sheets.mappers.provider.provider_row_mapper import (
    ProviderRowMapper,
)

from src.infrastructure.persistence.google_sheets.repos.provider.provider_repository import (
    GoogleSheetsProviderRepository,
)

from src.main.infrastructure_containers.utils_sheets_composition_root import (
    build_google_sheets_query_service,
    build_google_sheet_catalog,
)


@dataclass(frozen=True, slots=True)
class GoogleSheetsProviderRepositories:
    provider_repository: ProviderRepositoryPort


def build_google_sheets_provider_repositories(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> GoogleSheetsProviderRepositories:
    query_service = build_google_sheets_query_service(
        settings=settings,
    )

    catalog = build_google_sheet_catalog(
        settings=settings,
        app_config=app_config,
    )

    provider_repository: ProviderRepositoryPort = (
        GoogleSheetsProviderRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=ProviderRowMapper(),
        ))

    return GoogleSheetsProviderRepositories(
        provider_repository=provider_repository,
    )
