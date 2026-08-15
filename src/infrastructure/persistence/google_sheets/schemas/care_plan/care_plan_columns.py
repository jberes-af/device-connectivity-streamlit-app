# /src/infrastructure/persistence/schemas

class CarePlanColumns:
    CARE_PLAN_ID: str = "care_plan_id"
    PATIENT_ID: str = "patient_id"
    TITLE: str = "title"
    SUMMARY: str = "summary"
    CREATED_BY_USER_ID: str = "created_by_user_id"
    RESPONSIBLE_COORDINATOR_ID: str = "responsible_coordinator_id"
    START_DATE: str = "start_date"
    TARGET_REVIEW_DATE: str = "target_review_date"
    STATUS: str = "status"
    CREATED_AT: str = "created_at"
    UPDATED_AT: str = "updated_at"
    ORDER = (
CARE_PLAN_ID,
PATIENT_ID,
TITLE,
SUMMARY,
CREATED_BY_USER_ID,
RESPONSIBLE_COORDINATOR_ID,
START_DATE,
TARGET_REVIEW_DATE,
STATUS,
CREATED_AT,
UPDATED_AT,
)