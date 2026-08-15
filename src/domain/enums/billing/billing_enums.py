# /src/domain/entities/billing_enums.py

from enum import StrEnum


class BillingCaseStatus(StrEnum):
    OPEN = "open"
    READY_FOR_SUBMISSION = "ready_for_submission"
    SUBMITTED = "submitted"
    CLOSED = "closed"
    VOIDED = "voided"


class BillingEvidenceType(StrEnum):
    PATIENT_CONSENT = "patient_consent"
    DIAGNOSIS = "diagnosis"
    MEDICAL_NECESSITY = "medical_necessity"
    TREATMENT_PLAN = "treatment_plan"
    DEVICE_SETUP = "device_setup"
    MONITORING_PERIOD = "monitoring_period"
    MONITORING_DATA = "monitoring_data"
    PROVIDER_REVIEW = "provider_review"
    COMMUNICATION = "communication"
    TIME_ENTRY = "time_entry"
    TREATMENT_DECISION = "treatment_decision"
    CLINICAL_NOTE = "clinical_note"
    PROVIDER_SIGNATURE = "provider_signature"
    OTHER = "other"


class BillingRequirementType(StrEnum):
    PATIENT_CONSENT_DOCUMENTED = (
        "patient_consent_documented"
    )
    ELIGIBLE_DIAGNOSIS_DOCUMENTED = (
        "eligible_diagnosis_documented"
    )
    MEDICAL_NECESSITY_DOCUMENTED = (
        "medical_necessity_documented"
    )
    ACTIVE_TREATMENT_PLAN_DOCUMENTED = (
        "active_treatment_plan_documented"
    )
    DEVICE_SETUP_DOCUMENTED = (
        "device_setup_documented"
    )
    REQUIRED_MONITORING_DATA_AVAILABLE = (
        "required_monitoring_data_available"
    )
    MONITORING_DAY_REQUIREMENT_SATISFIED = (
        "monitoring_day_requirement_satisfied"
    )
    PROVIDER_REVIEW_COMPLETED = (
        "provider_review_completed"
    )
    INTERACTIVE_COMMUNICATION_DOCUMENTED = (
        "interactive_communication_documented"
    )
    TIME_REQUIREMENT_SATISFIED = (
        "time_requirement_satisfied"
    )
    TREATMENT_DECISION_DOCUMENTED = (
        "treatment_decision_documented"
    )
    CLINICAL_NOTE_COMPLETED = (
        "clinical_note_completed"
    )
    PROVIDER_SIGNATURE_COMPLETED = (
        "provider_signature_completed"
    )


class RequirementStatus(StrEnum):
    NOT_EVALUATED = "not_evaluated"
    SATISFIED = "satisfied"
    NOT_SATISFIED = "not_satisfied"
    NOT_APPLICABLE = "not_applicable"
    REQUIRES_REVIEW = "requires_review"
    OVERRIDDEN = "overridden"


class BillingRuleValueType(StrEnum):
    BOOLEAN = "boolean"
    INTEGER = "integer"
    DECIMAL = "decimal"
    TEXT = "text"


class CodeEligibilityStatus(StrEnum):
    NOT_EVALUATED = "not_evaluated"
    POTENTIALLY_SUPPORTED = "potentially_supported"
    MISSING_REQUIREMENTS = "missing_requirements"
    REQUIRES_PROVIDER_CONFIRMATION = "requires_provider_confirmation"
    REQUIRES_BILLING_REVIEW = "requires_billing_review"
    APPROVED = "approved"
    NOT_APPROVED = "not_approved"
    NOT_APPLICABLE = "not_applicable"


class ProviderConfirmationStatus(StrEnum):
    NOT_REQUESTED = "not_requested"
    PENDING = "pending"
    CONFIRMED = "confirmed"
    REJECTED = "rejected"
    RETURNED_FOR_CORRECTION = "returned_for_correction"


class BillingReviewStatus(StrEnum):
    NOT_STARTED = "not_started"
    IN_REVIEW = "in_review"
    APPROVED = "approved"
    REJECTED = "rejected"
    RETURNED_FOR_CORRECTION = "returned_for_correction"


class ClaimPreparationStatus(StrEnum):
    DRAFT = "draft"
    READY_FOR_EXPORT = "ready_for_export"
    EXPORTED = "exported"
    CANCELLED = "cancelled"


class ClaimExportType(StrEnum):
    CSV = "csv"
    PDF = "pdf"
    EDI_837P = "edi_837p"
    PRACTICE_MANAGEMENT_SYSTEM = "practice_management_system"
    MANUAL_ENTRY_PACKET = "manual_entry_packet"


class ClaimExportStatus(StrEnum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"


class ClaimSubmissionStatus(StrEnum):
    SUBMITTED = "submitted"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    PROCESSING = "processing"
    ADJUDICATED = "adjudicated"
    CANCELLED = "cancelled"


class ClaimOutcomeStatus(StrEnum):
    PAID = "paid"
    PARTIALLY_PAID = "partially_paid"
    DENIED = "denied"
    PENDING = "pending"
    REVERSED = "reversed"


class MissingInformationSeverity(StrEnum):
    BLOCKING = "blocking"
    WARNING = "warning"
    INFORMATIONAL = "informational"


class BillingAuditEventType(StrEnum):
    CASE_CREATED = "case_created"
    REQUIREMENTS_EVALUATED = "requirements_evaluated"
    CODE_EVALUATED = "code_evaluated"
    PROVIDER_CONFIRMED = "provider_confirmed"
    BILLING_REVIEW_COMPLETED = "billing_review_completed"
    CLAIM_PREPARED = "claim_prepared"
    CLAIM_EXPORTED = "claim_exported"
    CLAIM_SUBMITTED = "claim_submitted"
    CLAIM_PAID = "claim_paid"
    CLAIM_DENIED = "claim_denied"
    CLAIM_CORRECTED = "claim_corrected"
    CLAIM_RESUBMITTED = "claim_resubmitted"
    STATUS_CHANGED = "status_changed"
