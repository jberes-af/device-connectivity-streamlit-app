# /src/infrastructure/persistence/google_sheets/repos/CommunicationAttachment.py


# AUTO GENERATED

from src.application.ports.communication_attachment_repository_port import (
    CommunicationAttachmentRepositoryPort,
)

from src.domain.entities.communication_attachment_entities import (
    CommunicationAttachment,
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

from src.infrastructure.persistence.mappers.communication_attachment.communication_attachment_row_mapper import (
    CommunicationAttachmentRowMapper,
)


from src.infrastructure.persistence.schemas.communication_attachment.communication_attachment_columns import (
    CommunicationAttachmentColumns,
)


class GoogleSheetsCommunicationAttachmentRepository(
    GoogleSheetsRepository,
    CommunicationAttachmentRepositoryPort,
):

    TABLE_NAME = "communication_attachment"
    ID_COLUMN = CommunicationAttachmentColumns.ENTITY_ID


    def __init__(
        self,
        *,
        query_service: GoogleSheetsQueryService,
        catalog: GoogleSheetCatalog,
        mapper: CommunicationAttachmentRowMapper,
    ) -> None:

        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_communication_attachments(self) -> tuple[CommunicationAttachment, ...]:

        return tuple(
            self._mapper.from_raw(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> CommunicationAttachment:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.from_raw(raw_row)

    def append_open_event(
            self,
            event: CommunicationAttachment,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=CommunicationAttachmentColumns.ORDER,
        )
