# /src/application/ports/rtm_repo_ports.py

from typing import Protocol, Sequence

from src.domain.entities.care.rtm_entities import (
    RtmEnrollment,
    RtmMedicalNecessity,
)


class RtmEnrollmentRepositoryPort(Protocol):

    def list_rtm_enrollments(self) -> tuple[RtmEnrollment, ...]:
        ...

    def get_by_id(
            self,
            rtm_enrollment_id: str,
    ) -> RtmEnrollment:
        ...

    def get_by_ids(
            self,
            rtm_enrollment_ids: Sequence[str],
    ) -> tuple[RtmEnrollment, ...]:
        ...


class RtmNecessityRepositoryPort(Protocol):

    def list_rtm_necessity_records(self) -> tuple[RtmMedicalNecessity, ...]:
        ...

    def get_by_id(
            self,
            rtm_necessity_id: str,
    ) -> RtmMedicalNecessity:
        ...

    def get_by_ids(
            self,
            rtm_necessity_ids: Sequence[str],
    ) -> tuple[RtmMedicalNecessity, ...]:
        ...

    def list_rtm_necessity_records_patient_id(
            self,
            patient_id: str,
    ) -> tuple[RtmMedicalNecessity, ...]:
        ...
