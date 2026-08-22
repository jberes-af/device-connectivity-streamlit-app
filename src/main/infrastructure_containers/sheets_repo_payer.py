# /src/main/infrastructure_containers/sheets_repo_payer.py

from dataclasses import dataclass

from src.application.ports.payer_repo_ports import (
    PayerRepositoryPort,
)

from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)
from src.infrastructure.config.settings_model import (
    Settings,
)

from src.infrastructure.persistence.google_sheets.mappers.payer.payer_row_mapper import (
    PayerRowMapper,
)

from src.infrastructure.persistence.google_sheets.repos.payer.payer_repository import (
    GoogleSheetsPayerRepository,
)

from src.main.infrastructure_containers.utils_sheets_composition_root import (
    build_google_sheets_query_service,
    build_google_sheet_catalog,
)


@dataclass(frozen=True, slots=True)
class GoogleSheetsPayerRepositories:
    payer_repository: PayerRepositoryPort


def build_google_sheets_payer_repositories(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> GoogleSheetsPayerRepositories:
    query_service = build_google_sheets_query_service(
        settings=settings,
    )

    catalog = build_google_sheet_catalog(
        settings=settings,
        app_config=app_config,
    )

    payer_repository: PayerRepositoryPort = (
        GoogleSheetsPayerRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=PayerRowMapper(),
        ))

    return GoogleSheetsPayerRepositories(
        payer_repository=payer_repository,
    )
