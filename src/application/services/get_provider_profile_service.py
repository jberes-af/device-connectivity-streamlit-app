# /src/application/services/get_provider_profile_service.py

from typing import Sequence

from src.domain.entities.care.provider_entities import ProviderProfile

from src.application.ports.provider_repo_ports import (
    ProviderRepositoryPort,
)


class FetchProviderProfileService:

    def __init__(
            self,
            *,
            provider_repository: ProviderRepositoryPort,
    ):
        self._provider_repo = provider_repository

    def fetch_provider_profile(
            self,
            provider_id: str,
    ) -> ProviderProfile:
        return self._provider_repo.get_by_id(provider_id=provider_id)

    def fetch_provider_profiles(
            self,
            provider_ids: Sequence[str],
    ) -> tuple[ProviderProfile, ...]:
        return tuple(
            self._provider_repo.get_by_ids(
                provider_ids=provider_ids)
        )
