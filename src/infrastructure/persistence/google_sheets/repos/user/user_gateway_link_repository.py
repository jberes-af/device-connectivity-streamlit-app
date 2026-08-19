# /src/infrastructure/persistence/google_sheets/repos/UserGatewayLink.py


# AUTO GENERATED

from src.application.ports.user_gateway_link_repository_port import (
    UserGatewayLinkRepositoryPort,
)

from src.domain.entities.user_gateway_link_entities import (
    UserGatewayLink,
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
    UserGatewayLinkRowMapper,
)


from src.infrastructure.persistence.google_sheets.schemas import (
    UserGatewayLinkColumns,
)


class GoogleSheetsUserGatewayLinkRepository(
    GoogleSheetsRepository,
    UserGatewayLinkRepositoryPort,
):

    TABLE_NAME = "user_gateway_link"
    ID_COLUMN = UserGatewayLinkColumns.ENTITY_ID


    def __init__(
        self,
        *,
        query_service: GoogleSheetsQueryService,
        catalog: GoogleSheetCatalog,
        mapper: UserGatewayLinkRowMapper,
    ) -> None:

        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_user_gateway_links(self) -> tuple[UserGatewayLink, ...]:

        return tuple(
            self._mapper.from_raw(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> UserGatewayLink:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.from_raw(raw_row)

    def append_open_event(
            self,
            event: UserGatewayLink,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=UserGatewayLinkColumns.ORDER,
        )
