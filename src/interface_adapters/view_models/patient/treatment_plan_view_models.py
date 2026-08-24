# /src/interface_adapters/view_models/patient/treatment_plan_view_models.py

from dataclasses import dataclass

from src.interface_adapters.view_models.widgets.card_view_models import (
    MetricCardViewModel,
)


from src.interface_adapters.view_models.widgets.badge_view_model import (
    BadgeViewModel,
)

from src.interface_adapters.view_models.widgets.property_field_view_model import (
    PropertyFieldViewModel,
)


@dataclass(frozen=True)
class TherapeuticGoalViewModel:
    goal_id: str
    description: str
    target_date_display: str


@dataclass(frozen=True)
class TreatmentInterventionViewModel:
    intervention_id: str
    treatment_type_display: str
    description: str
    status_badge: BadgeViewModel
    date_range_display: str


@dataclass(frozen=True)
class TreatmentMonitoringParameterViewModel:
    monitoring_parameter_id: str
    measure_name: str
    baseline_display: str
    target_display: str


@dataclass(frozen=True)
class TreatmentPlanReviewViewModel:
    review_id: str
    reviewed_at_display: str
    provider_display: str
    clinical_findings: str
    treatment_decision: str
    next_review_date_display: str


@dataclass(frozen=True)
class TreatmentPlanCardViewModel:
    treatment_plan_id: str
    title: str
    status_badge: BadgeViewModel
    properties: tuple[PropertyFieldViewModel, ...]

    goals: tuple[TherapeuticGoalViewModel, ...]
    interventions: tuple[TreatmentInterventionViewModel, ...]
    monitoring_parameters: tuple[TreatmentMonitoringParameterViewModel, ...]
    reviews: tuple[TreatmentPlanReviewViewModel, ...]


@dataclass(frozen=True)
class TreatmentPlanTabViewModel:
    metrics: tuple[MetricCardViewModel, ...]
    plans: tuple[TreatmentPlanCardViewModel, ...]
