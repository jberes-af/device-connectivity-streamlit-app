# /src/domain/entities/billing_entities.py


from dataclasses import dataclass
from datetime import date, datetime

from src.domain.enums.billing_enums import (
    BillingCaseStatus,
    BillingRequirementType,
    BillingEvidenceType,
    BillingReviewStatus,
    BillingRuleValueType,
    BillingAuditEventType,
    ClaimSubmissionStatus,
    CodeEligibilityStatus,
    ClaimExport,
    ClaimExportType,
    ClaimExportStatus,
    ClaimOutcomeStatus,
    ClaimPreparationStatus,
    ProviderConfirmationStatus,
    RequirementStatus,
    MissingInformationSeverity,
)


@dataclass(frozen=True)
class BillingCase:
    billing_case_id: str
    patient_id: str
    monitoring_period_id: str
    service_period_start: date
    service_period_end: date
    billing_provider_id: str
    rendering_provider_id: str
    payer_id: str
    patient_payer_id: str | None
    status: BillingCaseStatus
    created_at: datetime
    created_by_user_id: str
    updated_at: datetime
    updated_by_user_id: str
    approved_at: datetime | None
    approved_by_user_id: str | None
    voided_at: datetime | None
    void_reason: str | None


@dataclass(frozen=True)
class BillingCaseNote:
    note_id: str
    billing_case_id: str
    author_user_id: str
    created_at: datetime
    note: str


@dataclass(frozen=True)
class BillingEvidenceReference:
    evidence_reference_id: str
    billing_case_id: str

    evidence_type: BillingEvidenceType
    source_record_id: str
    source_record_version: str | None

    description: str
    captured_at: datetime


@dataclass(frozen=True)
class BillingRequirementAssessment:
    assessment_id: str
    billing_case_id: str

    requirement_type: BillingRequirementType
    status: RequirementStatus

    rule_code: str
    rule_version: str

    explanation: str
    missing_information: str | None

    evaluated_at: datetime
    evaluated_by_system: bool

    reviewed_by_user_id: str | None
    reviewed_at: datetime | None

    override_reason: str | None


@dataclass(frozen=True)
class BillingRequirementEvidence:
    requirement_evidence_id: str
    assessment_id: str
    evidence_reference_id: str

    relevance_summary: str


@dataclass(frozen=True)
class BillingCodeEvaluation:
    code_evaluation_id: str
    billing_case_id: str

    code_system: str
    code: str
    code_description: str

    eligibility_status: CodeEligibilityStatus

    rule_set_version: str
    evaluated_at: datetime

    supporting_summary: str
    missing_requirements_summary: str | None

    provider_confirmation_required: bool
    billing_review_required: bool


@dataclass(frozen=True)
class BillingCodeRequirementResult:
    code_requirement_result_id: str
    code_evaluation_id: str
    assessment_id: str

    is_required_for_code: bool
    status: RequirementStatus
    explanation: str


@dataclass(frozen=True)
class ProviderBillingConfirmation:
    confirmation_id: str
    billing_case_id: str
    provider_id: str

    status: ProviderConfirmationStatus

    confirms_services_furnished: bool
    confirms_documentation_accurate: bool
    confirms_time_accurate: bool
    confirms_medical_necessity: bool

    provider_comments: str | None

    confirmed_at: datetime | None
    attestation_text: str | None


@dataclass(frozen=True)
class BillingReview:
    billing_review_id: str
    billing_case_id: str

    reviewer_user_id: str
    review_status: BillingReviewStatus

    reviewed_code_evaluation_ids: tuple[str, ...]
    approved_code_evaluation_ids: tuple[str, ...]

    findings: str | None
    correction_instructions: str | None

    started_at: datetime
    completed_at: datetime | None


@dataclass(frozen=True)
class ClaimPreparation:
    claim_preparation_id: str
    billing_case_id: str

    status: ClaimPreparationStatus

    billing_provider_id: str
    rendering_provider_id: str
    payer_id: str

    place_of_service_code: str | None
    diagnosis_codes: tuple[str, ...]
    prepared_code_evaluation_ids: tuple[str, ...]

    prepared_by_user_id: str
    prepared_at: datetime

    approved_by_user_id: str | None
    approved_at: datetime | None


@dataclass(frozen=True)
class ClaimLine:
    claim_line_id: str
    claim_preparation_id: str

    procedure_code: str
    service_date: date

    units: int
    diagnosis_pointers: tuple[int, ...]

    modifier_codes: tuple[str, ...]

    charge_amount_cents: int | None
    notes: str | None


@dataclass(frozen=True)
class ClaimExport:
    claim_export_id: str
    claim_preparation_id: str

    export_type: ClaimExportType
    status: ClaimExportStatus

    file_reference: str | None
    destination: str | None

    requested_by_user_id: str
    requested_at: datetime
    completed_at: datetime | None

    failure_reason: str | None


@dataclass(frozen=True)
class ClaimSubmission:
    claim_submission_id: str
    claim_preparation_id: str

    external_claim_id: str | None
    clearinghouse_reference: str | None

    status: ClaimSubmissionStatus

    submitted_at: datetime
    submitted_by_user_id: str

    last_status_at: datetime
    rejection_reason: str | None


@dataclass(frozen=True)
class ClaimOutcome:
    claim_outcome_id: str
    claim_submission_id: str

    status: ClaimOutcomeStatus

    adjudicated_at: datetime | None

    submitted_amount_cents: int | None
    allowed_amount_cents: int | None
    paid_amount_cents: int | None
    patient_responsibility_cents: int | None

    denial_code: str | None
    denial_reason: str | None

    remittance_reference: str | None


@dataclass(frozen=True)
class ClaimCorrection:
    claim_correction_id: str
    original_claim_preparation_id: str
    corrected_claim_preparation_id: str

    correction_reason: str
    corrected_by_user_id: str
    corrected_at: datetime


@dataclass(frozen=True)
class MissingBillingInformation:
    missing_information_id: str
    billing_case_id: str

    requirement_type: BillingRequirementType
    severity: MissingInformationSeverity

    description: str
    recommended_action: str

    responsible_user_id: str | None
    due_date: date | None

    resolved: bool
    resolved_at: datetime | None
    resolution_notes: str | None


@dataclass(frozen=True)
class BillingAuditEvent:
    audit_event_id: str
    billing_case_id: str

    event_type: BillingAuditEventType
    occurred_at: datetime
    performed_by_user_id: str

    previous_value: str | None
    new_value: str | None
    reason: str | None
