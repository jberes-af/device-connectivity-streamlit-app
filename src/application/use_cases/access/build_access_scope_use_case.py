# /src/application/use_cases/access/build_access_scope_use_case.py

from src.application.context import AccessScope

from src.domain.enums.access.permission_enums import PermissionEnum

from src.domain.enums.access.role_enums import UserRoleEnum

from src.domain.entities.access.membership_entities import (
    UserTenantMembership,
    UserTenantRoleAssignment,
)

from src.domain.entities.access.authorization_entities import (
    RolePermission,
    RoleResourceScope,
)

from src.domain.entities.access.resource_access_entities import (
    UserResourceAssignment,
)

from src.application.services.access.get_user_tenant_services import (
    FetchUserTenantMembershipService,
    FetchUserTenantRoleAssignmentService,
)

from src.application.services.access.get_roles_service import (
    FetchRolePermissionService,
    FetchRoleResourceScopeService,
)

from src.application.services.access.get_user_resource_service import (
    FetchUserResourceAssignmentService
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
            fetch_user_tenant_membership_service: FetchUserTenantMembershipService,
            fetch_user_tenant_role_assignment_service: FetchUserTenantRoleAssignmentService,
            fetch_role_permission_service: FetchRolePermissionService,
            fetch_user_resource_assignment_service: FetchUserResourceAssignmentService,
            fetch_role_resource_scope_service: FetchRoleResourceScopeService,
    ) -> None:
        self._fetch_user_tenant_membership_service = fetch_user_tenant_membership_service
        self._fetch_user_tenant_role_service = fetch_user_tenant_role_assignment_service
        self._fetch_role_permission_service = fetch_role_permission_service
        self._fetch_user_resource_service = fetch_user_resource_assignment_service
        self._fetch_resource_scope_service = fetch_role_resource_scope_service

    def execute(
            self,
            request: BuildAccessScopeRequestDTO,
    ) -> BuildAccessScopeResultDTO:
        # --- RESOLVE MEMBERSHIP

        membership: UserTenantMembership = (
            self._fetch_user_tenant_membership_service
            .fetch_user_tenant_membership(
                user_id=request.user_id,
                tenant_id=request.tenant_id,
            ))

        if not membership.is_active:
            raise PermissionError(
                "User does not have an active tenant membership."
            )

        # --- RESOLVE ROLES

        role_assignments: tuple[UserTenantRoleAssignment, ...] = (
            self._fetch_user_tenant_role_service
            .fetch_user_tenant_role_assignments_for_membership(
                membership_id=membership.membership_id,
            )
        )

        roles: frozenset[UserRoleEnum] = frozenset(
            assignment.role
            for assignment in role_assignments
            if assignment.is_active
        )

        if not roles:
            raise PermissionError(
                "User does not have an active role."
            )

        # --- RESOLVE PERMISSIONS

        role_permissions: tuple[RolePermission, ...] = (
            self._fetch_role_permission_service.fetch_permissions_for_roles(
                roles=tuple(roles),
            ))

        permissions: frozenset[PermissionEnum] = frozenset(
            role_permission.permission
            for role_permission in role_permissions
        )

        # --- RESOLVE RESOURCE SCOPES

        role_resource_scopes: tuple[
            RoleResourceScope, ...
        ] = (
            self._fetch_resource_scope_service
            .fetch_resource_scopes_for_roles(
                roles=tuple(roles),
            )
        )

        resident_scope: ResourceScopeEnum = (
            self._resolve_resource_scope(
                resource_type=AccessResourceTypeEnum.RESIDENT,
                role_resource_scopes=role_resource_scopes,
            )
        )

        sensor_scope: ResourceScopeEnum = (
            self._resolve_resource_scope(
                resource_type=AccessResourceTypeEnum.SENSOR,
                role_resource_scopes=role_resource_scopes,
            )
        )

        gateway_scope: ResourceScopeEnum = (
            self._resolve_resource_scope(
                resource_type=AccessResourceTypeEnum.GATEWAY,
                role_resource_scopes=role_resource_scopes,
            )
        )

        # --- RESOLVE RESOURCE ASSIGNMENTS

        resource_assignments: tuple[
            UserResourceAssignment, ...
        ] = (
            self._fetch_user_resource_service
            .fetch_resource_assignments_for_user(
                user_id=request.user_id,
                tenant_id=request.tenant_id,
            )
        )

        active_assignments: tuple[
            UserResourceAssignment, ...
        ] = tuple(
            assignment
            for assignment in resource_assignments
            if assignment.is_active
        )

        # --- Resolve IDs WHERE SCOPE == ASSIGNED

        resident_ids: frozenset[str] = (
            self._resolve_assigned_resource_ids(
                resource_type=AccessResourceTypeEnum.RESIDENT,
                scope=resident_scope,
                assignments=active_assignments,
            )
        )

        sensor_ids: frozenset[str] = (
            self._resolve_assigned_resource_ids(
                resource_type=AccessResourceTypeEnum.SENSOR,
                scope=sensor_scope,
                assignments=active_assignments,
            )
        )

        gateway_ids: frozenset[str] = (
            self._resolve_assigned_resource_ids(
                resource_type=AccessResourceTypeEnum.GATEWAY,
                scope=gateway_scope,
                assignments=active_assignments,
            )
        )

        # --- RESOLVE TENANT BOUNDARY

        has_platform_scope = any(
            scope == ResourceScopeEnum.PLATFORM
            for scope in (
                resident_scope,
                sensor_scope,
                gateway_scope,
            )
        )

        tenant_ids: frozenset[str] = (
            frozenset()
            if has_platform_scope
            else frozenset({
                request.tenant_id,
            })
        )

        # BUILD ACCESS SCOPE

        access_scope = AccessScope(
            user_id=request.user_id,
            roles=roles,
            permissions=permissions,
            resident_scope=resident_scope,
            sensor_scope=sensor_scope,
            gateway_scope=gateway_scope,
            tenant_ids=tenant_ids,
            resident_ids=resident_ids,
            sensor_ids=sensor_ids,
            gateway_ids=gateway_ids,
        )

        return BuildAccessScopeResultDTO(
            access_scope=access_scope,
        )

    @staticmethod
    def _resolve_resource_scope(
            *,
            resource_type: AccessResourceTypeEnum,
            role_resource_scopes: tuple[
                RoleResourceScope, ...
            ],
    ) -> ResourceScopeEnum:

        matching_scopes = tuple(
            item.scope
            for item in role_resource_scopes
            if item.resource_type == resource_type
        )

        if not matching_scopes:
            return ResourceScopeEnum.ASSIGNED

        scope_rank = {
            ResourceScopeEnum.ASSIGNED: 1,
            ResourceScopeEnum.TENANT: 2,
            ResourceScopeEnum.PLATFORM: 3,
        }

        return max(
            matching_scopes,
            key=lambda scope: scope_rank[scope],
        )

    @staticmethod
    def _resolve_assigned_resource_ids(
            *,
            resource_type: AccessResourceTypeEnum,
            scope: ResourceScopeEnum,
            assignments: tuple[
                UserResourceAssignment, ...
            ],
    ) -> frozenset[str]:

        if scope != ResourceScopeEnum.ASSIGNED:
            return frozenset()

        return frozenset(
            assignment.resource_id
            for assignment in assignments
            if assignment.resource_type == resource_type
        )
