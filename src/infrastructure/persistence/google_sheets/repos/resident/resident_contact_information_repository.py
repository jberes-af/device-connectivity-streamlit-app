# /src/infrastructure/persistence/google_sheets/repos/resident/resident_contact_information.py

from typing import Sequence

from src.application.ports.resident_repo_ports import (
    ResidentContactInformationRepositoryPort,
)

from src.domain.entities.resident.resident_entities import (
    ResidentInCaseOfNeedContact,
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

from src.infrastructure.persistence.google_sheets.mappers.resident.resident_contact_information_row_mapper import (
    ResidentContactInformationRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.resident.resident_contact_information_columns import (
    ResidentContactInformationColumns,
)


class GoogleSheetsResidentContactInformationRepository(
    GoogleSheetsRepository,
    ResidentContactInformationRepositoryPort,
):
    TABLE_NAME = "resident_contact_information"
    ID_COLUMN = ResidentContactInformationColumns.RESIDENT_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: ResidentContactInformationRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def get_by_id(
            self,
            resident_id: str,
    ) -> ResidentInCaseOfNeedContact:
        raw_row: RawRow = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=resident_id,
        )

        return self._mapper.to_domain(raw_row)

    from typing import Sequence

    def get_by_ids(
            self,
            resident_ids: Sequence[str],
    ) -> tuple[ResidentInCaseOfNeedContact, ...]:
        raw_rows: list[RawRow] = (
            self._find_rows_for_multiple_values(
                rows=self._read_rows(),
                column_name=self.ID_COLUMN,
                values=resident_ids,
            )
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )
