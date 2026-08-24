# /src/infrastructure/persistence/google_sheets/repos/treatment/therapeutic_goal_repository.py

from typing import Sequence

from src.application.ports.treatment_repo_ports import (
    TherapeuticGoalRepositoryPort,
)

from src.domain.entities.care.treatment_entities import (
    TherapeuticGoal,
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

from src.infrastructure.persistence.google_sheets.mappers.treatment.therapeutic_goal_row_mapper import (
    TherapeuticGoalRowMapper,
)

from src.infrastructure.persistence.google_sheets.schemas.treatment.therapeutic_goal_columns import (
    TherapeuticGoalColumns,
)


class GoogleSheetsTherapeuticGoalRepository(
    GoogleSheetsRepository,
    TherapeuticGoalRepositoryPort,
):
    TABLE_NAME = "therapeutic_goal"
    ID_COLUMN = TherapeuticGoalColumns.GOAL_ID

    def __init__(
            self,
            *,
            query_service: GoogleSheetsQueryService,
            catalog: GoogleSheetCatalog,
            mapper: TherapeuticGoalRowMapper,
    ) -> None:
        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_therapeutic_goals(
            self,
    ) -> tuple[TherapeuticGoal, ...]:
        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )

    def get_by_id(
            self,
            goal_id: str,
    ) -> TherapeuticGoal:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=goal_id,
        )

        return self._mapper.to_domain(raw_row)

    def get_by_ids(
            self,
            goal_ids: Sequence[str],
    ) -> tuple[TherapeuticGoal, ...]:
        raw_rows: list[RawRow] = (
            self._find_rows_for_multiple_values(
                rows=self._read_rows(),
                column_name=self.ID_COLUMN,
                values=goal_ids,
            )
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )

    def list_for_treatment_plan_id(
            self,
            treatment_plan_id: str,
    ) -> tuple[TherapeuticGoal, ...]:
        raw_rows: list[RawRow] = self._find_rows(
            rows=self._read_rows(),
            column_name=TherapeuticGoalColumns.TREATMENT_PLAN_ID,
            value=treatment_plan_id,
        )

        return tuple(
            self._mapper.to_domain(row)
            for row in raw_rows
        )
