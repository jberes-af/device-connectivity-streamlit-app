# /src/application/ports/treatment_repo_ports.py

from typing import Protocol, Sequence

from src.domain.entities.care.treatment_entities import (
    TreatmentPlan,
    TherapeuticGoal,
)


class TreatmentPlanRepositoryPort(Protocol):

    def list_treatment_plans(self) -> tuple[TreatmentPlan, ...]:
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

    def list_therapeutic_goals(self) -> tuple[TherapeuticGoal, ...]:
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
