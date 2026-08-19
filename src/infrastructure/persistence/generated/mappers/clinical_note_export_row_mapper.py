# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.clinical_note_export_columns import ClinicalNoteExportColumns

from src.domain.entities.entities import ClinicalNoteExport

from src.infrastructure.persistence.common.utils_parsing import *


class ClinicalNoteExportRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> ClinicalNoteExport:
        schema = ClinicalNoteExportColumns

        return ClinicalNoteExport(
            export_id=parse_required_text(
                row.get(schema.EXPORT_ID),
                field_name=schema.EXPORT_ID,
            ),
            clinical_note_id=parse_required_text(
                row.get(schema.CLINICAL_NOTE_ID),
                field_name=schema.CLINICAL_NOTE_ID,
            ),
            export_type=parse_optional_text(
                row.get(schema.EXPORT_TYPE),
                field_name=schema.EXPORT_TYPE,
            ),
            status=parse_optional_text(
                row.get(schema.STATUS),
                field_name=schema.STATUS,
            ),
            destination=parse_optional_text(
                row.get(schema.DESTINATION),
                field_name=schema.DESTINATION,
            ),
            file_reference=parse_optional_text(
                row.get(schema.FILE_REFERENCE),
                field_name=schema.FILE_REFERENCE,
            ),
            requested_by_user_id=parse_required_text(
                row.get(schema.REQUESTED_BY_USER_ID),
                field_name=schema.REQUESTED_BY_USER_ID,
            ),
            requested_at=parse_required_datetime(
                row.get(schema.REQUESTED_AT),
                field_name=schema.REQUESTED_AT,
            ),
            completed_at=parse_optional_datetime(
                row.get(schema.COMPLETED_AT),
                field_name=schema.COMPLETED_AT,
            ),
            failure_reason=parse_optional_text(
                row.get(schema.FAILURE_REASON),
                field_name=schema.FAILURE_REASON,
            ),
        )


    @staticmethod
    def to_row(
        clinical_note_export: ClinicalNoteExport,
    ) -> RawRow:
        schema = ClinicalNoteExportColumns

        return {

            schema.EXPORT_ID:
                clinical_note_export.export_id,

            schema.CLINICAL_NOTE_ID:
                clinical_note_export.clinical_note_id,

            schema.EXPORT_TYPE:
                clinical_note_export.export_type,

            schema.STATUS:
                clinical_note_export.status,

            schema.DESTINATION:
                clinical_note_export.destination,

            schema.FILE_REFERENCE:
                clinical_note_export.file_reference,

            schema.REQUESTED_BY_USER_ID:
                clinical_note_export.requested_by_user_id,

            schema.REQUESTED_AT:
                clinical_note_export.requested_at.isoformat(),

            schema.COMPLETED_AT:
                clinical_note_export.completed_at.isoformat(),

            schema.FAILURE_REASON:
                clinical_note_export.failure_reason,

        }