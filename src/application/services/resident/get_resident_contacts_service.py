# /src/application/services/resident/get_resident_contacts_service.py

import inspect

from typing import Sequence

from src.domain.entities.resident.resident_entities import (
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
        print()
        print("CONTACT SERVICE DEBUG")
        print("repo object:", self._contacts_repo)
        print("repo type:", type(self._contacts_repo))
        print("repo module:", type(self._contacts_repo).__module__)
        print("repo source:", inspect.getfile(type(self._contacts_repo)))
        print("has get_by_ids:", hasattr(self._contacts_repo, "get_by_ids"))
        print(
            "get_by_ids defined on concrete class:",
            "get_by_ids" in type(self._contacts_repo).__dict__,
        )
        print("get_by_ids:", getattr(self._contacts_repo, "get_by_ids", None))
        print()

        result = self._contacts_repo.get_by_ids(
            resident_ids=resident_ids,
        )

        print("repository result:", result)
        print("repository result type:", type(result))

        return result