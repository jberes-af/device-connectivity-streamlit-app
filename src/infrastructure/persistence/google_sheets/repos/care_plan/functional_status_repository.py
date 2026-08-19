# /src/infrastructure/persistence/google_sheets/repos/FunctionalStatus.py


# AUTO GENERATED

from src.application.ports.functional_status_repository_port import (
    FunctionalStatusRepositoryPort,
)

from src.domain.entities.functional_status_entities import (
    FunctionalStatus,
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

from src.infrastructure.persistence.google_sheets.mappers import (
    FunctionalStatusRowMapper,
)


from src.infrastructure.persistence.google_sheets.schemas import (
    FunctionalStatusColumns,
)


class GoogleSheetsFunctionalStatusRepository(
    GoogleSheetsRepository,
    FunctionalStatusRepositoryPort,
):

    TABLE_NAME = "functional_status"
    ID_COLUMN = FunctionalStatusColumns.ENTITY_ID


    def __init__(
        self,
        *,
        query_service: GoogleSheetsQueryService,
        catalog: GoogleSheetCatalog,
        mapper: FunctionalStatusRowMapper,
    ) -> None:

        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_functional_statuses(self) -> tuple[FunctionalStatus, ...]:

        return tuple(
            self._mapper.from_raw(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> FunctionalStatus:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.from_raw(raw_row)

    def append_open_event(
            self,
            event: FunctionalStatus,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=FunctionalStatusColumns.ORDER,
        )
