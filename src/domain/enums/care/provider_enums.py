# /src/domain/enums/provider_enums.py

from enum import StrEnum


class ReviewStatus(StrEnum):
    DRAFT = "draft"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    SIGNED = "signed"
    LOCKED = "locked"


class DataReviewedType(StrEnum):
    ACTIVITY_TRENDS = "activity_trends"
    MOBILITY = "mobility"
    TRANSFERS = "transfers"
    BED_OCCUPANCY = "bed_occupancy"
    CHAIR_OCCUPANCY = "chair_occupancy"
    BATHROOM_VISITS = "bathroom_visits"
    NIGHTTIME_ACTIVITY = "nighttime_activity"
    ROUTINE_ADHERENCE = "routine_adherence"
    PATIENT_REPORTED_INFORMATION = "patient_reported_information"
    PREVIOUS_CLINICAL_NOTES = "previous_clinical_notes"
    PREVIOUS_COMMUNICATIONS = "previous_communications"


class ClinicalFindingType(StrEnum):
    FUNCTIONAL_DECLINE = "functional_decline"
    FUNCTIONAL_IMPROVEMENT = "functional_improvement"
    ADHERENCE = "adherence"
    SYMPTOM = "symptom"
    OTHER = "other"


class CommunicationMethod(StrEnum):
    TELEPHONE = "telephone"
    VIDEO = "video"
    PATIENT_PORTAL = "patient_portal"
    IN_PERSON = "in_person"
    OTHER = "other"


class TimeCategory(StrEnum):
    REVIEW_MONITORING_DATA = "review_monitoring_data"
    CLINICAL_ANALYSIS = "clinical_analysis"
    INTERACTIVE_COMMUNICATION = "interactive_communication"
    CARE_TEAM_COORDINATION = "care_team_coordination"
    DOCUMENTATION = "documentation"
    OTHER = "other"


class PatientProviderRoleEnum(StrEnum):
    TREATING_PROVIDER = "treating_provider"
    ORDERING_PROVIDER = "ordering_provider"
    SUPERVISING_PROVIDER = "supervising_provider"
    PRIMARY_CARE_PROVIDER = "primary_care_provider"
    REFERRING_PROVIDER = "referring_provider"
    CONSULTING_PROVIDER = "consulting_provider"
    THERAPIST = "therapist"
    OTHER = "other"
