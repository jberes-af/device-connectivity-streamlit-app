# /src/infrastructure/persistence/google_sheets/repos/CarePlan.py


# AUTO GENERATED

from src.application.ports.care_plan_repository_port import (
    CarePlanRepositoryPort,
)

from src.domain.entities.care.care_plan_entities import (
    CarePlan,
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

from src.infrastructure.persistence.google_sheets.mappers.care_plan import (
    CarePlanRowMapper,
)


from src.infrastructure.persistence.google_sheets.schemas.care_plan.care_plan_columns import (
    CarePlanColumns,
)


class GoogleSheetsCarePlanRepository(
    GoogleSheetsRepository,
    CarePlanRepositoryPort,
):

    TABLE_NAME = "care"
    ID_COLUMN = CarePlanColumns.ENTITY_ID


    def __init__(
        self,
        *,
        query_service: GoogleSheetsQueryService,
        catalog: GoogleSheetCatalog,
        mapper: CarePlanRowMapper,
    ) -> None:

        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_care_plans(self) -> tuple[CarePlan, ...]:

        return tuple(
            self._mapper.from_raw(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> CarePlan:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.from_raw(raw_row)

    def append_open_event(
            self,
            event: CarePlan,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=CarePlanColumns.ORDER,
        )
