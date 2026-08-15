# /src/infrastructure/persistence/schemas

class CarePlanGoalColumns:
    GOAL_ID: str = "goal_id"
    CARE_PLAN_ID: str = "care_plan_id"
    TITLE: str = "title"
    DESCRIPTION: str = "description"
    PRIORITY: str = "priority"
    TARGET_DATE: str = "target_date"
    STATUS: str = "status"
    SUCCESS_CRITERIA: str = "success_criteria"
    ORDER = (
GOAL_ID,
CARE_PLAN_ID,
TITLE,
DESCRIPTION,
PRIORITY,
TARGET_DATE,
STATUS,
SUCCESS_CRITERIA,
)