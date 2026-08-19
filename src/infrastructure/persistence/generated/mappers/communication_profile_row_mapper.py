# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.communication_profile_columns import CommunicationProfileColumns

from src.domain.entities.entities import CommunicationProfile

from src.infrastructure.persistence.common.utils_parsing import *


class CommunicationProfileRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> CommunicationProfile:
        schema = CommunicationProfileColumns

        return CommunicationProfile(
            communication_id=parse_required_text(
                row.get(schema.COMMUNICATION_ID),
                field_name=schema.COMMUNICATION_ID,
            ),
            patient_id=parse_required_text(
                row.get(schema.PATIENT_ID),
                field_name=schema.PATIENT_ID,
            ),
            occurred_at=parse_required_datetime(
                row.get(schema.OCCURRED_AT),
                field_name=schema.OCCURRED_AT,
            ),
            method=parse_optional_text(
                row.get(schema.METHOD),
                field_name=schema.METHOD,
            ),
            communication_type=parse_optional_text(
                row.get(schema.COMMUNICATION_TYPE),
                field_name=schema.COMMUNICATION_TYPE,
            ),
            status=parse_optional_text(
                row.get(schema.STATUS),
                field_name=schema.STATUS,
            ),
            initiated_by_type=parse_optional_text(
                row.get(schema.INITIATED_BY_TYPE),
                field_name=schema.INITIATED_BY_TYPE,
            ),
            initiated_by_id=parse_optional_text(
                row.get(schema.INITIATED_BY_ID),
                field_name=schema.INITIATED_BY_ID,
            ),
            duration_minutes=parse_optional_int(
                row.get(schema.DURATION_MINUTES),
                field_name=schema.DURATION_MINUTES,
            ),
            summary=parse_required_text(
                row.get(schema.SUMMARY),
                field_name=schema.SUMMARY,
            ),
            clinical_impact=parse_optional_text(
                row.get(schema.CLINICAL_IMPACT),
                field_name=schema.CLINICAL_IMPACT,
            ),
            monitoring_period_id=parse_optional_text(
                row.get(schema.MONITORING_PERIOD_ID),
                field_name=schema.MONITORING_PERIOD_ID,
            ),
            provider_review_id=parse_optional_text(
                row.get(schema.PROVIDER_REVIEW_ID),
                field_name=schema.PROVIDER_REVIEW_ID,
            ),
            counts_toward_rtm_period=parse_optional_text(
                row.get(schema.COUNTS_TOWARD_RTM_PERIOD),
                field_name=schema.COUNTS_TOWARD_RTM_PERIOD,
            ),
            created_by_user_id=parse_required_text(
                row.get(schema.CREATED_BY_USER_ID),
                field_name=schema.CREATED_BY_USER_ID,
            ),
            created_at=parse_required_datetime(
                row.get(schema.CREATED_AT),
                field_name=schema.CREATED_AT,
            ),
        )


    @staticmethod
    def to_row(
        communication_profile: CommunicationProfile,
    ) -> RawRow:
        schema = CommunicationProfileColumns

        return {

            schema.COMMUNICATION_ID:
                communication_profile.communication_id,

            schema.PATIENT_ID:
                communication_profile.patient_id,

            schema.OCCURRED_AT:
                communication_profile.occurred_at.isoformat(),

            schema.METHOD:
                communication_profile.method,

            schema.COMMUNICATION_TYPE:
                communication_profile.communication_type,

            schema.STATUS:
                communication_profile.status,

            schema.INITIATED_BY_TYPE:
                communication_profile.initiated_by_type,

            schema.INITIATED_BY_ID:
                communication_profile.initiated_by_id,

            schema.DURATION_MINUTES:
                communication_profile.duration_minutes,

            schema.SUMMARY:
                communication_profile.summary,

            schema.CLINICAL_IMPACT:
                communication_profile.clinical_impact,

            schema.MONITORING_PERIOD_ID:
                communication_profile.monitoring_period_id,

            schema.PROVIDER_REVIEW_ID:
                communication_profile.provider_review_id,

            schema.COUNTS_TOWARD_RTM_PERIOD:
                communication_profile.counts_toward_rtm_period,

            schema.CREATED_BY_USER_ID:
                communication_profile.created_by_user_id,

            schema.CREATED_AT:
                communication_profile.created_at.isoformat(),

        }