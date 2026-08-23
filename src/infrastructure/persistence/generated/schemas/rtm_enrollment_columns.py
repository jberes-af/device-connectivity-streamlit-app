# /src/infrastructure/persistence/schemas

class RtmEnrollmentColumns:
    ENROLLMENT_ID: str = "enrollment_id"
    PATIENT_ID: str = "patient_id"
    ENROLLMENT_STATUS: str = "enrollment_status"
    ENROLLMENT_DATE: str = "enrollment_date"
    SERVICE_START_DATE: str = "service_start_date"
    SERVICE_END_DATE: str = "service_end_date"
    CONSENT_STATUS: str = "consent_status"
    CONSENT_OBTAINED_AT: str = "consent_obtained_at"
    CONSENT_METHOD: str = "consent_method"
    CONSENT_DOCUMENT_REFERENCE: str = "consent_document_reference"
    DISCONTINUATION_REASON: str = "discontinuation_reason"
    ORDER = (
ENROLLMENT_ID,
PATIENT_ID,
ENROLLMENT_STATUS,
ENROLLMENT_DATE,
SERVICE_START_DATE,
SERVICE_END_DATE,
CONSENT_STATUS,
CONSENT_OBTAINED_AT,
CONSENT_METHOD,
CONSENT_DOCUMENT_REFERENCE,
DISCONTINUATION_REASON,
)