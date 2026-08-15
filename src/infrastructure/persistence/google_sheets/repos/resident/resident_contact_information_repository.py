# /src/infrastructure/persistence/google_sheets/repos/ResidentContactInformation.py


# AUTO GENERATED

from src.application.ports.resident_contact_information_repository_port import (
    ResidentContactInformationRepositoryPort,
)

from src.domain.entities.resident_contact_information_entities import (
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

from src.infrastructure.persistence.google_sheets.mappers import (
    ResidentContactInformationRowMapper,
)


from src.infrastructure.persistence.google_sheets.schemas import (
    ResidentContactInformationColumns,
)


class GoogleSheetsResidentContactInformationRepository(
    GoogleSheetsRepository,
    ResidentContactInformationRepositoryPort,
):

    TABLE_NAME = "resident_contact_information"
    ID_COLUMN = ResidentContactInformationColumns.ENTITY_ID


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

    def list_resident_contact_informations(self) -> tuple[ResidentContactInformation, ...]:

        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )


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

    def append_open_event(
            self,
            event: ResidentContactInformation,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=ResidentContactInformationColumns.ORDER,
        )
