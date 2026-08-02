# /src/application/use_cases/get_patient_overview/get_patient_overview_uc.py

from src.domain.entities.patient_entities import (
    Patient,
    PatientDiagnosis,
    PatientProvider,
    PatientPayer, RTMEnrollment,
)

from src.application.ports.patient_repo_ports import (
    PatientRepositoryPort,
    PatientDiagnosisRepositoryPort,
    PatientProviderRepositoryPort,
    PatientPayerRepositoryPort,
    RTMEnrollmentRepositoryPort,
)

from src.application.use_cases.get_patient_overview.get_patient_info_uc_dtos import (
    PatientOverviewDevDTO,
    PatientAdministrationDTO,
    RTMEnrollmentSummaryDTO,

    GetPatientOverviewRequestDTO,
    GetPatientOverviewResultDTO,
)


class GetPatientOverviewUseCase:

    def __init__(
            self,
            *,
            patient_repository: PatientRepositoryPort,
            patient_diagnosis_repository: PatientDiagnosisRepositoryPort,
            patient_provider_repository: PatientProviderRepositoryPort,
            patient_payer_repository: PatientPayerRepositoryPort,
            rtm_enrollment_repository: RTMEnrollmentRepositoryPort,
    ):
        self._patient_repo = patient_repository
        self._patient_diagnosis_repository = patient_diagnosis_repository
        self._patient_provider_repository = patient_provider_repository
        self._patient_payer_repository = patient_payer_repository
        self._enrollment_repository = rtm_enrollment_repository

    def execute(
            self,
            request: GetPatientOverviewRequestDTO,
    ) -> GetPatientOverviewResultDTO:
        patient_id = request.patient_id
        patient_record: Patient = self._patient_repo.get_by_id(
            patient_id=patient_id,
        )

        patient_diagnosis: PatientDiagnosis = self._patient_diagnosis_repository.get_by_id(
            patient_id=patient_id,
        )

        patient_provider: PatientProvider = self._patient_provider_repository.get_by_id(
            patient_id=patient_id,
        )

        patient_payer: PatientPayer = self._patient_payer_repository.get_by_id(
            patient_id=patient_id,
        )

        rtm_enrollment: RTMEnrollment = self._enrollment_repository.get_by_id(
            patient_id=patient_id,
        )

        patient_admin: PatientAdministrationDTO = (
            self._build_patient_admin_object(
                patient_id=patient_id,
                patient=patient_record,
                diagnosis=patient_diagnosis,
                provider=patient_provider,
                payer=patient_payer,
            ))

        enrollment_summary: RTMEnrollmentSummaryDTO = (
            self._build_rtm_enrollment_summary(
                rtm_enrollment=rtm_enrollment,
            ))

        return GetPatientOverviewResultDTO(
            overview=PatientOverviewDevDTO(
                administration=patient_admin,
                enrollment_summary=enrollment_summary,
                most_recent_provider_review_summary=None,
                most_recent_communication_summary=None,
            )
        )

    @staticmethod
    def _build_patient_admin_object(
            patient_id: str,
            patient: Patient,
            diagnosis: PatientDiagnosis,
            provider: PatientProvider,
            payer: PatientPayer,
    ) -> PatientAdministrationDTO:

        if patient.middle_name:
            full_name: str = (
                f'{patient.first_name} {patient.middle_name}. {patient.last_name}'
            )
        else:
            full_name: str = f'{patient.first_name} {patient.last_name}'

        return PatientAdministrationDTO(
            patient_id=patient_id,
            full_name=full_name,
            date_of_birth=patient.date_of_birth,
            primary_diagnosis=diagnosis.diagnosis_id,
            treating_provider=provider.provider_id,
            primary_payer=payer.payer_id,
            telephone=patient.telephone,
            email=patient.email,
        )

    @staticmethod
    def _build_rtm_enrollment_summary(
            rtm_enrollment: RTMEnrollment

    ) -> RTMEnrollmentSummaryDTO:
        return RTMEnrollmentSummaryDTO(
            enrollment_status=rtm_enrollment.enrollment_status,
            assigned_device=None,
            consent_status=rtm_enrollment.consent_status,
        )
