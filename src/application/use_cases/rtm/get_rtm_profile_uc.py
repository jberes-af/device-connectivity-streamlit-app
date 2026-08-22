# /src/application/use_cases/rtm/get_rtm_profile_uc.py

from src.domain.entities.person.patient_entities import (
    RtmEnrollment,
)

from src.application.ports.rtm_repo_ports import RtmEnrollmentRepositoryPort

from src.application.use_cases.rtm.rtm_profile_uc_dtos import (
    RtmEnrollmentSummaryDTO,
    GetRtmProfileRequestDTO,
    GetRtmProfileResultDTO,
)


class GetPatientOverviewUseCase:

    def __init__(
            self,
            *,
            rtm_enrollment_repository: RtmEnrollmentRepositoryPort,

    ):
        self._enrollment_repository = rtm_enrollment_repository

    def execute(
            self,
            request: GetRtmProfileRequestDTO,
    ) -> GetRtmProfileResultDTO:
        # --- PATIENT RECORD FOR SELECTED PATIENT ID

        patient_id = request.patient_id

        rtm_enrollment: RtmEnrollment = self._enrollment_repository.get_by_id(
            patient_id=patient_id,
        )

        enrollment_summary: RtmEnrollmentSummaryDTO = (
            self._build_rtm_enrollment_summary(
                rtm_enrollment=rtm_enrollment,
            ))

        return GetRtmProfileResultDTO(
            enrollment_summary=enrollment_summary,
        )

    @staticmethod
    def _build_rtm_enrollment_summary(
            rtm_enrollment: RtmEnrollment

    ) -> RtmEnrollmentSummaryDTO:
        return RtmEnrollmentSummaryDTO(
            enrollment_status=rtm_enrollment.enrollment_status,
            assigned_device=None,
            consent_status=rtm_enrollment.consent_status,
        )
