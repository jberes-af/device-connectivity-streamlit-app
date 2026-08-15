from __future__ import annotations


class GatewayRtdbSchema:
    ROOT = "gateway"

    FIELD_SENSORS = "sensor"
    FIELD_USERS = "user"
    FIELD_TIMEZONE_NAME = "timezone_name"
    FIELD_UTC_OFFSET = "utc_offset"

    @classmethod
    def gateway_path(cls, gateway_id: str) -> str:
        return f"{cls.ROOT}/{gateway_id}"
