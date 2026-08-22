# /src/application/ports/rtm_repo_ports.py

from typing import Protocol

from src.domain.entities.person.patient_entities import RtmEnrollment


class RtmEnrollmentRepositoryPort(Protocol):

    def list_rtm_enrollments(self) -> tuple[RtmEnrollment, ...]:
        ...

    def get_by_id(
            self,
            patient_id: str,
    ) -> RtmEnrollment:
        ...
