# /src/infrastructure/persistence/google_sheets/repos/CarePlanRisk.py


# AUTO GENERATED

from src.application.ports.care_plan_risk_repository_port import (
    CarePlanRiskRepositoryPort,
)

from src.domain.entities.care_plan_risk_entities import (
    CarePlanRisk,
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
    CarePlanRiskRowMapper,
)


from src.infrastructure.persistence.google_sheets.schemas import (
    CarePlanRiskColumns,
)


class GoogleSheetsCarePlanRiskRepository(
    GoogleSheetsRepository,
    CarePlanRiskRepositoryPort,
):

    TABLE_NAME = "care_plan_risk"
    ID_COLUMN = CarePlanRiskColumns.ENTITY_ID


    def __init__(
        self,
        *,
        query_service: GoogleSheetsQueryService,
        catalog: GoogleSheetCatalog,
        mapper: CarePlanRiskRowMapper,
    ) -> None:

        super().__init__(
            query_service=query_service,
            catalog=catalog,
        )

        self._mapper = mapper

    def list_care_plan_risks(self) -> tuple[CarePlanRisk, ...]:

        return tuple(
            self._mapper.from_raw(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> CarePlanRisk:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.from_raw(raw_row)

    def append_open_event(
            self,
            event: CarePlanRisk,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=CarePlanRiskColumns.ORDER,
        )
