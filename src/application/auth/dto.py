# /src/application/auth/dto.py

"""
AuthenticationResultDTO = auth provider output
TenantMembershipDTO = tenant membership projection
LoginRequestDTO = client input
LoginResultDTO = application output
"""

from dataclasses import dataclass

from src.domain.entities.access.membership_entities import UserTenantMembership


@dataclass(frozen=True)
class AuthenticatedUserDTO:
    email: str
    uid: str
    id_token: str = ""
    refresh_token: str = ""
    display_name: str = ""


"""
@dataclass(frozen=True, slots=True)
class TenantMembershipDTO:
    tenant_id: str
    role: UserRoleEnum
"""


@dataclass(frozen=True, slots=True)
class LoginRequestDTO:
    email: str
    password: str


@dataclass(frozen=True, slots=True)
class LoginResultDTO:
    user_id: str
    email: str
    display_name: str
    # memberships: tuple[TenantMembershipDTO, ...]
    memberships: tuple[UserTenantMembership, ...]
