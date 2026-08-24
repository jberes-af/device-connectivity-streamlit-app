# /src/infrastructure/persistence/google_sheets/repos/person/resident_contact_information.py


from src.application.ports.resident_repo_ports import (
    ResidentContactInformationRepositoryPort,
)

from src.domain.entities.person.resident_entities import (
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

from src.infrastructure.persistence.google_sheets.mappers.resident.resident_need_case_contact_row_mapper import (
    ResidentNeedCaseContactRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.resident.resident_need_case_contact_columns import (
    ResidentNeedCaseContactColumns,
)


class GoogleSheetsResidentNeedCaseContactRepository(
    GoogleSheetsRepository,
    ResidentContactInformationRepositoryPort,
):
    TABLE_NAME = "resident_contact_information"
    ID_COLUMN = ResidentNeedCaseContactColumns.RESIDENT_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: ResidentNeedCaseContactRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def get_by_id(
            self,
            patient_id: str,
    ) -> ResidentInCaseOfNeedContact:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)
