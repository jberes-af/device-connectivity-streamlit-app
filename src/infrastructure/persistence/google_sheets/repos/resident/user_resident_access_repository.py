# /src/infrastructure/persistence/google_sheets/repos/UserResidentAccess.py


# AUTO GENERATED

from src.application.ports.user_resident_access_repository_port import (
    UserResidentAccessRepositoryPort,
)

from src.domain.entities.user_resident_access_entities import (
    UserResidentAccess,
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
    UserResidentAccessRowMapper,
)


from src.infrastructure.persistence.google_sheets.schemas import (
    UserResidentAccessColumns,
)


class GoogleSheetsUserResidentAccessRepository(
    GoogleSheetsRepository,
    UserResidentAccessRepositoryPort,
):

    TABLE_NAME = "user_resident_access"
    ID_COLUMN = UserResidentAccessColumns.ENTITY_ID


    def __init__(
        self,
        *,
        query_service: GoogleSheetsQueryService,
        catalog: GoogleSheetCatalog,
        mapper: UserResidentAccessRowMapper,
    ) -> None:

        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_user_resident_accesses(self) -> tuple[UserResidentAccess, ...]:

        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> UserResidentAccess:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)

    def append_open_event(
            self,
            event: UserResidentAccess,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=UserResidentAccessColumns.ORDER,
        )
