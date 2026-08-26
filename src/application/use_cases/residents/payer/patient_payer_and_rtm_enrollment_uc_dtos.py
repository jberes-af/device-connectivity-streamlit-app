# /src/application/use_cases/residents/payer/patient_payer_and_rtm_enrollment_uc_dtos.py

from dataclasses import dataclass

from src.application.use_cases.residents.payer.patient_payer_uc_dtos import (
    PatientPayerProfileDTO,
)

from src.application.use_cases.residents.rtm.rtm_enrollment_uc_dtos import (
    RtmEnrollmentDTO,
)


@dataclass(frozen=True)
class GetPatientPayersAndRtmEnrollmentRequestDTO:
    patient_id: str


@dataclass(frozen=True)
class GetPatientPayersAndRtmEnrollmentResultDTO:
    patient_id: str
    patient_payer_profiles: tuple[PatientPayerProfileDTO, ...]
    rtm_enrollments: tuple[RtmEnrollmentDTO, ...]
