# /src/infrastructure/persistence/google_sheets/repos/treatment/rtm_necessity.py

from typing import Sequence

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
            rtm_necessity_id: str,
    ) -> RtmMedicalNecessity:
        raw_row: RawRow = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=rtm_necessity_id,
        )

        return self._mapper.to_domain(raw_row)

    def get_by_ids(
            self,
            rtm_necessity_ids: Sequence[str],
    ) -> tuple[RtmMedicalNecessity, ...]:
        raw_rows: list[RawRow] = self._find_rows_for_multiple_values(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            values=rtm_necessity_ids,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )

    def list_rtm_necessity_records_patient_id(
            self,
            patient_id: str,
    ) -> tuple[RtmMedicalNecessity, ...]:
        raw_rows: list[RawRow] = self._find_rows(
            rows=self._read_rows(),
            column_name="patient_id",
            value=patient_id,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )
