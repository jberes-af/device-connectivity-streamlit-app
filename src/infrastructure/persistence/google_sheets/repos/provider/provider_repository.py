# /src/infrastructure/persistence/google_sheets/repos/provider/provider_repository.py

from src.application.ports.provider_repo_ports import ProviderRepositoryPort

from src.domain.entities.care.provider_entities import Provider

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

from src.infrastructure.persistence.google_sheets.mappers.provider.provider_row_mapper import (
    ProviderRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.provider.provider_columns import (
    ProviderColumns,
)


class GoogleSheetsProviderRepository(
    GoogleSheetsRepository,
    ProviderRepositoryPort,
):
    TABLE_NAME = "provider"
    ID_COLUMN = ProviderColumns.PROVIDER_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: ProviderRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_providers(self) -> tuple[Provider, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def get_by_id(
            self,
            patient_id: str,
    ) -> Provider:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)

    def append_open_event(
            self,
            event: Provider,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=ProviderColumns.ORDER,
        )
