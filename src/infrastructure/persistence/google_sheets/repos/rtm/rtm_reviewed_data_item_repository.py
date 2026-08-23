# /src/infrastructure/persistence/google_sheets/repos/RtmReviewedDataItem.py


# AUTO GENERATED

from src.application.ports.rtm_reviewed_data_item_repository_port import (
    RtmReviewedDataItemRepositoryPort,
)

from src.domain.entities.rtm_reviewed_data_item_entities import (
    RtmReviewedDataItem,
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

from src.infrastructure.persistence.mappers.rtm_reviewed_data_item.rtm_reviewed_data_item_row_mapper import (
    RtmReviewedDataItemRowMapper,
)


from src.infrastructure.persistence.schemas.rtm_reviewed_data_item.rtm_reviewed_data_item_columns import (
    RtmReviewedDataItemColumns,
)


class GoogleSheetsRtmReviewedDataItemRepository(
    GoogleSheetsRepository,
    RtmReviewedDataItemRepositoryPort,
):

    TABLE_NAME = "rtm_reviewed_data_item"
    ID_COLUMN = RtmReviewedDataItemColumns.ENTITY_ID


    def __init__(
        self,
        *,
        query_service: GoogleSheetsQueryService,
        catalog: GoogleSheetCatalog,
        mapper: RtmReviewedDataItemRowMapper,
    ) -> None:

        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_rtm_reviewed_data_items(self) -> tuple[RtmReviewedDataItem, ...]:

        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> RtmReviewedDataItem:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)

    def append_open_event(
            self,
            event: RtmReviewedDataItem,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=RtmReviewedDataItemColumns.ORDER,
        )
