from __future__ import annotations

from firebase.mappers.routine_mapper import RoutineRtdbMapper
from firebase.repositories._protocols import RtdbClientProtocol
from firebase.schemas.routine_schema import RoutineRtdbSchema

from src.domain.entities.routine.routine_entities import AlertaRoutineProfile


class FirebaseRoutineRepository:
    def __init__(self, client: RtdbClientProtocol) -> None:
        self._client = client

    def get(
        self,
        routine_id: str,
        tenant_id: str,
    ) -> AlertaRoutineProfile | None:
        raw = self._client.get_all_sensor_events(
            RoutineRtdbSchema.routine_path(routine_id)
        )

        if raw is None:
            return None

        return RoutineRtdbMapper.from_raw(
            routine_id=routine_id,
            tenant_id=tenant_id,
            data=raw,
        )

    def save(self, entity: AlertaRoutineProfile) -> None:
        self._client.set(
            RoutineRtdbSchema.routine_path(entity.routine_id),
            RoutineRtdbMapper.to_rtdb(entity),
        )
