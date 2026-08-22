# /src/application/ports/provider_repo_ports.py

from typing import Protocol, Sequence

from src.domain.entities.care.provider_entities import (
    ProviderProfile,
)


class ProviderRepositoryPort(Protocol):

    def list_providers(self) -> tuple[ProviderProfile, ...]:
        ...

    def get_by_id(
            self,
            provider_id: str,
    ) -> ProviderProfile:
        ...

    def get_by_ids(
            self,
            provider_ids: Sequence[str],
    ) -> tuple[ProviderProfile, ...]:
        ...
