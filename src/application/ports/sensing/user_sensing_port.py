# /src/application/ports/sensing/user_sensing_port.py

from typing import Protocol

from src.application.models.sensing_models import (
    UserSensingDomainObjects,
    UserSensorProfiles,
)


class UserSensingRepositoryPort(Protocol):

    def get_by_user_id(
            self,
            user_id: str,
    ) -> UserSensingDomainObjects | None:
        ...

    def get_sensor_profiles_by_user_id(
            self,
            user_id: str,
    ) -> UserSensorProfiles | None:
        ...

    def get_all_user_ids(
            self,
    ) -> tuple[str, ...]:
        ...

    def save(self, user: UserSensingDomainObjects) -> None:
        ...
