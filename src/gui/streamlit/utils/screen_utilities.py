# /src/gui/screens/screen_utils

from dataclasses import asdict
from datetime import date, time, datetime
from typing import Any, Sequence

from src.domain.entities.person.patient_entities import (
    Facility,
    PaceProgram,
    PipelineEntity,
    PipelineActivity,
)

from src.application.dto.filter_pipeline_uc_dtos import EntityTypeRecordDTO

import streamlit as st


def render_labeled_value(
        *,
        label: str,
        value: object | None,
) -> None:
    st.caption(label)
    st.write(value if value not in (None, "") else "—")


def find_entity_type_record(
        *,
        entity_id: str,
        records: Sequence[EntityTypeRecordDTO],
) -> EntityTypeRecordDTO | None:
    return next(
        (
            record
            for record in records
            if record.entity_id == entity_id
        ),
        None,
    )


"""
def find_entity_type_record(
        *,
        entity_id: str,
        records: Sequence[EntityTypeRecordDTO],  # Sequence[Facility | PaceProgram],
) -> Facility | PaceProgram | None:
    return next(
        (
            record
            for record in records
            if record.entity_id == entity_id
        ),
        None,
    )
"""


def enum_display_value(value: object | None) -> str:
    if value is None:
        return ""

    enum_value = getattr(value, "value", None)

    if enum_value is not None:
        return str(enum_value)

    return str(value)


"""
def get_size_description(
        record: Facility | PaceProgram | None,
) -> str:
    if record is None:
        return ""

    if isinstance(record, Facility):
        capacity = getattr(record, "size", None)

        if capacity is None:
            capacity = getattr(record, "licensed_capacity", None)

        if capacity is not None:
            return f"{capacity} beds"

    if isinstance(record, PaceProgram):
        participant_count = getattr(
            record,
            "participant_count",
            None,
        )

        if participant_count is not None:
            return f"{participant_count} participants"

    return ""
"""


def get_entity_address_display(
        entity: PipelineEntity,
) -> str:
    entity_address: str = (
        f"{entity.street_address}<br>{entity.city} • {entity.state}"
    )

    return entity_address


def record_to_display_dictionary(
        record: Facility | PaceProgram,
) -> dict[str, Any]:
    """
    Convert a dataclass record to JSON-compatible display values.

    This is only for the temporary raw-detail expander.
    A polished UI should render explicitly selected fields instead.
    """

    values = asdict(record)

    return {
        key: to_display_value(value)
        for key, value in values.items()
    }


def to_display_value(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: to_display_value(item)
            for key, item in value.items()
        }

    if isinstance(value, (list, tuple)):
        return [
            to_display_value(item)
            for item in value
        ]

    enum_value = getattr(value, "value", None)

    if enum_value is not None:
        return enum_value

    return value


def get_size_description(
        record: EntityTypeRecordDTO | None,
) -> str | None:
    if record is None:
        return None

    if record.record_type == "Facility":
        return get_display_field_value(record, "capacity")

    if record.record_type == "PACE Program":
        return get_display_field_value(record, "census")

    return None


def get_display_field_value(
        record: EntityTypeRecordDTO | None,
        key: str,
) -> str | None:
    if record is None:
        return None

    return next(
        (
            field.value
            for field in record.fields
            if field.key == key
        ),
        None,
    )


def display_text(value: str | None) -> str:
    return value.strip() if value and value.strip() else "—"


def display_url(value: str | None) -> str:
    return value.strip() if value and value.strip() else "—"


def sort_activity_objects_reverse_date(
        activities: Sequence[PipelineActivity],
) -> Sequence[PipelineActivity]:
    sorted_activities = sorted(
        activities,
        key=lambda activity: (
            activity.contact_date or date.min,
            activity.contact_time or time.min,
        ),
        reverse=True,
    )

    return sorted_activities


def display_time(value: time | None) -> str:
    if value is None:
        return "—"

    hour_24 = value.hour
    minute = value.minute

    period = "AM" if hour_24 < 12 else "PM"

    hour_12 = hour_24 % 12
    if hour_12 == 0:
        hour_12 = 12

    return f"{hour_12}:{minute:02d} {period}"


def display_date(value: date | datetime | None) -> str:
    date_value = (
        value.strftime("%B %d, %Y")
        if value
        else "---"
    )
    return date_value


def display_integer(value: int | str | None) -> int:
    if value is None:
        return 0

    if isinstance(value, str):
        return int(value.strip().replace(",", ""))

    else:
        return int(value)
