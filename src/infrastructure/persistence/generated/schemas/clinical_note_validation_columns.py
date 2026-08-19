# /src/infrastructure/persistence/schemas

class ClinicalNoteValidationColumns:
    VALIDATION_ID: str = "validation_id"
    CLINICAL_NOTE_ID: str = "clinical_note_id"
    SEVERITY: str = "severity"
    STATUS: str = "status"
    MESSAGE: str = "message"
    ORDER = (
VALIDATION_ID,
CLINICAL_NOTE_ID,
SEVERITY,
STATUS,
MESSAGE,
)