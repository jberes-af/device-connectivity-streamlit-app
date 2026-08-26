# /src/application/use_cases/residents/rtm/rtm_enrollment_uc_dtos.py

from dataclasses import dataclass
from datetime import date, datetime

from src.domain.enums.care.rtm_enums import (
    EnrollmentStatusEnum,
    ConsentStatusEnum,
    ConsentMethodEnum,
)


@dataclass(frozen=True)
class RtmEnrollmentDTO:
    enrollment_id: str
    patient_id: str
    enrollment_status: EnrollmentStatusEnum
    enrollment_date: date
    service_start_date: date
    service_end_date: date | None
    consent_status: ConsentStatusEnum
    consent_obtained_at: datetime | None
    consent_method: ConsentMethodEnum | None
    consent_document_reference: str | None
    discontinuation_reason: str | None


@dataclass(frozen=True)
class GetRtmEnrollmentRequestDTO:
    patient_id: str


@dataclass(frozen=True)
class GetRtmEnrollmentResultDTO:
    patient_id: str
    rtm_enrollments: tuple[RtmEnrollmentDTO, ...]
