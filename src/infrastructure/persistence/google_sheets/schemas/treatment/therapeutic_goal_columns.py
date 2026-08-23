# /src/infrastructure/persistence/google_sheets/schemas/treatment/therapeutic_plan_columns.py

class TherapeuticGoalColumns:
    GOAL_ID: str = "goal_id"
    TREATMENT_PLAN_ID: str = "treatment_plan_id"
    DESCRIPTION: str = "description"
    TARGET_DATE: str = "target_date"
    ORDER = (
        GOAL_ID,
        TREATMENT_PLAN_ID,
        DESCRIPTION,
        TARGET_DATE,
    )
