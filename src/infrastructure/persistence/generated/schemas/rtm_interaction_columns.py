# /src/infrastructure/persistence/schemas

class RtmInteractionColumns:
    INTERACTION_ID: str = "interaction_id"
    ACTIVITY_ID: str = "activity_id"
    PARTICIPANT_TYPE: str = "participant_type"
    PARTICIPANT_ID: str = "participant_id"
    COMMUNICATION_METHOD: str = "communication_method"
    IS_REAL_TIME: str = "is_real_time"
    OCCURRED_AT: str = "occurred_at"
    DURATION_MINUTES: str = "duration_minutes"
    SUMMARY: str = "summary"
    ORDER = (
INTERACTION_ID,
ACTIVITY_ID,
PARTICIPANT_TYPE,
PARTICIPANT_ID,
COMMUNICATION_METHOD,
IS_REAL_TIME,
OCCURRED_AT,
DURATION_MINUTES,
SUMMARY,
)