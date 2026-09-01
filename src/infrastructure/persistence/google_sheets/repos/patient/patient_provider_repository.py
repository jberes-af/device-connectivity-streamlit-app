# /src/infrastructure/persistence/google_sheets/repos/treatment/patient_provider_repository.py

from src.application.ports.patient_repo_ports import (
    PatientProviderRepositoryPort,
)

from src.domain.entities.resident.patient_entities import (
    PatientProvider,
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

from src.infrastructure.persistence.google_sheets.mappers.patient.patient_provider_row_mapper import (
    PatientProviderRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.patient.patient_provider_columns import (
    PatientProviderColumns,
)


class GoogleSheetsPatientProviderRepository(
    GoogleSheetsRepository,
    PatientProviderRepositoryPort,
):
    TABLE_NAME = "patient_provider"
    ID_COLUMN = PatientProviderColumns.PATIENT_PROVIDER_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: PatientProviderRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_patient_providers(self) -> tuple[PatientProvider, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def list_providers_for_patient_id(
            self,
            patient_id: str,
    ) -> tuple[PatientProvider, ...]:
        raw_rows: list[RawRow] = self._find_rows(
            rows=self._read_rows(),
            column_name="patient_id",
            value=patient_id,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )

    def get_by_id(
            self,
            patient_provider_id: str,
    ) -> PatientProvider:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_provider_id,
        )

        return self._mapper.to_domain(raw_row)
