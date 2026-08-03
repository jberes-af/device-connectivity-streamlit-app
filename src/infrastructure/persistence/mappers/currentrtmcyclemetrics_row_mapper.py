# AUTO GENERATED

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.currentrtmcyclemetrics_columns import CurrentRTMCycleMetricsColumns

from src.domain.entities.patient_entities import CurrentRTMCycleMetrics

from src.infrastructure.persistence.common.utils_parsing import *

class CurrentRTMCycleMetricsRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> CurrentRTMCycleMetrics:

        schema = CurrentRTMCycleMetricsColumns

        return CurrentRTMCycleMetrics(
            patient_id=parse_required_text(
                row.get(schema.PATIENT_ID),
            ),
            monitoring_period_id=parse_required_text(
                row.get(schema.MONITORING_PERIOD_ID),
            ),
            monitoring_days=parse_required_int(
                row.get(schema.MONITORING_DAYS),
            ),
            required_monitoring_days=parse_optional_int(
                row.get(schema.REQUIRED_MONITORING_DAYS),
            ),
            management_minutes=parse_required_int(
                row.get(schema.MANAGEMENT_MINUTES),
            ),
            target_management_minutes=parse_optional_int(
                row.get(schema.TARGET_MANAGEMENT_MINUTES),
            ),
            interactive_communication_completed=parse_optional_text(
                row.get(schema.INTERACTIVE_COMMUNICATION_COMPLETED),
            ),
            interactive_communication_minutes=parse_required_int(
                row.get(schema.INTERACTIVE_COMMUNICATION_MINUTES),
            ),
            activity_change_from_baseline_pct=parse_optional_text(
                row.get(schema.ACTIVITY_CHANGE_FROM_BASELINE_PCT),
            ),
            open_clinical_alert_count=parse_required_int(
                row.get(schema.OPEN_CLINICAL_ALERT_COUNT),
            ),
            documentation_status=parse_optional_text(
                row.get(schema.DOCUMENTATION_STATUS),
            ),
            billing_readiness_status=parse_optional_text(
                row.get(schema.BILLING_READINESS_STATUS),
            ),
        )