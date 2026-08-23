# /src/infrastructure/persistence/schemas

class TreatmentInterventionColumns:
    INTERVENTION_ID: str = "intervention_id"
    TREATMENT_PLAN_ID: str = "treatment_plan_id"
    TREATMENT_TYPE: str = "treatment_type"
    DESCRIPTION: str = "description"
    START_DATE: str = "start_date"
    END_DATE: str = "end_date"
    STATUS: str = "status"
    ORDER = (
INTERVENTION_ID,
TREATMENT_PLAN_ID,
TREATMENT_TYPE,
DESCRIPTION,
START_DATE,
END_DATE,
STATUS,
)