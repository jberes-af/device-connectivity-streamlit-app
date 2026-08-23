# /src/infrastructure/persistence/schemas/diagnosis/diagnosis_definition_columns.py

class DiagnosisDefinitionColumns:
    DIAGNOSIS_ID: str = "diagnosis_id"
    DIAGNOSIS_NAME: str = "diagnosis_name"
    DIAGNOSIS_DESCRIPTION: str = "diagnosis_description"
    ORDER = (
        DIAGNOSIS_ID,
        DIAGNOSIS_NAME,
        DIAGNOSIS_DESCRIPTION,
    )
