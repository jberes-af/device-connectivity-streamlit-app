# /src/application/ports/sensing/device_ports.py

from typing import Protocol

from src.domain.entities.sensing.device_entities import (
    GatewayProfile,
    SensorSystemProfile,
    SensorEvent,
)

from src.application.models.sensing_models import GatewayDomainObjects


class GatewayRepositoryPort(Protocol):

    def get(
            self,
            gateway_id: str,
            tenant_id: str,
    ) -> GatewayDomainObjects | None:
        ...

    def save(self, gateway: GatewayProfile) -> None:
        ...


class SensorDeviceRepositoryPort(Protocol):

    def get(
            self,
            sensor_id: str,
            tenant_id: str,
    ) -> SensorSystemProfile | None:
        ...

    def save(self, gateway: SensorSystemProfile) -> None:
        ...


class SensorEventRepositoryPort(Protocol):

    def get_all_sensor_events(
            self,
            sensor_id: str,
    ) -> tuple[SensorEvent, ...] | None:
        ...

    def get_last_sensor_event(
            self,
            sensor_id: str,
    ) -> SensorEvent | None:
        ...
