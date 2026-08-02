# AUTO GENERATED

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.therapeuticgoal_columns import TherapeuticGoalColumns

from src.domain.entities.patient_entities import TherapeuticGoal

from src.infrastructure.persistence.common.utils_parsing import *

class TherapeuticGoalRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> TherapeuticGoal:

        schema = TherapeuticGoalColumns

        return TherapeuticGoal(
            goal_id=parse_required_text(
                row.get(schema.GOAL_ID),
                field_name=schema.GOAL_ID,
            ),
            treatment_plan_id=parse_required_text(
                row.get(schema.TREATMENT_PLAN_ID),
                field_name=schema.TREATMENT_PLAN_ID,
            ),
            outcome_measure_id=parse_required_text(
                row.get(schema.OUTCOME_MEASURE_ID),
                field_name=schema.OUTCOME_MEASURE_ID,
            ),
            description=parse_required_text(
                row.get(schema.DESCRIPTION),
                field_name=schema.DESCRIPTION,
            ),
            target_value=parse_optional_text(
                row.get(schema.TARGET_VALUE),
                field_name=schema.TARGET_VALUE,
            ),
            target_date=parse_optional_date(
                row.get(schema.TARGET_DATE),
                field_name=schema.TARGET_DATE,
            ),
            success_criteria=parse_required_text(
                row.get(schema.SUCCESS_CRITERIA),
                field_name=schema.SUCCESS_CRITERIA,
            ),
        )