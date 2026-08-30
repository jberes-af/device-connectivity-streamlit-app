# /src/infrastructure/persistence/google_sheets/repos/access/user_resource_assignment.py

from src.application.ports.access_repo_ports import (
    UserResourceAssignmentRepositoryPort,
)

from src.domain.entities.access.resource_access_entities import (
    UserResourceAssignment,
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

from src.infrastructure.persistence.google_sheets.mappers.access.user_resource_assignment_row_mapper import (
    UserResourceAssignmentRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.access.user_resource_assignment_columns import (
    UserResourceAssignmentColumns,
)


class GoogleSheetsUserResourceAssignmentRepository(
    GoogleSheetsRepository,
    UserResourceAssignmentRepositoryPort,
):
    TABLE_NAME = "user_resource_assignment"

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: UserResourceAssignmentRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )
        self._mapper = mapper

    def list_for_user_and_tenant(
            self,
            *,
            user_id: str,
            tenant_id: str,
    ) -> tuple[UserResourceAssignment, ...]:
        raw_rows = self._find_rows_by_fields(
            rows=self._read_rows(),
            filters={
                UserResourceAssignmentColumns.USER_ID:
                    user_id,

                UserResourceAssignmentColumns.TENANT_ID:
                    tenant_id,
            },
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )
