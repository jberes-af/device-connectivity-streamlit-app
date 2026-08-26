# /src/application/use_cases/residents/treatment/diagnoses_and_treatment_uc_dtos.py

from dataclasses import dataclass
from datetime import date, datetime

from src.domain.enums.care.rtm_enums import (
    ClinicalIndicationEnum,
    RtmClinicalUseEnum,
    RtmNecessityStatus,
    RtmMonitoringReasonEnum,
)

from src.domain.enums.care.treatment_enums import (
    InterventionStatus,
    TreatmentPlanStatus,
    TreatmentType,
)


# --- PATIENT DIAGNOSIS


@dataclass(frozen=True)
class DiagnosisDTO:
    patient_diagnosis_id: str
    diagnosis_id: str
    diagnosis_name: str
    diagnosis_description: str
    diagnosed_date: date | None
    resolved_date: date | None
    is_primary: bool


# --- TREATMENT PLAN


@dataclass(frozen=True)
class TreatmentPlanDTO:
    treatment_plan_id: str
    patient_id: str
    rtm_program_id: str
    treating_provider_id: str
    start_date: date
    expected_end_date: date | None
    status: TreatmentPlanStatus
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class TherapeuticGoalDTO:
    goal_id: str
    treatment_plan_id: str
    description: str
    target_date: date | None


@dataclass(frozen=True)
class TreatmentInterventionDTO:
    intervention_id: str
    treatment_plan_id: str
    treatment_type: TreatmentType
    description: str
    start_date: date
    end_date: date | None
    status: InterventionStatus


@dataclass(frozen=True)
class TreatmentMonitoringParameterDTO:
    monitoring_parameter_id: str
    treatment_plan_id: str
    goal_id: str
    measure_definition_id: str
    baseline_value: float | None
    target_value: float | None
    unit: str | None


@dataclass(frozen=True)
class TreatmentPlanReviewDTO:
    review_id: str
    treatment_plan_id: str
    provider_id: str
    reviewed_at: datetime
    clinical_findings: str
    treatment_decision: str
    next_review_date: date | None


@dataclass(frozen=True)
class TherapeuticPlanDTO:
    treatment_plan: TreatmentPlanDTO
    goals: tuple[TherapeuticGoalDTO, ...]
    interventions: tuple[TreatmentInterventionDTO, ...]
    monitoring_parameters: tuple[TreatmentMonitoringParameterDTO, ...]
    reviews: tuple[TreatmentPlanReviewDTO, ...]


# --- RTM NECESSITY


@dataclass(frozen=True, slots=True)
class RtmNecessityDTO:
    rtm_necessity_id: str
    rtm_program_id: str
    patient_id: str
    treatment_plan_id: str
    primary_diagnosis_code: str
    secondary_diagnosis_codes: tuple[str, ...]
    clinical_indications: tuple[ClinicalIndicationEnum, ...]
    clinical_indication_notes: str | None
    monitoring_reasons: tuple[RtmMonitoringReasonEnum, ...]
    monitoring_rationale: str
    expected_clinical_benefit: str
    intended_clinical_uses: tuple[RtmClinicalUseEnum, ...]
    determined_by_provider_id: str
    determined_at: datetime
    is_attested: bool
    attestation_version: str
    effective_from: datetime
    effective_to: datetime | None
    status: RtmNecessityStatus
    last_reviewed_at: datetime | None = None
    last_reviewed_by_provider_id: str | None = None


# --- USE CASE


@dataclass(frozen=True)
class GetDiagnosesAndTreatmentRequestDTO:
    patient_id: str


@dataclass(frozen=True)
class GetDiagnosisAndTreatmentResultDTO:
    patient_id: str
    diagnoses: tuple[DiagnosisDTO, ...]
    treatment_plans: tuple[TherapeuticPlanDTO, ...]
    rtm_necessity_records: tuple[RtmNecessityDTO, ...]
