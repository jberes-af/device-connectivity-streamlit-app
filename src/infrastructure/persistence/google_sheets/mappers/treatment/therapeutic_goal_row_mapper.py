# /src/infrastructure/persistence/google_sheets/mappers/treatment/therapeutic_goal_row_mapper.py

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.treatment.therapeutic_goal_columns import (
    TherapeuticGoalColumns
)

from src.domain.entities.care.treatment_entities import TherapeuticGoal

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
            description=parse_required_text(
                row.get(schema.DESCRIPTION),
                field_name=schema.DESCRIPTION,
            ),
            target_date=parse_optional_date(
                row.get(schema.TARGET_DATE),
                field_name=schema.TARGET_DATE,
            ),
        )

    @staticmethod
    def to_row(
            therapeutic_goal: TherapeuticGoal,
    ) -> RawRow:
        schema = TherapeuticGoalColumns

        return {

            schema.GOAL_ID:
                therapeutic_goal.goal_id,

            schema.TREATMENT_PLAN_ID:
                therapeutic_goal.treatment_plan_id,

            schema.DESCRIPTION:
                therapeutic_goal.description,

            schema.TARGET_DATE:
                therapeutic_goal.target_date,

        }
