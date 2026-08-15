# /src/main/infrastructure_containers/sheets_repo_user.py

from dataclasses import dataclass

from src.application.ports.user_repo_ports import (
    UserProfileRepositoryPort,
    UserTenantMembershipRepositoryPort,
)

from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)
from src.infrastructure.config.settings_model import (
    Settings,
)
from src.infrastructure.persistence.google_sheets.mappers.user.user_profile_row_mapper import (
    UserProfileRowMapper,
)

from src.infrastructure.persistence.google_sheets.mappers.user.user_tenant_membership_row_mapper import (
    UserTenantMembershipRowMapper,
)

from src.infrastructure.persistence.google_sheets.repos.user.user_profile_repository import (
    GoogleSheetsUserProfileRepository,
)

from src.infrastructure.persistence.google_sheets.repos.user.user_tenant_membership_repository import (
    GoogleSheetsUserTenantMembershipRepository,
)

from src.main.infrastructure_containers.utils_sheets_composition_root import (
    build_google_sheets_query_service,
    build_google_sheet_catalog,
)


@dataclass(frozen=True, slots=True)
class GoogleSheetsUserRepositories:
    user_profile_repository: UserProfileRepositoryPort
    user_tenant_membership_repository: UserTenantMembershipRepositoryPort


def build_google_sheets_user_repositories(
        *,
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> GoogleSheetsUserRepositories:
    query_service = build_google_sheets_query_service(
        settings=settings,
    )

    catalog = build_google_sheet_catalog(
        settings=settings,
        app_config=app_config,
    )

    user_profile_repository: UserProfileRepositoryPort = (
        GoogleSheetsUserProfileRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=UserProfileRowMapper(),
        ))

    user_tenant_membership_repository: UserTenantMembershipRepositoryPort = (
        GoogleSheetsUserTenantMembershipRepository(
            query_service=query_service,
            catalog=catalog,
            mapper=UserTenantMembershipRowMapper(),
        ))

    return GoogleSheetsUserRepositories(
        user_profile_repository=user_profile_repository,
        user_tenant_membership_repository=user_tenant_membership_repository,
    )
