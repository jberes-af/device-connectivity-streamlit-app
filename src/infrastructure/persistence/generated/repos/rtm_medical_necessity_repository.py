# /src/infrastructure/persistence/google_sheets/repos/RTMMedicalNecessity.py


# AUTO GENERATED

from src.application.ports.rtm_medical_necessity_repository_port import (
    RTMMedicalNecessityRepositoryPort,
)

from src.domain.entities.rtm_medical_necessity_entities import (
    RTMMedicalNecessity,
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

from src.infrastructure.persistence.mappers.rtm_medical_necessity.rtm_medical_necessity_row_mapper import (
    RTMMedicalNecessityRowMapper,
)


from src.infrastructure.persistence.schemas.rtm_medical_necessity.rtm_medical_necessity_columns import (
    RTMMedicalNecessityColumns,
)


class GoogleSheetsRTMMedicalNecessityRepository(
    GoogleSheetsRepository,
    RTMMedicalNecessityRepositoryPort,
):

    TABLE_NAME = "rtm_medical_necessity"
    ID_COLUMN = RTMMedicalNecessityColumns.ENTITY_ID


    def __init__(
        self,
        *,
        query_service: GoogleSheetsQueryService,
        catalog: GoogleSheetCatalog,
        mapper: RTMMedicalNecessityRowMapper,
    ) -> None:

        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_rtm_medical_necessities(self) -> tuple[RTMMedicalNecessity, ...]:

        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> RTMMedicalNecessity:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)

    def append_open_event(
            self,
            event: RTMMedicalNecessity,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=RTMMedicalNecessityColumns.ORDER,
        )
