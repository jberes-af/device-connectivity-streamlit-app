# /src/domain/enums/sensing/device_enums.py

from enum import StrEnum
from typing import Final, Mapping


class DeviceTypeEnum(StrEnum):
    SENSOR = "sensor"
    GATEWAY = "gateway"


class SensorTypeEnum(StrEnum):
    CHAIR_PAD = "chair_pad"
    MATTRESS_PAD = "mattress_pad"
    LARGE_FLOOR_MAT = "floor_mat"
    SMALL_FLOOR_MAT = "floor_mat_1015"


class SensorPurposeEnum(StrEnum):
    RESIDENT_MONITORING = "resident_monitoring"
    FACILITY_EXIT = "facility_exit"
    COMMON_AREA = "common_area"
    INGRESS_EGRESS = "room_ingress_egress"
    GATEWAY = "gateway"
    OTHER = "other"


class SensorStateDefinitionEnum(StrEnum):
    OFF = "Off"
    ON = "On"


class SensorStateDisplayNamesEnum(StrEnum):
    ACTIVATED = "Activated"
    EXIT = "Exit"


SENSOR_STATE_CODE_LOOKUP: Final[
    Mapping[str, SensorStateDefinitionEnum]
] = {
    "C8": SensorStateDefinitionEnum.OFF,
    "14": SensorStateDefinitionEnum.ON,
}
