# /src/infrastructure/persistence/schemas

class FunctionalStatusColumns:
    FUNCTIONAL_STATUS_ID: str = "functional_status_id"
    PATIENT_ID: str = "patient_id"
    ASSESSMENT_DATE: str = "assessment_date"
    ASSESSED_BY_USER_ID: str = "assessed_by_user_id"
    MOBILITY: str = "mobility"
    TRANSFERS: str = "transfers"
    BATHING: str = "bathing"
    DRESSING: str = "dressing"
    TOILETING: str = "toileting"
    EATING: str = "eating"
    CONTINENCE: str = "continence"
    COGNITION: str = "cognition"
    FALL_RISK: str = "fall_risk"
    NOTES: str = "notes"
    ORDER = (
FUNCTIONAL_STATUS_ID,
PATIENT_ID,
ASSESSMENT_DATE,
ASSESSED_BY_USER_ID,
MOBILITY,
TRANSFERS,
BATHING,
DRESSING,
TOILETING,
EATING,
CONTINENCE,
COGNITION,
FALL_RISK,
NOTES,
)