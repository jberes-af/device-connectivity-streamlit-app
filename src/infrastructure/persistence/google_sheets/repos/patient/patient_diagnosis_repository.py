# /src/infrastructure/persistence/google_sheets/repos/treatment/patient_diagnosis_repository.py

from typing import Sequence

from src.domain.entities.person.patient_entities import PatientDiagnosis

from src.application.ports.patient_repo_ports import (
    PatientDiagnosisRepositoryPort,
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

from src.infrastructure.persistence.google_sheets.mappers.patient.patient_diagnosis_row_mapper import (
    PatientDiagnosisRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.patient.patient_diagnosis_columns import (
    PatientDiagnosisColumns,
)


class GoogleSheetsPatientDiagnosisRepository(
    GoogleSheetsRepository,
    PatientDiagnosisRepositoryPort,
):
    TABLE_NAME = "patient_diagnosis"
    ID_COLUMN = PatientDiagnosisColumns.PATIENT_DIAGNOSIS_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: PatientDiagnosisRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_patient_diagnoses(self) -> tuple[PatientDiagnosis, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def get_by_id(
            self,
            patient_diagnosis_id: str,
    ) -> PatientDiagnosis:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_diagnosis_id,
        )

        return self._mapper.to_domain(raw_row)

    def get_by_ids(
            self,
            patient_diagnosis_ids: Sequence[str],
    ) -> tuple[PatientDiagnosis, ...]:
        raw_rows: list[RawRow] = self._find_rows_for_multiple_values(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            values=patient_diagnosis_ids,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )

    def list_diagnoses_for_patient_id(
            self,
            patient_id: str,
    ) -> tuple[PatientDiagnosis, ...]:
        raw_rows: list[RawRow] = self._find_rows(
            rows=self._read_rows(),
            column_name="patient_id",
            value=patient_id,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )
