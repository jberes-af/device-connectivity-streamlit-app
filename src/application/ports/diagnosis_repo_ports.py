# /src/application/ports/diagnosis_repo_ports.py

from typing import Protocol, Sequence

from src.domain.entities.care.diagnosis_entities import (
    DiagnosisDefinition,
)


class DiagnosisDefinitionRepositoryPort(Protocol):

    def list_diagnoses(self) -> tuple[DiagnosisDefinition, ...]:
        ...

    def get_by_id(
            self,
            diagnosis_id: str,
    ) -> DiagnosisDefinition:
        ...

    def get_by_ids(
            self,
            diagnosis_ids: Sequence[str],
    ) -> tuple[DiagnosisDefinition, ...]:
        ...
