# /src/main/compose_root_application.py

from dataclasses import dataclass

# --- APPLICATION CONTEXT

from src.application.context import (
    UserContext,
    # SessionContext,
)

# --- APPLICATION SERVICES

from src.main.application_service_containers.fetch_repos_services import (
    FetchRepositoryService,
)

# --- APPLICATION USE CASES

from src.application.use_cases.access.build_access_scope_use_case import (
    BuildAccessScopeUseCase,
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

from src.application.use_cases.sensing.sensing_admin.get_device_admin_uc import (
    GetDeviceAdministrationUseCase,
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

from src.interface_adapters.presenters.sensing.device_admin.device_admin_presenter import (
    DeviceAdministrationPresenter,
)


# --- SERVICE ADAPTERS

# from src.main.compo_root_m365 import build_m365_graph_mail_service


@dataclass(frozen=True, slots=True)
class AppContainer:
    # --- ACCESS

    user_context: UserContext

    get_user_access_scope_use_case: BuildAccessScopeUseCase

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

    # --- DEVICE / SENSING ADMIN

    get_device_admin_use_case: GetDeviceAdministrationUseCase
    device_admin_page_presenter: DeviceAdministrationPresenter


def build_application_container(
        infrastructure: InfrastructureContainer,
        user_context: UserContext,
) -> AppContainer:
    # --- ASSIGN REPOSITORIES
    _repo = FetchRepositoryService(
        infrastructure=infrastructure,
    )
    patient_repos = infrastructure.patient_repository
    sensing_repos = infrastructure.sensing_repositories

    # --- ACCESS RECORDS

    get_access_scope = BuildAccessScopeUseCase(
        fetch_user_tenant_membership_service=_repo.fetch_user_tenant_membership_service(),
        fetch_user_tenant_role_assignment_service=_repo.fetch_user_tenant_role_assignment_service(),
        fetch_role_permission_service=_repo.fetch_role_permission_service(),
        fetch_user_resource_assignment_service=_repo.fetch_user_resource_assignment_service(),
        fetch_role_resource_scope_service=_repo.fetch_role_resource_scope_service(),
    )

    # MAIN DASHBOARD

    build_main_dashboard = BuildMainDashboardUseCase()  # DEMO!!
    main_dashboard_presenter = DashboardMainPagePresenter()

    # --- RESIDENT RECORDS

    get_resident_records_for_user = GetAllResidentRecordsForUserUseCase(
        # user_resident_access_repository=.user_resident_access_repository,  # IS THIS NEEDED?????
        fetch_resident_profile_repository=_repo.fetch_resident_profile_service(),
        fetch_resident_contacts_repository=_repo.fetch_resident_contacts_service(),
    )

    # --- RESIDENT / PATIENT DIAGNOSES & TREATMENT RECORDS

    get_diagnosis_and_treatment = GetPatientDiagnosesAndTreatmentsUseCase(
        fetch_diagnosis_definition_service=_repo.fetch_diagnosis_definition_service(),
        fetch_patient_diagnosis_service=_repo.fetch_patient_diagnosis_service(),
        fetch_treatment_plan_service=_repo.fetch_treatment_plan_service(),
        fetch_therapeutic_goal_service=_repo.fetch_therapeutic_goal_service(),
        fetch_rtm_necessity_service=_repo.fetch_rtm_necessity_service(),
        fetch_treatment_intervention_service=_repo.fetch_treatment_intervention_service(),
        fetch_treatment_monitoring_parameter_service=_repo.fetch_treatment_monitoring_parameter_service(),
        fetch_treatment_plan_review_service=_repo.fetch_treatment_plan_review_service(),
    )

    # --- RESIDENT / PATIENT PAYER & RTM ENROLLMENT RECORDS

    get_patient_payer_profile = GetPatientPayerProfileUseCase(
        fetch_patient_payer_service=_repo.fetch_patient_payer_service(),
        fetch_payer_profile_service=_repo.fetch_payer_profile_service(),
    )

    get_rtm_enrollment = GetRtmEnrollmentUseCase(
        fetch_rtm_enrollment_service=_repo.fetch_rtm_enrollment_service(),
    )

    get_patient_payer_and_rtm_enrollment = GetPatientPayerAndRtmEnrollmentUseCase(
        get_patient_payer_profile_use_case=get_patient_payer_profile,
        get_rtm_enrollment_use_case=get_rtm_enrollment,
    )

    # --- RESIDENT / PATIENT PROVIDER RECORDS

    get_patient_provider_profile = GetPatientProviderProfileUseCase(
        fetch_provider_profile_service=_repo.fetch_provider_profile_service(),
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

    get_device_administration = GetDeviceAdministrationUseCase(
        fetch_device_admin_service=_repo.fetch_device_admin_service(),
        gateway_repository=sensing_repos.gateway_repository,
        sensor_repository=sensing_repos.sensor_device_repository,
        user_sensing_repository=sensing_repos.user_sensing_repository,
    )

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

        get_device_admin_use_case=get_device_administration,
        device_admin_page_presenter=DeviceAdministrationPresenter(),
    )
