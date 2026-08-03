# /src/main/composition_root.py

from dataclasses import dataclass
from pathlib import Path

# --- APPLICATION DTOs


# --- APPLICATION PORTS

from src.application.ports.patient_repo_ports import (
    PatientRepositoryPort,
)

# from src.application.ports.m365_email_ports import MailSenderPort

# --- APPLICATION USE CASES

from src.application.use_cases.get_patient_records.get_patient_overview_uc import (
    GetPatientOverviewUseCase,
)

# --- INFRASTRUCTURE CONFIGURATION

from src.infrastructure.config.app_config_loader import (
    AppConfigLoader,
)
from src.infrastructure.config.app_config_models import (
    AppRuntimeConfig,
)
from src.infrastructure.config.secret_provider import (
    EnvSecretProvider,
    StreamlitSecretProvider,
    FallbackSecretProvider,
    SecretProvider,
)

from src.infrastructure.config.settings_loader import (
    load_settings,
)

from src.infrastructure.config.settings_model import (
    Settings,
)

# --- REPOSITORY BUILDERS

from src.main.compo_root_google_sheets_repos.compo_root_patient_repos import (
    GoogleSheetsPatientRepositories,
    build_google_sheets_patient_repositories,
)

# --- INTERFACE ADAPTERS

from src.interface_adapters.presenters.patient.patient_overview_presenter import (
    PatientOverviewPresenter,
)

# --- SERVICE ADAPTERS

# from src.main.compo_root_m365 import build_m365_graph_mail_service

import logging


@dataclass(frozen=True, slots=True)
class AppContainer:
    # settings: Settings
    # app_config: AppRuntimeConfig
    # patient_admin_repo: PatientRepositoryPort
    get_patient_overview_use_case: GetPatientOverviewUseCase
    patient_overview_presenter: PatientOverviewPresenter


def _resolve_project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _build_secret_provider(
        *,
        project_root: Path,
) -> SecretProvider:
    secret_provider = FallbackSecretProvider(
        StreamlitSecretProvider(),
        EnvSecretProvider(
            env_path=project_root / ".env",
            require_env_file=False,
        ),
    )
    return secret_provider


def load_runtime_config() -> tuple[Settings, AppRuntimeConfig]:
    project_root = _resolve_project_root()

    logging.info("Project root resolved: %s", project_root)

    secret_provider = _build_secret_provider(
        project_root=project_root,
    )

    settings = load_settings(
        project_root=project_root,
        secret_provider=secret_provider,
    )

    app_config = AppConfigLoader.load_from_json(
        settings.config_path,
        project_root=project_root,
    )

    return settings, app_config


def build_app_container() -> AppContainer:
    runtime_config: tuple[Settings, AppRuntimeConfig] = load_runtime_config()
    settings: Settings = runtime_config[0]
    app_config: AppRuntimeConfig = runtime_config[1]

    # --- ASSIGN REPOSITORIES: PATIENT

    patient_repos: GoogleSheetsPatientRepositories = (
        build_google_sheets_patient_repositories(
            settings=settings,
            app_config=app_config,
        ))

    # --- ASSIGN USE CASES

    # Stateless use case: runtime records are supplied in the request DTO.
    # filter_pipeline_records_uc = FilterPipelineRecordsUseCase()

    patient_overview_uc = GetPatientOverviewUseCase(
        patient_repository=patient_repos.patient_repository,
        patient_diagnosis_repository=patient_repos.patient_diagnosis_repository,
        patient_provider_repository=patient_repos.patient_provider_repository,
        patient_payer_repository=patient_repos.patient_payer_repository,
        rtm_enrollment_repository=patient_repos.rtm_enrollment_repository,
    )

    # --- ASSIGN PRESENTERS

    return AppContainer(
        get_patient_overview_use_case=patient_overview_uc,
        patient_overview_presenter=PatientOverviewPresenter(),
    )
