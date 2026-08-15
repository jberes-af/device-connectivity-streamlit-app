# /src/domain/entities/sensing/timeline_entities.py

from dataclasses import dataclass

from src.domain.enums.sensing.timeline_enums import (
    TimelineEventSourceTypeEnum,
)

"""
@dataclass(frozen=True)
class TimelineQueryDTO:
    tenant_id: str
    scope: TimelineScopeEnum
    start_time_iso: str
    end_time_iso: str
    sensor
    ids: tuple[str, ...]
    sensor
    group
    ids: tuple[str, ...]
    resident
    ids: tuple[str, ...]


@dataclass(frozen=True)
class TimelineResponseDTO:
    query: TimelineQueryDTO
    events: tuple[TimelineEvent, ...]


"""

@dataclass(frozen=True)
class TimelineEvent:
    timeline_event_id: str
    tenant_id: str
    occurred_at_iso: str
    source_event_id: str
    source_event_type: TimelineEventSourceTypeEnum
    title: str
    message: str
    sensor_id: str | None
    sensor_name: str | None
    sensor_type: str | None
    resident_id: str | None
    resident_name: str | None
    group_id: str | None
    group_name: str | None
    location: str | None
    state: str | None


@dataclass(frozen=True)
class TimelineEventPersistence:
    timeline_event_id: str
    tenant_id: str
    occurred_at_iso: str
    source_event_id: str
    source_event_type: str
    sensor_id: str | None
    resident_id: str | None
    group_id: str | None
    title: str
    message: str
