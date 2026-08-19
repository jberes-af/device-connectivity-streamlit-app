# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.clinical_note_validation_columns import ClinicalNoteValidationColumns

from src.domain.entities.entities import ClinicalNoteValidation

from src.infrastructure.persistence.common.utils_parsing import *


class ClinicalNoteValidationRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> ClinicalNoteValidation:
        schema = ClinicalNoteValidationColumns

        return ClinicalNoteValidation(
            validation_id=parse_required_text(
                row.get(schema.VALIDATION_ID),
                field_name=schema.VALIDATION_ID,
            ),
            clinical_note_id=parse_required_text(
                row.get(schema.CLINICAL_NOTE_ID),
                field_name=schema.CLINICAL_NOTE_ID,
            ),
            severity=parse_optional_text(
                row.get(schema.SEVERITY),
                field_name=schema.SEVERITY,
            ),
            status=parse_optional_text(
                row.get(schema.STATUS),
                field_name=schema.STATUS,
            ),
            message=parse_required_text(
                row.get(schema.MESSAGE),
                field_name=schema.MESSAGE,
            ),
        )


    @staticmethod
    def to_row(
        clinical_note_validation: ClinicalNoteValidation,
    ) -> RawRow:
        schema = ClinicalNoteValidationColumns

        return {

            schema.VALIDATION_ID:
                clinical_note_validation.validation_id,

            schema.CLINICAL_NOTE_ID:
                clinical_note_validation.clinical_note_id,

            schema.SEVERITY:
                clinical_note_validation.severity,

            schema.STATUS:
                clinical_note_validation.status,

            schema.MESSAGE:
                clinical_note_validation.message,

        }