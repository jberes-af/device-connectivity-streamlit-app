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

from src.infrastructure.persistence.google_sheets.schemas.access.role_permission_columns import (
    RolePermissionColumns,
)


class GoogleSheetsRolePermissionRepository(
    GoogleSheetsRepository,
    RolePermissionRepositoryPort,
):
    TABLE_NAME = "role_permission"
    ID_COLUMN = RolePermissionColumns.ROLE

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
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    """
    def get_by_id(
            self,
            patient_id: str,
    ) -> RolePermission:
        raw_row: RawRow = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)
    """
