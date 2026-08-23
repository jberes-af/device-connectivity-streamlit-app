# /src/infrastructure/persistence/google_sheets/repos/RtmInteraction.py


# AUTO GENERATED

from src.application.ports.rtm_interaction_repository_port import (
    RtmInteractionRepositoryPort,
)

from src.domain.entities.rtm_interaction_entities import (
    RtmInteraction,
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

from src.infrastructure.persistence.mappers.rtm_interaction.rtm_interaction_row_mapper import (
    RtmInteractionRowMapper,
)


from src.infrastructure.persistence.schemas.rtm_interaction.rtm_interaction_columns import (
    RtmInteractionColumns,
)


class GoogleSheetsRtmInteractionRepository(
    GoogleSheetsRepository,
    RtmInteractionRepositoryPort,
):

    TABLE_NAME = "rtm_interaction"
    ID_COLUMN = RtmInteractionColumns.ENTITY_ID


    def __init__(
        self,
        *,
        query_service: GoogleSheetsQueryService,
        catalog: GoogleSheetCatalog,
        mapper: RtmInteractionRowMapper,
    ) -> None:

        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_rtm_interactions(self) -> tuple[RtmInteraction, ...]:

        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> RtmInteraction:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)

    def append_open_event(
            self,
            event: RtmInteraction,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=RtmInteractionColumns.ORDER,
        )
