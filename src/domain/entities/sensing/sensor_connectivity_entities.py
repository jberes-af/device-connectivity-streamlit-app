# /src/domain/entities/sensing/sensor_connectivity_entities.py

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class SensorConnectivityStatus:
    sensor_id: str
    last_seen_at_utc: datetime | None
    status_at_utc: datetime | None
    connectivity_state: str | None
