# /src/domain/entities/communication_enums.py

from enum import StrEnum


class CommunicationMethod(StrEnum):
    TELEPHONE = "telephone"
    VIDEO = "video"
    PATIENT_PORTAL = "patient_portal"
    IN_PERSON = "in_person"
    OTHER_INTERACTIVE = "other_interactive"


class CommunicationStatus(StrEnum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    UNSUCCESSFUL = "unsuccessful"
    CANCELLED = "cancelled"


class CommunicationType(StrEnum):
    INTERACTIVE_CLINICAL = "interactive_clinical"
    INTERNAL_STAFF_NOTE = "internal_staff_note"
    OUTREACH_ATTEMPT = "outreach_attempt"
    CARE_COORDINATION = "care_coordination"


class ParticipantRole(StrEnum):
    PROVIDER = "provider"
    CLINICAL_STAFF = "clinical_staff"
    PATIENT = "treatment"
    CAREGIVER = "caregiver"
    THERAPIST = "therapist"
    OTHER = "other"


class CommunicationTopic(StrEnum):
    ACTIVITY_TRENDS = "activity_trends"
    MOBILITY = "mobility"
    TRANSFERS = "transfers"
    BED_ACTIVITY = "bed_activity"
    CHAIR_ACTIVITY = "chair_activity"
    NIGHTTIME_ACTIVITY = "nighttime_activity"
    ROUTINE_ADHERENCE = "routine_adherence"
    SYMPTOMS = "symptoms"
    TREATMENT_ADHERENCE = "treatment_adherence"
    TREATMENT_PROGRESS = "treatment_progress"
    OTHER = "other"


class MonitoringDataType(StrEnum):
    ACTIVITY_TREND = "activity_trend"
    MOBILITY = "mobility"
    TRANSFERS = "transfers"
    BED_OCCUPANCY = "bed_occupancy"
    CHAIR_OCCUPANCY = "chair_occupancy"
    BATHROOM_VISITS = "bathroom_visits"
    NIGHTTIME_ACTIVITY = "nighttime_activity"
    ROUTINE_ADHERENCE = "routine_adherence"
    OTHER = "other"


class CommunicationDecisionType(StrEnum):
    CONTINUE_TREATMENT = "continue_treatment"
    MODIFY_TREATMENT = "modify_treatment"
    SCHEDULE_FOLLOW_UP = "schedule_follow_up"
    CONTACT_PROVIDER = "contact_provider"
    CONTACT_THERAPIST = "contact_therapist"
    ORDER_EVALUATION = "order_evaluation"
    CONTINUE_RTM = "continue_rtm"
    DISCONTINUE_RTM = "discontinue_rtm"
    NO_CHANGE = "no_change"
    OTHER = "other"
