# /src/infrastructure/persistence/google_sheets/repos/TreatmentMonitoringParameter.py

from typing import Sequence

from src.application.ports.treatment_repo_ports import (
    TreatmentMonitoringParameterRepositoryPort,
)

from src.domain.entities.care.treatment_entities import (
    TreatmentMonitoringParameter,
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

from src.infrastructure.persistence.google_sheets.mappers.treatment.treatment_monitoring_parameter_row_mapper import (
    TreatmentMonitoringParameterRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.treatment.treatment_monitoring_parameter_columns import (
    TreatmentMonitoringParameterColumns,
)


class GoogleSheetsTreatmentMonitoringParameterRepository(
    GoogleSheetsRepository,
    TreatmentMonitoringParameterRepositoryPort,
):
    TABLE_NAME = "treatment_monitoring_parameter"
    ID_COLUMN = TreatmentMonitoringParameterColumns.MONITORING_PARAMETER_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: TreatmentMonitoringParameterRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_treatment_monitoring_parameters(
            self,
    ) -> tuple[TreatmentMonitoringParameter, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def list_for_treatment_plan_id(
            self,
            treatment_plan_id: str,
    ) -> tuple[TreatmentMonitoringParameter, ...]:
        raw_rows: list[RawRow] = self._find_rows(
            rows=self._read_rows(),
            column_name=(
                TreatmentMonitoringParameterColumns.TREATMENT_PLAN_ID
            ),
            value=treatment_plan_id,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )

    def get_by_id(
            self,
            treatment_monitoring_parameter_id: str,
    ) -> TreatmentMonitoringParameter:
        raw_row: RawRow = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=treatment_monitoring_parameter_id,
        )

        return self._mapper.to_domain(raw_row)

    def get_by_ids(
            self,
            treatment_monitoring_parameter_ids: Sequence[str],
    ) -> tuple[TreatmentMonitoringParameter, ...]:
        raw_rows: list[RawRow] = self._find_rows_for_multiple_values(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            values=treatment_monitoring_parameter_ids,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )
