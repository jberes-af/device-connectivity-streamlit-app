# /src/application/ports/patient_repo_ports.py

from typing import Protocol

from src.domain.entities.person.patient_entities import (
    Patient,
    PatientDeviceAssignment,
    PatientDiagnosis,
    PatientEmergencyContact,
    PatientPayer,
    PatientProvider,
    RTMEnrollment,
)


class PatientRepositoryPort(Protocol):

    def list_patients(self) -> tuple[Patient, ...]:
        ...

    def get_by_id(
            self,
            patient_id: str,
    ) -> Patient:
        ...

    """
    def add_patient(
            self,
            patient_record: Patient,
    ) -> Patient:
        ...

    def update_patient(
            self,
            patient_record: Patient,
    ) -> Patient:
        ...
    """


class PatientDiagnosisRepositoryPort(Protocol):

    def list_patient_diagnoses(self) -> tuple[PatientDiagnosis, ...]:
        ...

    def get_by_id(
            self,
            patient_id: str,
    ) -> PatientDiagnosis:
        ...


class PatientProviderRepositoryPort(Protocol):

    def list_patient_providers(self) -> tuple[PatientProvider, ...]:
        ...

    def get_by_id(
            self,
            patient_id: str,
    ) -> PatientProvider:
        ...


class PatientPayerRepositoryPort(Protocol):

    def list_patient_payers(self) -> tuple[PatientPayer, ...]:
        ...

    def get_by_id(
            self,
            patient_id: str,
    ) -> PatientPayer:
        ...


class RTMEnrollmentRepositoryPort(Protocol):

    def list_rtm_enrollments(self) -> tuple[RTMEnrollment, ...]:
        ...

    def get_by_id(
            self,
            patient_id: str,
    ) -> RTMEnrollment:
        ...


class PatientDeviceAssignmentRepositoryPort(Protocol):

    def list_patient_device_assignments(self) -> tuple[PatientDeviceAssignment, ...]:
        ...

    def get_by_id(
            self,
            assignment_id: str,
    ) -> PatientDeviceAssignment:
        ...
