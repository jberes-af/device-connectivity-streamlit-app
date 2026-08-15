# /src/application/ports/tenant_repo_ports.py

from typing import Protocol

from src.domain.entities.person.tenant_entities import (
    TenantProfile,
)


class TenantProfileRepositoryPort(Protocol):

    def list_tenant_profiles(self) -> tuple[TenantProfile, ...]:
        ...

    def get_by_id(
            self,
            tenant_id: str,
    ) -> TenantProfile:
        ...
