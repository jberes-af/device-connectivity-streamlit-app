# /src/application/services/get_treatment_service.py

from typing import Sequence

from src.domain.entities.care.provider_entities import ProviderProfile

from src.application.ports.provider_repo_ports import (
    ProviderRepositoryPort,
)


class FetchProviderProfileService:

    def __init__(
            self,
            *,
            treatment_repository: ProviderRepositoryPort,
    ):
        self._treatment_repo = treatment_repository

    def fetch_treatment_profile(
            self,
            provider_id: str,
    ) -> ProviderProfile:
        return self._treatment_repo.get_by_id(provider_id=provider_id)

    def fetch_treatment_profiles(
            self,
            provider_ids: Sequence[str],
    ) -> tuple[ProviderProfile, ...]:
        return tuple(
            self._treatment_repo.get_by_ids(
                provider_ids=provider_ids)
        )
