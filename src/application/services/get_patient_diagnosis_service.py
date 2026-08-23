# /src/application/services/get_patient_diagnosis_service.py

from typing import Sequence

from src.domain.entities.person.patient_entities import PatientDiagnosisProfile

from src.application.ports.treatment_repo_ports import (
    PatientDiagnosisRepositoryPort,
)


class FetchPatientDiagnosisService:

    def __init__(
            self,
            *,
            patient_diagnosis_repository: DiagnosisRepositoryPort,
    ):
        self._patient_diagnosis_repo = patient_diagnosis_repository

    def fetch_diagnosis_profile(
            self,
            diagnosis_id: str,
    ) -> DiagnosisProfile:
        return self._patient_diagnosis_repo.get_by_id(diagnosis_id=diagnosis_id)

    def fetch_diagnosis_profiles(
            self,
            diagnosis_ids: Sequence[str],
    ) -> tuple[DiagnosisProfile, ...]:
        return tuple(
            self._patient_diagnosis_repo.get_by_ids(
                diagnosis_ids=diagnosis_ids)
        )
