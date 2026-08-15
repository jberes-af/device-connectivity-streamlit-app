from __future__ import annotations


class SensorSystemRtdbSchema:
    ROOT = "sensor"

    FIELD_BRAND = "brand"
    FIELD_TYPE = "type"
    FIELD_ICON = "icon"

    @classmethod
    def sensor_path(cls, sensor_id: str) -> str:
        return f"{cls.ROOT}/{sensor_id}"


class SensorUserRtdbSchema:
    ROOT = "users"
    DEVICES_NODE = "devices"

    FIELD_NAME = "name"
    FIELD_LOCATION = "location"
    FIELD_ZONE = "zone"
    FIELD_IMAGE = "image"

    @classmethod
    def sensor_path(cls, user_id: str, sensor_id: str) -> str:
        return f"{cls.ROOT}/{user_id}/{cls.DEVICES_NODE}/{sensor_id}"
