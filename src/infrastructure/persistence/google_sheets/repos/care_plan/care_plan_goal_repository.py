# /src/infrastructure/persistence/google_sheets/repos/CarePlanGoal.py


# AUTO GENERATED

from src.application.ports.care_plan_goal_repository_port import (
    CarePlanGoalRepositoryPort,
)

from src.domain.entities.care_plan_goal_entities import (
    CarePlanGoal,
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

from src.infrastructure.persistence.google_sheets.mappers import (
    CarePlanGoalRowMapper,
)


from src.infrastructure.persistence.google_sheets.schemas import (
    CarePlanGoalColumns,
)


class GoogleSheetsCarePlanGoalRepository(
    GoogleSheetsRepository,
    CarePlanGoalRepositoryPort,
):

    TABLE_NAME = "care_plan_goal"
    ID_COLUMN = CarePlanGoalColumns.ENTITY_ID


    def __init__(
        self,
        *,
        query_service: GoogleSheetsQueryService,
        catalog: GoogleSheetCatalog,
        mapper: CarePlanGoalRowMapper,
    ) -> None:

        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_care_plan_goals(self) -> tuple[CarePlanGoal, ...]:

        return tuple(
            self._mapper.from_raw(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> CarePlanGoal:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.from_raw(raw_row)

    def append_open_event(
            self,
            event: CarePlanGoal,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=CarePlanGoalColumns.ORDER,
        )
