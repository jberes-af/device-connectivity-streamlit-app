# /src/infrastructure/persistence/google_sheets/repos/role_permission_repository.py

from typing import Sequence

from src.domain.enums.access.role_enums import UserRoleEnum

from src.domain.entities.access.authorization_entities import (
    RolePermission,
)

from src.application.ports.access_repo_ports import (
    RolePermissionRepositoryPort,
)

# from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.base_repository import (
    GoogleSheetsRepository,
)

from src.infrastructure.persistence.google_sheets.google_sheet_catalog import (
    GoogleSheetCatalog,
)

from src.infrastructure.persistence.google_sheets.sheets_query_service import (
    GoogleSheetsQueryService,
)

from src.infrastructure.persistence.google_sheets.mappers.access.role_permission_row_mapper import (
    RolePermissionRowMapper,
)


class GoogleSheetsRolePermissionRepository(
    GoogleSheetsRepository,
    RolePermissionRepositoryPort,
):
    TABLE_NAME = "role_permission"

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: RolePermissionRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )
        self._mapper = mapper

    def list_for_roles(
            self,
            *,
            roles: Sequence[UserRoleEnum],
    ) -> tuple[RolePermission, ...]:
        role_values = {role.value for role in roles}

        if not role_values:
            return ()

        rows = self._read_rows()

        matching_rows = (
            row
            for row in rows
            if str(row.get("role", "")).strip() in role_values
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in matching_rows
        )

    """
    def list_for_roles(
            self,
            *,
            roles: Sequence[UserRoleEnum],
    ) -> tuple[RolePermission, ...]:
        role_set = set(roles)

        if not role_set:
            return ()

        records = (
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

        print()
        print("records")
        print(records)
        print()

        return tuple(
            record
            for record in records
            if record.role in role_set
        )
    """
