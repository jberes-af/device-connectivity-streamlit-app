# /src/domain/enums/rtm_enums.py

from enum import StrEnum


class ClinicalIndicationEnum(StrEnum):
    FUNCTIONAL_LIMITATION = "functional_limitation"
    PAIN = "pain"
    MOBILITY_IMPAIRMENT = "mobility_impairment"
    THERAPY_ADHERENCE = "therapy_adherence"
    POSTOPERATIVE_REHABILITATION = "postoperative_rehabilitation"
    THERAPEUTIC_RESPONSE = "therapeutic_response"
    OTHER = "other"


class RtmMonitoringReasonEnum(StrEnum):
    THERAPY_ADHERENCE = "therapy_adherence"
    THERAPY_RESPONSE = "therapy_response"
    DEVICE_UTILIZATION = "device_utilization"
    FUNCTIONAL_STATUS = "functional_status"
    SYMPTOM_RESPONSE = "symptom_response"
    OTHER = "other"


class RtmClinicalUseEnum(StrEnum):
    EVALUATE_ADHERENCE = "evaluate_adherence"
    EVALUATE_RESPONSE = "evaluate_response"
    MODIFY_TREATMENT = "modify_treatment"
    MODIFY_EXERCISE_PROGRAM = "modify_exercise_program"
    ADJUST_DEVICE_USE = "adjust_device_use"
    PATIENT_EDUCATION = "patient_education"
    CAREGIVER_EDUCATION = "caregiver_education"
    DETERMINE_FOLLOW_UP = "determine_follow_up"
    OTHER = "other"


class RtmMedicalNecessityStatus(StrEnum):
    DRAFT = "draft"
    ACTIVE = "active"
    SUPERSEDED = "superseded"
    ENDED = "ended"


class RtmActivityType(StrEnum):
    DATA_REVIEW = "data_review"
    CLINICAL_ASSESSMENT = "clinical_assessment"
    TREATMENT_ADJUSTMENT = "treatment_adjustment"
    PATIENT_EDUCATION = "patient_education"
    CAREGIVER_EDUCATION = "caregiver_education"
    CLINICAL_DOCUMENTATION = "clinical_documentation"
    INTERACTIVE_COMMUNICATION = "interactive_communication"
    OTHER = "other"


class ParticipantType(StrEnum):
    PATIENT = "patient"
    CAREGIVER = "caregiver"
    OTHER = "other"


class CommunicationMethod(StrEnum):
    PHONE = "phone"
    AUDIO_VIDEO = "audio_video"
    IN_PERSON = "in_person"
    OTHER = "other"


class DataReviewedType(StrEnum):
    THERAPEUTIC_MEASURE = "therapeutic_measure"
    SENSOR_ACTIVITY = "sensor_activity"
    ADL_ASSESSMENT = "adl_assessment"
    PATIENT_REPORTED = "patient_reported"
    CAREGIVER_REPORTED = "caregiver_reported"
    TREATMENT_PLAN = "treatment_plan"
    OTHER = "other"
