# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas import CarePlanTaskColumns

from src.domain.entities.entities import CarePlanTask

from src.infrastructure.persistence.common.utils_parsing import *


class CarePlanTaskRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> CarePlanTask:
        schema = CarePlanTaskColumns

        return CarePlanTask(
            task_id=parse_required_text(
                row.get(schema.TASK_ID),
                field_name=schema.TASK_ID,
            ),
            care_plan_id=parse_required_text(
                row.get(schema.CARE_PLAN_ID),
                field_name=schema.CARE_PLAN_ID,
            ),
            related_goal_id=parse_optional_text(
                row.get(schema.RELATED_GOAL_ID),
                field_name=schema.RELATED_GOAL_ID,
            ),
            title=parse_required_text(
                row.get(schema.TITLE),
                field_name=schema.TITLE,
            ),
            description=parse_required_text(
                row.get(schema.DESCRIPTION),
                field_name=schema.DESCRIPTION,
            ),
            assigned_role=parse_optional_text(
                row.get(schema.ASSIGNED_ROLE),
                field_name=schema.ASSIGNED_ROLE,
            ),
            frequency=parse_optional_text(
                row.get(schema.FREQUENCY),
                field_name=schema.FREQUENCY,
            ),
            preferred_time_of_day=parse_optional_text(
                row.get(schema.PREFERRED_TIME_OF_DAY),
                field_name=schema.PREFERRED_TIME_OF_DAY,
            ),
            active=parse_optional_text(
                row.get(schema.ACTIVE),
                field_name=schema.ACTIVE,
            ),
        )


    @staticmethod
    def to_row(
        care_plan_task: CarePlanTask,
    ) -> RawRow:
        schema = CarePlanTaskColumns

        return {

            schema.TASK_ID:
                care_plan_task.task_id,

            schema.CARE_PLAN_ID:
                care_plan_task.care_plan_id,

            schema.RELATED_GOAL_ID:
                care_plan_task.related_goal_id,

            schema.TITLE:
                care_plan_task.title,

            schema.DESCRIPTION:
                care_plan_task.card_text,

            schema.ASSIGNED_ROLE:
                care_plan_task.assigned_role,

            schema.FREQUENCY:
                care_plan_task.frequency,

            schema.PREFERRED_TIME_OF_DAY:
                care_plan_task.preferred_time_of_day,

            schema.ACTIVE:
                care_plan_task.active,

        }