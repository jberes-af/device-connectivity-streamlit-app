# utils_presenters
from datetime import datetime, date


def format_optional(value: str | None) -> str:
    return value or "—"


def format_bool(value: bool | None) -> str:
    if value is None:
        return "Unknown"
    if value:
        return "Active"
    return "Inactive"


def format_date2(
        value: datetime | date | None,
) -> str:
    if value is None:
        return "—"

    return value.strftime("%b %d, %Y")


def format_date(
        value: datetime | date | None,
        *,
        empty_value: str | None = None,
) -> str:
    if value is None and empty_value is None:
        "—"

    return value.strftime("%b %d, %Y")


def format_state_postal(
        state: str | None,
        postal_code: str | None,
) -> str:
    parts = [
        value
        for value in (state, postal_code)
        if value
    ]

    return " • ".join(parts) if parts else "—"


def format_datetime(
        value: datetime,
) -> str:
    return value.strftime("%b %d, %Y %I:%M %p")


def format_optional_datetime(
        cls,
        value: datetime | None,
        *,
        empty_value: str = "—",
) -> str:
    if value is None:
        return empty_value

    return cls._format_datetime(value)


def format_values(
        values: tuple[str, ...],
) -> str:
    if not values:
        return "—"

    return ", ".join(values)


def format_enum_values(
        cls,
        values: tuple,
) -> str:
    if not values:
        return "—"

    return ", ".join(
        cls._format_enum(value)
        for value in values
    )


def format_enum(
        value,
) -> str:
    enum_value = getattr(
        value,
        "value",
        str(value),
    )

    return (
        str(enum_value)
        .replace("_", " ")
        .title()
    )
