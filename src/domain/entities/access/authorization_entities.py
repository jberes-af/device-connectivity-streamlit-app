# authorization_entities.py

from dataclasses import dataclass
from datetime import datetime

from src.domain.enums.access.permission_enums import PermissionEnum
from src.domain.enums.access.resource_access_enums import (
    AccessResourceTypeEnum,
    ResourceScopeEnum,
)
from src.domain.enums.access.role_enums import UserRoleEnum


@dataclass(frozen=True)
class RolePermission:
    role: UserRoleEnum
    permission: PermissionEnum


@dataclass(frozen=True, slots=True)
class RoleResourceScope:
    role: UserRoleEnum
    resource_type: AccessResourceTypeEnum
    scope: ResourceScopeEnum


@dataclass(frozen=True)
class UserPermissionOverride:
    override_id: str
    user_id: str
    tenant_id: str
    permission: PermissionEnum
    is_granted: bool
    granted_by_user_id: str
    created_at: datetime
