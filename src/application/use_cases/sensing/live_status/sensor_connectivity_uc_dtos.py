# /src/application/dto/sensor_events_uc_dtos.py

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class MostRecentSensorEventDTO:
    sensor_id: str
    activated_at: datetime | None


@dataclass(frozen=True)
class SensorLastSeenDTO:
    sensor_id: str
    last_seen_at_utc: datetime | None
    status_at_utc: datetime | None
    connectivity_state: str | None


@dataclass(frozen=True)
class GetSensorLiveStatusRequestDTO:
    sensor_ids: tuple[str, ...]


@dataclass(frozen=True)
class GetSensorLiveStatusResultDTO:
    sensor_online_statuses: tuple[SensorLastSeenDTO, ...]
    most_recent_events: tuple[MostRecentSensorEventDTO, ...]
