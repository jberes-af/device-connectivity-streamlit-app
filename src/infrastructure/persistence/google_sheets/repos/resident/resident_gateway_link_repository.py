# /src/infrastructure/persistence/google_sheets/repos/ResidentGatewayLink.py


# AUTO GENERATED

from src.application.ports.resident_gateway_link_repository_port import (
    ResidentGatewayLinkRepositoryPort,
)

from src.domain.entities.resident_gateway_link_entities import (
    ResidentGatewayLink,
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
    ResidentGatewayLinkRowMapper,
)


from src.infrastructure.persistence.google_sheets.schemas import (
    ResidentGatewayLinkColumns,
)


class GoogleSheetsResidentGatewayLinkRepository(
    GoogleSheetsRepository,
    ResidentGatewayLinkRepositoryPort,
):

    TABLE_NAME = "resident_gateway_link"
    ID_COLUMN = ResidentGatewayLinkColumns.ENTITY_ID


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
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)

    def append_open_event(
            self,
            event: ResidentGatewayLink,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=ResidentGatewayLinkColumns.ORDER,
        )
