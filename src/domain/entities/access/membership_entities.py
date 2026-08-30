# /src/domain/entities/access/membership_entities.py

from dataclasses import dataclass

from src.domain.enums.access.role_enums import UserRoleEnum


@dataclass(frozen=True)
class UserTenantMembership:
    membership_id: str
    user_id: str
    tenant_id: str
    is_active: bool = True


@dataclass(frozen=True)
class UserTenantRoleAssignment:
    role_assignment_id: str
    membership_id: str
    role: UserRoleEnum
    is_active: bool = True
