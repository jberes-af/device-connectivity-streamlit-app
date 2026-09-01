# /src/application/services/resident/get_resident_profile_service.py

from typing import Sequence

from src.application.ports.resident_repo_ports import (
    ResidentProfileRepositoryPort,
)

from src.domain.entities.resident.resident_entities import (
    ResidentProfile,
)


class FetchResidentProfileService:

    def __init__(
            self,
            *,
            resident_profile_repository: ResidentProfileRepositoryPort,
    ) -> None:
        self._profile_repo = resident_profile_repository

    def fetch_resident_profile(
            self,
            resident_id: str,
    ) -> ResidentProfile:
        return self._profile_repo.get_by_id(
            resident_id=resident_id,
        )

    def fetch_resident_profiles(
            self,
            resident_ids: Sequence[str],
    ) -> tuple[ResidentProfile, ...]:
        return self._profile_repo.get_by_ids(
            resident_ids=resident_ids,
        )

    def fetch_resident_profiles_for_tenant_ids(
            self,
            tenant_ids: Sequence[str],
    ) -> tuple[ResidentProfile, ...]:
        return self._profile_repo.list_profiles_for_tenant_ids(
            tenant_ids=tenant_ids,
        )

    def fetch_all_resident_profiles(
            self,
    ) -> tuple[ResidentProfile, ...]:
        return self._profile_repo.list_resident_profiles()
