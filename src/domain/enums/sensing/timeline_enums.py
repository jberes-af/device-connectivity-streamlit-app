# timeline_enums.py

from enum import StrEnum


class TimelineScopeEnum(StrEnum):
    ALL = "All"
    SENSOR = "Sensor"
    SENSOR_GROUP = "Sensor Group"
    RESIDENT = "Resident"


class TimelineEventSourceTypeEnum(StrEnum):
    SENSOR_EVENT = "Sensor Event"
    ROUTINE_OUTCOME = "Routine Outcome"
    PRIORITY_ITEM = "Priority Item"
    ADL_RECORD = "ADL Record"
    NOTE = "Note"
