# /src/application/ports/user_repo_ports.py

from typing import Protocol

from src.domain.entities.person.user_entities import UserTenantMembership, UserProfile


class UserProfileRepositoryPort(Protocol):

    def list_user_profiles(self) -> tuple[UserProfile, ...]:
        ...

    def get_by_id(
            self,
            user_id: str,
    ) -> UserProfile:
        ...


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