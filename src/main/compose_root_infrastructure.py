# /src/main/compose_root_infrastructure.py

from dataclasses import dataclass

from src.application.ports.sensing.realtime_database_port import (
    RealtimeDatabasePort,
)

from src.application.ports.sensing.sensor_connectivity_status_port import (
    SensorConnectivityStatusPort
)

# --- INFRASTRUCTURE CONFIGURATION

from src.infrastructure.config.settings_model import (
    Settings,
)
from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)

# --- REPOSITORY BUILDERS

from src.main.infrastructure_containers.compose_root_aws_appsync import (
    build_aws_appsync_adapter
)

from src.main.infrastructure_containers.firebase_rtdb import (
    build_realtime_database_adapter,
)

from src.main.infrastructure_containers.sheets_repo_access import (
    GoogleSheetsAccessRepositories,
    build_google_sheets_access_repositories,
)
from src.main.infrastructure_containers.sheets_repo_device_admin import (
    GoogleSheetsDeviceAdminRepositories,
    build_google_sheets_device_admin_repositories,
)


from src.main.infrastructure_containers.sheets_repo_tenant import (
    GoogleSheetsTenantRepositories,
    build_google_sheets_tenant_repositories,
)
from src.main.infrastructure_containers.sheets_repo_user import (
    GoogleSheetsUserRepositories,
    build_google_sheets_user_repositories,
)

from src.main.infrastructure_containers.firebase_repositories import (
    FirebaseSensingRepositories,
    build_firebase_sensing_repositories,
)


# from src.main.compo_root_m365 import build_m365_graph_mail_service


@dataclass(frozen=True, slots=True)
class InfrastructureContainer:
    settings: Settings

    appsync: SensorConnectivityStatusPort

    rtdb: RealtimeDatabasePort
    sensing_repositories: FirebaseSensingRepositories

    access_repository: GoogleSheetsAccessRepositories
    device_admin_repository: GoogleSheetsDeviceAdminRepositories
    tenant_repository: GoogleSheetsTenantRepositories
    user_repository: GoogleSheetsUserRepositories


def build_infrastructure_container(
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> InfrastructureContainer:
    # --- AWS APPSYNC

    appsync_adapter: SensorConnectivityStatusPort = (
        build_aws_appsync_adapter(
            settings=settings,
        )
    )

    # --- FIREBASE REAL-TIME DATABASE

    fb_rtdb: RealtimeDatabasePort = build_realtime_database_adapter(
        settings=settings,
    )

    sensing_repos = build_firebase_sensing_repositories(
        database=fb_rtdb,
    )

    # --- GOOGLE SHEETS REPOSITORIES

    access_repos: GoogleSheetsAccessRepositories = (
        build_google_sheets_access_repositories(
            settings=settings,
            app_config=app_config,
        ))

    device_admin_repos: GoogleSheetsDeviceAdminRepositories = (
        build_google_sheets_device_admin_repositories(
            settings=settings,
            app_config=app_config,
        )
    )

    tenant_repos: GoogleSheetsTenantRepositories = (
        build_google_sheets_tenant_repositories(
            settings=settings,
            app_config=app_config,
        ))


    user_repos: GoogleSheetsUserRepositories = (
        build_google_sheets_user_repositories(
            settings=settings,
            app_config=app_config,
        ))


    # --- ASSIGN PRESENTERS

    return InfrastructureContainer(
        settings=settings,

        appsync=appsync_adapter,

        rtdb=fb_rtdb,
        sensing_repositories=sensing_repos,

        access_repository=access_repos,
        device_admin_repository=device_admin_repos,
        tenant_repository=tenant_repos,
        user_repository=user_repos,
    )
