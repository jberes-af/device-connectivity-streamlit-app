# /src/infrastructure/persistence/google_sheets/repos/treatment/treatment_plan_repository.py

from typing import Sequence

from src.application.ports.treatment_repo_ports import (
    TreatmentPlanRepositoryPort,
)

from src.domain.entities.care.treatment_entities import (
    TreatmentPlan,
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

from src.infrastructure.persistence.google_sheets.mappers.treatment.treatment_plan_row_mapper import (
    TreatmentPlanRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.treatment.treatment_plan_columns import (
    TreatmentPlanColumns,
)


class GoogleSheetsTreatmentPlanRepository(
    GoogleSheetsRepository,
    TreatmentPlanRepositoryPort,
):
    TABLE_NAME = "treatment_plan"
    ID_COLUMN = TreatmentPlanColumns.TREATMENT_PLAN_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: TreatmentPlanRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_treatment_plans(self) -> tuple[TreatmentPlan, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def get_by_id(
            self,
            treatment_plan_id: str,
    ) -> TreatmentPlan:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=treatment_plan_id,
        )

        return self._mapper.to_domain(raw_row)

    def get_by_ids(
            self,
            treatment_plan_ids: Sequence[str],
    ) -> tuple[TreatmentPlan, ...]:
        raw_rows: list[RawRow] = self._find_rows_for_multiple_values(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            values=treatment_plan_ids,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )
