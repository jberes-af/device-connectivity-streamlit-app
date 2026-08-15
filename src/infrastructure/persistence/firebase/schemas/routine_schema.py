from __future__ import annotations


class RoutineRtdbSchema:
    ROOT = "routine"

    FIELD_RULE_COUNT = "rule_count"
    FIELD_SENSOR_IDS = "sensor_ids"
    FIELD_USER_ID = "user_id"
    FIELD_ORPHAN = "orphan"
    FIELD_EXISTS_IN_ROUTINE = "exists_in_routine"
    FIELD_EXISTS_IN_USER = "exists_in_user"

    @classmethod
    def routine_path(cls, routine_id: str) -> str:
        return f"{cls.ROOT}/{routine_id}"
