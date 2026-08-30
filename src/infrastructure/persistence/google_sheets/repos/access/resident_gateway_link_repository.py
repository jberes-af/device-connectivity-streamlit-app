# /src/infrastructure/persistence/google_sheets/repos/contact/resident_gateway_link.py

from src.application.ports.sensing.device_ports import ResidentGatewayLinkRepositoryPort

from src.domain.entities.sensing.assignment_entities import ResidentGatewayLink

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

from src.infrastructure.persistence.google_sheets.mappers.access.resident_gateway_link_row_mapper import (
    ResidentGatewayLinkRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.access.resident_gateway_link_columns import (
    ResidentGatewayLinkColumns,
)


class GoogleSheetsResidentGatewayLinkRepository(
    GoogleSheetsRepository,
    ResidentGatewayLinkRepositoryPort,
):
    TABLE_NAME = "resident_gateway_link"
    ID_COLUMN = ResidentGatewayLinkColumns.RESIDENT_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: ResidentGatewayLinkRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_resident_gateway_links(self) -> tuple[ResidentGatewayLink, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def get_by_id(
            self,
            patient_id: str,
    ) -> ResidentGatewayLink:
        raw_row: RawRow = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)

    """
    def append_open_event(
            self,
            event: ResidentGatewayLink,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=ResidentGatewayLinkColumns.ORDER,
        )
    """
