# /src/domin/entities/priority_item_entities.py

from dataclasses import dataclass
from datetime import datetime

from src.domain.enums.priority_item_enums import (
    PriorityItemLevelEnum,
    PriorityItemStatusEnum,
)


@dataclass(frozen=True)
class PriorityItemNote:
    note_id: str
    tenant_id: str
    user_id: str
    created_at: datetime
    note: str


@dataclass(frozen=True)
class PriorityItemRecommendation:
    recommendation_id: str
    tenant_id: str
    user_id: str
    created_at: datetime
    recommendation: str


@dataclass(frozen=True)
class PriorityItemRecord:
    item_id: str
    tenant_id: str
    resident_id: str

    item_description: str
    reason_for_priority: str

    priority_level: PriorityItemLevelEnum
    status: PriorityItemStatusEnum

    assigned_to_user_id: str | None

    created_at: datetime
    created_by_user_id: str

    due_at: datetime | None = None

    acknowledged_at: datetime | None = None
    acknowledged_by_user_id: str | None = None

    resolved_at: datetime | None = None
    resolved_by_user_id: str | None = None
    resolution_summary: str | None = None

    closed_at: datetime | None = None
    closed_by_user_id: str | None = None

    source_type: str | None = None
    source_id: str | None = None

    item_notes: tuple[PriorityItemNote, ...] = ()
    recommendations: tuple[PriorityItemRecommendation, ...] = ()
