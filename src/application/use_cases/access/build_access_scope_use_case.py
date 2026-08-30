# /src/application/use_cases/access/build_access_scope_use_case.py

from src.application.context import AccessScope

from src.application.ports.access_repo_ports import (
    RolePermissionRepositoryPort,
    UserResourceAssignmentRepositoryPort,
    UserTenantMembershipRepositoryPort,
    UserTenantRoleAssignmentRepositoryPort,
)

from src.application.use_cases.access.access_scope_uc_dtos import (
    BuildAccessScopeRequestDTO,
    BuildAccessScopeResultDTO,
)

from src.domain.enums.access.resource_access_enums import (
    AccessResourceTypeEnum,
    ResourceScopeEnum,
)


class BuildAccessScopeUseCase:

    def __init__(
        self,
        *,
        membership_repository: UserTenantMembershipRepositoryPort,
        role_assignment_repository: UserTenantRoleAssignmentRepositoryPort,
        role_permission_repository: RolePermissionRepositoryPort,
        resource_assignment_repository: UserResourceAssignmentRepositoryPort,
    ) -> None:
        self._membership_repository = membership_repository
        self._role_assignment_repository = role_assignment_repository
        self._role_permission_repository = role_permission_repository
        self._resource_assignment_repository = resource_assignment_repository

    def execute(
        self,
        request: BuildAccessScopeRequestDTO,
    ) -> BuildAccessScopeResultDTO:

        # 1. Resolve tenant membership
        membership = self._membership_repository.get_by_user_and_tenant(
            user_id=request.user_id,
            tenant_id=request.tenant_id,
        )

        if not membership.is_active:
            raise PermissionError(
                "User does not have an active tenant membership."
            )

        # 2. Resolve roles
        role_assignments = (
            self._role_assignment_repository.list_for_membership_id(
                membership_id=membership.membership_id,
            )
        )

        roles = frozenset(
            assignment.role
            for assignment in role_assignments
            if assignment.is_active
        )

        # 3. Resolve permissions
        role_permissions = self._role_permission_repository.list_for_roles(
            roles=tuple(roles),
        )

        permissions = frozenset(
            role_permission.permission
            for role_permission in role_permissions
        )

        # 4. Resolve explicit resource assignments
        resource_assignments = (
            self._resource_assignment_repository.list_for_user_and_tenant(
                user_id=request.user_id,
                tenant_id=request.tenant_id,
            )
        )

        active_assignments = tuple(
            assignment
            for assignment in resource_assignments
            if assignment.is_active
        )

        resident_ids = frozenset(
            assignment.resource_id
            for assignment in active_assignments
            if assignment.resource_type
            == AccessResourceTypeEnum.RESIDENT
        )

        sensor_ids = frozenset(
            assignment.resource_id
            for assignment in active_assignments
            if assignment.resource_type
            == AccessResourceTypeEnum.SENSOR
        )

        gateway_ids = frozenset(
            assignment.resource_id
            for assignment in active_assignments
            if assignment.resource_type
            == AccessResourceTypeEnum.GATEWAY
        )

        # 5. Build resolved scope
        access_scope = AccessScope(
            user_id=request.user_id,
            tenant_id=request.tenant_id,

            roles=roles,
            permissions=permissions,

            resident_scope=ResourceScopeEnum.ASSIGNED,
            sensor_scope=ResourceScopeEnum.ASSIGNED,
            gateway_scope=ResourceScopeEnum.ASSIGNED,

            resident_ids=resident_ids,
            sensor_ids=sensor_ids,
            gateway_ids=gateway_ids,
        )

        return BuildAccessScopeResultDTO(
            access_scope=access_scope,
        )