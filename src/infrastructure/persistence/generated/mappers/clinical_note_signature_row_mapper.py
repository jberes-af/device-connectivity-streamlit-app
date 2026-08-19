# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.clinical_note_signature_columns import ClinicalNoteSignatureColumns

from src.domain.entities.entities import ClinicalNoteSignature

from src.infrastructure.persistence.common.utils_parsing import *


class ClinicalNoteSignatureRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> ClinicalNoteSignature:
        schema = ClinicalNoteSignatureColumns

        return ClinicalNoteSignature(
            signature_id=parse_required_text(
                row.get(schema.SIGNATURE_ID),
                field_name=schema.SIGNATURE_ID,
            ),
            clinical_note_id=parse_required_text(
                row.get(schema.CLINICAL_NOTE_ID),
                field_name=schema.CLINICAL_NOTE_ID,
            ),
            provider_id=parse_required_text(
                row.get(schema.PROVIDER_ID),
                field_name=schema.PROVIDER_ID,
            ),
            signature_type=parse_optional_text(
                row.get(schema.SIGNATURE_TYPE),
                field_name=schema.SIGNATURE_TYPE,
            ),
            signed_at=parse_required_datetime(
                row.get(schema.SIGNED_AT),
                field_name=schema.SIGNED_AT,
            ),
        )


    @staticmethod
    def to_row(
        clinical_note_signature: ClinicalNoteSignature,
    ) -> RawRow:
        schema = ClinicalNoteSignatureColumns

        return {

            schema.SIGNATURE_ID:
                clinical_note_signature.signature_id,

            schema.CLINICAL_NOTE_ID:
                clinical_note_signature.clinical_note_id,

            schema.PROVIDER_ID:
                clinical_note_signature.provider_id,

            schema.SIGNATURE_TYPE:
                clinical_note_signature.signature_type,

            schema.SIGNED_AT:
                clinical_note_signature.signed_at.isoformat(),

        }