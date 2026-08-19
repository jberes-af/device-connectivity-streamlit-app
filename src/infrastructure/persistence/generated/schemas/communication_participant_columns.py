# /src/infrastructure/persistence/schemas

class CommunicationParticipantColumns:
    COMMUNICATION_PARTICIPANT_ID: str = "communication_participant_id"
    COMMUNICATION_ID: str = "communication_id"
    PARTICIPANT_ROLE: str = "participant_role"
    PARTICIPANT_ID: str = "participant_id"
    PARTICIPANT_NAME: str = "participant_name"
    WAS_PRESENT: str = "was_present"
    ORDER = (
COMMUNICATION_PARTICIPANT_ID,
COMMUNICATION_ID,
PARTICIPANT_ROLE,
PARTICIPANT_ID,
PARTICIPANT_NAME,
WAS_PRESENT,
)