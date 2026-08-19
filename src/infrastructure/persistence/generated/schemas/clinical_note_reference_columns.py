# /src/infrastructure/persistence/schemas

class ClinicalNoteReferenceColumns:
    REFERENCE_ID: str = "reference_id"
    CLINICAL_NOTE_ID: str = "clinical_note_id"
    SOURCE_TYPE: str = "source_type"
    SOURCE_RECORD_ID: str = "source_record_id"
    ORDER = (
REFERENCE_ID,
CLINICAL_NOTE_ID,
SOURCE_TYPE,
SOURCE_RECORD_ID,
)