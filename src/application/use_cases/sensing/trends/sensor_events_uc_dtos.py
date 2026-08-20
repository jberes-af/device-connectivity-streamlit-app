# /src/application/use_cases/sensing/trends/sensor_events_uc_dtos.py

from dataclasses import dataclass
from datetime import date, datetime

from src.domain.entities.sensing.device_entities import SensorEvent

"""
@dataclass(frozen=True)
class MostRecentSensorEventDTO:
    sensor_id: str
    activated_at: datetime | None
    # sensor_state: str | None

@dataclass(frozen=True)
class SensorLastSeenDTO:
    sensor_id: str
    last_seen_time_utc: datetime | str
    last_seen_time_cst: datetime | str
    connectivity_status: str
    status_timestamp: datetime
"""


@dataclass(frozen=True)
class SensorEventsRequestDTO:
    sensor_ids: tuple[str, ...]
    start_date: date
    end_date: date
    local_timezone: str = "America/New_York"


@dataclass(frozen=True)
class SensorEventsResultDTO:
    sensor_id: str
    start_time: datetime
    end_time: datetime
    collapsed_events: tuple[SensorEvent, ...]
    # all_events:  list[SensorEvent]
