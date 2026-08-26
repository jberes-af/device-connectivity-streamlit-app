# /src/domain/treatment/diagnosis_entities.py

from dataclasses import dataclass


@dataclass(frozen=True)
class DiagnosisDefinition:
    diagnosis_id: str
    diagnosis_name: str
    diagnosis_description: str
