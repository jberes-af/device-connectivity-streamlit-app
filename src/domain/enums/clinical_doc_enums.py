# /src/domain/entities/clinical_doc_enums.py


from enum import StrEnum


class ClinicalNoteStatus(StrEnum):
    DRAFT = "draft"
    READY_FOR_REVIEW = "ready_for_review"
    VALIDATION_FAILED = "validation_failed"
    READY_FOR_SIGNATURE = "ready_for_signature"
    SIGNED = "signed"
    LOCKED = "locked"
    VOIDED = "voided"


class ClinicalNoteType(StrEnum):
    MONTHLY_RTM = "monthly_rtm"
    PROGRESS_NOTE = "progress_note"
    ADDENDUM = "addendum"
    CORRECTION = "correction"


class NoteSectionType(StrEnum):
    PATIENT_IDENTIFICATION = "patient_identification"
    DIAGNOSIS = "diagnosis"
    MEDICAL_NECESSITY = "medical_necessity"
    ACTIVE_TREATMENT = "active_treatment"
    THERAPEUTIC_GOALS = "therapeutic_goals"
    MONITORING_PERIOD = "monitoring_period"
    DEVICE_INFORMATION = "device_information"
    DATA_REVIEWED = "data_reviewed"
    CLINICAL_FINDINGS = "clinical_findings"
    CLINICAL_INTERPRETATION = "clinical_interpretation"
    INTERACTIVE_COMMUNICATION = "interactive_communication"
    TREATMENT_DECISIONS = "treatment_decisions"
    ASSESSMENT = "assessment"
    PLAN = "plan"
    MANAGEMENT_TIME = "management_time"
    PROVIDER_ATTESTATION = "provider_attestation"


class ContentOrigin(StrEnum):
    SYSTEM_GENERATED = "system_generated"
    PROVIDER_ENTERED = "provider_entered"
    SYSTEM_GENERATED_PROVIDER_EDITED = (
        "system_generated_provider_edited"
    )
    IMPORTED = "imported"



class SourceRecordType(StrEnum):
    PATIENT = "patient"
    RTM_ENROLLMENT = "rtm_enrollment"
    TREATMENT_PLAN = "treatment_plan"
    THERAPEUTIC_GOAL = "therapeutic_goal"
    MONITORING_PERIOD = "monitoring_period"
    ACTIVITY_SUMMARY = "activity_summary"
    CLINICAL_ALERT = "clinical_alert"
    PROVIDER_REVIEW = "provider_review"
    CLINICAL_FINDING = "clinical_finding"
    COMMUNICATION = "communication"
    TIME_ENTRY = "time_entry"
    DEVICE_ASSIGNMENT = "device_assignment"


class ValidationSeverity(StrEnum):
    ERROR = "error"
    WARNING = "warning"
    INFORMATION = "information"


class ValidationStatus(StrEnum):
    PASSED = "passed"
    FAILED = "failed"
    NOT_APPLICABLE = "not_applicable"
    OVERRIDDEN = "overridden"


class SignatureType(StrEnum):
    ELECTRONIC = "electronic"
    DIGITAL_CERTIFICATE = "digital_certificate"
    IMPORTED = "imported"


class ExportType(StrEnum):
    PDF = "pdf"
    EHR = "ehr"
    FHIR = "fhir"
    HL7 = "hl7"
    MANUAL_DOWNLOAD = "manual_download"


class ExportStatus(StrEnum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

