# /src/application/ports/resident_repo_ports.py

from typing import Protocol

from src.domain.entities.person.resident_entities import (
    ResidentProfile,
    ResidentInCaseOfNeedContact,
)


class ResidentProfileRepositoryPort(Protocol):

    def list_resident_profiles(self) -> tuple[ResidentProfile, ...]:
        ...

    def get_by_id(
            self,
            resident_id: str,
    ) -> ResidentProfile:
        ...


class ResidentContactInformationRepositoryPort(Protocol):

    def get_by_id(
            self,
            resident_id: str,
    ) -> ResidentInCaseOfNeedContact:
        ...


