# /src/application/ports/access_repo_ports.py

from typing import Protocol, Sequence

from src.domain.enums.access.role_enums import UserRoleEnum

from src.domain.entities.access.authorization_entities import RolePermission

from src.domain.entities.access.membership_entities import (
    UserTenantMembership,
    UserTenantRoleAssignment,
)

from src.domain.entities.access.resource_access_entities import (
    UserResourceAssignment,
)


class UserTenantMembershipRepositoryPort(Protocol):

    def get_by_user_and_tenant(
            self,
            *,
            user_id: str,
            tenant_id: str,
    ) -> UserTenantMembership:
        ...


class UserTenantRoleAssignmentRepositoryPort(Protocol):

    def list_for_membership_id(
            self,
            *,
            membership_id: str,
    ) -> tuple[UserTenantRoleAssignment, ...]:
        ...


class RolePermissionRepositoryPort(Protocol):

    def list_for_roles(
            self,
            *,
            roles: Sequence[UserRoleEnum],
    ) -> tuple[RolePermission, ...]:
        ...


class UserResourceAssignmentRepositoryPort(Protocol):

    def list_for_user_and_tenant(
            self,
            *,
            user_id: str,
            tenant_id: str,
    ) -> tuple[UserResourceAssignment, ...]:
        ...
