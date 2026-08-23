# /src/infrastructure/persistence/schemas

class TreatmentPlanReviewColumns:
    REVIEW_ID: str = "review_id"
    TREATMENT_PLAN_ID: str = "treatment_plan_id"
    PROVIDER_ID: str = "provider_id"
    REVIEWED_AT: str = "reviewed_at"
    CLINICAL_FINDINGS: str = "clinical_findings"
    TREATMENT_DECISION: str = "treatment_decision"
    NEXT_REVIEW_DATE: str = "next_review_date"
    ORDER = (
REVIEW_ID,
TREATMENT_PLAN_ID,
PROVIDER_ID,
REVIEWED_AT,
CLINICAL_FINDINGS,
TREATMENT_DECISION,
NEXT_REVIEW_DATE,
)