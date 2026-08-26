# /src/application/services/payer/get_patient_payer_service.py

from typing import Sequence

from src.domain.entities.person.patient_entities import PatientPayer

from src.application.ports.patient_repo_ports import (
    PatientPayerRepositoryPort,
)


class FetchPatientPayerProfileService:

    def __init__(
            self,
            *,
            patient_payer_repository: PatientPayerRepositoryPort,
    ):
        self._payer_repo = patient_payer_repository

    def fetch_payer_profile(
            self,
            patient_payer_id: str,
    ) -> PatientPayer:
        return self._payer_repo.get_by_id(
            patient_payer_id=patient_payer_id)

    def fetch_payer_profiles(
            self,
            patient_payer_ids: Sequence[str],
    ) -> tuple[PatientPayer, ...]:
        return tuple(
            self._payer_repo.get_by_ids(
                patient_payer_ids=patient_payer_ids)
        )

    def fetch_payer_profiles_for_patient(
            self,
            patient_id: str,
    ) -> tuple[PatientPayer, ...]:
        return tuple(
            self._payer_repo.list_patient_payers_for_patient_id(
                patient_id=patient_id)
        )
