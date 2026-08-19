# /src/infrastructure/persistence/schemas

class ClinicalNoteExportColumns:
    EXPORT_ID: str = "export_id"
    CLINICAL_NOTE_ID: str = "clinical_note_id"
    EXPORT_TYPE: str = "export_type"
    STATUS: str = "status"
    DESTINATION: str = "destination"
    FILE_REFERENCE: str = "file_reference"
    REQUESTED_BY_USER_ID: str = "requested_by_user_id"
    REQUESTED_AT: str = "requested_at"
    COMPLETED_AT: str = "completed_at"
    FAILURE_REASON: str = "failure_reason"
    ORDER = (
EXPORT_ID,
CLINICAL_NOTE_ID,
EXPORT_TYPE,
STATUS,
DESTINATION,
FILE_REFERENCE,
REQUESTED_BY_USER_ID,
REQUESTED_AT,
COMPLETED_AT,
FAILURE_REASON,
)