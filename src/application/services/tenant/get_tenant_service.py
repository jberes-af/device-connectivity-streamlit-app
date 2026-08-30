# /src/application/services/sensing/get_tenant_service.py


from src.domain.entities.tenant.tenant_entities import (
    TenantProfile,
)

from src.application.ports.tenant_repo_ports import (
    TenantProfileRepositoryPort,
)


class FetchTenantAdminService:

    def __init__(
            self,
            *,
            tenant_repository: TenantProfileRepositoryPort,
    ) -> None:
        self._tenant_repo = tenant_repository

    def fetch_all_tenant_profiles(
            self) -> tuple[TenantProfile, ...]:
        return self._tenant_repo.list_tenant_profiles()

    def get_by_id(
            self,
            tenant_id: str,
    ) -> TenantProfile:
        return self._tenant_repo.get_by_id(
            tenant_id=tenant_id
        )

    def get_by_ids(
            self,
            tenant_ids: tuple[str, ...],
    ) -> tuple[TenantProfile, ...]:
        return self._tenant_repo.get_by_ids(
            tenant_ids=tenant_ids
        )
