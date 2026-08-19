# /src/infrastructure/persistence/google_sheets/repos/resident/resident_contact_information.py


from src.application.ports.resident_repo_ports import (
    ResidentContactInformationRepositoryPort,
)

from src.domain.entities.person.resident_entities import (
    ResidentContactInformation,
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
            patient_id: str,
    ) -> ResidentContactInformation:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)
