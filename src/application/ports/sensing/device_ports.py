# /src/application/ports/sensing/device_ports.py

from typing import Protocol, Sequence

from src.domain.entities.sensing.device_entities import (
    GatewayProfile,
    SensorSystemProfile,
    SensorEvent,
    DeviceAdministrationProfile
)

from src.domain.entities.sensing.assignment_entities import (
    ResidentGatewayLink,
    ResidentSensorLink,
)

from src.application.models.sensing_models import GatewayDomainObjects


# --- FIREBASE

class GatewayRepositoryPort(Protocol):

    def get(
            self,
            gateway_id: str,
    ) -> GatewayDomainObjects | None:
        ...

    def save(self, gateway: GatewayProfile) -> None:
        ...


class SensorDeviceRepositoryPort(Protocol):

    def get(
            self,
            sensor_id: str,
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


# --- GOOGLE SHEETS


class DeviceAdministrationRepositoryPort(Protocol):

    def list_device_admin_profiles(self) -> tuple[DeviceAdministrationProfile, ...]:
        ...

    def get_by_id(
            self,
            device_id: str,
    ) -> DeviceAdministrationProfile:
        ...

    def get_by_ids(
            self,
            device_ids: Sequence[str],
    ) -> tuple[DeviceAdministrationProfile, ...]:
        ...

    def list_devices_for_tenant_id(
            self,
            tenant_id: str,
    ) -> tuple[DeviceAdministrationProfile, ...]:
        ...

    def list_devices_for_tenant_ids(
            self,
            tenant_ids: tuple[str, ...],
    ) -> tuple[DeviceAdministrationProfile, ...]:
        ...


class ResidentGatewayLinkRepositoryPort(Protocol):

    def list_resident_gateway_links(
            self) -> tuple[ResidentGatewayLink, ...]:
        ...

    def get_by_id(
            self,
            resident_id: str,
    ) -> ResidentGatewayLink:
        ...


class ResidentSensorLinkRepositoryPort(Protocol):

    def list_resident_sensor_links(
            self) -> tuple[ResidentSensorLink, ...]:
        ...

    def get_by_id(
            self,
            resident_id: str,
    ) -> ResidentSensorLink:
        ...
