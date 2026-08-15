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

from src.main.infrastructure_containers.sheets_repo_patient import (
    GoogleSheetsPatientRepositories,
    build_google_sheets_patient_repositories,
)

from src.main.infrastructure_containers.sheets_repo_tenant import (
    GoogleSheetsTenantRepositories,
    build_google_sheets_tenant_repositories,
)

from src.main.infrastructure_containers.sheets_repo_user import (
    GoogleSheetsUserRepositories,
    build_google_sheets_user_repositories,
)

# --- INTERFACE ADAPTERS

# --- SERVICE ADAPTERS

# from src.main.compo_root_m365 import build_m365_graph_mail_service

import logging


@dataclass(frozen=True, slots=True)
class InfrastructureContainer:
    settings: Settings
    rtdb: RealtimeDatabasePort

    patient_repository: GoogleSheetsPatientRepositories
    tenant_repository: GoogleSheetsTenantRepositories
    user_repository: GoogleSheetsUserRepositories


def build_infrastructure_container(
        settings: Settings,
        app_config: AppRuntimeConfig,
) -> InfrastructureContainer:
    # FIREBASE REAL-TIME DATABASE

    fb_rtdb = build_realtime_database_adapter(
        settings=settings,
    )

    # --- GOOGLE SHEETS REPOSITORIES: PATIENT

    patient_repos: GoogleSheetsPatientRepositories = (
        build_google_sheets_patient_repositories(
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
    # payer
    # provider_repos TBD
    # resident_repos TBD
    # treatment

    # --- ASSIGN PRESENTERS

    return InfrastructureContainer(
        settings=settings,
        rtdb=fb_rtdb,

        patient_repository=patient_repos,
        tenant_repository=tenant_repos,
        user_repository=user_repos,

    )
