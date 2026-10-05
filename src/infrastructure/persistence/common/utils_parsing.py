# /src/infrastructure/persistence/widgets/utils_parsing.py

from datetime import date, datetime, time
from enum import StrEnum
from typing import Any, TypeVar

TEnum = TypeVar("TEnum", bound=StrEnum)


def parse_text(
        value: Any,
) -> str:
    if value is None:
        return ""

    return str(value).strip()


def parse_required_text(
        value: Any,
        field_name: str,
) -> str:
    text = parse_text(value)

    if not text:
        raise ValueError(
            f"Missing required field: {field_name}"
        )

    return text


def parse_optional_text(
        value: Any,
        field_name: str,
) -> str | None:
    del field_name

    text = parse_text(value)

    return text or None


def parse_required_int(
        value: Any,
        field_name: str,
) -> int:
    parsed = parse_optional_int(
        value,
        field_name,
    )

    if parsed is None:
        raise ValueError(
            f"Missing required field: {field_name}"
        )

    return parsed


def parse_optional_int(
        value: Any,
        field_name: str,
) -> int | None:
    if value is None:
        return None

    text = parse_text(value)

    if not text:
        return None

    normalized = text.replace(",", "")

    try:
        return int(normalized)

    except ValueError as exc:
        raise ValueError(
            f"Invalid integer value for "
            f"{field_name}: {text!r}"
        ) from exc


def parse_optional_date(
        value: Any,
        field_name: str,
) -> date | None:
    if value is None:
        return None

    # Already a Python datetime.
    # datetime must be checked before date because
    # datetime is a subclass of date.
    if isinstance(value, datetime):
        return value.date()

    # Already a Python date.
    if isinstance(value, date):
        return value

    text = parse_text(value)

    if not text:
        return None

    # --- DATE FORMATS

    accepted_date_formats = (
        "%Y-%m-%d",
        "%m/%d/%Y",
        "%m/%d/%y",
        "%d-%m-%Y",
        "%d-%m-%y",
    )

    for date_format in accepted_date_formats:
        try:
            return datetime.strptime(
                text,
                date_format,
            ).date()

        except ValueError:
            continue

    # --- DATETIME FORMATS

    accepted_datetime_formats = (
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
    )

    for datetime_format in accepted_datetime_formats:
        try:
            return datetime.strptime(
                text,
                datetime_format,
            ).date()

        except ValueError:
            continue

    raise ValueError(
        f"Invalid date value for "
        f"{field_name}: {text!r}"
    )


def parse_required_date(
        value: Any,
        field_name: str,
) -> date:
    parsed = parse_optional_date(
        value,
        field_name,
    )

    if parsed is None:
        raise ValueError(
            f"Missing required field: {field_name}"
        )

    return parsed


def parse_required_time(
        value: Any,
        field_name: str,
) -> time:
    parsed = parse_optional_time(
        value,
        field_name,
    )

    if parsed is None:
        raise ValueError(
            f"Missing required field: {field_name}"
        )

    return parsed


def parse_optional_time(
        value: Any,
        field_name: str,
) -> time | None:
    if value is None:
        return None

    if isinstance(value, datetime):
        return value.time()

    if isinstance(value, time):
        return value

    text = parse_text(value)

    if not text:
        return None

    accepted_time_formats = (
        "%H:%M:%S",
        "%H:%M",
        "%I:%M %p",
        "%I:%M:%S %p",
    )

    for time_format in accepted_time_formats:
        try:
            return datetime.strptime(
                text,
                time_format,
            ).time()

        except ValueError:
            continue

    accepted_datetime_formats = (
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
    )

    for datetime_format in accepted_datetime_formats:
        try:
            return datetime.strptime(
                text,
                datetime_format,
            ).time()

        except ValueError:
            continue

    raise ValueError(
        f"Invalid time value for "
        f"{field_name}: {text!r}"
    )


def parse_required_bool(
        value: Any,
        field_name: str,
) -> bool:
    parsed = parse_optional_bool(
        value,
        field_name,
    )

    if parsed is None:
        raise ValueError(
            f"Missing required field: {field_name}"
        )

    return parsed


def parse_optional_bool(
        value: Any,
        field_name: str,
) -> bool | None:
    if value is None:
        return None

    if isinstance(value, bool):
        return value

    text = parse_text(value)

    if not text:
        return None

    normalized = text.lower()

    if normalized in (
            "true",
            "t",
            "yes",
            "y",
            "1",
    ):
        return True

    if normalized in (
            "false",
            "f",
            "no",
            "n",
            "0",
    ):
        return False

    raise ValueError(
        f"Invalid boolean value for "
        f"{field_name}: {text!r}"
    )


def parse_required_datetime(
        value: Any,
        field_name: str,
) -> datetime:
    parsed = parse_optional_datetime(
        value,
        field_name,
    )

    if parsed is None:
        raise ValueError(
            f"Missing required field: {field_name}"
        )

    return parsed


def parse_optional_datetime(
        value: Any,
        field_name: str,
) -> datetime | None:
    if value is None:
        return None

    if isinstance(value, datetime):
        return value

    text = parse_text(value)

    if not text:
        return None

    # Parse ISO 8601 timestamps, including UTC "Z" and offsets.
    try:
        return datetime.fromisoformat(
            text.replace("Z", "+00:00")
        )
    except ValueError:
        pass

    accepted_formats = (
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%m/%d/%Y %H:%M:%S",
        "%m/%d/%Y %H:%M",
        "%m/%d/%Y %I:%M %p",
        "%m/%d/%Y %I:%M:%S %p",
        "%m/%d/%y %H:%M:%S",
        "%m/%d/%y %H:%M",
        "%m/%d/%y %I:%M %p",
        "%m/%d/%y %I:%M:%S %p",
    )

    for datetime_format in accepted_formats:
        try:
            return datetime.strptime(
                text,
                datetime_format,
            )

        except ValueError:
            continue

    raise ValueError(
        f"Invalid datetime value for "
        f"{field_name}: {text!r}"
    )


def parse_required_enum(
        value: object,
        *,
        enum_type: type[TEnum],
        field_name: str,
) -> TEnum:
    parsed = parse_optional_enum(
        value,
        enum_type=enum_type,
        field_name=field_name,
    )

    if parsed is None:
        raise ValueError(
            f"Missing required field: {field_name}"
        )

    return parsed


def parse_optional_enum(
        value: object,
        *,
        enum_type: type[TEnum],
        field_name: str,
) -> TEnum | None:
    if value is None:
        return None

    text = parse_text(value)

    if not text:
        return None

    try:
        return enum_type(text)

    except ValueError as exc:
        valid_values = ", ".join(
            member.value
            for member in enum_type
        )

        raise ValueError(
            f"{field_name} has invalid value "
            f"{text!r}. Expected one of: "
            f"{valid_values}."
        ) from exc


def parse_optional_text_tuple(
        value: Any,
        field_name: str,
        delimiter: str = ",",
) -> tuple[str, ...]:
    del field_name

    if value is None:
        return ()

    text = parse_text(value)

    if not text:
        return ()

    return tuple(
        item.strip()
        for item in text.split(delimiter)
        if item.strip()
    )


def parse_optional_enum_tuple(
        value: Any,
        *,
        enum_type: type[TEnum],
        field_name: str,
        delimiter: str = ",",
) -> tuple[TEnum, ...]:
    values = parse_optional_text_tuple(
        value,
        field_name=field_name,
        delimiter=delimiter,
    )

    parsed: list[TEnum] = []

    for item in values:
        try:
            parsed.append(
                enum_type(item)
            )

        except ValueError as exc:
            valid_values = ", ".join(
                member.value
                for member in enum_type
            )

            raise ValueError(
                f"{field_name} has invalid value "
                f"{item!r}. Expected one of: "
                f"{valid_values}."
            ) from exc

    return tuple(parsed)


def parse_required_enum_tuple(
        value: Any,
        *,
        enum_type: type[TEnum],
        field_name: str,
        delimiter: str = ",",
) -> tuple[TEnum, ...]:
    parsed = parse_optional_enum_tuple(
        value,
        enum_type=enum_type,
        field_name=field_name,
        delimiter=delimiter,
    )

    if not parsed:
        raise ValueError(
            f"Missing required field: {field_name}"
        )

    return parsed


def parse_optional_float(
        value: Any,
        field_name: str,
) -> float | None:
    if value is None:
        return None

    text = parse_text(value)

    if not text:
        return None

    normalized = text.replace(",", "")

    try:
        return float(normalized)

    except ValueError as exc:
        raise ValueError(
            f"Invalid integer value for "
            f"{field_name}: {text!r}"
        ) from exc
