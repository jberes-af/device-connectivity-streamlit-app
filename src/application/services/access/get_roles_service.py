# /src/application/services/access/get_roles_service.py

from typing import Sequence

from src.domain.enums.access.role_enums import UserRoleEnum

from src.domain.entities.access.authorization_entities import (
    RolePermission,
    RoleResourceScope,
)

from src.application.ports.access_repo_ports import (
    RolePermissionRepositoryPort,
    RoleResourceScopeRepositoryPort,
)


class FetchRolePermissionService:

    def __init__(
            self,
            *,
            role_permission_repository: RolePermissionRepositoryPort
    ):
        self._role_repo = role_permission_repository

    def fetch_permissions_for_roles(
            self,
            roles: Sequence[UserRoleEnum],
    ) -> tuple[RolePermission, ...]:
        return tuple(
            self._role_repo.list_for_roles(
                roles=roles)
        )


class FetchRoleResourceScopeService:
    def __init__(
            self,
            *,
            role_resource_scope_repository: RoleResourceScopeRepositoryPort
    ):
        self._scope_repo = role_resource_scope_repository

    def fetch_resource_scopes_for_roles(
            self,
            *,
            roles: Sequence[UserRoleEnum],
    ) -> tuple[RoleResourceScope, ...]:
        return tuple(
            self._scope_repo.list_for_roles(
                roles=roles)
        )
