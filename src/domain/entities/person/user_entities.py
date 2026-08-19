# /src/domain/entities/person/user_entities.py

from dataclasses import dataclass

from src.domain.enums.person.tenant_enums import (
    UserRoleEnum,
    PermissionEnum,
)


@dataclass(frozen=True)
class UserTenantMembership:
    user_id: str
    tenant_id: str
    role: UserRoleEnum
    is_active: bool = True


@dataclass(frozen=True)
class UserPermissionOverride:
    user_id: str
    tenant_id: str
    permission: PermissionEnum
    is_granted: bool


@dataclass(frozen=True)
class UserLoginCredentials:
    user_id: str
    user_login_id: str
    user_password: str


@dataclass(frozen=True)
class UserProfile:
    user_id: str
    user_name: str
    telephone: str
    email_address: str
    user_image: str
    color_scheme: str


"""
@dataclass(frozen=True)
class UserResidentAccess:
    tenant_id: str
    user_id: str
    resident_id: str
"""
