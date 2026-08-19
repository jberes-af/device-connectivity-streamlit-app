# /src/infrastructure/persistence/schemas

class ClinicalCommunicationDecisionColumns:
    COMMUNICATION_DECISION_ID: str = "communication_decision_id"
    COMMUNICATION_ID: str = "communication_id"
    DECISION_TYPE: str = "decision_type"
    RATIONALE: str = "rationale"
    FOLLOW_UP_DUE_AT: str = "follow_up_due_at"
    RESPONSIBLE_PROVIDER_ID: str = "responsible_provider_id"
    COMPLETED: str = "completed"
    ORDER = (
COMMUNICATION_DECISION_ID,
COMMUNICATION_ID,
DECISION_TYPE,
RATIONALE,
FOLLOW_UP_DUE_AT,
RESPONSIBLE_PROVIDER_ID,
COMPLETED,
)