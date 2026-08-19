# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.communication_attachment_columns import CommunicationAttachmentColumns

from src.domain.entities.entities import CommunicationAttachment

from src.infrastructure.persistence.common.utils_parsing import *


class CommunicationAttachmentRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> CommunicationAttachment:
        schema = CommunicationAttachmentColumns

        return CommunicationAttachment(
            attachment_id=parse_required_text(
                row.get(schema.ATTACHMENT_ID),
                field_name=schema.ATTACHMENT_ID,
            ),
            communication_id=parse_required_text(
                row.get(schema.COMMUNICATION_ID),
                field_name=schema.COMMUNICATION_ID,
            ),
            file_name=parse_required_text(
                row.get(schema.FILE_NAME),
                field_name=schema.FILE_NAME,
            ),
            content_type=parse_required_text(
                row.get(schema.CONTENT_TYPE),
                field_name=schema.CONTENT_TYPE,
            ),
            storage_reference=parse_required_text(
                row.get(schema.STORAGE_REFERENCE),
                field_name=schema.STORAGE_REFERENCE,
            ),
            uploaded_at=parse_required_datetime(
                row.get(schema.UPLOADED_AT),
                field_name=schema.UPLOADED_AT,
            ),
        )


    @staticmethod
    def to_row(
        communication_attachment: CommunicationAttachment,
    ) -> RawRow:
        schema = CommunicationAttachmentColumns

        return {

            schema.ATTACHMENT_ID:
                communication_attachment.attachment_id,

            schema.COMMUNICATION_ID:
                communication_attachment.communication_id,

            schema.FILE_NAME:
                communication_attachment.file_name,

            schema.CONTENT_TYPE:
                communication_attachment.content_type,

            schema.STORAGE_REFERENCE:
                communication_attachment.storage_reference,

            schema.UPLOADED_AT:
                communication_attachment.uploaded_at.isoformat(),

        }