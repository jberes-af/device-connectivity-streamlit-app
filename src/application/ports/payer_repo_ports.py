# /src/application/ports/payer_repo_ports.py

from typing import Protocol

from src.domain.entities.payer_entities import (
    Payer,
)


class PayerRepositoryPort(Protocol):

    def list_payers(self) -> tuple[Payer, ...]:
        ...

    def get_by_id(
            self,
            payer_id: str,
    ) -> Payer:
        ...
