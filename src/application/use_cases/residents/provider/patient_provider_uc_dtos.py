# /src/application/use_cases/residents/provider/patient_provider_uc_dtos.py

from dataclasses import dataclass
from datetime import date

from src.domain.enums.access.status_and_method_enums import PatientProviderRoleEnum


@dataclass(frozen=True)
class PatientProviderProfileDTO:
    patient_provider_id: str
    provider_id: str
    national_provider_identifier: str | None
    first_name: str
    middle_name: str | None
    last_name: str
    credentials: str | None
    role: PatientProviderRoleEnum
    specialty: str | None
    organization_id: str | None
    effective_date: date | None
    termination_date: date | None
    is_active: bool


# --- USE CASES


@dataclass(frozen=True)
class GetPatientProviderProfileRequestDTO:
    patient_id: str


@dataclass(frozen=True)
class GetPatientProviderProfileResultDTO:
    provider_profiles: tuple[PatientProviderProfileDTO, ...]


"""
@dataclass(frozen=True)
class PatientAdministrationDTO:
    patient_id: str
    full_name: str
    date_of_birth: date
    primary_diagnosis: str
    treating_provider: str
    primary_payer: str
    telephone: str | None
    email: str | None


@dataclass(frozen=True)
class CurrentClinicalSummaryDTO:
    patient_id: str
    medical_necessity_summary: str
    treatment_plan_summary: str | None
    therapeutic_goal_summaries: tuple[str, ...]
    monitoring_period_start: date | None
    monitoring_period_end: date | None
    # recent_clinical_alert_count: int
    # monthly_trend_summary: str | None
    most_recent_provider_review_summary: str | None
    most_recent_communication_summary: str | None
    billing_readiness_status: str
    missing_billing_requirements: tuple[str, ...]


@dataclass(frozen=True)
class RTMEnrollmentDTO:
    enrollment_date: date
    enrollment_status: str
    assigned_device: str | None
    consent_status: str
    consent_date: date | None
    patient_education_completed: bool


@dataclass(frozen=True, slots=True)
class RTMEnrollmentSummaryDTO:
    enrollment_status: str
    assigned_device: str | None
    consent_status: str

@dataclass(frozen=True)
class DiagnosisAndMedicalNecessityDTO:
    primary_diagnosis: str
    relevant_secondary_diagnoses: tuple[str, ...]
    functional_limitation: str
    medical_necessity_for_rtm: str
    remote_monitoring_rationale: str



@dataclass(frozen=True)
class GetPatientDiagnosesRequestDTO:
    patient_id: str


@dataclass(frozen=True)
class GetPatientDiagnosesResultDTO:
    patient_diagnoses: tuple[DiagnosisAndMedicalNecessityDTO, ...]


"""
