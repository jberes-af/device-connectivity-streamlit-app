from datetime import UTC, datetime
import unittest

from src.application.services.access.get_roles_service import (
    FetchRolePermissionService,
    FetchRoleResourceScopeService,
)
from src.application.services.access.get_user_resource_service import (
    FetchUserResourceAssignmentService,
)
from src.application.services.access.get_user_tenant_services import (
    FetchUserTenantMembershipService,
    FetchUserTenantRoleAssignmentService,
)
from src.application.use_cases.access.access_scope_uc_dtos import (
    BuildAccessScopeRequestDTO,
)
from src.application.use_cases.access.build_access_scope_use_case import (
    BuildAccessScopeUseCase,
)
from src.domain.entities.access.authorization_entities import (
    RolePermission,
    RoleResourceScope,
)
from src.domain.entities.access.membership_entities import (
    UserTenantMembership,
    UserTenantRoleAssignment,
)
from src.domain.entities.access.resource_access_entities import (
    UserResourceAssignment,
)
from src.domain.enums.access.permission_enums import PermissionEnum
from src.domain.enums.access.resource_access_enums import (
    AccessResourceTypeEnum,
    ResourceScopeEnum,
)
from src.domain.enums.access.role_enums import UserRoleEnum
from src.infrastructure.persistence.google_sheets.mappers.access.role_resource_scope_row_mapper import (
    RoleResourceScopeRowMapper,
)


USER_ID = "user-1"
TENANT_ID = "tenant-1"
MEMBERSHIP_ID = "membership-1"


class MembershipRepository:
    def __init__(self, membership: UserTenantMembership | None) -> None:
        self.membership = membership

    def get_by_user_and_tenant(
            self,
            *,
            user_id: str,
            tenant_id: str,
    ) -> UserTenantMembership:
        if (
                self.membership is None
                or self.membership.user_id != user_id
                or self.membership.tenant_id != tenant_id
        ):
            raise KeyError("Membership not found.")
        return self.membership


class RoleAssignmentRepository:
    def __init__(
            self,
            assignments: tuple[UserTenantRoleAssignment, ...],
    ) -> None:
        self.assignments = assignments

    def list_for_membership_id(
            self,
            *,
            membership_id: str,
    ) -> tuple[UserTenantRoleAssignment, ...]:
        return tuple(
            assignment
            for assignment in self.assignments
            if assignment.membership_id == membership_id
        )


class RolePermissionRepository:
    def __init__(self, records: tuple[RolePermission, ...]) -> None:
        self.records = records
        self.requested_roles: frozenset[UserRoleEnum] = frozenset()

    def list_for_roles(self, *, roles) -> tuple[RolePermission, ...]:
        self.requested_roles = frozenset(roles)
        return tuple(
            record
            for record in self.records
            if record.role in self.requested_roles
        )


class RoleResourceScopeRepository:
    def __init__(self, records: tuple[RoleResourceScope, ...]) -> None:
        self.records = records

    def list_for_roles(self, *, roles) -> tuple[RoleResourceScope, ...]:
        role_set = frozenset(roles)
        return tuple(
            record
            for record in self.records
            if record.role in role_set
        )


class ResourceAssignmentRepository:
    def __init__(
            self,
            assignments: tuple[UserResourceAssignment, ...],
    ) -> None:
        self.assignments = assignments

    def list_for_user_and_tenant(
            self,
            *,
            user_id: str,
            tenant_id: str,
    ) -> tuple[UserResourceAssignment, ...]:
        return tuple(
            assignment
            for assignment in self.assignments
            if assignment.user_id == user_id
            and assignment.tenant_id == tenant_id
        )


def role_assignment(
        role: UserRoleEnum,
        *,
        is_active: bool = True,
) -> UserTenantRoleAssignment:
    return UserTenantRoleAssignment(
        role_assignment_id=f"assignment-{role.value}",
        membership_id=MEMBERSHIP_ID,
        role=role,
        is_active=is_active,
    )


def resource_assignment(
        resource_type: AccessResourceTypeEnum,
        resource_id: str,
        *,
        is_active: bool = True,
) -> UserResourceAssignment:
    return UserResourceAssignment(
        assignment_id=f"assignment-{resource_id}",
        user_id=USER_ID,
        tenant_id=TENANT_ID,
        resource_type=resource_type,
        resource_id=resource_id,
        granted_by_user_id="grantor-1",
        granted_at=datetime(2026, 1, 1, tzinfo=UTC),
        is_active=is_active,
    )


def scope_record(
        role: UserRoleEnum,
        resource_type: AccessResourceTypeEnum,
        scope: ResourceScopeEnum,
) -> RoleResourceScope:
    return RoleResourceScope(
        role=role,
        resource_type=resource_type,
        scope=scope,
    )


class BuildAccessScopeHarness:
    def __init__(
            self,
            *,
            membership: UserTenantMembership | None = None,
            membership_exists: bool = True,
            role_assignments: tuple[UserTenantRoleAssignment, ...] = (),
            permissions: tuple[RolePermission, ...] = (),
            scopes: tuple[RoleResourceScope, ...] = (),
            resource_assignments: tuple[UserResourceAssignment, ...] = (),
    ) -> None:
        if membership is None and membership_exists:
            membership = UserTenantMembership(
                membership_id=MEMBERSHIP_ID,
                user_id=USER_ID,
                tenant_id=TENANT_ID,
            )

        self.permission_repository = RolePermissionRepository(permissions)
        self.use_case = BuildAccessScopeUseCase(
            fetch_user_tenant_membership_service=(
                FetchUserTenantMembershipService(
                    user_tenant_membership_repository=(
                        MembershipRepository(membership)
                    ),
                )
            ),
            fetch_user_tenant_role_assignment_service=(
                FetchUserTenantRoleAssignmentService(
                    user_tenant_role_assignment_repository=(
                        RoleAssignmentRepository(role_assignments)
                    ),
                )
            ),
            fetch_role_permission_service=FetchRolePermissionService(
                role_permission_repository=self.permission_repository,
            ),
            fetch_role_resource_scope_service=(
                FetchRoleResourceScopeService(
                    role_resource_scope_repository=(
                        RoleResourceScopeRepository(scopes)
                    ),
                )
            ),
            fetch_user_resource_assignment_service=(
                FetchUserResourceAssignmentService(
                    user_resource_assignment_repository=(
                        ResourceAssignmentRepository(resource_assignments)
                    ),
                )
            ),
        )

    def execute(self):
        return self.use_case.execute(
            BuildAccessScopeRequestDTO(
                user_id=USER_ID,
                tenant_id=TENANT_ID,
            )
        ).access_scope


class BuildAccessScopeUseCaseTests(unittest.TestCase):
    def test_assigned_caregiver_gets_only_active_explicit_residents(self) -> None:
        scope = BuildAccessScopeHarness(
            role_assignments=(role_assignment(UserRoleEnum.CAREGIVER),),
            permissions=(
                RolePermission(
                    role=UserRoleEnum.CAREGIVER,
                    permission=PermissionEnum.RESIDENT_VIEW,
                ),
                RolePermission(
                    role=UserRoleEnum.CAREGIVER,
                    permission=PermissionEnum.RESIDENT_VIEW,
                ),
            ),
            scopes=(
                scope_record(
                    UserRoleEnum.CAREGIVER,
                    AccessResourceTypeEnum.RESIDENT,
                    ResourceScopeEnum.ASSIGNED,
                ),
            ),
            resource_assignments=(
                resource_assignment(AccessResourceTypeEnum.RESIDENT, "resident-1"),
                resource_assignment(
                    AccessResourceTypeEnum.RESIDENT,
                    "resident-inactive",
                    is_active=False,
                ),
                resource_assignment(AccessResourceTypeEnum.SENSOR, "sensor-1"),
            ),
        ).execute()

        self.assertEqual(scope.resident_scope, ResourceScopeEnum.ASSIGNED)
        self.assertEqual(scope.resident_ids, frozenset({"resident-1"}))
        self.assertEqual(
            scope.permissions,
            frozenset({PermissionEnum.RESIDENT_VIEW}),
        )

    def test_tenant_owner_has_tenant_boundary_and_no_explicit_ids(self) -> None:
        scopes = tuple(
            scope_record(
                UserRoleEnum.OWNER,
                resource_type,
                ResourceScopeEnum.TENANT,
            )
            for resource_type in (
                AccessResourceTypeEnum.RESIDENT,
                AccessResourceTypeEnum.SENSOR,
                AccessResourceTypeEnum.GATEWAY,
            )
        )
        scope = BuildAccessScopeHarness(
            role_assignments=(role_assignment(UserRoleEnum.OWNER),),
            scopes=scopes,
            resource_assignments=(
                resource_assignment(AccessResourceTypeEnum.RESIDENT, "resident-1"),
                resource_assignment(AccessResourceTypeEnum.SENSOR, "sensor-1"),
                resource_assignment(AccessResourceTypeEnum.GATEWAY, "gateway-1"),
            ),
        ).execute()

        self.assertEqual(scope.tenant_ids, frozenset({TENANT_ID}))
        self.assertEqual(scope.resident_scope, ResourceScopeEnum.TENANT)
        self.assertEqual(scope.sensor_scope, ResourceScopeEnum.TENANT)
        self.assertEqual(scope.gateway_scope, ResourceScopeEnum.TENANT)
        self.assertEqual(scope.resident_ids, frozenset())
        self.assertEqual(scope.sensor_ids, frozenset())
        self.assertEqual(scope.gateway_ids, frozenset())

    def test_platform_administrator_has_no_tenant_or_explicit_ids(self) -> None:
        scopes = tuple(
            scope_record(
                UserRoleEnum.PLATFORM_ADMINISTRATOR,
                resource_type,
                ResourceScopeEnum.PLATFORM,
            )
            for resource_type in (
                AccessResourceTypeEnum.RESIDENT,
                AccessResourceTypeEnum.SENSOR,
                AccessResourceTypeEnum.GATEWAY,
            )
        )
        scope = BuildAccessScopeHarness(
            role_assignments=(
                role_assignment(UserRoleEnum.PLATFORM_ADMINISTRATOR),
            ),
            scopes=scopes,
        ).execute()

        self.assertEqual(scope.tenant_ids, frozenset())
        self.assertEqual(scope.resident_scope, ResourceScopeEnum.PLATFORM)
        self.assertEqual(scope.sensor_scope, ResourceScopeEnum.PLATFORM)
        self.assertEqual(scope.gateway_scope, ResourceScopeEnum.PLATFORM)
        self.assertEqual(scope.resident_ids, frozenset())
        self.assertEqual(scope.sensor_ids, frozenset())
        self.assertEqual(scope.gateway_ids, frozenset())

    def test_multiple_roles_use_broadest_scope_for_each_resource(self) -> None:
        cases = (
            (
                (UserRoleEnum.CAREGIVER, ResourceScopeEnum.ASSIGNED),
                (UserRoleEnum.OWNER, ResourceScopeEnum.TENANT),
                ResourceScopeEnum.TENANT,
            ),
            (
                (UserRoleEnum.OWNER, ResourceScopeEnum.TENANT),
                (
                    UserRoleEnum.PLATFORM_ADMINISTRATOR,
                    ResourceScopeEnum.PLATFORM,
                ),
                ResourceScopeEnum.PLATFORM,
            ),
        )

        for first, second, expected in cases:
            with self.subTest(first=first, second=second):
                scope = BuildAccessScopeHarness(
                    role_assignments=(
                        role_assignment(first[0]),
                        role_assignment(second[0]),
                    ),
                    scopes=(
                        scope_record(
                            first[0],
                            AccessResourceTypeEnum.SENSOR,
                            first[1],
                        ),
                        scope_record(
                            second[0],
                            AccessResourceTypeEnum.SENSOR,
                            second[1],
                        ),
                    ),
                ).execute()

                self.assertEqual(scope.sensor_scope, expected)

    def test_mixed_scopes_preserve_required_tenant_boundary(self) -> None:
        scope = BuildAccessScopeHarness(
            role_assignments=(role_assignment(UserRoleEnum.OWNER),),
            scopes=(
                scope_record(
                    UserRoleEnum.OWNER,
                    AccessResourceTypeEnum.RESIDENT,
                    ResourceScopeEnum.TENANT,
                ),
                scope_record(
                    UserRoleEnum.OWNER,
                    AccessResourceTypeEnum.SENSOR,
                    ResourceScopeEnum.PLATFORM,
                ),
                scope_record(
                    UserRoleEnum.OWNER,
                    AccessResourceTypeEnum.GATEWAY,
                    ResourceScopeEnum.ASSIGNED,
                ),
            ),
            resource_assignments=(
                resource_assignment(AccessResourceTypeEnum.GATEWAY, "gateway-1"),
            ),
        ).execute()

        self.assertEqual(scope.resident_scope, ResourceScopeEnum.TENANT)
        self.assertEqual(scope.sensor_scope, ResourceScopeEnum.PLATFORM)
        self.assertEqual(scope.gateway_scope, ResourceScopeEnum.ASSIGNED)
        self.assertEqual(scope.tenant_ids, frozenset({TENANT_ID}))
        self.assertEqual(scope.gateway_ids, frozenset({"gateway-1"}))

    def test_tenant_boundary_is_preserved_when_only_sensor_scope_is_tenant(
            self,
    ) -> None:
        scope = BuildAccessScopeHarness(
            role_assignments=(role_assignment(UserRoleEnum.OWNER),),
            scopes=(
                scope_record(
                    UserRoleEnum.OWNER,
                    AccessResourceTypeEnum.RESIDENT,
                    ResourceScopeEnum.PLATFORM,
                ),
                scope_record(
                    UserRoleEnum.OWNER,
                    AccessResourceTypeEnum.SENSOR,
                    ResourceScopeEnum.TENANT,
                ),
                scope_record(
                    UserRoleEnum.OWNER,
                    AccessResourceTypeEnum.GATEWAY,
                    ResourceScopeEnum.PLATFORM,
                ),
            ),
        ).execute()

        self.assertEqual(scope.tenant_ids, frozenset({TENANT_ID}))

    def test_inactive_membership_is_rejected(self) -> None:
        membership = UserTenantMembership(
            membership_id=MEMBERSHIP_ID,
            user_id=USER_ID,
            tenant_id=TENANT_ID,
            is_active=False,
        )
        harness = BuildAccessScopeHarness(
            membership=membership,
            role_assignments=(role_assignment(UserRoleEnum.CAREGIVER),),
        )

        with self.assertRaises(PermissionError):
            harness.execute()

    def test_nonexistent_membership_is_rejected(self) -> None:
        harness = BuildAccessScopeHarness(
            membership_exists=False,
            role_assignments=(role_assignment(UserRoleEnum.CAREGIVER),),
        )

        with self.assertRaises(KeyError):
            harness.execute()

    def test_inactive_role_assignment_contributes_nothing(self) -> None:
        harness = BuildAccessScopeHarness(
            role_assignments=(
                role_assignment(UserRoleEnum.CAREGIVER),
                role_assignment(
                    UserRoleEnum.PLATFORM_ADMINISTRATOR,
                    is_active=False,
                ),
            ),
            permissions=(
                RolePermission(
                    role=UserRoleEnum.CAREGIVER,
                    permission=PermissionEnum.RESIDENT_VIEW,
                ),
                RolePermission(
                    role=UserRoleEnum.PLATFORM_ADMINISTRATOR,
                    permission=PermissionEnum.ACCESS_MANAGE,
                ),
            ),
            scopes=(
                scope_record(
                    UserRoleEnum.PLATFORM_ADMINISTRATOR,
                    AccessResourceTypeEnum.RESIDENT,
                    ResourceScopeEnum.PLATFORM,
                ),
            ),
        )

        scope = harness.execute()

        self.assertEqual(scope.roles, frozenset({UserRoleEnum.CAREGIVER}))
        self.assertEqual(scope.permissions, frozenset({PermissionEnum.RESIDENT_VIEW}))
        self.assertEqual(scope.resident_scope, ResourceScopeEnum.ASSIGNED)
        self.assertEqual(
            harness.permission_repository.requested_roles,
            frozenset({UserRoleEnum.CAREGIVER}),
        )

    def test_missing_resource_scope_defaults_to_assigned(self) -> None:
        scope = BuildAccessScopeHarness(
            role_assignments=(role_assignment(UserRoleEnum.CAREGIVER),),
        ).execute()

        self.assertEqual(scope.resident_scope, ResourceScopeEnum.ASSIGNED)
        self.assertEqual(scope.sensor_scope, ResourceScopeEnum.ASSIGNED)
        self.assertEqual(scope.gateway_scope, ResourceScopeEnum.ASSIGNED)

    def test_role_resource_scope_mapper_emits_persistence_values(self) -> None:
        row = RoleResourceScopeRowMapper.to_row(
            scope_record(
                UserRoleEnum.OWNER,
                AccessResourceTypeEnum.RESIDENT,
                ResourceScopeEnum.TENANT,
            )
        )

        self.assertEqual(
            row,
            {
                "role": "owner",
                "resource_type": "resident",
                "scope": "tenant",
            },
        )


if __name__ == "__main__":
    unittest.main()
