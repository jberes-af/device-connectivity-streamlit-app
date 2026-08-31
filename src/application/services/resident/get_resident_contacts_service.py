# /src/application/services/resident/get_resident_contacts_service.py

from typing import Sequence

from src.domain.entities.person.resident_entities import (
    ResidentInCaseOfNeedContact
)

from src.application.ports.resident_repo_ports import (
    ResidentContactInformationRepositoryPort,
)


class FetchResidentContactsService:

    def __init__(
            self,
            *,
            resident_contacts_repository: ResidentContactInformationRepositoryPort,
    ):
        self._contacts_repo = resident_contacts_repository

    def fetch_resident_contacts_profile(
            self,
            resident_id: str,
    ) -> ResidentInCaseOfNeedContact:
        return self._contacts_repo.get_by_id(resident_id=resident_id)

    def fetch_resident_contacts_profiles(
            self,
            resident_ids: Sequence[str],
    ) -> tuple[ResidentInCaseOfNeedContact, ...]:
        return tuple(
            self._contacts_repo.get_by_ids(
                resident_ids=resident_ids)
        )
