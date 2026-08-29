# /src/main/compose_root_application.py

from dataclasses import dataclass

# --- APPLICATION CONTEXT

from src.application.context import (
    UserContext,
    # SessionContext,
)

# --- APPLICATION SERVICES

from src.application.services.payer.get_payer_profile_service import (
    FetchPayerProfileService,
)

from src.application.services.payer.get_patient_payer_service import (
    FetchPatientPayerProfileService
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
    FetchRtmEnrollmentService,
)

from src.application.services.care.get_treatment_service import (
    FetchTreatmentPlanService,
    FetchTherapeuticGoalService,
    FetchTreatmentMonitoringParameterService,
    FetchTreatmentInterventionService,
    FetchTreatmentPlanReviewService,
)

# --- APPLICATION USE CASES

from src.application.use_cases.access.get_access_scope_uc import (
    GetUserAccessScopeUseCase,
)
from src.application.use_cases.dashboard.build_main_dashboard_use_case import (
    BuildMainDashboardUseCase
)

from src.application.use_cases.residents.main.get_all_resident_records_for_user_uc import (
    GetAllResidentRecordsForUserUseCase,
)

from src.application.use_cases.residents.payer.get_patient_payer_profile_uc import (
    GetPatientPayerProfileUseCase,
)

from src.application.use_cases.residents.payer.get_payer_and_rtm_enrollment_uc import (
    GetPatientPayerAndRtmEnrollmentUseCase,
)

from src.application.use_cases.residents.provider.get_patient_provider_profile_uc import (
    GetPatientProviderProfileUseCase,
)

from src.application.use_cases.residents.treatment.get_patient_diagnosis_and_treatment_uc import (
    GetPatientDiagnosesAndTreatmentsUseCase,
)

from src.application.use_cases.residents.rtm.get_rtm_enrollment_uc import (
    GetRtmEnrollmentUseCase
)

from src.application.use_cases.sensing.sensing_admin.get_devices_overview_uc import (
    GetDevicesOverviewUseCase,
)

from src.application.use_cases.residents.sensing.get_resident_sensing_profile_uc import (
    GetResidentSensingProfileUseCase,
)

from src.application.use_cases.sensing.trends.build_sensor_events_use_case import (
    BuildSensorEventsUseCase,
)

# from src.application.use_cases.treatment.get_patient_overview_uc import (GetPatientOverviewUseCase, )

# --- INFRASTRUCTURE ADAPTERS

from src.main.compose_root_infrastructure import InfrastructureContainer

# --- INTERFACE ADAPTERS

from src.interface_adapters.presenters.dashboard.dashboard_main_presenter import (
    DashboardMainPagePresenter
)

from src.interface_adapters.presenters.residents.main_page.residents_page_presenter import (
    ResidentMainPagePresenter,
)

from src.interface_adapters.presenters.residents.treatment.treatment_section_tabs_presenter import (
    TreatmentSectionPresenter,
)


# --- SERVICE ADAPTERS

# from src.main.compo_root_m365 import build_m365_graph_mail_service


@dataclass(frozen=True, slots=True)
class AppContainer:
    # --- ACCESS

    user_context: UserContext

    get_user_access_scope_use_case: GetUserAccessScopeUseCase

    # --- DASHBOARD

    build_main_dashboard_use_case: BuildMainDashboardUseCase
    main_dashboard_presenter: DashboardMainPagePresenter

    # --- RESIDENT

    get_resident_records_for_user_use_case: GetAllResidentRecordsForUserUseCase
    resident_main_page_presenter: ResidentMainPagePresenter

    get_patient_diagnosis_and_treatment_use_case: GetPatientDiagnosesAndTreatmentsUseCase
    treatment_section_presenter: TreatmentSectionPresenter

    get_payers_and_rtm_enrollment_use_case: GetPatientPayerAndRtmEnrollmentUseCase
    # presenter

    get_patient_provider_profile_use_case: GetPatientProviderProfileUseCase
    # presenter

    get_user_sensing_account_use_case: GetResidentSensingProfileUseCase
    build_sensor_event_timeline_use_case: BuildSensorEventsUseCase

    # get_patient_overview_use_case: GetPatientOverviewUseCase
    # patient_overview_presenter: PatientOverviewPresenter

    # --- DEVICE / SENSING ADMIN

    # get_device_admin_use_case: GetDevicesOverviewUseCase
    # sensing_page_presenter: SensingPagePresenter


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

    fetch_diagnosis_definition_service = FetchDiagnosisDefinitionService(
        diagnosis_definition_repository=diagnosis_repos.diagnosis_definition_repository,
    )

    fetch_patient_diagnosis_service = FetchPatientDiagnosisService(
        patient_diagnosis_repository=patient_repos.patient_diagnosis_repository,
    )

    fetch_patient_payer_service = FetchPatientPayerProfileService(
        patient_payer_repository=patient_repos.patient_payer_repository,
    )

    fetch_payer_profile_service = FetchPayerProfileService(
        payer_repository=payer_repos.payer_repository,
    )

    fetch_provider_profile_service = FetchProviderProfileService(
        provider_repository=provider_repos.provider_repository,
    )

    fetch_rtm_enrollment_service = FetchRtmEnrollmentService(
        rtm_enrollment_repository=rtm_repos.rtm_enrollment_repository,
    )

    fetch_rtm_necessity_service = FetchRtmNecessityService(
        rtm_necessity_repository=rtm_repos.rtm_necessity_repository,
    )

    fetch_therapeutic_goal_service = FetchTherapeuticGoalService(
        therapeutic_goal_repository=treatment_repos.therapeutic_goal_repository,
    )

    fetch_treatment_plan_service = FetchTreatmentPlanService(
        treatment_plan_repository=treatment_repos.treatment_plan_repository,
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

    # MAIN DASHBOARD

    build_main_dashboard = BuildMainDashboardUseCase()  # DEMO!!
    main_dashboard_presenter = DashboardMainPagePresenter()

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

    # --- RESIDENT / PATIENT PAYER & RTM ENROLLMENT RECORDS

    get_patient_payer_profile = GetPatientPayerProfileUseCase(
        fetch_patient_payer_service=fetch_patient_payer_service,
        fetch_payer_profile_service=fetch_payer_profile_service,
    )

    get_rtm_enrollment = GetRtmEnrollmentUseCase(
        fetch_rtm_enrollment_service=fetch_rtm_enrollment_service,
    )

    get_patient_payer_and_rtm_enrollment = GetPatientPayerAndRtmEnrollmentUseCase(
        get_patient_payer_profile_use_case=get_patient_payer_profile,
        get_rtm_enrollment_use_case=get_rtm_enrollment,
    )

    # --- RESIDENT / PATIENT PROVIDER RECORDS

    get_patient_provider_profile = GetPatientProviderProfileUseCase(
        fetch_provider_profile_service=fetch_provider_profile_service,
        patient_provider_repository=patient_repos.patient_provider_repository,
    )

    # --- RESIDENT SENSING RECORDS

    get_user_sensing_account = GetResidentSensingProfileUseCase(
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

        build_main_dashboard_use_case=build_main_dashboard,
        main_dashboard_presenter=main_dashboard_presenter,

        get_resident_records_for_user_use_case=get_resident_records_for_user,
        resident_main_page_presenter=ResidentMainPagePresenter(),

        get_patient_diagnosis_and_treatment_use_case=get_diagnosis_and_treatment,
        treatment_section_presenter=TreatmentSectionPresenter(),

        get_payers_and_rtm_enrollment_use_case=get_patient_payer_and_rtm_enrollment,
        get_patient_provider_profile_use_case=get_patient_provider_profile,

        get_user_sensing_account_use_case=get_user_sensing_account,
        build_sensor_event_timeline_use_case=build_sensor_events,

    )
