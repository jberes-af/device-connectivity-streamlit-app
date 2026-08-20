# /src/application/ports/access_repo_ports.py

from typing import Protocol

from src.domain.entities.access.access_entities import UserTenantMembership, ResidentGatewayLink, ResidentSensorLink, \
    UserResidentAccess


class UserTenantMembershipRepositoryPort(Protocol):

    def list_all_user_tenant_memberships(
            self) -> tuple[UserTenantMembership, ...]:
        ...

    def list_tenant_memberships_by_user_id(
            self,
            user_id: str,
    ) -> tuple[UserTenantMembership, ...]:
        ...

    def get_by_user_and_tenant(
            self,
            user_id: str,
            tenant_id: str,
    ) -> UserTenantMembership | None:
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
