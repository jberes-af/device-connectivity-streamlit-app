# /src/main/compose_root_application.py

from dataclasses import dataclass
from pathlib import Path

# --- APPLICATION CONTEXT

from src.application.context import (
    UserContext,
    SessionContext,
)

# --- APPLICATION DTOs


# --- APPLICATION PORTS


# --- APPLICATION USE CASES

from src.application.use_cases.get_patient_records.get_patient_overview_uc import (
    GetPatientOverviewUseCase,
)

# --- INFRASTRUCTURE ADAPTERS

from src.main.compose_root_infrastructure import InfrastructureContainer

# --- INTERFACE ADAPTERS

from src.interface_adapters.presenters.patient.patient_overview_presenter import (
    PatientOverviewPresenter,
)

# --- SERVICE ADAPTERS

# from src.main.compo_root_m365 import build_m365_graph_mail_service

import logging


@dataclass(frozen=True, slots=True)
class AppContainer:
    get_patient_overview_use_case: GetPatientOverviewUseCase
    patient_overview_presenter: PatientOverviewPresenter


def build_application_container(
        infrastructure: InfrastructureContainer,
        user_context: UserContext,
) -> AppContainer:
    # --- ASSIGN USE CASES

    patient_repos = infrastructure.patient_repository

    patient_overview_uc = GetPatientOverviewUseCase(
        patient_repository=patient_repos.patient_repository,
        patient_diagnosis_repository=patient_repos.patient_diagnosis_repository,
        patient_provider_repository=patient_repos.patient_provider_repository,
        patient_payer_repository=patient_repos.patient_payer_repository,
        rtm_enrollment_repository=patient_repos.rtm_enrollment_repository,
        provider_repository=patient_repos.provider_repository,
        payer_repository=patient_repos.payer_repository,
    )

    # --- ASSIGN PRESENTERS

    return AppContainer(
        get_patient_overview_use_case=patient_overview_uc,
        patient_overview_presenter=PatientOverviewPresenter(),
    )
