# /src/domain/entities/person/patient_entities.py

from dataclasses import dataclass
from datetime import date, datetime

from src.domain.enums.person.patient_enums import (
    ConsentMethod,
    ConsentStatus,
    EnrollmentStatus,
    # MonitoringStatus,
    PatientProviderRole,
)


@dataclass(frozen=True)
class Patient:
    patient_id: str
    first_name: str
    middle_name: str | None
    last_name: str
    date_of_birth: date
    telephone: str | None
    email: str | None
    address_line_1: str | None
    address_line_2: str | None
    city: str | None
    state: str | None
    postal_code: str | None


@dataclass(frozen=True)
class PatientDiagnosis:
    patient_diagnosis_id: str
    patient_id: str
    diagnosis_id: str
    diagnosed_date: date | None
    resolved_date: date | None
    is_primary: bool


@dataclass(frozen=True)
class PatientProvider:
    patient_provider_id: str
    patient_id: str
    provider_id: str
    role: PatientProviderRole
    effective_date: date | None
    termination_date: date | None


@dataclass(frozen=True)
class PatientPayer:
    patient_payer_id: str
    patient_id: str
    payer_id: str
    member_id: str
    group_number: str | None
    is_primary: bool
    effective_date: date | None
    termination_date: date | None


@dataclass(frozen=True)
class PatientEmergencyContact:
    emergency_contact_id: str
    patient_id: str
    name: str
    relationship: str
    telephone: str


@dataclass(frozen=True)
class RTMEnrollment:
    enrollment_id: str
    patient_id: str
    enrollment_status: EnrollmentStatus
    enrollment_date: date
    service_start_date: date
    service_end_date: date | None
    consent_status: ConsentStatus
    consent_obtained_at: datetime | None
    consent_method: ConsentMethod | None
    consent_document_reference: str | None
    discontinuation_reason: str | None


@dataclass(frozen=True)
class PatientDeviceAssignment:
    assignment_id: str
    patient_id: str
    device_id: str
    assigned_date: date
    removed_date: date | None
    setup_completed: bool
    setup_date: date | None
    patient_education_completed: bool
    patient_education_date: date | None
