# /src/infrastructure/persistence/schemas

class CarePlanTaskColumns:
    TASK_ID: str = "task_id"
    CARE_PLAN_ID: str = "care_plan_id"
    RELATED_GOAL_ID: str = "related_goal_id"
    TITLE: str = "title"
    DESCRIPTION: str = "description"
    ASSIGNED_ROLE: str = "assigned_role"
    FREQUENCY: str = "frequency"
    PREFERRED_TIME_OF_DAY: str = "preferred_time_of_day"
    ACTIVE: str = "active"
    ORDER = (
TASK_ID,
CARE_PLAN_ID,
RELATED_GOAL_ID,
TITLE,
DESCRIPTION,
ASSIGNED_ROLE,
FREQUENCY,
PREFERRED_TIME_OF_DAY,
ACTIVE,
)