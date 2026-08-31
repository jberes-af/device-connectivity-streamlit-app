# /src/application/services/access/get_user_tenant_services.py

from src.domain.entities.access.membership_entities import (
    UserTenantMembership,
    UserTenantRoleAssignment,
)

from src.application.ports.access_repo_ports import (
    UserTenantMembershipRepositoryPort,
    UserTenantRoleAssignmentRepositoryPort,
)


class FetchUserTenantMembershipService:

    def __init__(
            self,
            *,
            user_tenant_membership_repository: UserTenantMembershipRepositoryPort
    ):
        self._membership_repo = user_tenant_membership_repository

    def fetch_user_tenant_membership(
            self,
            user_id: str,
            tenant_id: str,
    ) -> UserTenantMembership:
        return self._membership_repo.get_by_user_and_tenant(
            user_id=user_id,
            tenant_id=tenant_id,
        )


class FetchUserTenantRoleAssignmentService:

    def __init__(
            self,
            *,
            user_tenant_role_assignment_repository: UserTenantRoleAssignmentRepositoryPort
    ):
        self._user_tenant_role_repo = user_tenant_role_assignment_repository

    def fetch_user_tenant_role_assignments_for_membership(
            self,
            membership_id: str,
    ) -> tuple[UserTenantRoleAssignment, ...]:
        return self._user_tenant_role_repo.list_for_membership_id(
            membership_id=membership_id)
