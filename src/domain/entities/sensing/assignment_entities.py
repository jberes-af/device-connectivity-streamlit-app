# /src/domain/entities/sensing/assignment_entities.py

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class ResidentGatewayLink:
    resident_id: str
    gateway_id: str
    tenant_id: str | None
    active_from_date: date | None = None
    active_to_date: date | None = None
    setup_date: date | None = None
    removed_date: date | None = None


@dataclass(frozen=True)
class ResidentSensorLink:
    resident_id: str
    sensor_id: str
    tenant_id: str | None
    active_from_date: date | None = None
    active_to_date: date | None = None
    setup_date: date | None = None
    removed_date: date | None = None
