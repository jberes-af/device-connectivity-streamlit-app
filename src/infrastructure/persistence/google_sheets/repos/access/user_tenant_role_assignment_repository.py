# /src/infrastructure/persistence/google_sheets/repos/access/user_tenant_role_assignment_repository.py

from src.application.ports.access_repo_ports import (
    UserTenantRoleAssignmentRepositoryPort,
)

from src.domain.entities.access.membership_entities import (
    UserTenantRoleAssignment,
)

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.base_repository import (
    GoogleSheetsRepository,
)

from src.infrastructure.persistence.google_sheets.google_sheet_catalog import (
    GoogleSheetCatalog,
)

from src.infrastructure.persistence.google_sheets.sheets_query_service import (
    GoogleSheetsQueryService,
)

from src.infrastructure.persistence.google_sheets.mappers.access.user_tenant_role_assignment_row_mapper import (
    UserTenantRoleAssignmentRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.access.user_tenant_role_assignment_columns import (
    UserTenantRoleAssignmentColumns,
)


class GoogleSheetsUserTenantRoleAssignmentRepository(
    GoogleSheetsRepository,
    UserTenantRoleAssignmentRepositoryPort,
):
    TABLE_NAME = "user_tenant_role_assignment"
    ID_COLUMN = UserTenantRoleAssignmentColumns.ROLE_ASSIGNMENT_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: UserTenantRoleAssignmentRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_for_membership_id(
            self,
            *,
            membership_id: str,
    ) -> tuple[UserTenantRoleAssignment, ...]:
        raw_rows: list[RawRow] = self._find_rows(
            rows=self._read_rows(),
            column_name="patient_id",
            value=membership_id,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )

    def list_user_tenant_role_assignments(self) -> tuple[UserTenantRoleAssignment, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def get_by_id(
            self,
            role_assignment_id: str,
    ) -> UserTenantRoleAssignment:
        raw_row: RawRow = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=role_assignment_id,
        )

        return self._mapper.to_domain(raw_row)
