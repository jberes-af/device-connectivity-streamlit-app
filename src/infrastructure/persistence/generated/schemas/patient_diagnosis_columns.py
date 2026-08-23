# /src/infrastructure/persistence/schemas

class PatientDiagnosisColumns:
    PATIENT_DIAGNOSIS_ID: str = "patient_diagnosis_id"
    PATIENT_ID: str = "patient_id"
    DIAGNOSIS_ID: str = "diagnosis_id"
    DIAGNOSED_DATE: str = "diagnosed_date"
    RESOLVED_DATE: str = "resolved_date"
    IS_PRIMARY: str = "is_primary"
    ORDER = (
PATIENT_DIAGNOSIS_ID,
PATIENT_ID,
DIAGNOSIS_ID,
DIAGNOSED_DATE,
RESOLVED_DATE,
IS_PRIMARY,
)