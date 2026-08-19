# /src/infrastructure/persistence/google_sheets/repos/ClinicalNoteExport.py


# AUTO GENERATED

from src.application.ports.clinical_note_export_repository_port import (
    ClinicalNoteExportRepositoryPort,
)

from src.domain.entities.clinical_note_export_entities import (
    ClinicalNoteExport,
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

from src.infrastructure.persistence.mappers.clinical_note_export.clinical_note_export_row_mapper import (
    ClinicalNoteExportRowMapper,
)


from src.infrastructure.persistence.schemas.clinical_note_export.clinical_note_export_columns import (
    ClinicalNoteExportColumns,
)


class GoogleSheetsClinicalNoteExportRepository(
    GoogleSheetsRepository,
    ClinicalNoteExportRepositoryPort,
):

    TABLE_NAME = "clinical_note_export"
    ID_COLUMN = ClinicalNoteExportColumns.ENTITY_ID


    def __init__(
        self,
        *,
        query_service: GoogleSheetsQueryService,
        catalog: GoogleSheetCatalog,
        mapper: ClinicalNoteExportRowMapper,
    ) -> None:

        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_clinical_note_exports(self) -> tuple[ClinicalNoteExport, ...]:

        return tuple(
            self._mapper.from_raw(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> ClinicalNoteExport:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.from_raw(raw_row)

    def append_open_event(
            self,
            event: ClinicalNoteExport,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=ClinicalNoteExportColumns.ORDER,
        )
