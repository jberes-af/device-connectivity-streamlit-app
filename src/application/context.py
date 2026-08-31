# /src/application/context.py

from dataclasses import dataclass

from src.domain.enums.access.role_enums import UserRoleEnum

from src.domain.enums.access.resource_access_enums import ResourceScopeEnum

from src.domain.enums.access.permission_enums import PermissionEnum


@dataclass(frozen=True)
class UserContext:
    user_id: str
    tenant_id: str


@dataclass(frozen=True, slots=True)
class AccessScope:
    user_id: str
    roles: frozenset[UserRoleEnum]
    permissions: frozenset[PermissionEnum]
    resident_scope: ResourceScopeEnum
    sensor_scope: ResourceScopeEnum
    gateway_scope: ResourceScopeEnum
    tenant_ids: frozenset[str]
    resident_ids: frozenset[str]
    sensor_ids: frozenset[str]
    gateway_ids: frozenset[str]


@dataclass
class SessionContext:
    user_context: UserContext | None = None
    access_scope: AccessScope | None = None

    @property
    def is_authenticated(self) -> bool:
        return self.user_context is not None
