# /src/domain/enums/sensing/routine_enums.py

from enum import StrEnum


class AlertaRoutineTimeframeStateEnum(StrEnum):
    NOT_STARTED = "Not Started"
    ACTIVE = "Active"
    EXPIRED = "Expired"


class AlertaRoutineOutcomeStateEnum(StrEnum):
    OCCURRED = "Occurred"
    DID_NOT_OCCUR = "Did Not Occur"
    NOT_AVAILABLE_PENDING = "Not Available - Pending"


class AlertaRoutineEvaluationModeEnum(StrEnum):
    ALL_RULES_MET = "All Rules Met"
    ANY_RULE_MET = "Any Rule Met"
    SEQUENCE_MET = "Sequence Met"
