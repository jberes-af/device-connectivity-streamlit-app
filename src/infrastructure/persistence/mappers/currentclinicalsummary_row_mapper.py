# AUTO GENERATED

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.currentclinicalsummary_columns import CurrentClinicalSummaryColumns

from src.domain.entities.patient_entities import CurrentClinicalSummary

from src.infrastructure.persistence.common.utils_parsing import *

class CurrentClinicalSummaryRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> CurrentClinicalSummary:

        schema = CurrentClinicalSummaryColumns

        return CurrentClinicalSummary(
            patient_id=parse_required_text(
                row.get(schema.PATIENT_ID),
            ),
            medical_necessity_summary=parse_required_text(
                row.get(schema.MEDICAL_NECESSITY_SUMMARY),
            ),
            treatment_plan_id=parse_optional_text(
                row.get(schema.TREATMENT_PLAN_ID),
            ),
            treatment_plan_summary=parse_optional_text(
                row.get(schema.TREATMENT_PLAN_SUMMARY),
            ),
            therapeutic_goal_summaries=parse_tuple(
                row.get(schema.THERAPEUTIC_GOAL_SUMMARIES),
            ),
            monitoring_period_id=parse_optional_text(
                row.get(schema.MONITORING_PERIOD_ID),
            ),
            monitoring_period_start=parse_optional_date(
                row.get(schema.MONITORING_PERIOD_START),
            ),
            monitoring_period_end=parse_optional_date(
                row.get(schema.MONITORING_PERIOD_END),
            ),
            billing_year=parse_required_int(
                row.get(schema.BILLING_YEAR),
            ),
            billing_month=parse_required_int(
                row.get(schema.BILLING_MONTH),
            ),
            recent_clinical_alert_count=parse_required_int(
                row.get(schema.RECENT_CLINICAL_ALERT_COUNT),
            ),
            recent_clinical_alert_summaries=parse_tuple(
                row.get(schema.RECENT_CLINICAL_ALERT_SUMMARIES),
            ),
            monthly_trend_summary=parse_optional_text(
                row.get(schema.MONTHLY_TREND_SUMMARY),
            ),
            most_recent_provider_review_at=parse_optional_datetime(
                row.get(schema.MOST_RECENT_PROVIDER_REVIEW_AT),
            ),
            most_recent_provider_review_summary=parse_optional_text(
                row.get(schema.MOST_RECENT_PROVIDER_REVIEW_SUMMARY),
            ),
            most_recent_communication_at=parse_optional_datetime(
                row.get(schema.MOST_RECENT_COMMUNICATION_AT),
            ),
            most_recent_communication_summary=parse_optional_text(
                row.get(schema.MOST_RECENT_COMMUNICATION_SUMMARY),
            ),
            billing_readiness_status=parse_optional_text(
                row.get(schema.BILLING_READINESS_STATUS),
            ),
            missing_billing_requirements=parse_tuple(
                row.get(schema.MISSING_BILLING_REQUIREMENTS),
            ),
        )