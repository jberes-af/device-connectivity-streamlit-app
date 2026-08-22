# /src/main/compose_root_infrastructure.py

from dataclasses import dataclass

from src.application.ports.sensing.realtime_database_port import (
    RealtimeDatabasePort,
)

# --- INFRASTRUCTURE CONFIGURATION

from src.infrastructure.config.settings_model import (
    Settings,
)
from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)

# --- REPOSITORY BUILDERS

from src.main.infrastructure_containers.firebase_rtdb import (
    build_realtime_database_adapter,
)

from src.main.infrastructure_containers.sheets_repo_access import (
    GoogleSheetsAccessRepositories,
    build_google_sheets_access_repositories,
)

from src.main.infrastructure_containers.sheets_repo_patient import (
    GoogleSheetsPatientRepositories,
    build_google_sheets_patient_repositories,
)

from src.main.infrastructure_containers.sheets_repo_payer import (
    GoogleSheetsPayerRepositories,
    build_google_sheets_payer_repositories,
)

from src.main.infrastructure_containers.sheets_repo_provider import (
    GoogleSheetsProviderRepositories,
    build_google_sheets_provider_repositories,
)

from src.main.infrastructure_containers.sheets_repo_resident import (
    GoogleSheetsResidentRepositories,
    build_google_sheets_resident_repositories,
)

from src.main.infrastructure_containers.sheets_repo_rtm import (
    GoogleSheetsRtmRepositories,
    build_google_sheets_rtm_repositories,
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

# --- INTERFACE ADAPTERS

# --- SERVICE ADAPTERS

# from src.main.compo_root_m365 import build_m365_graph_mail_service

# import logging


@dataclass(frozen=True, slots=True)
class InfrastructureContainer:
    settings: Settings

    rtdb: RealtimeDatabasePort
    sensing_repositories: FirebaseSensingRepositories

    access_repository: GoogleSheetsAccessRepositories
    patient_repository: GoogleSheetsPatientRepositories
    payer_repository: GoogleSheetsPayerRepositories
    provider_repository: GoogleSheetsProviderRepositories
    resident_repository: GoogleSheetsResidentRepositories
    rtm_repository: GoogleSheetsRtmRepositories
    tenant_repository: GoogleSheetsTenantRepositories
    user_repository: GoogleSheetsUserRepositories


def build_infrastructure_container(
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> InfrastructureContainer:
    # FIREBASE REAL-TIME DATABASE

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

    payer_repos: GoogleSheetsPayerRepositories = (
        build_google_sheets_payer_repositories(
            settings=settings,
            app_config=app_config,
        ))

    provider_repos: GoogleSheetsProviderRepositories = (
        build_google_sheets_provider_repositories(
            settings=settings,
            app_config=app_config,
        ))

    patient_repos: GoogleSheetsPatientRepositories = (
        build_google_sheets_patient_repositories(
            settings=settings,
            app_config=app_config,
        ))

    resident_repos: GoogleSheetsResidentRepositories = (
        build_google_sheets_resident_repositories(
            settings=settings,
            app_config=app_config,
        ))

    rtm_repos: GoogleSheetsRtmRepositories = (
        build_google_sheets_rtm_repositories(
            settings=settings,
            app_config=app_config,
        ))

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

    # billing repos TBD
    # care plan
    # treatment

    # --- ASSIGN PRESENTERS

    return InfrastructureContainer(
        settings=settings,

        rtdb=fb_rtdb,
        sensing_repositories=sensing_repos,

        access_repository=access_repos,
        patient_repository=patient_repos,
        payer_repository=payer_repos,
        provider_repository=provider_repos,
        resident_repository=resident_repos,
        rtm_repository=rtm_repos,
        tenant_repository=tenant_repos,
        user_repository=user_repos,
    )
