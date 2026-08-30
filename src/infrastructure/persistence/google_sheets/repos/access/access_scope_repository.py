# /src/infrastructure/persistence/google_sheets/repos/AccessScope.py


# AUTO GENERATED

from src.application.ports.access_scope_repository_port import (
    AccessScopeRepositoryPort,
)

from src.domain.entities.access_scope_entities import (
    AccessScope,
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

from src.infrastructure.persistence.mappers.access_scope.access_scope_row_mapper import (
    AccessScopeRowMapper,
)


from src.infrastructure.persistence.schemas.access_scope.access_scope_columns import (
    AccessScopeColumns,
)


class GoogleSheetsAccessScopeRepository(
    GoogleSheetsRepository,
    AccessScopeRepositoryPort,
):

    TABLE_NAME = "access_scope"
    ID_COLUMN = AccessScopeColumns.ENTITY_ID


    def __init__(
        self,
        *,
        query_service: GoogleSheetsQueryService,
        catalog: GoogleSheetCatalog,
        mapper: AccessScopeRowMapper,
    ) -> None:

        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_access_scopes(self) -> tuple[AccessScope, ...]:

        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> AccessScope:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)

    def append_open_event(
            self,
            event: AccessScope,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=AccessScopeColumns.ORDER,
        )
