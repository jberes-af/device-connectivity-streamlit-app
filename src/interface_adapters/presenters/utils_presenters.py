# /src/interface_adapters/presenters/utils_presenters

from datetime import datetime, date
from zoneinfo import ZoneInfo


# --- BOOLEAN

def format_bool(value: bool | None) -> str:
    if value is None:
        return "Unknown"
    if value:
        return "Active"
    return "Inactive"


# --- DATE & TIME

def format_date(
        value: datetime | date | None,
        *,
        empty_value: str = "—",
) -> str:
    if value is None:
        return empty_value

    return value.strftime("%b %d, %Y").replace(" 0", " ")


def format_date_range(
        *,
        start_date: date,
        end_date: date | None,
) -> str:
    start = format_date(start_date)

    if end_date is None:
        return f"{start} – Present"

    return (
        f"{start} – "
        f"{format_date(end_date)}"
    )


def format_datetime(
        value: datetime | None,
        *,
        empty_value: str = "—",
) -> str:
    if value is None:
        return empty_value

    return (
        value
        .strftime("%b %d, %Y %I:%M %p")
        .replace(" 0", " ")
    )


def format_optional_datetime(
        value: datetime | None,
        *,
        empty_value: str = "—",
) -> str:
    if value is None:
        return empty_value

    return format_datetime(value)


def format_change_since_yesterday(
        value: int,
) -> str:
    if value == 0:
        return "No change since yesterday"

    return f"{value:+d} since yesterday"


def format_elapsed_time(
        occurred_at: datetime | None,
) -> str | None:
    if occurred_at is None:
        return None

    # Ideally use an injected clock rather than datetime.now()
    elapsed = datetime.now(tz=occurred_at.tzinfo) - occurred_at

    total_minutes = int(elapsed.total_seconds() // 60)

    if total_minutes < 60:
        return f"{total_minutes}m"

    total_hours = total_minutes // 60

    if total_hours < 24:
        return f"{total_hours}h"

    total_days = total_hours // 24
    return f"{total_days}d"


def format_utc_to_timezone(
        utc_time: datetime | None,
        timezone: str | None = None,
) -> datetime | None:
    return utc_time.astimezone(ZoneInfo(timezone))


# --- ENUM

def format_enum_values(
        values: tuple,
) -> str:
    if not values:
        return "—"

    return ", ".join(
        format_enum(value)
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


# --- NUMBERS


# --- TEXT

def format_optional(value: str | None) -> str:
    return value or "—"


def format_values(
        values: tuple[str, ...],
) -> str:
    if not values:
        return "—"

    return ", ".join(values)


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


def format_measurement_value(
        *,
        value: float | None,
        unit: str | None,
) -> str:
    if value is None:
        return "—"

    value_display = f"{value:g}"

    if not unit:
        return value_display

    return f"{value_display} {unit}"


def format_percentage(
        value: float,
) -> str:
    return f"{value:.0%}"


def format_percentage_delta(
        value: float | None,
) -> str | None:
    if value is None:
        return None

    return f"{value:+.1%}"


def format_signed_delta(
        value: int | None,
) -> str | None:
    if value is None:
        return None

    return f"{value:+d}"
