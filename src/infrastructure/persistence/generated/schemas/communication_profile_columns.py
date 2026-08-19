# /src/infrastructure/persistence/schemas

class CommunicationProfileColumns:
    COMMUNICATION_ID: str = "communication_id"
    PATIENT_ID: str = "patient_id"
    OCCURRED_AT: str = "occurred_at"
    METHOD: str = "method"
    COMMUNICATION_TYPE: str = "communication_type"
    STATUS: str = "status"
    INITIATED_BY_TYPE: str = "initiated_by_type"
    INITIATED_BY_ID: str = "initiated_by_id"
    DURATION_MINUTES: str = "duration_minutes"
    SUMMARY: str = "summary"
    CLINICAL_IMPACT: str = "clinical_impact"
    MONITORING_PERIOD_ID: str = "monitoring_period_id"
    PROVIDER_REVIEW_ID: str = "provider_review_id"
    COUNTS_TOWARD_RTM_PERIOD: str = "counts_toward_rtm_period"
    CREATED_BY_USER_ID: str = "created_by_user_id"
    CREATED_AT: str = "created_at"
    ORDER = (
COMMUNICATION_ID,
PATIENT_ID,
OCCURRED_AT,
METHOD,
COMMUNICATION_TYPE,
STATUS,
INITIATED_BY_TYPE,
INITIATED_BY_ID,
DURATION_MINUTES,
SUMMARY,
CLINICAL_IMPACT,
MONITORING_PERIOD_ID,
PROVIDER_REVIEW_ID,
COUNTS_TOWARD_RTM_PERIOD,
CREATED_BY_USER_ID,
CREATED_AT,
)