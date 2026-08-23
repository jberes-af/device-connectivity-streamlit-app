# /src/infrastructure/persistence/google_sheets/repos/TreatmentMonitoringParameter.py


# AUTO GENERATED

from src.application.ports.treatment_monitoring_parameter_repository_port import (
    TreatmentMonitoringParameterRepositoryPort,
)

from src.domain.entities.treatment_monitoring_parameter_entities import (
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

from src.infrastructure.persistence.mappers.treatment_monitoring_parameter.treatment_monitoring_parameter_row_mapper import (
    TreatmentMonitoringParameterRowMapper,
)


from src.infrastructure.persistence.schemas.treatment_monitoring_parameter.treatment_monitoring_parameter_columns import (
    TreatmentMonitoringParameterColumns,
)


class GoogleSheetsTreatmentMonitoringParameterRepository(
    GoogleSheetsRepository,
    TreatmentMonitoringParameterRepositoryPort,
):

    TABLE_NAME = "treatment_monitoring_parameter"
    ID_COLUMN = TreatmentMonitoringParameterColumns.ENTITY_ID


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

    def list_treatment_monitoring_parameters(self) -> tuple[TreatmentMonitoringParameter, ...]:

        return tuple(
            self._mapper.to_domain(row)
            for row in self._read_rows()
        )


    def get_by_id(
            self,
            patient_id: str,
    ) -> TreatmentMonitoringParameter:
        raw_row = self._find_single_row(
            rows=self._read_rows(),
            column_name=self.ID_COLUMN,
            value=patient_id,
        )

        return self._mapper.to_domain(raw_row)

    def append_open_event(
            self,
            event: TreatmentMonitoringParameter,
    ) -> None:
        raw_row: RawRow = self._mapper.to_row(event)

        self._append_raw_row(
            row=raw_row,
            columns=TreatmentMonitoringParameterColumns.ORDER,
        )
