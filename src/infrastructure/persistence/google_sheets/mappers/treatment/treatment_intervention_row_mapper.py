# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.treatment_intervention_columns import TreatmentInterventionColumns

from src.domain.entities.entities import TreatmentIntervention

from src.infrastructure.persistence.common.utils_parsing import *


class TreatmentInterventionRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> TreatmentIntervention:
        schema = TreatmentInterventionColumns

        return TreatmentIntervention(
            intervention_id=parse_required_text(
                row.get(schema.INTERVENTION_ID),
                field_name=schema.INTERVENTION_ID,
            ),
            treatment_plan_id=parse_required_text(
                row.get(schema.TREATMENT_PLAN_ID),
                field_name=schema.TREATMENT_PLAN_ID,
            ),
            treatment_type=parse_optional_text(
                row.get(schema.TREATMENT_TYPE),
                field_name=schema.TREATMENT_TYPE,
            ),
            description=parse_required_text(
                row.get(schema.DESCRIPTION),
                field_name=schema.DESCRIPTION,
            ),
            start_date=parse_required_date(
                row.get(schema.START_DATE),
                field_name=schema.START_DATE,
            ),
            end_date=parse_optional_date(
                row.get(schema.END_DATE),
                field_name=schema.END_DATE,
            ),
            status=parse_optional_text(
                row.get(schema.STATUS),
                field_name=schema.STATUS,
            ),
        )


    @staticmethod
    def to_row(
        treatment_intervention: TreatmentIntervention,
    ) -> RawRow:
        schema = TreatmentInterventionColumns

        return {

            schema.INTERVENTION_ID:
                treatment_intervention.intervention_id,

            schema.TREATMENT_PLAN_ID:
                treatment_intervention.treatment_plan_id,

            schema.TREATMENT_TYPE:
                treatment_intervention.treatment_type,

            schema.DESCRIPTION:
                treatment_intervention.description,

            schema.START_DATE:
                treatment_intervention.start_date,

            schema.END_DATE:
                treatment_intervention.end_date,

            schema.STATUS:
                treatment_intervention.status,

        }