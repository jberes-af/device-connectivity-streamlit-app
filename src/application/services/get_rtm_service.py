# /src/application/services/get_rtm_service.py

from typing import Sequence

from src.domain.entities.care.provider_entities import ProviderProfile

from src.application.ports.provider_repo_ports import (
    ProviderRepositoryPort,
)


class FetchRtmService:

    def __init__(
            self,
            *,
            rtm_repository: ProviderRepositoryPort,
    ):
        self._rtm_repo = rtm_repository

    def fetch_rtm_enrollment(
            self,
            provider_id: str,
    ) -> ProviderProfile:
        return self._rtm_repo.get_by_id(provider_id=provider_id)

    def fetch_rtm_necessity(
            self,
            provider_ids: Sequence[str],
    ) -> tuple[ProviderProfile, ...]:
        return tuple(
            self._rtm_repo.get_by_ids(
                provider_ids=provider_ids)
        )
