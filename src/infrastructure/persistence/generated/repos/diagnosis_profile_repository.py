# /src/infrastructure/persistence/google_sheets/repos/DiagnosisProfile.py


# AUTO GENERATED

from src.application.ports.diagnosis_profile_repository_port import (
    DiagnosisProfileRepositoryPort,
)

from src.domain.entities.diagnosis_profile_entities import (
    DiagnosisProfile,
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

from src.infrastructure.persistence.mappers.diagnosis_profile.diagnosis_profile_row_mapper import (
    DiagnosisProfileRowMapper,
)


from src.infrastructure.persistence.schemas.diagnosis_profile.diagnosis_profile_columns import (
    DiagnosisProfileColumns,
)


class GoogleSheetsDiagnosisProfileRepository(
    GoogleSheetsRepository,
    DiagnosisProfileRepositoryPort,
):

    TABLE_NAME = "diagnosis_profile"
    ID_COLUMN = DiagnosisProfileColumns.ENTITY_ID


    def __init__(
        self,
        *,
        query_service: GoogleSheetsQueryService,
        catalog: GoogleSheetCatalog,
        mapper: DiagnosisProfileRowMapper,
    ) -> None:

        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_diagnosis_profiles(self) -> tuple[DiagnosisProfile, ...]:

        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> DiagnosisProfile:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)

    def append_open_event(
            self,
            event: DiagnosisProfile,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=DiagnosisProfileColumns.ORDER,
        )
