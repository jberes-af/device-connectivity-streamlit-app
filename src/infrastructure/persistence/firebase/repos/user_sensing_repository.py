# /src/infrastructure/persistence/firebase/repos/user_sensing_repository.py

from src.application.models.sensing_models import UserSensingDomainObjects

from src.application.ports.sensing.realtime_database_port import (
    RealtimeDatabasePort,
)

from src.application.ports.sensing.user_sensing_port import (
    UserSensingRepositoryPort,
)

from src.infrastructure.persistence.firebase.mappers.user_sensing_mappers import (
    UserRtdbDTO,
    UserRtdbMapper,
    UserDomainMapper,
)

from src.infrastructure.persistence.firebase.schemas.user_sensing_schema import (
    UserRtdbSchema)


class FirebaseUserSensingRepository(UserSensingRepositoryPort):
    def __init__(self, database: RealtimeDatabasePort) -> None:
        self._database = database

    def get(
            self,
            user_id: str,
            tenant_id: str,
    ) -> UserSensingDomainObjects | None:
        raw = self._database.read_node(
            UserRtdbSchema.user_path(user_id)
        )

        if raw is None:
            return None

        rtdb: UserRtdbDTO = UserRtdbMapper.from_raw(data=raw)

        return UserDomainMapper.to_domain(
            user_id=user_id,
            tenant_id=tenant_id,
            dto=rtdb,
        )

    """
    def save(self, entity: UserAccount) -> None:
        self._client.set(
            UserRtdbSchema.user_path(entity.user_id),
            UserRtdbMapper.to_rtdb(entity),
        )

    def update(self, entity: UserAccount) -> None:
        self._client.update(
            UserRtdbSchema.user_path(entity.user_id),
            UserRtdbMapper.to_rtdb(entity),
        )
    """
