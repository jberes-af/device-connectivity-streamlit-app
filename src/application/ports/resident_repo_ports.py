# /src/application/ports/resident_repo_ports.py

from typing import Protocol, Sequence

from src.domain.entities.resident.resident_entities import (
    ResidentProfile,
    ResidentInCaseOfNeedContact,
)


class ResidentProfileRepositoryPort(Protocol):

    def list_resident_profiles(
            self,
    ) -> tuple[ResidentProfile, ...]:
        ...

    def get_by_id(
            self,
            resident_id: str,
    ) -> ResidentProfile:
        ...

    def get_by_ids(
            self,
            resident_ids: Sequence[str],
    ) -> tuple[ResidentProfile, ...]:
        ...

    def list_profiles_for_tenant_ids(
            self,
            tenant_ids: Sequence[str],
    ) -> tuple[ResidentProfile, ...]:
        ...


class ResidentContactInformationRepositoryPort(Protocol):

    def get_by_id(
            self,
            resident_id: str,
    ) -> ResidentInCaseOfNeedContact:
        ...

    def get_by_ids(
            self,
            resident_ids: Sequence[str],
    ) -> tuple[ResidentInCaseOfNeedContact, ...]:
        ...
