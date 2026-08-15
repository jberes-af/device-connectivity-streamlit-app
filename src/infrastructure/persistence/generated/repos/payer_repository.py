# /src/infrastructure/persistence/google_sheets/repos/Payer.py


# AUTO GENERATED

from src.application.ports.payer_repository_port import (
    PayerRepositoryPort,
)

from src.domain.entities.billing.payer_entities import (
    Payer,
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

from src.infrastructure.persistence.google_sheets.mappers.payer.payer_row_mapper import (
    PayerRowMapper,
)


from src.infrastructure.persistence.google_sheets.schemas.payer.payer_columns import (
    PayerColumns,
)


class GoogleSheetsPayerRepository(
    GoogleSheetsRepository,
    PayerRepositoryPort,
):

    TABLE_NAME = "payer"
    ID_COLUMN = PayerColumns.ENTITY_ID


    def __init__(
        self,
        *,
        query_service: GoogleSheetsQueryService,
        catalog: GoogleSheetCatalog,
        mapper: PayerRowMapper,
    ) -> None:

        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_payers(self) -> tuple[Payer, ...]:

        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> Payer:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)

    def append_open_event(
            self,
            event: Payer,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=PayerColumns.ORDER,
        )
