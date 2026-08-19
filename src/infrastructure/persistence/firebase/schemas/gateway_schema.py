# /src/infrastructure/persistence/firebase/schemas/gateway_schema.py

class GatewayRtdbSchema:
    ROOT = "iotg"
    FIELD_SENSORS = "sensor"
    FIELD_USERS = "user"
    FIELD_TIMEZONE_NAME = "timezone_name"
    FIELD_UTC_OFFSET = "utc_offset"

    @classmethod
    def gateway_path(cls, gateway_id: str) -> str:
        return f"/{cls.ROOT}/{gateway_id}"
