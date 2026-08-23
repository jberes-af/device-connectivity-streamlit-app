# /src/infrastructure/persistence/google_sheets/repos/treatment/rtm_necessity.py

from src.domain.entities.care.rtm_entities import RtmMedicalNecessity

from src.application.ports.rtm_repo_ports import RtmNecessityRepositoryPort

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

from src.infrastructure.persistence.google_sheets.mappers.rtm.rtm_necessity_row_mapper import (
    RtmNecessityRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.rtm.rtm_necessity_columns import (
    RtmNecessityColumns,
)


class GoogleSheetsRtmNecessityRepository(
    GoogleSheetsRepository,
    RtmNecessityRepositoryPort,
):
    TABLE_NAME = "rtm_necessity"
    ID_COLUMN = RtmNecessityColumns.RTM_NECESSITY_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: RtmNecessityRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_rtm_necessity_records(self) -> tuple[RtmMedicalNecessity, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def get_by_id(
            self,
            patient_id: str,
    ) -> RtmMedicalNecessity:
        raw_row: RawRow = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)
