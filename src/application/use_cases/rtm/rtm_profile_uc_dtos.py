# /src/application/use_cases/rtm/rtm_profile_uc_dtos.py

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class RtmEnrollmentDTO:
    enrollment_date: date
    enrollment_status: str
    assigned_device: str | None
    consent_status: str
    consent_date: date | None
    patient_education_completed: bool


@dataclass(frozen=True, slots=True)
class RtmEnrollmentSummaryDTO:
    enrollment_status: str
    assigned_device: str | None
    consent_status: str


@dataclass(frozen=True)
class PatientOverviewDTO:
    enrollment_summary: RtmEnrollmentSummaryDTO


@dataclass(frozen=True)
class PatientSearchableRecordDTO:
    patient_id: str
    full_name: str
    date_of_birth: date
    city: str | None
    state: str | None
    telephone: str | None
    email: str | None
    treating_provider: str | None
    primary_payer: str | None


# --- DEV OBJECTS

@dataclass(frozen=True)
class PatientOverviewDevDTO:
    enrollment_summary: RtmEnrollmentSummaryDTO
    most_recent_provider_review_summary: str | None
    most_recent_communication_summary: str | None


# --- USE CASE

@dataclass(frozen=True)
class GetRtmProfileRequestDTO:
    patient_id: str


@dataclass(frozen=True)
class GetRtmProfileResultDTO:
    enrollment_summary: RtmEnrollmentSummaryDTO
