# /src/infrastructure/persistence/firebase/schemas/sensor_schema.py

class SensorSystemRtdbSchema:
    ROOT = "sensor"
    FIELD_BRAND = "brand"
    FIELD_TYPE = "type"
    FIELD_ICON = "icon"

    @classmethod
    def sensor_path(cls, sensor_id: str) -> str:
        return f"/{cls.ROOT}/{sensor_id}"


"""
class SensorUserRtdbSchema:
    ROOT = "user"
    DEVICES_NODE = "device"
    FIELD_NAME = "name"
    FIELD_LOCATION = "location"
    FIELD_ZONE = "zone"
    FIELD_IMAGE = "image"

    @classmethod
    def user_sensor_path(cls, user_id: str, sensor_id: str) -> str:
        return f"/{cls.ROOT}/{user_id}/{cls.DEVICES_NODE}"

    @classmethod
    def user_sensor_id_path(cls, user_id: str, sensor_id: str) -> str:
        return f"/{cls.ROOT}/{user_id}/{cls.DEVICES_NODE}/{sensor_id}"
"""


class SensorEventRtdbSchema:
    ROOT = "notification"
    COLLECTION_ALL = "all"
    COLLECTION_LAST = "last"

    @classmethod
    def sensor_event_all_path(cls, sensor_id: str) -> str:
        return f"/{cls.ROOT}/{cls.COLLECTION_ALL}/{sensor_id}"

    @classmethod
    def sensor_event_last_path(cls, sensor_id: str) -> str:
        return f"/{cls.ROOT}/{cls.COLLECTION_LAST}/{sensor_id}"
