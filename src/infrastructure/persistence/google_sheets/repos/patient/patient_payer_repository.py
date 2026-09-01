# /src/infrastructure/persistence/google_sheets/repos/patient/patient_payer_repository.py# repository.py.tpl

from typing import Sequence

from src.application.ports.patient_repo_ports import (
    PatientPayerRepositoryPort,
)

from src.domain.entities.resident.patient_entities import (
    PatientPayer,
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

from src.infrastructure.persistence.google_sheets.mappers.patient.patient_payer_row_mapper import (
    PatientPayerRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.patient.patient_payer_columns import (
    PatientPayerColumns,
)


class GoogleSheetsPatientPayerRepository(
    GoogleSheetsRepository,
    PatientPayerRepositoryPort,
):
    TABLE_NAME = "patient_payer"
    ID_COLUMN = PatientPayerColumns.PATIENT_PAYER_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: PatientPayerRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_patient_payers(self) -> tuple[PatientPayer, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def list_patient_payers_for_patient_id(
            self,
            patient_id: str,
    ) -> tuple[PatientPayer, ...]:
        raw_rows: list[RawRow] = self._find_rows(
            rows=self._read_rows(),
            column_name=PatientPayerColumns.PATIENT_ID,
            value=patient_id,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )

    def get_by_id(
            self,
            patient_payer_id: str,
    ) -> PatientPayer:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_payer_id,
        )

        return self._mapper.to_domain(raw_row)


    def get_by_ids(
            self,
            patient_payer_ids: Sequence[str],
    ) -> tuple[PatientPayer, ...]:
        raw_rows: list[RawRow] = self._find_rows_for_multiple_values(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            values=patient_payer_ids,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )
