# /src/main/application_service_containers/fetch_repos_service.py

# --- ACCESS

from src.application.services.access.get_user_tenant_services import (
    FetchUserTenantMembershipService,
    FetchUserTenantRoleAssignmentService,
)

from src.application.services.access.get_roles_service import (
    FetchRolePermissionService,
    FetchRoleResourceScopeService,
)

from src.application.services.access.get_user_resource_service import (
    FetchUserResourceAssignmentService
)

# --- DEVICE

from src.application.services.sensing.get_device_admin_service import (
    FetchDeviceAdminService
)

# --- TENANT

from src.application.services.tenant.get_tenant_service import (
    FetchTenantAdminService,
)

# --- PAYER

from src.application.services.payer.get_payer_profile_service import (
    FetchPayerProfileService,
)

from src.application.services.payer.get_patient_payer_service import (
    FetchPatientPayerProfileService
)

# --- PROVIDER

from src.application.services.provider.get_provider_profile_service import (
    FetchProviderProfileService,
)

# --- DIAGNOSIS

from src.application.services.care.get_diagnosis_definition_service import (
    FetchDiagnosisDefinitionService
)

# --- RESIDENT

from src.application.services.resident.get_patient_diagnosis_service import (
    FetchPatientDiagnosisService
)

from src.application.services.resident.get_resident_contacts_service import (
    FetchResidentContactsService
)

from src.application.services.resident.get_resident_profile_service import (
    FetchResidentProfileService,
)

# --- RTM

from src.application.services.care.get_rtm_service import (
    FetchRtmNecessityService,
    FetchRtmEnrollmentService,
)

# --- TREATMENT

from src.application.services.care.get_treatment_service import (
    FetchTreatmentPlanService,
    FetchTherapeuticGoalService,
    FetchTreatmentMonitoringParameterService,
    FetchTreatmentInterventionService,
    FetchTreatmentPlanReviewService,
)

# --- INFRASTRUCTURE ADAPTERS

from src.main.compose_root_infrastructure import InfrastructureContainer


# --- ASSIGN REPOSITORIES

class FetchRepositoryService:
    def __init__(
            self,
            infrastructure: InfrastructureContainer,
    ):
        self._infrastructure = infrastructure
        self._access_repos = infrastructure.access_repository
        self._diagnosis_repos = infrastructure.diagnosis_repository
        self._device_repos = infrastructure.device_admin_repository
        self._patient_repos = infrastructure.patient_repository
        self._payer_repos = infrastructure.payer_repository
        self._provider_repos = infrastructure.provider_repository
        self._resident_repos = infrastructure.resident_repository
        self._rtm_repos = infrastructure.rtm_repository
        self._sensing_repos = infrastructure.sensing_repositories
        self._tenant_repos = infrastructure.tenant_repository
        self._treatment_repos = infrastructure.treatment_repository

    def fetch_user_tenant_membership_service(self):
        return FetchUserTenantMembershipService(
            user_tenant_membership_repository=(
                self._access_repos.user_tenant_membership_repository
            ))

    def fetch_user_tenant_role_assignment_service(self):
        return FetchUserTenantRoleAssignmentService(
            user_tenant_role_assignment_repository=(
                self._access_repos.user_tenant_role_assignment_repository
            ))

    def fetch_role_permission_service(self):
        return FetchRolePermissionService(
            role_permission_repository=(
                self._access_repos.role_permission_repository
            ))

    def fetch_role_resource_scope_service(self):
        return FetchRoleResourceScopeService(
            role_resource_scope_repository=(
                self._access_repos.role_resource_scope_repository
            )
        )

    def fetch_user_resource_assignment_service(self):
        return FetchUserResourceAssignmentService(
            user_resource_assignment_repository=(
                self._access_repos.user_resource_assignment_repository
            ))

    def fetch_device_admin_service(self):
        return FetchDeviceAdminService(
            device_admin_repository=self._device_repos.device_admin_profile_repository
        )

    def fetch_diagnosis_definition_service(self):
        return FetchDiagnosisDefinitionService(
            diagnosis_definition_repository=self._diagnosis_repos.diagnosis_definition_repository,
        )

    def fetch_patient_diagnosis_service(self):
        return FetchPatientDiagnosisService(
            patient_diagnosis_repository=self._patient_repos.patient_diagnosis_repository,
        )

    def fetch_patient_payer_service(self):
        return FetchPatientPayerProfileService(
            patient_payer_repository=self._patient_repos.patient_payer_repository,
        )

    def fetch_payer_profile_service(self):
        return FetchPayerProfileService(
            payer_repository=self._payer_repos.payer_repository,
        )

    def fetch_provider_profile_service(self):
        return FetchProviderProfileService(
            provider_repository=self._provider_repos.provider_repository,
        )

    def fetch_resident_contacts_service(self):
        return FetchResidentContactsService(
            resident_contacts_repository=self._resident_repos.resident_contact_info_repository,
        )

    def fetch_resident_profile_service(self):
        return FetchResidentProfileService(
            resident_profile_repository=self._resident_repos.resident_profile_repository,
        )

    def fetch_rtm_enrollment_service(self):
        return FetchRtmEnrollmentService(
            rtm_enrollment_repository=self._rtm_repos.rtm_enrollment_repository,
        )

    def fetch_rtm_necessity_service(self):
        return FetchRtmNecessityService(
            rtm_necessity_repository=self._rtm_repos.rtm_necessity_repository,
        )

    def fetch_tenant_admin_service(self):
        return FetchTenantAdminService(
            tenant_repository=self._tenant_repos.tenant_profile_repository,
        )

    def fetch_therapeutic_goal_service(self):
        return FetchTherapeuticGoalService(
            therapeutic_goal_repository=self._treatment_repos.therapeutic_goal_repository,
        )

    def fetch_treatment_plan_service(self):
        return FetchTreatmentPlanService(
            treatment_plan_repository=self._treatment_repos.treatment_plan_repository,
        )

    def fetch_treatment_intervention_service(self):
        return FetchTreatmentInterventionService(
            treatment_intervention_repository=self._treatment_repos.treatment_intervention_repository,
        )

    def fetch_treatment_monitoring_parameter_service(self):
        return FetchTreatmentMonitoringParameterService(
            treatment_monitoring_parameter_repository=self._treatment_repos.treatment_monitoring_parameter_repository,
        )

    def fetch_treatment_plan_review_service(self):
        return FetchTreatmentPlanReviewService(
            treatment_plan_review_repository=self._treatment_repos.treatment_plan_review_repository,
        )
