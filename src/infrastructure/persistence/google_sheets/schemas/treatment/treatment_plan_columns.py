# /src/infrastructure/persistence/google_sheets/schemas/treatment/treatment_plan_columns.py

class TreatmentPlanColumns:
    TREATMENT_PLAN_ID: str = "treatment_plan_id"
    RTM_PROGRAM_ID: str = "rtm_program_id"
    PATIENT_ID: str = "patient_id"
    TREATING_PROVIDER_ID: str = "treating_provider_id"
    START_DATE: str = "start_date"
    EXPECTED_END_DATE: str = "expected_end_date"
    STATUS: str = "status"
    CREATED_AT: str = "created_at"
    UPDATED_AT: str = "updated_at"
    ORDER = (
        TREATMENT_PLAN_ID,
        RTM_PROGRAM_ID,
        PATIENT_ID,
        TREATING_PROVIDER_ID,
        START_DATE,
        EXPECTED_END_DATE,
        STATUS,
        CREATED_AT,
        UPDATED_AT,
    )
