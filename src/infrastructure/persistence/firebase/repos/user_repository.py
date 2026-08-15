from __future__ import annotations

from firebase.mappers.user_mapper import UserRtdbMapper
from firebase.repositories._protocols import RtdbClientProtocol
from firebase.schemas.user_schema import UserRtdbSchema

from src.domain.entities.person.user_entities import UserAccount


class FirebaseUserRepository:
    def __init__(self, client: RtdbClientProtocol) -> None:
        self._client = client

    def get(self, user_id: str) -> UserAccount | None:
        raw = self._client.get(UserRtdbSchema.user_path(user_id))
        if raw is None:
            return None
        return UserRtdbMapper.to_domain(user_id=user_id, data=raw)

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
