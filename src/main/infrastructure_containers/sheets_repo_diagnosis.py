# /src/main/infrastructure_containers/sheets_repo_diagnosis.py

from dataclasses import dataclass

from src.application.ports.diagnosis_repo_ports import (
    DiagnosisDefinitionRepositoryPort,
)

from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)
from src.infrastructure.config.settings_model import (
    Settings,
)

from src.infrastructure.persistence.google_sheets.mappers.diagnosis.diagnosis_definition_row_mapper import (
    DiagnosisDefinitionRowMapper,
)

from src.infrastructure.persistence.google_sheets.repos.diagnosis.diagnosis_definition_repository import (
    GoogleSheetsDiagnosisDefinitionRepository,
)

from src.main.infrastructure_containers.utils_sheets_composition_root import (
    build_google_sheets_query_service,
    build_google_sheet_catalog,
)


@dataclass(frozen=True, slots=True)
class GoogleSheetsDiagnosisRepositories:
    diagnosis_definition_repository: DiagnosisDefinitionRepositoryPort


def build_google_sheets_diagnosis_repositories(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> GoogleSheetsDiagnosisRepositories:
    query_service = build_google_sheets_query_service(
        settings=settings,
    )

    catalog = build_google_sheet_catalog(
        settings=settings,
        app_config=app_config,
    )

    diagnosis_definition_repo: DiagnosisDefinitionRepositoryPort = (
        GoogleSheetsDiagnosisDefinitionRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=DiagnosisDefinitionRowMapper(),
        ))

    return GoogleSheetsDiagnosisRepositories(
        diagnosis_definition_repository=diagnosis_definition_repo,
    )
