# /src/main/infrastructure_containers/sheets_repo_treatment.py

from dataclasses import dataclass

from src.application.ports.treatment_repo_ports import (
    TreatmentPlanRepositoryPort,
    TherapeuticGoalRepositoryPort,
    TreatmentInterventionRepositoryPort,
    TreatmentMonitoringParameterRepositoryPort,
    TreatmentPlanReviewRepositoryPort,
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

from src.infrastructure.persistence.google_sheets.mappers.treatment.treatment_intervention_row_mapper import (
    TreatmentInterventionRowMapper
)

from src.infrastructure.persistence.google_sheets.mappers.treatment.treatment_monitoring_parameter_row_mapper import (
    TreatmentMonitoringParameterRowMapper
)

from src.infrastructure.persistence.google_sheets.mappers.treatment.treatment_plan_review_row_mapper import (
    TreatmentPlanReviewRowMapper
)

from src.infrastructure.persistence.google_sheets.repos.treatment.treatment_plan_repository import (
    GoogleSheetsTreatmentPlanRepository,
)

from src.infrastructure.persistence.google_sheets.repos.treatment.therapeutic_goal_repository import (
    GoogleSheetsTherapeuticGoalRepository,
)

from src.infrastructure.persistence.google_sheets.repos.treatment.treatment_intervention_repository import (
    GoogleSheetsTreatmentInterventionRepository,
)

from src.infrastructure.persistence.google_sheets.repos.treatment.treatment_monitoring_parameter_repository import (
    GoogleSheetsTreatmentMonitoringParameterRepository,
)

from src.infrastructure.persistence.google_sheets.repos.treatment.treatment_plan_review_repository import (
    GoogleSheetsTreatmentPlanReviewRepository,
)

from src.main.infrastructure_containers.utils_sheets_composition_root import (
    build_google_sheets_query_service,
    build_google_sheet_catalog,
)


@dataclass(frozen=True, slots=True)
class GoogleSheetsTreatmentRepositories:
    treatment_plan_repository: TreatmentPlanRepositoryPort
    therapeutic_goal_repository: TherapeuticGoalRepositoryPort
    treatment_intervention_repository: TreatmentInterventionRepositoryPort
    treatment_monitoring_parameter_repository: TreatmentMonitoringParameterRepositoryPort
    treatment_plan_review_repository: TreatmentPlanReviewRepositoryPort


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

    treatment_intervention_repo: TreatmentInterventionRepositoryPort = (
        GoogleSheetsTreatmentInterventionRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=TreatmentInterventionRowMapper(),
        ))

    treatment_monitoring_parameter_repo: TreatmentMonitoringParameterRepositoryPort = (
        GoogleSheetsTreatmentMonitoringParameterRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=TreatmentMonitoringParameterRowMapper(),
        ))

    treatment_plan_review_repo: TreatmentPlanReviewRepositoryPort = (
        GoogleSheetsTreatmentPlanReviewRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=TreatmentPlanReviewRowMapper(),
        ))

    return GoogleSheetsTreatmentRepositories(
        treatment_plan_repository=treatment_plan_repo,
        therapeutic_goal_repository=therapeutic_goal_repo,
        treatment_intervention_repository=treatment_intervention_repo,
        treatment_monitoring_parameter_repository=treatment_monitoring_parameter_repo,
        treatment_plan_review_repository=treatment_plan_review_repo,

    )
