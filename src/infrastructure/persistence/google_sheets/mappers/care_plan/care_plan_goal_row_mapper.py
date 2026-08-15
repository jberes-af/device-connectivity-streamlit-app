# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas import CarePlanGoalColumns

from src.domain.entities.entities import CarePlanGoal

from src.infrastructure.persistence.common.utils_parsing import *


class CarePlanGoalRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> CarePlanGoal:
        schema = CarePlanGoalColumns

        return CarePlanGoal(
            goal_id=parse_required_text(
                row.get(schema.GOAL_ID),
                field_name=schema.GOAL_ID,
            ),
            care_plan_id=parse_required_text(
                row.get(schema.CARE_PLAN_ID),
                field_name=schema.CARE_PLAN_ID,
            ),
            title=parse_required_text(
                row.get(schema.TITLE),
                field_name=schema.TITLE,
            ),
            description=parse_required_text(
                row.get(schema.DESCRIPTION),
                field_name=schema.DESCRIPTION,
            ),
            priority=parse_optional_text(
                row.get(schema.PRIORITY),
                field_name=schema.PRIORITY,
            ),
            target_date=parse_optional_date(
                row.get(schema.TARGET_DATE),
                field_name=schema.TARGET_DATE,
            ),
            status=parse_optional_text(
                row.get(schema.STATUS),
                field_name=schema.STATUS,
            ),
            success_criteria=parse_optional_text(
                row.get(schema.SUCCESS_CRITERIA),
                field_name=schema.SUCCESS_CRITERIA,
            ),
        )


    @staticmethod
    def to_row(
        care_plan_goal: CarePlanGoal,
    ) -> RawRow:
        schema = CarePlanGoalColumns

        return {

            schema.GOAL_ID:
                care_plan_goal.goal_id,

            schema.CARE_PLAN_ID:
                care_plan_goal.care_plan_id,

            schema.TITLE:
                care_plan_goal.title,

            schema.DESCRIPTION:
                care_plan_goal.description,

            schema.PRIORITY:
                care_plan_goal.priority,

            schema.TARGET_DATE:
                care_plan_goal.target_date,

            schema.STATUS:
                care_plan_goal.status,

            schema.SUCCESS_CRITERIA:
                care_plan_goal.success_criteria,

        }