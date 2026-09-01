# src/application/ports/sensing/sensor_connectivity_status_port.py

from typing import Protocol

from src.domain.entities.sensing.sensor_connectivity_entities import (
    SensorConnectivityStatus,
)


class SensorConnectivityStatusPort(Protocol):

    def get_status(
        self,
        *,
        sensor_id: str,
    ) -> SensorConnectivityStatus | None:
        ...