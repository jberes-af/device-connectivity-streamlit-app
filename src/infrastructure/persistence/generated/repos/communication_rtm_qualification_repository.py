# /src/infrastructure/persistence/google_sheets/repos/CommunicationRTMQualification.py


# AUTO GENERATED

from src.application.ports.communication_rtm_qualification_repository_port import (
    CommunicationRTMQualificationRepositoryPort,
)

from src.domain.entities.communication_rtm_qualification_entities import (
    CommunicationRTMQualification,
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

from src.infrastructure.persistence.mappers.communication_rtm_qualification.communication_rtm_qualification_row_mapper import (
    CommunicationRTMQualificationRowMapper,
)


from src.infrastructure.persistence.schemas.communication_rtm_qualification.communication_rtm_qualification_columns import (
    CommunicationRTMQualificationColumns,
)


class GoogleSheetsCommunicationRTMQualificationRepository(
    GoogleSheetsRepository,
    CommunicationRTMQualificationRepositoryPort,
):

    TABLE_NAME = "communication_rtm_qualification"
    ID_COLUMN = CommunicationRTMQualificationColumns.ENTITY_ID


    def __init__(
        self,
        *,
        query_service: GoogleSheetsQueryService,
        catalog: GoogleSheetCatalog,
        mapper: CommunicationRTMQualificationRowMapper,
    ) -> None:

        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_communication_rtm_qualifications(self) -> tuple[CommunicationRTMQualification, ...]:

        return tuple(
            self._mapper.from_raw(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> CommunicationRTMQualification:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.from_raw(raw_row)

    def append_open_event(
            self,
            event: CommunicationRTMQualification,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=CommunicationRTMQualificationColumns.ORDER,
        )
