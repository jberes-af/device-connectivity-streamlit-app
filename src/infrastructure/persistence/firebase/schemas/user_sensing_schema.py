# /src/infrastructure/persistence/firebase/schemas/user_sensing_schema.py

class UserRtdbSchema:
    ROOT = "user"
    COLLECTION_ACCOUNT = "account"
    FIELD_EMAIL_RTDB = "email"
    FIELD_NAME = "name"
    FIELD_TELEPHONE = "tel"
    FIELD_ADL_ENTITIES = "activity"
    FIELD_ROUTINE_IDS = "routine"
    COLLECTION_SENSOR_IDS = "device"
    COLLECTION_GATEWAY_IDS = "iotg"
    FIELD_SETTINGS = "settings"
    FIELD_NOTES = "notes"
    FILED_GROUPING = "grouping"

    @classmethod
    def user_path(cls) -> str:
        return f"/{cls.ROOT}"

    @classmethod
    def user_id_path(cls, user_id: str) -> str:
        return f"/{cls.ROOT}/{user_id}"

    @classmethod
    def user_sensor_path(cls, user_id: str) -> str:
        return f"/{cls.ROOT}/{user_id}/{cls.COLLECTION_SENSOR_IDS}"

    @classmethod
    def user_sensor_id_path(cls, user_id: str, sensor_id: str) -> str:
        return f"/{cls.ROOT}/{user_id}/{cls.COLLECTION_SENSOR_IDS}/{sensor_id}"
