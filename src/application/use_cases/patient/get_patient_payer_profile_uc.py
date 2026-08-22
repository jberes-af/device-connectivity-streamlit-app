# /src/application/use_cases/patient/get_patient_payer_profile_uc.py

from src.domain.entities.person.patient_entities import (
    # Patient,
    PatientPayer,
)

from src.domain.entities.billing.payer_entities import PayerProfile

from src.application.ports.patient_repo_ports import (
    PatientPayerRepositoryPort,
)

from src.application.services.get_payer_profile_service import (
    FetchPayerProfileService,
)

from src.application.use_cases.patient.patient_profile_uc_dtos import (
    PatientPayerProfileDTO,
    GetPatientPayerProfileRequestDTO,
    GetPatientPayerProfileResultDTO,
)


class GetPatientPayerProfileUseCase:

    def __init__(
            self,
            *,
            fetch_payer_profile_service: FetchPayerProfileService,
            patient_payer_repository: PatientPayerRepositoryPort,
    ):
        self._fetch_payer_service = fetch_payer_profile_service
        self._patient_payer_repo = patient_payer_repository

    def execute(
            self,
            request: GetPatientPayerProfileRequestDTO,
    ) -> GetPatientPayerProfileResultDTO:
        # --- PATIENT RECORD FOR SELECTED PATIENT ID

        patient_id = request.patient_id

        """
        patient_record: Patient = self._patient_repo.get_by_id(
            patient_id=patient_id,
        )
        """

        patient_payers: tuple[PatientPayer, ...] = (
            self._patient_payer_repo.get_all_payers_for_patient_id(
                patient_id=patient_id,
            )
        )

        payer_profiles: tuple[PayerProfile, ...] = (
            self._fetch_payer_service.fetch_payer_profiles(
                payer_ids=tuple(
                    payer.payer_id
                    for payer in patient_payers
                ),
            )
        )

        payer_by_id = {
            payer.payer_id: payer
            for payer in payer_profiles
        }

        result_profiles = tuple(
            PatientPayerProfileDTO(
                patient_payer_id=patient_payer.patient_payer_id,
                payer_id=patient_payer.payer_id,
                payer_name=payer_by_id[patient_payer.payer_id].payer_name,
                payer_type=payer_by_id[patient_payer.payer_id].payer_type,
                member_id=patient_payer.member_id,
                group_number=patient_payer.group_number,
                effective_date=patient_payer.effective_date,
                termination_date=patient_payer.termination_date,
                is_primary=patient_payer.is_primary,
            )
            for patient_payer in patient_payers
        )

        return GetPatientPayerProfileResultDTO(
            payer_profiles=result_profiles,
        )
