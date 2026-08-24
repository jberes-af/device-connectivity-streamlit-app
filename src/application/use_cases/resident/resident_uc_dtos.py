# /src/application/use_cases/person/resident_uc_dtos.py

from src.domain.enums.person.tenant_enums import UserRoleEnum

from src.domain.entities.access.access_entities import ResidentGatewayLink, ResidentSensorLink

from src.domain.entities.person.resident_entities import (
    ResidentProfile,
    ResidentInCaseOfNeedContact,
)

from dataclasses import dataclass
from datetime import date

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
"""


@dataclass(frozen=True)
class ResidentProfileDTO:
    resident_id: str
    resident_profile: ResidentProfile


@dataclass(frozen=True)
class ResidentSearchableRecordDTO:
    resident_id: str
    full_name: str
    date_of_birth: date
    contact_name: str | None
    active_status: bool | None
    # telephone: str | None
    # email: str | None
    # treating_provider: str | None
    # primary_payer: str | None


# --- DEV OBJECTS

@dataclass(frozen=True)
class ResidentOverviewDevDTO:
    resident_profile: ResidentProfile
    # enrollment_summary: RTMEnrollmentSummaryDTO
    sensor_links: tuple[ResidentSensorLink, ...]
    gateway_links: tuple[ResidentGatewayLink, ...]


# --- USE CASES

@dataclass(frozen=True)
class GetAllResidentRecordsRequestDTO:
    user_id: str
    user_tenant_id: str
    user_role: UserRoleEnum


@dataclass(frozen=True)
class GetAllResidentRecordsResultDTO:
    # summary: ResidentOverviewDevDTO | None
    resident_profiles: tuple[ResidentProfile, ...]
    resident_need_case_contacts: tuple[ResidentInCaseOfNeedContact, ...]
    resident_table_records: tuple[ResidentSearchableRecordDTO, ...]


"""
@dataclass(frozen=True)
class GetResidentOverviewRequestDTO:
    resident_id: str


@dataclass(frozen=True)
class GetResidentOverviewResultDTO:
    overview: PatientOverviewDevDTO
    patient_table_records: tuple[PatientSearchableRecordDTO, ...]
"""
