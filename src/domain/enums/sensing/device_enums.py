# /src/domain/enums/sensing/device_enums.py

from enum import StrEnum

from typing import Final, Mapping


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
