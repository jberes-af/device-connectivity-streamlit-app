# /src/infrastructure/persistence/schemas

class CommunicationAttachmentColumns:
    ATTACHMENT_ID: str = "attachment_id"
    COMMUNICATION_ID: str = "communication_id"
    FILE_NAME: str = "file_name"
    CONTENT_TYPE: str = "content_type"
    STORAGE_REFERENCE: str = "storage_reference"
    UPLOADED_AT: str = "uploaded_at"
    ORDER = (
ATTACHMENT_ID,
COMMUNICATION_ID,
FILE_NAME,
CONTENT_TYPE,
STORAGE_REFERENCE,
UPLOADED_AT,
)