# /src/main/compose_root_application.py

from dataclasses import dataclass

# --- APPLICATION CONTEXT

from src.application.context import (
    UserContext,
    # SessionContext,
)

# --- APPLICATION USE CASES

from src.application.use_cases.access.get_access_scope_uc import (
    GetUserAccessScopeUseCase,
)

from src.application.use_cases.resident.get_all_resident_records_for_user_uc import (
    GetAllResidentRecordsForUserUseCase,
)

from src.application.use_cases.sensing.device_profiles.get_user_sensing_account_uc import (
    GetUserSensingAccountUseCase,
)

from src.application.use_cases.sensing.trends.build_sensor_events_use_case import (
    BuildSensorEventsUseCase,
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

    get_user_access_scope_use_case: GetUserAccessScopeUseCase

    get_resident_records_for_user_use_case: GetAllResidentRecordsForUserUseCase
    resident_main_page_presenter: ResidentMainPagePresenter

    get_user_sensing_account_use_case: GetUserSensingAccountUseCase
    build_sensor_event_timeline_use_case: BuildSensorEventsUseCase

    # get_patient_overview_use_case: GetPatientOverviewUseCase
    # patient_overview_presenter: PatientOverviewPresenter


def build_application_container(
        infrastructure: InfrastructureContainer,
        user_context: UserContext,
) -> AppContainer:
    # --- ASSIGN REPOSITORIES

    access_repos = infrastructure.access_repository
    resident_repos = infrastructure.resident_repository
    tenant_repos = infrastructure.tenant_repository

    sensing_repos = infrastructure.sensing_repositories

    # --- ACCESS RECORDS

    get_access_scope = GetUserAccessScopeUseCase(
        user_tenant_membership_repository=access_repos.user_tenant_membership_repository,
        user_resident_repository=access_repos.user_resident_access_repository,
        resident_gateway_repository=access_repos.resident_gateway_link_repository,
        resident_sensor_repository=access_repos.resident_sensor_link_repository,
        user_sensing_repository=sensing_repos.user_sensing_repository,
        tenant_profile_repository=tenant_repos.tenant_profile_repository
    )

    # --- RESIDENT RECORDS

    get_resident_records_for_user = GetAllResidentRecordsForUserUseCase(
        user_resident_access_repository=access_repos.user_resident_access_repository,  # IS THIS NEEDED?????
        resident_profile_repository=resident_repos.resident_profile_repository,
        resident_contacts_repository=resident_repos.resident_contact_info_repository,
    )

    # --- RESIDENT SENSING RECORDS

    get_user_sensing_account = GetUserSensingAccountUseCase(
        user_sensing_repository=sensing_repos.user_sensing_repository,
        gateway_repository=sensing_repos.gateway_repository,
        sensor_repository=sensing_repos.sensor_device_repository,
    )

    # --- SENSOR EVENTS

    build_sensor_events = BuildSensorEventsUseCase(
        sensor_event_repository=sensing_repos.sensor_event_repository,
    )

    # --- ASSIGN PRESENTERS

    return AppContainer(
        user_context=user_context,

        get_user_access_scope_use_case=get_access_scope,

        get_resident_records_for_user_use_case=get_resident_records_for_user,
        resident_main_page_presenter=ResidentMainPagePresenter(),

        get_user_sensing_account_use_case=get_user_sensing_account,
        build_sensor_event_timeline_use_case=build_sensor_events,
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
