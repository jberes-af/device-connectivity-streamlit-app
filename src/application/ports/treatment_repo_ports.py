# /src/application/ports/treatment_repo_ports.py


from typing import Protocol, Sequence

from src.domain.entities.care.treatment_entities import (
    TreatmentPlan,
    TherapeuticGoal,
    TreatmentIntervention,
    TreatmentMonitoringParameter,
    TreatmentPlanReview,
)


class TreatmentPlanRepositoryPort(Protocol):

    def list_treatment_plans(
            self,
    ) -> tuple[TreatmentPlan, ...]:
        ...

    def list_for_patient_id(
            self,
            patient_id: str,
    ) -> tuple[TreatmentPlan, ...]:
        ...

    def get_by_id(
            self,
            treatment_plan_id: str,
    ) -> TreatmentPlan:
        ...

    def get_by_ids(
            self,
            treatment_plan_ids: Sequence[str],
    ) -> tuple[TreatmentPlan, ...]:
        ...


class TherapeuticGoalRepositoryPort(Protocol):

    def list_therapeutic_goals(
            self,
    ) -> tuple[TherapeuticGoal, ...]:
        ...

    def list_for_treatment_plan_id(
            self,
            treatment_plan_id: str,
    ) -> tuple[TherapeuticGoal, ...]:
        ...

    def get_by_id(
            self,
            goal_id: str,
    ) -> TherapeuticGoal:
        ...

    def get_by_ids(
            self,
            goal_ids: Sequence[str],
    ) -> tuple[TherapeuticGoal, ...]:
        ...


class TreatmentInterventionRepositoryPort(Protocol):

    def list_treatment_interventions(
            self,
    ) -> tuple[TreatmentIntervention, ...]:
        ...

    def list_for_treatment_plan_id(
            self,
            treatment_plan_id: str,
    ) -> tuple[TreatmentIntervention, ...]:
        ...

    def get_by_id(
            self,
            treatment_intervention_id: str,
    ) -> TreatmentIntervention:
        ...

    def get_by_ids(
            self,
            treatment_intervention_ids: Sequence[str],
    ) -> tuple[TreatmentIntervention, ...]:
        ...


class TreatmentMonitoringParameterRepositoryPort(Protocol):

    def list_treatment_monitoring_parameters(
            self,
    ) -> tuple[TreatmentMonitoringParameter, ...]:
        ...

    def list_for_treatment_plan_id(
            self,
            treatment_plan_id: str,
    ) -> tuple[TreatmentMonitoringParameter, ...]:
        ...

    def get_by_id(
            self,
            treatment_monitoring_parameter_id: str,
    ) -> TreatmentMonitoringParameter:
        ...

    def get_by_ids(
            self,
            treatment_monitoring_parameter_ids: Sequence[str],
    ) -> tuple[TreatmentMonitoringParameter, ...]:
        ...


class TreatmentPlanReviewRepositoryPort(Protocol):

    def list_treatment_plan_reviews(
            self,
    ) -> tuple[TreatmentPlanReview, ...]:
        ...

    def list_for_treatment_plan_id(
            self,
            treatment_plan_id: str,
    ) -> tuple[TreatmentPlanReview, ...]:
        ...

    def get_by_id(
            self,
            treatment_plan_review_id: str,
    ) -> TreatmentPlanReview:
        ...

    def get_by_ids(
            self,
            treatment_plan_review_ids: Sequence[str],
    ) -> tuple[TreatmentPlanReview, ...]:
        ...
