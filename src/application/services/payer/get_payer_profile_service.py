# /src/application/services/payer/get_payer_profile_service.py

from typing import Sequence

from src.domain.entities.billing.payer_entities import PayerProfile

from src.application.ports.payer_repo_ports import (
    PayerRepositoryPort,
)


class FetchPayerProfileService:

    def __init__(
            self,
            *,
            payer_repository: PayerRepositoryPort,
    ):
        self._payer_repo = payer_repository

    def fetch_payer_profile(
            self,
            payer_id: str,
    ) -> PayerProfile:
        return self._payer_repo.get_by_id(payer_id=payer_id)

    def fetch_payer_profiles(
            self,
            payer_ids: Sequence[str],
    ) -> tuple[PayerProfile, ...]:
        return tuple(
            self._payer_repo.get_by_ids(
                payer_ids=payer_ids)
        )
