# /src/infrastructure/persistence/google_sheets/repos/diagnosis_definition_repository.py

from typing import Sequence

from src.application.ports.diagnosis_repo_ports import (
    DiagnosisDefinitionRepositoryPort,
)

from src.domain.entities.care.diagnosis_entities import (
    DiagnosisDefinition,
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

from src.infrastructure.persistence.google_sheets.mappers.diagnosis.diagnosis_definition_row_mapper import (
    DiagnosisDefinitionRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.diagnosis.diagnosis_definition_columns import (
    DiagnosisDefinitionColumns,
)


class GoogleSheetsDiagnosisDefinitionRepository(
    GoogleSheetsRepository,
    DiagnosisDefinitionRepositoryPort,
):
    TABLE_NAME = "diagnosis_definition"
    ID_COLUMN = DiagnosisDefinitionColumns.DIAGNOSIS_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: DiagnosisDefinitionRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_diagnosis_profiles(self) -> tuple[DiagnosisDefinition, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def get_by_id(
            self,
            diagnosis_id: str,
    ) -> DiagnosisDefinition:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=diagnosis_id,
        )

        return self._mapper.to_domain(raw_row)

    def get_by_ids(
            self,
            diagnosis_ids: Sequence[str],
    ) -> tuple[DiagnosisDefinition, ...]:
        raw_rows: list[RawRow] = self._find_rows_for_multiple_values(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            values=diagnosis_ids,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )
