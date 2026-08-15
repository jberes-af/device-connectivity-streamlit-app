# /src/infrastructure/persistence/schemas

class CarePlanInstructionColumns:
    INSTRUCTION_ID: str = "instruction_id"
    CARE_PLAN_ID: str = "care_plan_id"
    CATEGORY: str = "category"
    TITLE: str = "title"
    INSTRUCTION: str = "instruction"
    APPLIES_TO_GOAL_ID: str = "applies_to_goal_id"
    ACTIVE: str = "active"
    ORDER = (
INSTRUCTION_ID,
CARE_PLAN_ID,
CATEGORY,
TITLE,
INSTRUCTION,
APPLIES_TO_GOAL_ID,
ACTIVE,
)