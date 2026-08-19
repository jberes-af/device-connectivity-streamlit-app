# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.clinical_note_amendment_columns import ClinicalNoteAmendmentColumns

from src.domain.entities.entities import ClinicalNoteAmendment

from src.infrastructure.persistence.common.utils_parsing import *


class ClinicalNoteAmendmentRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> ClinicalNoteAmendment:
        schema = ClinicalNoteAmendmentColumns

        return ClinicalNoteAmendment(
            amendment_id=parse_required_text(
                row.get(schema.AMENDMENT_ID),
                field_name=schema.AMENDMENT_ID,
            ),
            clinical_note_id=parse_required_text(
                row.get(schema.CLINICAL_NOTE_ID),
                field_name=schema.CLINICAL_NOTE_ID,
            ),
            amended_at=parse_required_datetime(
                row.get(schema.AMENDED_AT),
                field_name=schema.AMENDED_AT,
            ),
            amended_by_provider_id=parse_required_text(
                row.get(schema.AMENDED_BY_PROVIDER_ID),
                field_name=schema.AMENDED_BY_PROVIDER_ID,
            ),
            reason=parse_required_text(
                row.get(schema.REASON),
                field_name=schema.REASON,
            ),
        )


    @staticmethod
    def to_row(
        clinical_note_amendment: ClinicalNoteAmendment,
    ) -> RawRow:
        schema = ClinicalNoteAmendmentColumns

        return {

            schema.AMENDMENT_ID:
                clinical_note_amendment.amendment_id,

            schema.CLINICAL_NOTE_ID:
                clinical_note_amendment.clinical_note_id,

            schema.AMENDED_AT:
                clinical_note_amendment.amended_at.isoformat(),

            schema.AMENDED_BY_PROVIDER_ID:
                clinical_note_amendment.amended_by_provider_id,

            schema.REASON:
                clinical_note_amendment.reason,

        }