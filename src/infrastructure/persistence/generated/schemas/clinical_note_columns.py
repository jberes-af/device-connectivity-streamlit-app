# /src/infrastructure/persistence/schemas

class ClinicalNoteColumns:
    CLINICAL_NOTE_ID: str = "clinical_note_id"
    PATIENT_ID: str = "patient_id"
    TREATMENT_PLAN_ID: str = "treatment_plan_id"
    MEASUREMENT_PERIOD_ID: str = "measurement_period_id"
    AUTHOR_PROVIDER_ID: str = "author_provider_id"
    NOTE_TYPE: str = "note_type"
    STATUS: str = "status"
    CREATED_AT: str = "created_at"
    UPDATED_AT: str = "updated_at"
    ORDER = (
CLINICAL_NOTE_ID,
PATIENT_ID,
TREATMENT_PLAN_ID,
MEASUREMENT_PERIOD_ID,
AUTHOR_PROVIDER_ID,
NOTE_TYPE,
STATUS,
CREATED_AT,
UPDATED_AT,
)