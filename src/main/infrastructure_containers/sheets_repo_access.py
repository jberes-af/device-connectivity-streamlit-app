# /src/main/infrastructure_containers/sheets_repo_access.py

from dataclasses import dataclass

from src.application.ports.access_repo_ports import (
    UserTenantMembershipRepositoryPort,
    UserTenantRoleAssignmentRepositoryPort,
    RolePermissionRepositoryPort,
    UserResourceAssignmentRepositoryPort, RoleResourceScopeRepositoryPort,
)

from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)
from src.infrastructure.config.settings_model import (
    Settings,
)
from src.infrastructure.persistence.google_sheets.mappers.access.role_resource_scope_row_mapper import \
    RoleResourceScopeRowMapper

from src.infrastructure.persistence.google_sheets.mappers.access.user_tenant_membership_row_mapper import (
    UserTenantMembershipRowMapper,
)

from src.infrastructure.persistence.google_sheets.mappers.access.user_tenant_role_assignment_row_mapper import (
    UserTenantRoleAssignmentRowMapper,
)

from src.infrastructure.persistence.google_sheets.mappers.access.role_permission_row_mapper import (
    RolePermissionRowMapper,
)

from src.infrastructure.persistence.google_sheets.mappers.access.user_resource_assignment_row_mapper import (
    UserResourceAssignmentRowMapper
)
from src.infrastructure.persistence.google_sheets.repos.access.role_resource_scope_repository import \
    GoogleSheetsRoleResourceScopeRepository

from src.infrastructure.persistence.google_sheets.repos.access.user_tenant_role_assignment_repository import (
    GoogleSheetsUserTenantRoleAssignmentRepository,
)

from src.infrastructure.persistence.google_sheets.repos.access.user_tenant_membership_repository import (
    GoogleSheetsUserTenantMembershipRepository,
)

from src.infrastructure.persistence.google_sheets.repos.access.user_resource_assignment_repository import (
    GoogleSheetsUserResourceAssignmentRepository
)

from src.infrastructure.persistence.google_sheets.repos.access.role_permission_repository import (
    GoogleSheetsRolePermissionRepository,
)

from src.main.infrastructure_containers.utils_sheets_composition_root import (
    build_google_sheets_query_service,
    build_google_sheet_catalog,
)


@dataclass(frozen=True, slots=True)
class GoogleSheetsAccessRepositories:
    user_tenant_membership_repository: UserTenantMembershipRepositoryPort
    user_tenant_role_assignment_repository: UserTenantRoleAssignmentRepositoryPort
    role_permission_repository: RolePermissionRepositoryPort
    user_resource_assignment_repository: UserResourceAssignmentRepositoryPort
    role_resource_scope_repository: RoleResourceScopeRepositoryPort


def build_google_sheets_access_repositories(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> GoogleSheetsAccessRepositories:
    query_service = build_google_sheets_query_service(
        settings=settings,
    )

    catalog = build_google_sheet_catalog(
        settings=settings,
        app_config=app_config,
    )

    user_tenant_membership_repo: UserTenantMembershipRepositoryPort = (
        GoogleSheetsUserTenantMembershipRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=UserTenantMembershipRowMapper(),
        ))

    user_tenant_role_repo: UserTenantRoleAssignmentRepositoryPort = (
        GoogleSheetsUserTenantRoleAssignmentRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=UserTenantRoleAssignmentRowMapper(),
        ))

    role_permission_repo: RolePermissionRepositoryPort = (
        GoogleSheetsRolePermissionRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=RolePermissionRowMapper(),
        )
    )

    role_scope_repo: RoleResourceScopeRepositoryPort = (
        GoogleSheetsRoleResourceScopeRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=RoleResourceScopeRowMapper(),
        )
    )

    user_resident_repo: UserResourceAssignmentRepositoryPort = (
        GoogleSheetsUserResourceAssignmentRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=UserResourceAssignmentRowMapper(),
        ))

    return GoogleSheetsAccessRepositories(
        user_tenant_membership_repository=user_tenant_membership_repo,
        user_tenant_role_assignment_repository=user_tenant_role_repo,
        role_permission_repository=role_permission_repo,
        user_resource_assignment_repository=user_resident_repo,
        role_resource_scope_repository=role_scope_repo,
    )
