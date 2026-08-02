# AUTO GENERATED

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.providerreview_columns import ProviderReviewColumns

from src.domain.entities.patient_entities import ProviderReview

from src.infrastructure.persistence.common.utils_parsing import *

class ProviderReviewRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> ProviderReview:

        schema = ProviderReviewColumns

        return ProviderReview(
            review_id=parse_required_text(
                row.get(schema.REVIEW_ID),
                field_name=schema.REVIEW_ID,
            ),
            patient_id=parse_required_text(
                row.get(schema.PATIENT_ID),
                field_name=schema.PATIENT_ID,
            ),
            measurement_period_id=parse_required_text(
                row.get(schema.MEASUREMENT_PERIOD_ID),
                field_name=schema.MEASUREMENT_PERIOD_ID,
            ),
            reviewing_provider_id=parse_required_text(
                row.get(schema.REVIEWING_PROVIDER_ID),
                field_name=schema.REVIEWING_PROVIDER_ID,
            ),
            reviewed_at=parse_required_datetime(
                row.get(schema.REVIEWED_AT),
                field_name=schema.REVIEWED_AT,
            ),
            started_at=parse_required_datetime(
                row.get(schema.STARTED_AT),
                field_name=schema.STARTED_AT,
            ),
            completed_at=parse_required_datetime(
                row.get(schema.COMPLETED_AT),
                field_name=schema.COMPLETED_AT,
            ),
            review_status=parse_optional_text(
                row.get(schema.REVIEW_STATUS),
                field_name=schema.REVIEW_STATUS,
            ),
            total_elapsed_minutes=parse_required_int(
                row.get(schema.TOTAL_ELAPSED_MINUTES),
                field_name=schema.TOTAL_ELAPSED_MINUTES,
            ),
            billable_minutes=parse_required_int(
                row.get(schema.BILLABLE_MINUTES),
                field_name=schema.BILLABLE_MINUTES,
            ),
        )