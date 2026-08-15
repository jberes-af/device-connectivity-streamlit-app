from __future__ import annotations


class UserRtdbSchema:
    ROOT = "users"

    FIELD_EMAIL = "email"
    FIELD_EMAIL_AUTH = "email_auth"
    FIELD_NAME = "name"
    FIELD_TELEPHONE = "tel"
    FIELD_PHONE = "phone"
    FIELD_ADL_ENTITIES = "adl_entities"
    FIELD_ROUTINE_IDS = "routine_ids"
    FIELD_SENSOR_IDS = "sensor_ids"
    FIELD_GATEWAY_IDS = "gateway_ids"
    FIELD_EXISTS_AUTH = "exists_auth"
    FIELD_EXISTS_RTDB = "exists_rtdb"

    @classmethod
    def user_path(cls, user_id: str) -> str:
        return f"{cls.ROOT}/{user_id}"
