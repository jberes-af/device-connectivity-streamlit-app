# /src/main/infrastructure_containers/sheets_repo_treatment.py

from dataclasses import dataclass

from src.application.ports.treatment_repo_ports import (
    TreatmentPlanRepositoryPort,
    TherapeuticGoalRepositoryPort,
)

from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)
from src.infrastructure.config.settings_model import (
    Settings,
)

from src.infrastructure.persistence.google_sheets.mappers.treatment.treatment_plan_row_mapper import (
    TreatmentPlanRowMapper,
)

from src.infrastructure.persistence.google_sheets.mappers.treatment.therapeutic_goal_row_mapper import (
    TherapeuticGoalRowMapper
)

from src.infrastructure.persistence.google_sheets.repos.treatment.treatment_plan_repository import (
    GoogleSheetsTreatmentPlanRepository,
)

from src.infrastructure.persistence.google_sheets.repos.treatment.therapeutic_goal_repository import (
    GoogleSheetsTherapeuticGoalRepository,
)

from src.main.infrastructure_containers.utils_sheets_composition_root import (
    build_google_sheets_query_service,
    build_google_sheet_catalog,
)


@dataclass(frozen=True, slots=True)
class GoogleSheetsTreatmentRepositories:
    treatment_plan_repository: TreatmentPlanRepositoryPort
    therapeutic_goal_repository: TherapeuticGoalRepositoryPort


def build_google_sheets_treatment_repositories(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> GoogleSheetsTreatmentRepositories:
    query_service = build_google_sheets_query_service(
        settings=settings,
    )

    catalog = build_google_sheet_catalog(
        settings=settings,
        app_config=app_config,
    )

    treatment_plan_repo: TreatmentPlanRepositoryPort = (
        GoogleSheetsTreatmentPlanRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=TreatmentPlanRowMapper(),
        ))

    therapeutic_goal_repo: TherapeuticGoalRepositoryPort = (
        GoogleSheetsTherapeuticGoalRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=TherapeuticGoalRowMapper(),
        ))

    return GoogleSheetsTreatmentRepositories(
        treatment_plan_repository=treatment_plan_repo,
        therapeutic_goal_repository=therapeutic_goal_repo
    )
