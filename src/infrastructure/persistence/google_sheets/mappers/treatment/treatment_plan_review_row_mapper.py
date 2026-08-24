# /src/infrastructure/persistence/google_sheets/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.treatment.treatment_plan_review_columns import (
    TreatmentPlanReviewColumns
)

from src.domain.entities.care.treatment_entities import TreatmentPlanReview

from src.infrastructure.persistence.common.utils_parsing import *


class TreatmentPlanReviewRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> TreatmentPlanReview:
        schema = TreatmentPlanReviewColumns

        return TreatmentPlanReview(
            review_id=parse_required_text(
                row.get(schema.REVIEW_ID),
                field_name=schema.REVIEW_ID,
            ),
            treatment_plan_id=parse_required_text(
                row.get(schema.TREATMENT_PLAN_ID),
                field_name=schema.TREATMENT_PLAN_ID,
            ),
            provider_id=parse_required_text(
                row.get(schema.PROVIDER_ID),
                field_name=schema.PROVIDER_ID,
            ),
            reviewed_at=parse_required_datetime(
                row.get(schema.REVIEWED_AT),
                field_name=schema.REVIEWED_AT,
            ),
            clinical_findings=parse_required_text(
                row.get(schema.CLINICAL_FINDINGS),
                field_name=schema.CLINICAL_FINDINGS,
            ),
            treatment_decision=parse_required_text(
                row.get(schema.TREATMENT_DECISION),
                field_name=schema.TREATMENT_DECISION,
            ),
            next_review_date=parse_optional_date(
                row.get(schema.NEXT_REVIEW_DATE),
                field_name=schema.NEXT_REVIEW_DATE,
            ),
        )

    @staticmethod
    def to_row(
            treatment_plan_review: TreatmentPlanReview,
    ) -> RawRow:
        schema = TreatmentPlanReviewColumns

        return {

            schema.REVIEW_ID:
                treatment_plan_review.review_id,

            schema.TREATMENT_PLAN_ID:
                treatment_plan_review.treatment_plan_id,

            schema.PROVIDER_ID:
                treatment_plan_review.provider_id,

            schema.REVIEWED_AT:
                treatment_plan_review.reviewed_at.isoformat(),

            schema.CLINICAL_FINDINGS:
                treatment_plan_review.clinical_findings,

            schema.TREATMENT_DECISION:
                treatment_plan_review.treatment_decision,

            schema.NEXT_REVIEW_DATE:
                treatment_plan_review.next_review_date,

        }
