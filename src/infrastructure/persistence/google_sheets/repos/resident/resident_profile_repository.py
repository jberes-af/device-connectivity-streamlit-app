# /src/infrastructure/persistence/google_sheets/repos/resident_profile_repository.py

from typing import Sequence

from src.application.ports.resident_repo_ports import (
    ResidentProfileRepositoryPort,
)

from src.domain.entities.person.resident_entities import (
    ResidentProfile,
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

from src.infrastructure.persistence.google_sheets.mappers.resident.resident_profile_row_mapper import (
    ResidentProfileRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.resident.resident_profile_columns import (
    ResidentProfileColumns,
)


class GoogleSheetsResidentProfileRepository(
    GoogleSheetsRepository,
    ResidentProfileRepositoryPort,
):
    TABLE_NAME = "resident_profile"
    ID_COLUMN = ResidentProfileColumns.RESIDENT_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: ResidentProfileRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_resident_profiles(self) -> tuple[ResidentProfile, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def get_by_id(
            self,
            resident_id: str,
    ) -> ResidentProfile:
        raw_row: RawRow = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=resident_id,
        )

        return self._mapper.to_domain(raw_row)

    def get_by_ids(
            self,
            resident_ids: Sequence[str],
    ) -> tuple[ResidentProfile, ...]:
        raw_rows: list[RawRow] = self._find_rows_for_multiple_values(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            values=resident_ids,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )
