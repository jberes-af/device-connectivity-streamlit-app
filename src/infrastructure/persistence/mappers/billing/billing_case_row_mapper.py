# AUTO GENERATED

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.billingcase_columns import BillingCaseColumns

from src.domain.entities.patient_entities import BillingCase

from src.infrastructure.persistence.common.utils_parsing import *

class BillingCaseRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> BillingCase:

        schema = BillingCaseColumns

        return BillingCase(
            billing_case_id=parse_required_text(
                row.get(schema.BILLING_CASE_ID),
                field_name=schema.BILLING_CASE_ID,
            ),
            patient_id=parse_required_text(
                row.get(schema.PATIENT_ID),
                field_name=schema.PATIENT_ID,
            ),
            monitoring_period_id=parse_required_text(
                row.get(schema.MONITORING_PERIOD_ID),
                field_name=schema.MONITORING_PERIOD_ID,
            ),
            service_period_start=parse_required_date(
                row.get(schema.SERVICE_PERIOD_START),
                field_name=schema.SERVICE_PERIOD_START,
            ),
            service_period_end=parse_required_date(
                row.get(schema.SERVICE_PERIOD_END),
                field_name=schema.SERVICE_PERIOD_END,
            ),
            billing_provider_id=parse_required_text(
                row.get(schema.BILLING_PROVIDER_ID),
                field_name=schema.BILLING_PROVIDER_ID,
            ),
            rendering_provider_id=parse_required_text(
                row.get(schema.RENDERING_PROVIDER_ID),
                field_name=schema.RENDERING_PROVIDER_ID,
            ),
            payer_id=parse_required_text(
                row.get(schema.PAYER_ID),
                field_name=schema.PAYER_ID,
            ),
            patient_payer_id=parse_optional_text(
                row.get(schema.PATIENT_PAYER_ID),
                field_name=schema.PATIENT_PAYER_ID,
            ),
            status=parse_optional_text(
                row.get(schema.STATUS),
                field_name=schema.STATUS,
            ),
            created_at=parse_required_datetime(
                row.get(schema.CREATED_AT),
                field_name=schema.CREATED_AT,
            ),
            created_by_user_id=parse_required_text(
                row.get(schema.CREATED_BY_USER_ID),
                field_name=schema.CREATED_BY_USER_ID,
            ),
            updated_at=parse_required_datetime(
                row.get(schema.UPDATED_AT),
                field_name=schema.UPDATED_AT,
            ),
            updated_by_user_id=parse_required_text(
                row.get(schema.UPDATED_BY_USER_ID),
                field_name=schema.UPDATED_BY_USER_ID,
            ),
            approved_at=parse_optional_datetime(
                row.get(schema.APPROVED_AT),
                field_name=schema.APPROVED_AT,
            ),
            approved_by_user_id=parse_optional_text(
                row.get(schema.APPROVED_BY_USER_ID),
                field_name=schema.APPROVED_BY_USER_ID,
            ),
            voided_at=parse_optional_datetime(
                row.get(schema.VOIDED_AT),
                field_name=schema.VOIDED_AT,
            ),
            void_reason=parse_optional_text(
                row.get(schema.VOID_REASON),
                field_name=schema.VOID_REASON,
            ),
        )