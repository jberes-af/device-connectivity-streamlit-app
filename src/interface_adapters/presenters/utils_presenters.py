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


def format_date(
        value: datetime | date | None,
) -> str:
    if value is None:
        return "—"

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
