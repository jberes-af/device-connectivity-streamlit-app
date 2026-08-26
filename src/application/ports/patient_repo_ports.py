# /src/application/ports/patient_repo_ports.py

from typing import Protocol, Sequence

from src.domain.entities.person.patient_entities import (
    PatientPayer,
    PatientProvider,
    PatientDiagnosis,
)


class PatientDiagnosisRepositoryPort(Protocol):

    def list_patient_diagnoses(self) -> tuple[PatientDiagnosis, ...]:
        ...

    def get_by_id(
            self,
            patient_diagnosis_id: str,
    ) -> PatientDiagnosis:
        ...

    def get_by_ids(
            self,
            patient_diagnosis_ids: Sequence[str],
    ) -> tuple[PatientDiagnosis, ...]:
        ...

    def list_diagnoses_for_patient_id(
            self,
            patient_id: str,
    ) -> tuple[PatientDiagnosis, ...]:
        ...


class PatientProviderRepositoryPort(Protocol):

    def list_patient_providers(self) -> tuple[PatientProvider, ...]:
        ...

    def list_providers_for_patient_id(
            self,
            patient_id: str,
    ) -> tuple[PatientProvider, ...]:
        ...

    def get_by_id(
            self,
            patient_provider_id: str,
    ) -> PatientProvider:
        ...


class PatientPayerRepositoryPort(Protocol):

    def list_patient_payers(self) -> tuple[PatientPayer, ...]:
        ...

    def get_by_id(
            self,
            patient_payer_id: str,
    ) -> PatientPayer:
        ...

    def get_by_ids(
            self,
            patient_payer_ids: Sequence[str],
    ) -> tuple[PatientPayer, ...]:
        ...

    def list_patient_payers_for_patient_id(
            self,
            patient_id: str,
    ) -> tuple[PatientPayer, ...]:
        ...


"""
class PatientRepositoryPort(Protocol):

    def list_patients(self) -> tuple[Patient, ...]:
        ...

    def get_by_id(
            self,
            patient_id: str,
    ) -> Patient:
        ...

class PatientDeviceAssignmentRepositoryPort(Protocol):

    def list_patient_device_assignments(self) -> tuple[PatientDeviceAssignment, ...]:
        ...

    def get_by_id(
            self,
            assignment_id: str,
    ) -> PatientDeviceAssignment:
        ...
"""
