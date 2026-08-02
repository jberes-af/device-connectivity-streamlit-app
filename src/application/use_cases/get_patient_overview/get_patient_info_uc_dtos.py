# /src/application/use_cases/get_patient_overview/get_patient_info_uc_dtos.py

from dataclasses import dataclass
from datetime import date

from src.domain.entities.patient_entities import Patient


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
class PatientPayerDTO:
    payer_name: str
    member_id: str
    group_number: str | None
    is_primary: bool


@dataclass(frozen=True)
class PatientProviderDTO:
    provider_name: str
    role: str


@dataclass(frozen=True)
class PatientOverviewDTO:
    administration: PatientAdministrationDTO
    enrollment_summary: RTMEnrollmentSummaryDTO
    current_summary: CurrentClinicalSummaryDTO

# --- DEV OBJECTS

@dataclass(frozen=True)
class PatientOverviewDevDTO:
    administration: PatientAdministrationDTO
    enrollment_summary: RTMEnrollmentSummaryDTO
    most_recent_provider_review_summary: str | None
    most_recent_communication_summary: str | None


# --- USE CASE

@dataclass(frozen=True)
class GetPatientOverviewRequestDTO:
    patient_id: str


@dataclass(frozen=True)
class GetPatientOverviewResultDTO:
    overview: PatientOverviewDevDTO
