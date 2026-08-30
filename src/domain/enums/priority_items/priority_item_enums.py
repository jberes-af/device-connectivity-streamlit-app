# /src/domain/enums/priority_item_enums.py

from enum import StrEnum

class PriorityItemLevelEnum(StrEnum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class PriorityItemStatusEnum(StrEnum):
    OPEN = "Open"
    RESOLVED = "Resolved"
    CLOSED = "Closed"

