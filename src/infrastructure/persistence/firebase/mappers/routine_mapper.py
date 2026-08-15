from __future__ import annotations

from typing import Any, Mapping

from firebase.schemas.routine_schema import RoutineRtdbSchema

# Adjust this import to match your project.
from src.domain.entities.routine.routine_entities import AlertaRoutineProfile


class RoutineRtdbMapper:
    @staticmethod
    def to_domain(
        routine_id: str,
        tenant_id: str,
        data: Mapping[str, Any] | None,
    ) -> AlertaRoutineProfile:
        raw = data or {}

        # This mapper intentionally maps only fields represented by the
        # domain entity. Extend when the RTDB routine schema is normalized
        # to the AlertaRoutineProfile domain model.
        return AlertaRoutineProfile(
            routine_id=routine_id,
            tenant_id=tenant_id,
            name=str(raw.get("name", "") or ""),
            start_time=str(raw.get("start_time", "") or ""),
            end_time=str(raw.get("end_time", "") or ""),
            rules=(),
            routine_state=None,  # Replace once state construction is defined.
        )

    @staticmethod
    def to_rtdb(entity: AlertaRoutineProfile) -> dict[str, Any]:
        return {
            "name": entity.name,
            "start_time": entity.start_time,
            "end_time": entity.end_time,
        }
