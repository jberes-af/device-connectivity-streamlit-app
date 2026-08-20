# /src/application/use_cases/build_sensor_events_use_case.py

from datetime import date, datetime, time
from zoneinfo import ZoneInfo

from src.application.ports.sensing.device_ports import (
    SensorEventRepositoryPort,
)

from src.domain.entities.sensing.device_entities import SensorEvent

from src.application.use_cases.sensing.trends.sensor_events_uc_dtos import (
    SensorEventsBySensorDTO,
    SensorEventsRequestDTO,
    SensorEventsResultDTO,
)


class BuildSensorEventsUseCase:
    def __init__(
            self,
            sensor_event_repository: SensorEventRepositoryPort,
    ) -> None:
        self._event_repo = sensor_event_repository

    def execute(
            self,
            request: SensorEventsRequestDTO,
    ) -> SensorEventsResultDTO:

        sensor_ids: tuple[str, ...] = request.sensor_ids

        # --- FETCH EVENTS FROM FIREBASE RTDB REPOSITORY

        events_by_id: dict[str, tuple[SensorEvent, ...]] = {
            sid: self._event_repo.get_all_sensor_events(sensor_id=sid)
            for sid in sensor_ids
        }

        # --- DEFINE START & END DATETIME

        start_time: datetime
        end_time: datetime
        start_time, end_time = self._convert_date_to_datetime(
            start_date=request.start_date,
            end_date=request.end_date,
            local_timezone=request.local_timezone,
        )

        # --- FILTER EVENTS BY START & END DATETIME

        filtered_events_by_id: dict[str, list[SensorEvent]] = {
            sid: (self._filter_events_by_time_period(
                events=events,
                start_time=start_time,
                end_time=end_time,
            ))
            for sid, events in events_by_id.items()
        }

        # --- DUPLICATE SEQUENTIAL SENSOR ID EVENTS

        collapsed_events_by_id: dict[str, list[SensorEvent]] = {
            sid: (self._collapse_consecutive_sensor_events(
                filtered_events_by_id[sid]
            ))
            for sid, events in filtered_events_by_id.items()
        }

        sensor_collapsed_events: [SensorEventsBySensorDTO] = [
            SensorEventsBySensorDTO(
                sensor_id=sid,
                collapsed_events=tuple(collapsed_events_by_id[sid]),
            )
            for sid in sensor_ids
        ]

        return SensorEventsResultDTO(
            start_time=start_time,
            end_time=end_time,
            sensor_collapsed_events=tuple(sensor_collapsed_events),
        )

    @staticmethod
    def _collapse_consecutive_sensor_events(
            events: list[SensorEvent],
    ) -> list[SensorEvent]:
        if not events:
            return []

        sorted_events = sorted(
            events,
            key=lambda event: event.activated_at_utc,
        )

        collapsed: list[SensorEvent] = []

        for event in sorted_events:
            if not collapsed:
                collapsed.append(event)
                continue

            previous = collapsed[-1]

            if event.sensor_id == previous.sensor_id:
                # Replace previous with later activation.
                collapsed[-1] = event
            else:
                collapsed.append(event)

        return collapsed

    @staticmethod
    def _convert_date_to_datetime(
            start_date: date,
            end_date: date,
            local_timezone: ZoneInfo | str,
    ) -> tuple[datetime, datetime]:
        tz = (
            ZoneInfo(local_timezone)
            if isinstance(local_timezone, str)
            else local_timezone
        )

        start_time = datetime.combine(
            start_date,
            time.min,
            tzinfo=tz,
        )

        end_time = datetime.combine(
            end_date,
            time.max,
            tzinfo=tz,
        )

        return start_time, end_time

    @staticmethod
    def _filter_events_by_time_period(
            events: tuple[SensorEvent, ...],
            start_time: datetime,
            end_time: datetime,
    ) -> list[SensorEvent]:
        return [
            event
            for event in events
            if start_time <= event.activated_at_local <= end_time
        ]
