# /src/application/services/person/get_patient_diagnosis_service.py

from typing import Sequence

from src.domain.entities.person.patient_entities import (
    PatientDiagnosis
)

from src.application.ports.patient_repo_ports import (
    PatientDiagnosisRepositoryPort,
)


class FetchPatientDiagnosisService:

    def __init__(
            self,
            *,
            patient_diagnosis_repository: PatientDiagnosisRepositoryPort,
    ):
        self._patient_diagnosis_repo = patient_diagnosis_repository

    def fetch_diagnosis_profile_for_profile_id(
            self,
            patient_diagnosis_id: str,
    ) -> PatientDiagnosis:
        return self._patient_diagnosis_repo.get_by_id(
            patient_diagnosis_id=patient_diagnosis_id)

    def fetch_diagnosis_profiles_by_profile_id(
            self,
            patient_diagnosis_ids: Sequence[str],
    ) -> tuple[PatientDiagnosis, ...]:
        return tuple(
            self._patient_diagnosis_repo.get_by_ids(
                patient_diagnosis_ids=patient_diagnosis_ids)
        )

    def fetch_diagnosis_profiles_for_patient(
            self,
            patient_id: str,
    ) -> tuple[PatientDiagnosis, ...]:
        return tuple(
            self._patient_diagnosis_repo.list_diagnoses_for_patient_id(
                patient_id=patient_id)
        )
