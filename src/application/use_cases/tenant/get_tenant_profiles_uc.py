# /src/application/use_cases/tenant/get_tenant_profiles_uc.py

import logging

from src.domain.entities.tenant.tenant_entities import TenantProfile

from src.application.services.tenant.get_tenant_service import (
    FetchTenantAdminService,
)

from src.application.use_cases.tenant.tenant_profiles_uc_dtos import (
    TenantProfileDTO,
    GetTenantProfilesResultDTO,
)

logger = logging.getLogger(__name__)


class GetTenantProfilesUseCase:

    def __init__(
            self,
            *,
            fetch_tenant_service: FetchTenantAdminService,
    ):
        self._fetch_tenant_service = fetch_tenant_service

    def execute(
            self,
            # request: GetDevicesAdministrationRequestDTO,
    ) -> GetTenantProfilesResultDTO:
        tenant_profiles: tuple[TenantProfile, ...] = (
            self._fetch_tenant_service.fetch_all_tenant_profiles()
        )

        dtos: tuple[TenantProfileDTO, ...] = (
            self._build_tenant_profiles(tenant_profiles)
        )

        return GetTenantProfilesResultDTO(
            tenant_profiles=dtos,
        )

    @staticmethod
    def _build_tenant_profiles(
            tenant_profiles: tuple[TenantProfile, ...]
    ) -> tuple[TenantProfileDTO, ...]:
        return tuple([
            TenantProfileDTO(
                tenant_id=profile.tenant_id,
                tenant_name=profile.tenant_name,
                tenant_type=profile.tenant_type,
                tenant_street=profile.tenant_street,
                tenant_city=profile.tenant_city,
                tenant_state=profile.tenant_state,
                tenant_postal_code=profile.tenant_postal_code,
                tenant_telephone=profile.tenant_telephone,
                tenant_manager=profile.tenant_manager,
                timezone=profile.timezone,
            )
            for profile in tenant_profiles
        ])
