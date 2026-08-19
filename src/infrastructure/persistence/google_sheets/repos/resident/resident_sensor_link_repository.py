# /src/infrastructure/persistence/google_sheets/repos/resident/resident_sensor_link.py

from src.application.ports.resident_repo_ports import (
    ResidentSensorLinkRepositoryPort,
)

from src.domain.entities.person.resident_entities import (
    ResidentSensorLink,
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

from src.infrastructure.persistence.google_sheets.mappers.resident.resident_sensor_link_row_mapper import (
    ResidentSensorLinkRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.resident.resident_sensor_link_columns import (
    ResidentSensorLinkColumns,
)


class GoogleSheetsResidentSensorLinkRepository(
    GoogleSheetsRepository,
    ResidentSensorLinkRepositoryPort,
):
    TABLE_NAME = "resident_sensor_link"
    ID_COLUMN = ResidentSensorLinkColumns.RESIDENT_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: ResidentSensorLinkRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_resident_sensor_links(self) -> tuple[ResidentSensorLink, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def get_by_id(
            self,
            patient_id: str,
    ) -> ResidentSensorLink:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)

    """
    def append_open_event(
            self,
            event: ResidentSensorLink,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=ResidentSensorLinkColumns.ORDER,
        )
    """
