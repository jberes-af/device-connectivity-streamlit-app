# /src/infrastructure/persistence/firebase/mappers/sensor_event_mapper.py

#     return sorted(events, key=lambda event: event.activated_at_utc)

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Mapping
from zoneinfo import ZoneInfo

from src.domain.entities.sensing.device_entities import (
    SensorEvent,
)

from src.domain.enums.sensing.device_enums import (
    SENSOR_STATE_CODE_LOOKUP,
    SensorStateDefinitionEnum,
)

from src.main.host_inputs import LOCAL_TIME_ZONE


@dataclass(frozen=True, slots=True)
class RawSensorEvent:
    sensor_id: str
    state: str
    timestamp: str


@dataclass(frozen=True, slots=True)
class SensorEventRtdbDTO:
    sensor_id: str
    state: SensorStateDefinitionEnum
    timestamp_utc: datetime


class SensorEventRtdbMapper:

    @staticmethod
    def from_raw(
            *,
            raw_events: tuple[RawSensorEvent, ...],
    ) -> tuple[SensorEventRtdbDTO, ...]:

        events: list[SensorEventRtdbDTO] = []

        for event in raw_events:
            timestamp_utc = _date_time_stamp_str_to_datetime(
                event.timestamp
            )

            sensor_state = SENSOR_STATE_CODE_LOOKUP.get(
                event.state
            )

            if sensor_state is None:
                raise ValueError(
                    f"Unknown sensor state code: {event.state!r}"
                )

            events.append(
                SensorEventRtdbDTO(
                    sensor_id=event.sensor_id,
                    state=sensor_state,
                    timestamp_utc=timestamp_utc,
                )
            )

        return tuple(events)


class SensorEventDomainMapper:

    @staticmethod
    def to_domain(
            dto: SensorEventRtdbDTO,
    ) -> SensorEvent:
        local_timezone = ZoneInfo(LOCAL_TIME_ZONE)

        return SensorEvent(
            sensor_id=dto.sensor_id,
            sensor_state=dto.state,
            activated_at_utc=dto.timestamp_utc,
            activated_at_local=_utc_to_local(
                timestamp_utc=dto.timestamp_utc,
                local_timezone=local_timezone,
            ),
            event_id=None,
        )

    @classmethod
    def many_to_domain(
            cls,
            dto: tuple[SensorEventRtdbDTO, ...],
    ) -> list[SensorEvent]:
        return [
            cls.to_domain(record)
            for record in dto
        ]


def build_raw_sensor_event_objects_from_all(
        sensor_id: str,
        data: Mapping[str, Any] | None,
) -> tuple[RawSensorEvent, ...]:
    raw = data or {}

    return tuple(
        RawSensorEvent(
            sensor_id=sensor_id,
            state=state,
            timestamp=timestamp,
        )
        for timestamp_state_map in raw.values()
        for timestamp, state in timestamp_state_map.items()
    )


def build_raw_sensor_event_objects_from_last(
        sensor_id: str,
        data: Mapping[str, Any] | None,
) -> tuple[RawSensorEvent, ...]:
    raw = data or {}

    return tuple(
        RawSensorEvent(
            sensor_id=sensor_id,
            state=state,
            timestamp=timestamp,
        )
        for timestamp, state in raw.items()
    )


def _utc_to_local(
        timestamp_utc: datetime,
        local_timezone: ZoneInfo,
) -> datetime:
    return timestamp_utc.astimezone(local_timezone)


def _date_time_stamp_str_to_datetime(
        dts_str: str,
) -> datetime:
    return (
        datetime.strptime(
            dts_str,
            "%Y%m%d%H%M%S",
        )
        .replace(tzinfo=timezone.utc)
    )
