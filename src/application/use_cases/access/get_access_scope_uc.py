# /src/application/use_cases/access/get_access_scope_uc.py

from src.domain.entities.access.access_entities import UserResidentAccess

from src.domain.enums.person.tenant_enums import TenantTypeEnum

from src.domain.entities.person.tenant_entities import TenantProfile

from src.application.models.sensing_models import UserSensingDomainObjects

from src.application.ports.tenant_repo_ports import TenantProfileRepositoryPort

from src.application.ports.access_repo_ports import (
    UserTenantMembershipRepositoryPort,
    UserResidentAccessRepositoryPort,
    ResidentGatewayLinkRepositoryPort,
    ResidentSensorLinkRepositoryPort,
)

from src.application.ports.sensing.user_sensing_port import (
    UserSensingRepositoryPort,
)

from src.application.use_cases.access.access_scope_uc_dtos import (
    AccessScopeRequestDTO,
    AccessScopeResultDTO,
)


class GetUserAccessScopeUseCase:

    def __init__(
            self,
            *,
            user_tenant_membership_repository: UserTenantMembershipRepositoryPort,
            user_resident_repository: UserResidentAccessRepositoryPort,
            resident_gateway_repository: ResidentGatewayLinkRepositoryPort,
            resident_sensor_repository: ResidentSensorLinkRepositoryPort,
            user_sensing_repository: UserSensingRepositoryPort,
            tenant_profile_repository: TenantProfileRepositoryPort,
    ):
        self._user_tenant_repo = user_tenant_membership_repository
        self._user_resident_repo = user_resident_repository
        self._resident_gateway_repo = resident_gateway_repository
        self._resident_sensor_repo = resident_sensor_repository
        self._user_sensing_repo = user_sensing_repository
        self._tenant_profile_repo = tenant_profile_repository

    def execute(
            self,
            request: AccessScopeRequestDTO,
    ) -> AccessScopeResultDTO:
        tenant_id: str = request.tenant_id
        user_id: str = request.user_id

        resident_ids: list[str] = self._fetch_resident_ids(user_id=user_id)

        gateway_ids: list[str]
        sensor_ids: list[str]
        sensor_ids, gateway_ids = self._fetch_device_ids(
            user_id=user_id,
            tenant_id=tenant_id)

        tenant_profile: TenantProfile = self._fetch_tenant_profile(
            tenant_id=tenant_id)

        return AccessScopeResultDTO(
            resident_ids=tuple(resident_ids),
            sensor_ids=tuple(sensor_ids),
            gateway_ids=tuple(gateway_ids),
            tenant_profile=tenant_profile,
        )

    def _fetch_tenant_profile(self, tenant_id: str) -> TenantProfile:
        data: TenantProfile = (
            self._tenant_profile_repo.get_by_id(tenant_id=tenant_id)
        )

        return TenantProfile(
            tenant_id=data.tenant_id,
            tenant_name=data.tenant_name,
            tenant_type=data.tenant_type,
            tenant_street=data.tenant_street,
            tenant_city=data.tenant_city,
            tenant_state=data.tenant_state,
            tenant_postal_code=data.tenant_postal_code,
            tenant_telephone=data.tenant_telephone,
            tenant_manager=data.tenant_manager,
            timezone=data.timezone,
        )

    def _fetch_resident_ids(self, user_id: str) -> list[str]:
        data: tuple[UserResidentAccess, ...] = (
            self._user_resident_repo.list_resident_access_records_for_user_id(
                user_id=user_id)
        )

        return [
            r.resident_id for r in data
        ]

    def _fetch_device_ids(
            self,
            user_id: str,
            tenant_id: str,
    ) -> tuple[list[str], list[str]]:
        sensing_objects: UserSensingDomainObjects = (
            self._user_sensing_repo.get_by_user_id(
                user_id=user_id,
                # tenant_id=tenant_id,
            ))

        user_sensor_ids: list[str] = [
            r.sensor_id for r in sensing_objects.user_sensor_links]

        user_gateway_ids: list[str] = [
            r.gateway_id for r in sensing_objects.user_gateway_links]

        return user_sensor_ids, user_gateway_ids
