# /src/application/ports/payer_repo_ports.py

from typing import Protocol, Sequence

from src.domain.entities.billing.payer_entities import (
    PayerProfile,
)


class PayerRepositoryPort(Protocol):

    def list_payers(self) -> tuple[PayerProfile, ...]:
        ...

    def get_by_id(
            self,
            payer_id: str,
    ) -> PayerProfile:
        ...

    def get_by_ids(
            self,
            payer_ids: Sequence[str],
    ) -> tuple[PayerProfile, ...]:
        ...
