# /src/infrastructure/persistence/google_sheets/mappers/treatment/treatment_monitoring_parameter_row_mapper.py

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.treatment.treatment_monitoring_parameter_columns import (
    TreatmentMonitoringParameterColumns
)

from src.domain.entities.care.treatment_entities import TreatmentMonitoringParameter

from src.infrastructure.persistence.common.utils_parsing import *


class TreatmentMonitoringParameterRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> TreatmentMonitoringParameter:
        schema = TreatmentMonitoringParameterColumns

        return TreatmentMonitoringParameter(
            monitoring_parameter_id=parse_required_text(
                row.get(schema.MONITORING_PARAMETER_ID),
                field_name=schema.MONITORING_PARAMETER_ID,
            ),
            treatment_plan_id=parse_required_text(
                row.get(schema.TREATMENT_PLAN_ID),
                field_name=schema.TREATMENT_PLAN_ID,
            ),
            goal_id=parse_required_text(
                row.get(schema.GOAL_ID),
                field_name=schema.GOAL_ID,
            ),
            measure_definition_id=parse_required_text(
                row.get(schema.MEASURE_DEFINITION_ID),
                field_name=schema.MEASURE_DEFINITION_ID,
            ),
            baseline_value=parse_optional_text(
                row.get(schema.BASELINE_VALUE),
                field_name=schema.BASELINE_VALUE,
            ),
            target_value=parse_optional_text(
                row.get(schema.TARGET_VALUE),
                field_name=schema.TARGET_VALUE,
            ),
            unit=parse_optional_text(
                row.get(schema.UNIT),
                field_name=schema.UNIT,
            ),
        )

    @staticmethod
    def to_row(
            treatment_monitoring_parameter: TreatmentMonitoringParameter,
    ) -> RawRow:
        schema = TreatmentMonitoringParameterColumns

        return {

            schema.MONITORING_PARAMETER_ID:
                treatment_monitoring_parameter.monitoring_parameter_id,

            schema.TREATMENT_PLAN_ID:
                treatment_monitoring_parameter.treatment_plan_id,

            schema.GOAL_ID:
                treatment_monitoring_parameter.goal_id,

            schema.MEASURE_DEFINITION_ID:
                treatment_monitoring_parameter.measure_definition_id,

            schema.BASELINE_VALUE:
                treatment_monitoring_parameter.baseline_value,

            schema.TARGET_VALUE:
                treatment_monitoring_parameter.target_value,

            schema.UNIT:
                treatment_monitoring_parameter.unit,

        }
