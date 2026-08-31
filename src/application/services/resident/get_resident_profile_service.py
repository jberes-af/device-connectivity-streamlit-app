# /src/application/services/resident/get_resident_profile_service.py

from typing import Sequence

from src.domain.entities.person.resident_entities import (
    ResidentProfile
)

from src.application.ports.resident_repo_ports import (
    ResidentProfileRepositoryPort,
)


class FetchResidentProfileService:

    def __init__(
            self,
            *,
            resident_profile_repository: ResidentProfileRepositoryPort,
    ):
        self._profile_repo = resident_profile_repository

    def fetch_resident_profile(
            self,
            resident_id: str,
    ) -> ResidentProfile:
        return self._profile_repo.get_by_id(
            resident_id=resident_id)

    def fetch_resident_profiles(
            self,
            resident_ids: Sequence[str],
    ) -> tuple[ResidentProfile, ...]:
        return tuple(
            self._profile_repo.get_by_ids(
                resident_ids=resident_ids)
        )
