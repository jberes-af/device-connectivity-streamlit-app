# /src/application/use_cases/treatment/get_resident_profile_uc.py

from src.application.use_cases.patient.patient_uc_dtos import (
    PatientOverviewDevDTO,
    PatientAdministrationDTO,
    RTMEnrollmentSummaryDTO,
    PatientSearchableRecordDTO,

)


class GetResidentOverviewUseCase:

    def __init__(
            self,
            *,
            patient_repository: PatientRepositoryPort,
            patient_diagnosis_repository: PatientDiagnosisRepositoryPort,
            patient_provider_repository: PatientProviderRepositoryPort,
            patient_payer_repository: PatientPayerRepositoryPort,
            rtm_enrollment_repository: RTMEnrollmentRepositoryPort,

            provider_repository: ProviderRepositoryPort,
            payer_repository: PayerRepositoryPort,
    ):
        self._patient_repo = patient_repository
        self._patient_diagnosis_repository = patient_diagnosis_repository
        self._patient_provider_repository = patient_provider_repository
        self._patient_payer_repository = patient_payer_repository
        self._enrollment_repository = rtm_enrollment_repository

        self._provider_repository = provider_repository
        self._payer_repository = payer_repository

    def execute(
            self,
            request: GetPatientOverviewRequestDTO,
    ) -> GetPatientOverviewResultDTO:
        # --- PATIENT RECORD FOR SELECTED PATIENT ID

        patient_id = request.patient_id
        patient_record: Patient = self._patient_repo.get_by_id(
            payer_id=patient_id,
        )

        patient_diagnosis: PatientDiagnosis = self._patient_diagnosis_repository.get_by_id(
            payer_id=patient_id,
        )

        patient_provider: PatientProvider = self._patient_provider_repository.get_by_id(
            payer_id=patient_id,
        )

        patient_payer: PatientPayer = self._patient_payer_repository.get_by_id(
            payer_id=patient_id,
        )

        rtm_enrollment: RTMEnrollment = self._enrollment_repository.get_by_id(
            payer_id=patient_id,
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

        # --- PATIENT RECORDS FOR SEARCHABLE TABLE

        all_patient_records: tuple[PatientSearchableRecordDTO, ...] = (
            self._build_patient_table())

        return GetPatientOverviewResultDTO(
            overview=PatientOverviewDevDTO(
                administration=patient_admin,
                enrollment_summary=enrollment_summary,
                most_recent_provider_review_summary=None,
                most_recent_communication_summary=None,
            ),
            patient_table_records=all_patient_records,
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

    def _build_patient_table(self) -> tuple[PatientSearchableRecordDTO, ...]:

        records: tuple[Patient, ...] = self._patient_repo.list_patients()

        providers: dict[str, str] = {
            r.provider_id: f"{r.first_name} {r.last_name} ({r.provider_id})"
            for r in self._provider_repository.list_providers()
        }

        payers: dict[str, str] = {
            r.payer_id: f"{r.payer_name} ({r.payer_type})"
            for r in self._payer_repository.list_payers()
        }

        patient_providers: dict[str, str] = {
            r.provider_id: r.patient_id
            for r in self._patient_provider_repository.list_patient_providers()
        }

        patient_payers: dict[str, str] = {
            r.payer_id: r.patient_id
            for r in self._patient_payer_repository.list_patient_payers()
        }

        results: [PatientSearchableRecordDTO] = []

        for record in records:
            patient_id = record.patient_id

            payer_ids = [
                v for k, v in patient_payers.items()
                if v == patient_id
            ]

            provider_ids = [
                v for k, v in patient_providers.items()
                if v == patient_id
            ]

            treating_provider_id: str = provider_ids[0]
            treating_provider_name = providers.get(treating_provider_id, "---")
            treating_provider = (
                f"{treating_provider_name}, multiple"
                if len(provider_ids) > 1 else treating_provider_name)

            full_name: str = f"{record.first_name} {record.last_name}"
            results.append(PatientSearchableRecordDTO(
                patient_id=record.patient_id,
                full_name=full_name,
                date_of_birth=record.date_of_birth,
                city=record.city,
                state=record.state,
                telephone=record.telephone,
                email=record.email,
                treating_provider=treating_provider,
                primary_payer=None,
            ))

        return tuple(results)
