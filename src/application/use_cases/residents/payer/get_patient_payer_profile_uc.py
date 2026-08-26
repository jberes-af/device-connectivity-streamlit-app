# /src/application/use_cases/residents/payer/get_patient_payer_profile_uc.py

from src.application.services.payer.get_patient_payer_service import (
    FetchPatientPayerProfileService,
)

from src.domain.entities.person.patient_entities import (
    # Patient,
    PatientPayer,
)

from src.domain.entities.billing.payer_entities import PayerProfile

from src.application.services.payer.get_payer_profile_service import (
    FetchPayerProfileService,
)

from src.application.use_cases.residents.payer.patient_payer_uc_dtos import (
    PayerContactDTO,
    PatientPayerProfileDTO,
    GetPatientPayerProfileRequestDTO,
    GetPatientPayerProfileResultDTO
)


class GetPatientPayerProfileUseCase:

    def __init__(
            self,
            *,
            fetch_payer_profile_service: FetchPayerProfileService,
            fetch_patient_payer_service: FetchPatientPayerProfileService,
    ):
        self._fetch_payer_service = fetch_payer_profile_service
        self._fetch_patient_payer_service = fetch_patient_payer_service

    def execute(
            self,
            request: GetPatientPayerProfileRequestDTO,
    ) -> GetPatientPayerProfileResultDTO:
        # --- PATIENT RECORD FOR SELECTED PATIENT ID

        patient_id = request.patient_id

        patient_payers: tuple[PatientPayer, ...] = (
            self._fetch_patient_payer_service.fetch_payer_profiles_for_patient(
                patient_id=patient_id,
            ))

        payer_ids: list[str] = [
            payer.payer_id for payer in patient_payers
        ]

        payer_profiles: tuple[PayerProfile, ...] = (
            self._fetch_payer_service.fetch_payer_profiles(
                payer_ids=payer_ids,
            )
        )

        payer_by_id = {
            payer.payer_id: payer
            for payer in payer_profiles
        }

        result_profiles: tuple[PatientPayerProfileDTO, ...] = (
            self._to_dto(
                patient_payers=patient_payers,
                payer_by_id=payer_by_id,
            )
        )

        return GetPatientPayerProfileResultDTO(
            patient_payer_profiles=result_profiles,
        )

    @staticmethod
    def _to_dto(
            patient_payers: tuple[PatientPayer, ...],
            payer_by_id: dict[str, PayerProfile],
    ) -> tuple[PatientPayerProfileDTO, ...]:
        result_profiles = [
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
                payer_contact=PayerContactDTO(
                    claims_address_line_1=payer_by_id[patient_payer.payer_id].claims_address_line_1,
                    claims_address_line_2=payer_by_id[patient_payer.payer_id].claims_address_line_2,
                    city=payer_by_id[patient_payer.payer_id].city,
                    state=payer_by_id[patient_payer.payer_id].state,
                    postal_code=payer_by_id[patient_payer.payer_id].postal_code,
                    telephone=payer_by_id[patient_payer.payer_id].telephone,
                    website=payer_by_id[patient_payer.payer_id].website,
                    electronic_payer_id=payer_by_id[patient_payer.payer_id].electronic_payer_id,
                    accepts_electronic_claims=payer_by_id[patient_payer.payer_id].accepts_electronic_claims,
                )
            )
            for patient_payer in patient_payers
        ]

        return tuple(result_profiles)
