# /src/domain/entities/clinical_documentation.py


from dataclasses import dataclass
from datetime import date, datetime
from enum import StrEnum

@dataclass(frozen=True)
class ClinicalNote:

    clinical_note_id: str

    patient_id: str

    treatment_plan_id: str | None

    measurement_period_id: str | None

    author_provider_id: str

    note_type: ClinicalNoteType

    status: ClinicalNoteStatus

    created_at: datetime

    updated_at: datetime



@dataclass(frozen=True)
class ClinicalNoteReference:

    reference_id: str

    clinical_note_id: str

    source_type: SourceRecordType

    source_record_id: str



@dataclass(frozen=True)
class ClinicalNoteValidation:

    validation_id: str

    clinical_note_id: str

    severity: ValidationSeverity

    status: ValidationStatus

    message: str


@dataclass(frozen=True)
class ClinicalNoteSignature:

    signature_id: str

    clinical_note_id: str

    provider_id: str

    signature_type: SignatureType

    signed_at: datetime


@dataclass(frozen=True)
class ClinicalNoteAmendment:

    amendment_id: str

    clinical_note_id: str

    amended_at: datetime

    amended_by_provider_id: str

    reason: str



@dataclass(frozen=True)
class ClinicalNoteExport:
    export_id: str
    clinical_note_id: str

    export_type: ExportType
    status: ExportStatus

    destination: str | None
    file_reference: str | None

    requested_by_user_id: str
    requested_at: datetime
    completed_at: datetime | None

    failure_reason: str | None


