# /src/domain/entities/treatment/treatment_entities.py

from dataclasses import dataclass
from datetime import date, datetime

from src.domain.enums.care.treatment_enums import (
    InterventionStatus,
    TreatmentPlanStatus,
    TreatmentType,
)


@dataclass(frozen=True)
class TreatmentPlan:
    treatment_plan_id: str
    rtm_program_id: str
    patient_id: str
    treating_provider_id: str
    start_date: date
    expected_end_date: date | None
    status: TreatmentPlanStatus
    created_at: datetime
    updated_at: datetime
    # functional_limitation: str
    # medical_necessity_for_rtm: str
    # remote_monitoring_rationale: str


@dataclass(frozen=True)
class TreatmentIntervention:
    intervention_id: str
    treatment_plan_id: str
    treatment_type: TreatmentType
    description: str
    start_date: date
    end_date: date | None
    status: InterventionStatus


@dataclass(frozen=True)
class TherapeuticGoal:
    goal_id: str
    treatment_plan_id: str
    description: str
    target_date: date | None
    # outcome_measure_id: str
    # baseline_value: float | None
    # target_value: float | None
    # unit_of_measure: str | None
    # success_criteria: str


@dataclass(frozen=True)
class TreatmentMonitoringParameter:
    monitoring_parameter_id: str
    treatment_plan_id: str
    goal_id: str
    measure_definition_id: str
    baseline_value: float | None
    target_value: float | None
    unit: str | None


@dataclass(frozen=True)
class TreatmentPlanReview:
    review_id: str
    treatment_plan_id: str
    provider_id: str
    reviewed_at: datetime
    # measurement_period_id: str
    clinical_findings: str
    # interpretation: str
    treatment_decision: str
    next_review_date: date | None


"""
@dataclass(frozen=True)
class TreatmentPlanDiagnosis:
    treatment_plan_diagnosis_id: str
    treatment_plan_id: str
    diagnosis_id: str
    is_primary: bool


@dataclass(frozen=True)
class InterventionSchedule:
    schedule_id: str
    intervention_id: str
    frequency: str
    duration: str


@dataclass(frozen=True)
class OutcomeMeasure:
    outcome_measure_id: str
    treatment_plan_id: str
    name: str
    description: str
    unit: str | None


@dataclass(frozen=True)
class OutcomeMeasurement:
    measurement_id: str
    outcome_measure_id: str
    measured_at: datetime
    value: float
    measured_by_provider_id: str | None


@dataclass(frozen=True)
class MeasurementPeriod:
    measurement_period_id: str
    patient_id: str
    start_date: date
    end_date: date
    status: MeasurementPeriodStatus


@dataclass(frozen=True)
class TreatmentPlanChange:
    change_id: str
    treatment_plan_id: str
    changed_at: datetime
    changed_by_provider_id: str
    entity_type: TreatmentPlanEntityType
    entity_id: str
    field_name: str | None
    previous_value: str | None
    new_value: str | None
    reason: str
"""
