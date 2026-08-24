# /src/main/compose_root_application.py

from dataclasses import dataclass

# --- APPLICATION CONTEXT

from src.application.context import (
    UserContext,
    # SessionContext,
)

# --- APPLICATION SERVICES

from src.application.services.get_payer_profile_service import (
    FetchPayerProfileService,
)

from src.application.services.person.get_provider_profile_service import (
    FetchProviderProfileService,
)

from src.application.services.care.get_diagnosis_definition_service import (
    FetchDiagnosisDefinitionService
)

from src.application.services.person.get_patient_diagnosis_service import (
    FetchPatientDiagnosisService
)

from src.application.services.care.get_rtm_service import (
    FetchRtmNecessityService,
)

from src.application.services.care.get_treatment_service import (
    FetchTreatmentPlanService,
    FetchTherapeuticGoalService, FetchTreatmentMonitoringParameterService, FetchTreatmentInterventionService,
    FetchTreatmentPlanReviewService,
)

# --- APPLICATION USE CASES

from src.application.use_cases.access.get_access_scope_uc import (
    GetUserAccessScopeUseCase,
)

from src.application.use_cases.resident.get_all_resident_records_for_user_uc import (
    GetAllResidentRecordsForUserUseCase,
)

from src.application.use_cases.patient.get_patient_payer_profile_uc import (
    GetPatientPayerProfileUseCase,
)

from src.application.use_cases.patient.get_patient_provider_profile_uc import (
    GetPatientProviderProfileUseCase,
)

from src.application.use_cases.patient.get_patient_diagnosis_and_treatment_uc import (
    GetPatientDiagnosesAndTreatmentsUseCase,
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

from src.interface_adapters.presenters.person.resident.resident_main_page_presenter import (
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

    get_patient_diagnosis_and_treatment_use_case: GetPatientDiagnosesAndTreatmentsUseCase
    # presenter

    get_patient_payer_profile_use_case: GetPatientPayerProfileUseCase
    # presenter

    get_patient_provider_profile_use_case: GetPatientProviderProfileUseCase
    # presenter

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
    diagnosis_repos = infrastructure.diagnosis_repository
    patient_repos = infrastructure.patient_repository
    payer_repos = infrastructure.payer_repository
    provider_repos = infrastructure.provider_repository
    resident_repos = infrastructure.resident_repository
    rtm_repos = infrastructure.rtm_repository
    sensing_repos = infrastructure.sensing_repositories
    tenant_repos = infrastructure.tenant_repository
    treatment_repos = infrastructure.treatment_repository

    # --- SERVICES

    fetch_payer_profile_service = FetchPayerProfileService(
        payer_repository=payer_repos.payer_repository,
    )

    fetch_provider_profile_service = FetchProviderProfileService(
        provider_repository=provider_repos.provider_repository,
    )

    fetch_diagnosis_definition_service = FetchDiagnosisDefinitionService(
        diagnosis_definition_repository=diagnosis_repos.diagnosis_definition_repository,
    )

    fetch_patient_diagnosis_service = FetchPatientDiagnosisService(
        patient_diagnosis_repository=patient_repos.patient_diagnosis_repository,
    )

    fetch_treatment_plan_service = FetchTreatmentPlanService(
        treatment_plan_repository=treatment_repos.treatment_plan_repository,
    )

    fetch_therapeutic_goal_service = FetchTherapeuticGoalService(
        therapeutic_goal_repository=treatment_repos.therapeutic_goal_repository,
    )

    fetch_rtm_necessity_service = FetchRtmNecessityService(
        rtm_necessity_repository=rtm_repos.rtm_necessity_repository,
    )

    fetch_treatment_intervention_service = FetchTreatmentInterventionService(
        treatment_intervention_repository=treatment_repos.treatment_intervention_repository,
    )

    fetch_treatment_monitoring_parameter_service = FetchTreatmentMonitoringParameterService(
        treatment_monitoring_parameter_repository=treatment_repos.treatment_monitoring_parameter_repository,
    )

    fetch_treatment_plan_review_service = FetchTreatmentPlanReviewService(
        treatment_plan_review_repository=treatment_repos.treatment_plan_review_repository,
    )

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

    # --- RESIDENT / PATIENT DIAGNOSES & TREATMENT RECORDS

    get_diagnosis_and_treatment = GetPatientDiagnosesAndTreatmentsUseCase(
        fetch_diagnosis_definition_service=fetch_diagnosis_definition_service,
        fetch_patient_diagnosis_service=fetch_patient_diagnosis_service,
        fetch_treatment_plan_service=fetch_treatment_plan_service,
        fetch_therapeutic_goal_service=fetch_therapeutic_goal_service,
        fetch_rtm_necessity_service=fetch_rtm_necessity_service,
        fetch_treatment_intervention_service=fetch_treatment_intervention_service,
        fetch_treatment_monitoring_parameter_service=fetch_treatment_monitoring_parameter_service,
        fetch_treatment_plan_review_service=fetch_treatment_plan_review_service,
    )

    # --- RESIDENT / PATIENT PAYER RECORDS

    get_patient_payer_profile = GetPatientPayerProfileUseCase(
        fetch_payer_profile_service=fetch_payer_profile_service,
        patient_payer_repository=patient_repos.patient_payer_repository,
    )

    # --- RESIDENT / PATIENT PROVIDER RECORDS

    get_patient_provider_profile = GetPatientProviderProfileUseCase(
        fetch_provider_profile_service=fetch_provider_profile_service,
        patient_provider_repository=patient_repos.patient_provider_repository,
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

        get_patient_diagnosis_and_treatment_use_case=get_diagnosis_and_treatment,

        get_patient_payer_profile_use_case=get_patient_payer_profile,
        get_patient_provider_profile_use_case=get_patient_provider_profile,

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
