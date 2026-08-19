# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.clinical_note_columns import ClinicalNoteColumns

from src.domain.entities.entities import ClinicalNote

from src.infrastructure.persistence.common.utils_parsing import *


class ClinicalNoteRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> ClinicalNote:
        schema = ClinicalNoteColumns

        return ClinicalNote(
            clinical_note_id=parse_required_text(
                row.get(schema.CLINICAL_NOTE_ID),
                field_name=schema.CLINICAL_NOTE_ID,
            ),
            patient_id=parse_required_text(
                row.get(schema.PATIENT_ID),
                field_name=schema.PATIENT_ID,
            ),
            treatment_plan_id=parse_optional_text(
                row.get(schema.TREATMENT_PLAN_ID),
                field_name=schema.TREATMENT_PLAN_ID,
            ),
            measurement_period_id=parse_optional_text(
                row.get(schema.MEASUREMENT_PERIOD_ID),
                field_name=schema.MEASUREMENT_PERIOD_ID,
            ),
            author_provider_id=parse_required_text(
                row.get(schema.AUTHOR_PROVIDER_ID),
                field_name=schema.AUTHOR_PROVIDER_ID,
            ),
            note_type=parse_optional_text(
                row.get(schema.NOTE_TYPE),
                field_name=schema.NOTE_TYPE,
            ),
            status=parse_optional_text(
                row.get(schema.STATUS),
                field_name=schema.STATUS,
            ),
            created_at=parse_required_datetime(
                row.get(schema.CREATED_AT),
                field_name=schema.CREATED_AT,
            ),
            updated_at=parse_required_datetime(
                row.get(schema.UPDATED_AT),
                field_name=schema.UPDATED_AT,
            ),
        )


    @staticmethod
    def to_row(
        clinical_note: ClinicalNote,
    ) -> RawRow:
        schema = ClinicalNoteColumns

        return {

            schema.CLINICAL_NOTE_ID:
                clinical_note.clinical_note_id,

            schema.PATIENT_ID:
                clinical_note.patient_id,

            schema.TREATMENT_PLAN_ID:
                clinical_note.treatment_plan_id,

            schema.MEASUREMENT_PERIOD_ID:
                clinical_note.measurement_period_id,

            schema.AUTHOR_PROVIDER_ID:
                clinical_note.author_provider_id,

            schema.NOTE_TYPE:
                clinical_note.note_type,

            schema.STATUS:
                clinical_note.status,

            schema.CREATED_AT:
                clinical_note.created_at.isoformat(),

            schema.UPDATED_AT:
                clinical_note.updated_at.isoformat(),

        }