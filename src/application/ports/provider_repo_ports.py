# /src/application/ports/provider_repo_ports.py

from typing import Protocol

from src.domain.entities.care.provider_entities import (
    Provider,
)


class ProviderRepositoryPort(Protocol):

    def list_providers(self) -> tuple[Provider, ...]:
        ...

    def get_by_id(
            self,
            provider_id: str,
    ) -> Provider:
        ...

