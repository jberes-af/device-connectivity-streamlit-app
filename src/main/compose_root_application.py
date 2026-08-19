# /src/main/compose_root_application.py

from dataclasses import dataclass

# --- APPLICATION CONTEXT

from src.application.context import (
    UserContext,
    # SessionContext,
)

# --- APPLICATION DTOs


# --- APPLICATION USE CASES

from src.application.use_cases.resident.get_all_resident_records_for_user_uc import (
    GetAllResidentRecordsForUserUseCase,
)

from src.application.use_cases.sensing.get_user_sensing_account_uc import (
    GetUserSensingAccountUseCase,
)

# from src.application.use_cases.patient.get_patient_overview_uc import (GetPatientOverviewUseCase, )

# --- INFRASTRUCTURE ADAPTERS

from src.main.compose_root_infrastructure import InfrastructureContainer

# --- INTERFACE ADAPTERS

# from src.interface_adapters.presenters.patient.patient_overview_presenter import (    PatientOverviewPresenter,)

from src.interface_adapters.presenters.resident.resident_main_page_presenter import (
    ResidentMainPagePresenter,
)


# --- SERVICE ADAPTERS

# from src.main.compo_root_m365 import build_m365_graph_mail_service

# import logging


@dataclass(frozen=True, slots=True)
class AppContainer:
    user_context: UserContext

    get_resident_records_for_user_use_case: GetAllResidentRecordsForUserUseCase
    resident_main_page_presenter: ResidentMainPagePresenter

    get_user_sensing_account_use_case: GetUserSensingAccountUseCase
    # get_patient_overview_use_case: GetPatientOverviewUseCase
    # patient_overview_presenter: PatientOverviewPresenter


def build_application_container(
        infrastructure: InfrastructureContainer,
        user_context: UserContext,
) -> AppContainer:
    # --- ASSIGN USE CASES

    resident_repos = infrastructure.resident_repository
    get_resident_records_for_user = GetAllResidentRecordsForUserUseCase(
        user_resident_access_repository=resident_repos.user_resident_access_repository,
        resident_profile_repository=resident_repos.resident_profile_repository,
        resident_contacts_repository=resident_repos.resident_contact_info_repository,
    )

    sensing_repos = infrastructure.sensing_repositories
    get_user_sensing_account = GetUserSensingAccountUseCase(
        user_sensing_repository=sensing_repos.user_sensing_repository,
        gateway_repository=sensing_repos.gateway_repository,
        sensor_repository=sensing_repos.sensor_repository,
    )

    # --- ASSIGN PRESENTERS

    return AppContainer(
        user_context=user_context,

        get_resident_records_for_user_use_case=get_resident_records_for_user,
        resident_main_page_presenter=ResidentMainPagePresenter(),

        get_user_sensing_account_use_case=get_user_sensing_account
    )


"""
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
"""
