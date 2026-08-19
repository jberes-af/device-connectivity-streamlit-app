# /src/application/ports/resident_repo_ports.py

from typing import Protocol

from src.domain.entities.person.resident_entities import (
    ResidentProfile,
    ResidentSensorLink,
    ResidentGatewayLink,
    ResidentContactInformation,
    UserResidentAccess,
)


class ResidentProfileRepositoryPort(Protocol):

    def list_resident_profiles(self) -> tuple[ResidentProfile, ...]:
        ...

    def get_by_id(
            self,
            resident_id: str,
    ) -> ResidentProfile:
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


class ResidentGatewayLinkRepositoryPort(Protocol):

    def list_resident_gateway_links(
            self) -> tuple[ResidentGatewayLink, ...]:
        ...

    def get_by_id(
            self,
            resident_id: str,
    ) -> ResidentGatewayLink:
        ...


class ResidentContactInformationRepositoryPort(Protocol):

    def get_by_id(
            self,
            resident_id: str,
    ) -> ResidentContactInformation:
        ...


class UserResidentAccessRepositoryPort(Protocol):

    def list_resident_access_records_for_user_id(
            self,
            user_id: str
    ) -> tuple[UserResidentAccess, ...]:
        ...

    def get_by_id(
            self,
            resident_id: str,
    ) -> UserResidentAccess:
        ...
