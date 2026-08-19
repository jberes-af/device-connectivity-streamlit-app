# /src/infrastructure/persistence/schemas

class ClinicalNoteAmendmentColumns:
    AMENDMENT_ID: str = "amendment_id"
    CLINICAL_NOTE_ID: str = "clinical_note_id"
    AMENDED_AT: str = "amended_at"
    AMENDED_BY_PROVIDER_ID: str = "amended_by_provider_id"
    REASON: str = "reason"
    ORDER = (
AMENDMENT_ID,
CLINICAL_NOTE_ID,
AMENDED_AT,
AMENDED_BY_PROVIDER_ID,
REASON,
)