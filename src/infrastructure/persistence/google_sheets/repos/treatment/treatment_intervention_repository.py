# /src/infrastructure/persistence/google_sheets/repos/treatment/treatment_intervention_repository.py


from typing import Sequence

from src.application.ports.treatment_repo_ports import (
    TreatmentInterventionRepositoryPort,
)

from src.domain.entities.care.treatment_entities import (
    TreatmentIntervention,
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

from src.infrastructure.persistence.google_sheets.mappers.treatment.treatment_intervention_row_mapper import (
    TreatmentInterventionRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.treatment.treatment_intervention_columns import (
    TreatmentInterventionColumns,
)


class GoogleSheetsTreatmentInterventionRepository(
    GoogleSheetsRepository,
    TreatmentInterventionRepositoryPort,
):
    TABLE_NAME = "treatment_intervention"
    ID_COLUMN = TreatmentInterventionColumns.INTERVENTION_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: TreatmentInterventionRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_treatment_interventions(
            self,
    ) -> tuple[TreatmentIntervention, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def list_for_treatment_plan_id(
            self,
            treatment_plan_id: str,
    ) -> tuple[TreatmentIntervention, ...]:
        raw_rows: list[RawRow] = self._find_rows(
            rows=self._read_rows(),
            column_name=TreatmentInterventionColumns.TREATMENT_PLAN_ID,
            value=treatment_plan_id,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )

    def get_by_id(
            self,
            treatment_intervention_id: str,
    ) -> TreatmentIntervention:
        raw_row: RawRow = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=treatment_intervention_id,
        )

        return self._mapper.to_domain(raw_row)

    def get_by_ids(
            self,
            treatment_intervention_ids: Sequence[str],
    ) -> tuple[TreatmentIntervention, ...]:
        raw_rows: list[RawRow] = self._find_rows_for_multiple_values(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            values=treatment_intervention_ids,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )
