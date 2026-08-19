# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.clinical_note_reference_columns import ClinicalNoteReferenceColumns

from src.domain.entities.entities import ClinicalNoteReference

from src.infrastructure.persistence.common.utils_parsing import *


class ClinicalNoteReferenceRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> ClinicalNoteReference:
        schema = ClinicalNoteReferenceColumns

        return ClinicalNoteReference(
            reference_id=parse_required_text(
                row.get(schema.REFERENCE_ID),
                field_name=schema.REFERENCE_ID,
            ),
            clinical_note_id=parse_required_text(
                row.get(schema.CLINICAL_NOTE_ID),
                field_name=schema.CLINICAL_NOTE_ID,
            ),
            source_type=parse_optional_text(
                row.get(schema.SOURCE_TYPE),
                field_name=schema.SOURCE_TYPE,
            ),
            source_record_id=parse_required_text(
                row.get(schema.SOURCE_RECORD_ID),
                field_name=schema.SOURCE_RECORD_ID,
            ),
        )


    @staticmethod
    def to_row(
        clinical_note_reference: ClinicalNoteReference,
    ) -> RawRow:
        schema = ClinicalNoteReferenceColumns

        return {

            schema.REFERENCE_ID:
                clinical_note_reference.reference_id,

            schema.CLINICAL_NOTE_ID:
                clinical_note_reference.clinical_note_id,

            schema.SOURCE_TYPE:
                clinical_note_reference.source_type,

            schema.SOURCE_RECORD_ID:
                clinical_note_reference.source_record_id,

        }