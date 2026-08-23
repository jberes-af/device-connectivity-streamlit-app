# /src/application/services/get_diagnosis_service.py

from typing import Sequence

from src.domain.entities.care.diagnosis_entities import DiagnosisDefinition

from src.application.ports.diagnosis_repo_ports import (
    DiagnosisDefinitionRepositoryPort,
)


class FetchDiagnosisDefinitionService:

    def __init__(
            self,
            *,
            diagnosis_definition_repository: DiagnosisDefinitionRepositoryPort,
    ):
        self._diagnosis_repo = diagnosis_definition_repository

    def fetch_diagnosis_profile(
            self,
            diagnosis_id: str,
    ) -> DiagnosisDefinition:
        return self._diagnosis_repo.get_by_id(diagnosis_id=diagnosis_id)

    def fetch_diagnosis_profiles(
            self,
            diagnosis_ids: Sequence[str],
    ) -> tuple[DiagnosisDefinition, ...]:
        return tuple(
            self._diagnosis_repo.get_by_ids(
                diagnosis_ids=diagnosis_ids)
        )
