# /src/domain/enums/sensing/device_enums.py

from enum import StrEnum

class SensorStateDefinitionEnum(StrEnum):
    OFF = "Off"
    ON = "On"


class SensorStateDisplayNamesEnum(StrEnum):
    ACTIVATED = "Activated"
    EXIT = "Exit"
