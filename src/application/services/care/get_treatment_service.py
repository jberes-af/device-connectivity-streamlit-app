# /src/application/services/care/get_treatment_service.py

from typing import Sequence

from src.domain.entities.care.treatment_entities import (
    TreatmentPlan,
    TherapeuticGoal,
    TreatmentIntervention,
    TreatmentMonitoringParameter,
    TreatmentPlanReview,
)

from src.application.ports.treatment_repo_ports import (
    TreatmentPlanRepositoryPort,
    TherapeuticGoalRepositoryPort,
    TreatmentInterventionRepositoryPort,
    TreatmentMonitoringParameterRepositoryPort,
    TreatmentPlanReviewRepositoryPort,
)


class FetchTreatmentPlanService:

    def __init__(
            self,
            *,
            treatment_plan_repository: TreatmentPlanRepositoryPort,
    ) -> None:
        self._repository = treatment_plan_repository

    def fetch_treatment_plan(
            self,
            treatment_plan_id: str,
    ) -> TreatmentPlan:
        return self._repository.get_by_id(
            treatment_plan_id=treatment_plan_id,
        )

    def fetch_treatment_plans(
            self,
            treatment_plan_ids: Sequence[str],
    ) -> tuple[TreatmentPlan, ...]:
        return self._repository.get_by_ids(
            treatment_plan_ids=treatment_plan_ids,
        )

    def fetch_treatment_plans_for_patient(
            self,
            patient_id: str,
    ) -> tuple[TreatmentPlan, ...]:
        return self._repository.list_for_patient_id(
            patient_id=patient_id,
        )


class FetchTherapeuticGoalService:

    def __init__(
            self,
            *,
            therapeutic_goal_repository: TherapeuticGoalRepositoryPort,
    ) -> None:
        self._repository = therapeutic_goal_repository

    def fetch_goal(
            self,
            goal_id: str,
    ) -> TherapeuticGoal:
        return self._repository.get_by_id(
            goal_id=goal_id,
        )

    def fetch_goals(
            self,
            goal_ids: Sequence[str],
    ) -> tuple[TherapeuticGoal, ...]:
        return self._repository.get_by_ids(
            goal_ids=goal_ids,
        )

    def fetch_goals_for_treatment_plan(
            self,
            treatment_plan_id: str,
    ) -> tuple[TherapeuticGoal, ...]:
        return self._repository.list_for_treatment_plan_id(
            treatment_plan_id=treatment_plan_id,
        )


class FetchTreatmentInterventionService:

    def __init__(
            self,
            *,
            treatment_intervention_repository:
            TreatmentInterventionRepositoryPort,
    ) -> None:
        self._repository = treatment_intervention_repository

    def fetch_intervention(
            self,
            treatment_intervention_id: str,
    ) -> TreatmentIntervention:
        return self._repository.get_by_id(
            treatment_intervention_id=treatment_intervention_id,
        )

    def fetch_interventions(
            self,
            treatment_intervention_ids: Sequence[str],
    ) -> tuple[TreatmentIntervention, ...]:
        return self._repository.get_by_ids(
            treatment_intervention_ids=treatment_intervention_ids,
        )

    def fetch_interventions_for_treatment_plan(
            self,
            treatment_plan_id: str,
    ) -> tuple[TreatmentIntervention, ...]:
        return self._repository.list_for_treatment_plan_id(
            treatment_plan_id=treatment_plan_id,
        )


class FetchTreatmentMonitoringParameterService:

    def __init__(
            self,
            *,
            treatment_monitoring_parameter_repository:
            TreatmentMonitoringParameterRepositoryPort,
    ) -> None:
        self._repository = treatment_monitoring_parameter_repository

    def fetch_monitoring_parameter(
            self,
            treatment_monitoring_parameter_id: str,
    ) -> TreatmentMonitoringParameter:
        return self._repository.get_by_id(
            treatment_monitoring_parameter_id=(
                treatment_monitoring_parameter_id
            ),
        )

    def fetch_monitoring_parameters(
            self,
            treatment_monitoring_parameter_ids: Sequence[str],
    ) -> tuple[TreatmentMonitoringParameter, ...]:
        return self._repository.get_by_ids(
            treatment_monitoring_parameter_ids=(
                treatment_monitoring_parameter_ids
            ),
        )

    def fetch_monitoring_parameters_for_treatment_plan(
            self,
            treatment_plan_id: str,
    ) -> tuple[TreatmentMonitoringParameter, ...]:
        return self._repository.list_for_treatment_plan_id(
            treatment_plan_id=treatment_plan_id,
        )


class FetchTreatmentPlanReviewService:

    def __init__(
            self,
            *,
            treatment_plan_review_repository:
            TreatmentPlanReviewRepositoryPort,
    ) -> None:
        self._repository = treatment_plan_review_repository

    def fetch_review(
            self,
            review_id: str,
    ) -> TreatmentPlanReview:
        return self._repository.get_by_id(
            review_id=review_id,
        )

    def fetch_reviews(
            self,
            review_ids: Sequence[str],
    ) -> tuple[TreatmentPlanReview, ...]:
        return self._repository.get_by_ids(
            review_ids=review_ids,
        )

    def fetch_reviews_for_treatment_plan(
            self,
            treatment_plan_id: str,
    ) -> tuple[TreatmentPlanReview, ...]:
        return self._repository.list_for_treatment_plan_id(
            treatment_plan_id=treatment_plan_id,
        )
