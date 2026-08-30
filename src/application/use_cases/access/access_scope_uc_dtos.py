# /src/application/use_cases/access/access_scope_uc_dtos.py

from dataclasses import dataclass

from src.domain.enums.access.permission_enums import PermissionEnum
from src.domain.enums.access.resource_access_enums import ResourceScopeEnum
from src.domain.enums.access.role_enums import UserRoleEnum


@dataclass(frozen=True, slots=True)
class BuildAccessScopeRequestDTO:
    user_id: str
    tenant_id: str


@dataclass(frozen=True, slots=True)
class AccessScope:
    user_id: str
    tenant_id: str
    roles: frozenset[UserRoleEnum]
    permissions: frozenset[PermissionEnum]
    resident_scope: ResourceScopeEnum
    sensor_scope: ResourceScopeEnum
    gateway_scope: ResourceScopeEnum
    resident_ids: frozenset[str]
    sensor_ids: frozenset[str]
    gateway_ids: frozenset[str]


@dataclass(frozen=True, slots=True)
class BuildAccessScopeResultDTO:
    access_scope: AccessScope


"""
@dataclass(frozen=True)
class AccessScopeRequestDTO:
    user_id: str
    tenant_id: str


@dataclass(frozen=True, slots=True)
class AccessScopeResultDTO:
    resident_ids: tuple[str, ...]
    sensor_ids: tuple[str, ...]
    gateway_ids: tuple[str, ...]
    tenant_profile: TenantProfile
"""
