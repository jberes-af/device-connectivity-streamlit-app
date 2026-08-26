# /src/application/use_cases/residents/payer/get_payer_and_rtm_enrollment_uc.py

from src.application.use_cases.residents.payer.patient_payer_uc_dtos import (
    GetPatientPayerProfileRequestDTO,
    GetPatientPayerProfileResultDTO,
)

from src.application.use_cases.residents.rtm.rtm_enrollment_uc_dtos import (
    GetRtmEnrollmentRequestDTO,
    GetRtmEnrollmentResultDTO,
)

from src.application.use_cases.residents.payer.get_patient_payer_profile_uc import (
    GetPatientPayerProfileUseCase,
)

from src.application.use_cases.residents.rtm.get_rtm_enrollment_uc import (
    GetRtmEnrollmentUseCase,
)

from src.application.use_cases.residents.payer.patient_payer_and_rtm_enrollment_uc_dtos import (
    GetPatientPayersAndRtmEnrollmentRequestDTO,
    GetPatientPayersAndRtmEnrollmentResultDTO,
)


class GetPatientPayerAndRtmEnrollmentUseCase:

    def __init__(
            self,
            *,
            get_patient_payer_profile_use_case: GetPatientPayerProfileUseCase,
            get_rtm_enrollment_use_case: GetRtmEnrollmentUseCase,
    ) -> None:
        self._payer_use_case = get_patient_payer_profile_use_case

        self._rtm_enrollment_use_case = get_rtm_enrollment_use_case

    def execute(
            self,
            request: GetPatientPayersAndRtmEnrollmentRequestDTO,
    ) -> GetPatientPayersAndRtmEnrollmentResultDTO:
        payer_result: GetPatientPayerProfileResultDTO = (
            self._payer_use_case.execute(
                GetPatientPayerProfileRequestDTO(
                    patient_id=request.patient_id,
                )
            )
        )

        enrollment_result: GetRtmEnrollmentResultDTO = (
            self._rtm_enrollment_use_case.execute(
                GetRtmEnrollmentRequestDTO(
                    patient_id=request.patient_id,
                )
            )
        )

        return GetPatientPayersAndRtmEnrollmentResultDTO(
            patient_id=request.patient_id,
            patient_payer_profiles=(
                payer_result.patient_payer_profiles
            ),
            rtm_enrollments=enrollment_result.rtm_enrollments,
        )
