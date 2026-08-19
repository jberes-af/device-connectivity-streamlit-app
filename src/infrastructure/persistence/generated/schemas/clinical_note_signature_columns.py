# /src/infrastructure/persistence/schemas

class ClinicalNoteSignatureColumns:
    SIGNATURE_ID: str = "signature_id"
    CLINICAL_NOTE_ID: str = "clinical_note_id"
    PROVIDER_ID: str = "provider_id"
    SIGNATURE_TYPE: str = "signature_type"
    SIGNED_AT: str = "signed_at"
    ORDER = (
SIGNATURE_ID,
CLINICAL_NOTE_ID,
PROVIDER_ID,
SIGNATURE_TYPE,
SIGNED_AT,
)