# /src/application/ports/sensing/device_ports.py

from typing import Protocol

from src.domain.entities.sensing.device_entities import (
    GatewayProfile,
    SensorSystemProfile,
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


class SensorRepositoryPort(Protocol):

    def get(
            self,
            sensor_id: str,
            tenant_id: str,
    ) -> SensorSystemProfile | None:
        ...

    def save(self, gateway: SensorSystemProfile) -> None:
        ...
