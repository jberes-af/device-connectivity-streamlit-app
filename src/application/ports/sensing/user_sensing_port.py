# /src/application/ports/sensing/user_sensing_port.py

from typing import Protocol

from src.application.models.sensing_models import (
    UserSensingDomainObjects,
)


class UserSensingRepositoryPort(Protocol):

    def get(
            self,
            user_id: str,
            tenant_id: str,
    ) -> UserSensingDomainObjects | None:
        ...

    def save(self, user: UserSensingDomainObjects) -> None:
        ...
