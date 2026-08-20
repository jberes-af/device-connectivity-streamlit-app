# /src/application/use_cases/build_sensor_events_use_case.py


from datetime import date, datetime, time
from typing import Any
from zoneinfo import ZoneInfo

from src.application.ports.sensing.device_ports import (
    SensorEventRepositoryPort,
)

from src.domain.entities.sensing.device_entities import SensorEvent

from src.application.use_cases.sensing.trends.sensor_events_uc_dtos import (
    SensorEventsRequestDTO,
    SensorEventsResultDTO,
)


class BuildSensorEventsUseCase:
    def __init__(
            self,
            sensor_event_repository: SensorEventRepositoryPort,
    ) -> None:
        self._sensor_event_repo = sensor_event_repository

    def execute(
            self,
            request: SensorEventsRequestDTO,
    ) -> SensorEventsResultDTO:

        sensor_ids: list[str] = request.sensor_id

        start_time: datetime
        end_time: datetime
        start_time, end_time = self._convert_date_to_datetime(
            start_date=request.start_date,
            end_date=request.end_date,
            local_timezone=local_tz,
        )

        time_period_events: list[SensorEvent] = (
            self._filter_events_by_time_period(
                events=events,
                start_time=start_time,
                end_time=end_time,
            ))

        # collapsed events: local time from request
        collapsed_events: list[SensorEvent] = (
            self._collapse_consecutive_sensor_events(
                time_period_events
            ))

        return SensorEventsResultDTO(
            start_time=start_time,
            end_time=end_time,
            collapsed_events=collapsed_events,
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
            local_timezone: ZoneInfo,
    ) -> tuple[datetime, datetime]:

        start_time = datetime.combine(
            start_date,
            time.min,
            tzinfo=local_timezone,
        )

        end_time = datetime.combine(
            end_date,
            time.max,
            tzinfo=local_timezone,
        )

        return start_time, end_time

    @staticmethod
    def _filter_events_by_time_period(
            events: list[SensorEvent],
            start_time: datetime,
            end_time: datetime,
    ) -> list[SensorEvent]:
        return [
            event
            for event in events
            if start_time <= event.activated_at_local <= end_time
        ]
