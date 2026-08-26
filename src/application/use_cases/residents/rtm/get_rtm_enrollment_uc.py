# /src/application/use_cases/residents/rtm/get_rtm_enrollment_uc.py

from src.domain.entities.care.rtm_entities import RtmEnrollment

from src.application.services.care.get_rtm_service import (
    FetchRtmEnrollmentService
)

from src.application.use_cases.residents.rtm.rtm_enrollment_uc_dtos import (
    RtmEnrollmentDTO,
    GetRtmEnrollmentRequestDTO,
    GetRtmEnrollmentResultDTO,
)


class GetRtmEnrollmentUseCase:

    def __init__(
            self,
            *,
            fetch_rtm_enrollment_service: FetchRtmEnrollmentService,
    ) -> None:
        self._rtm_service = fetch_rtm_enrollment_service

    def execute(
            self,
            request: GetRtmEnrollmentRequestDTO,
    ) -> GetRtmEnrollmentResultDTO:
        enrollments: tuple[RtmEnrollment, ...] = (
            self._rtm_service.fetch_rtm_enrollment_for_patient(
                patient_id=request.patient_id,
            ))

        return GetRtmEnrollmentResultDTO(
            patient_id=request.patient_id,
            rtm_enrollments=tuple(
                self._to_dto(enrollment)
                for enrollment in enrollments
            ),
        )

    @staticmethod
    def _to_dto(
            enrollment: RtmEnrollment,
    ) -> RtmEnrollmentDTO:
        return RtmEnrollmentDTO(
            enrollment_id=enrollment.enrollment_id,
            patient_id=enrollment.patient_id,
            enrollment_status=enrollment.enrollment_status,
            enrollment_date=enrollment.enrollment_date,
            service_start_date=enrollment.service_start_date,
            service_end_date=enrollment.service_end_date,
            consent_status=enrollment.consent_status,
            consent_obtained_at=enrollment.consent_obtained_at,
            consent_method=enrollment.consent_method,
            consent_document_reference=(
                enrollment.consent_document_reference
            ),
            discontinuation_reason=(
                enrollment.discontinuation_reason
            ),
        )
