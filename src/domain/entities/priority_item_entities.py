# priority_item_entities.py


class PriorityItemLevelEnum(StrEnum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"






#### PI-02: Priority Item Status Enum




class PriorityItemStatusEnum(StrEnum):
    OPEN = "Open"
    RESOLVED = "Resolved"
    CLOSED = "Closed"






#### PI-03: Priority Item Note DTO




@dataclass(frozen=True)
class PriorityItemNoteDTO:
    note_id: str
    tenant_id: str
    user_id: str
    created_at_iso: str
    note: str






#### PI-04: Priority Item Record DTO




@dataclass(frozen=True)
class PriorityItemRecordDTO:
    item_id: str
    tenant_id: str
    resident_id: str
    item_description: str
    reason_for_priority: str
    priority_level: PriorityItemLevelEnum
    assigned_to: str
    status: PriorityItemStatusEnum
    created_at_iso: str
    created_by_user_id: str
    resolved_at_iso: str | None = None
    closed_at_iso: str | None = None
    item_notes: tuple[PriorityItemNote, ...] = ()
    recommendation_notes: tuple[PriorityItemNote, ...] = ()




