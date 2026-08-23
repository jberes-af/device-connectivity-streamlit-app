# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.rtm_enrollment_columns import RtmEnrollmentColumns

from src.domain.entities.entities import RtmEnrollment

from src.infrastructure.persistence.common.utils_parsing import *


class RtmEnrollmentRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> RtmEnrollment:
        schema = RtmEnrollmentColumns

        return RtmEnrollment(
            enrollment_id=parse_required_text(
                row.get(schema.ENROLLMENT_ID),
                field_name=schema.ENROLLMENT_ID,
            ),
            patient_id=parse_required_text(
                row.get(schema.PATIENT_ID),
                field_name=schema.PATIENT_ID,
            ),
            enrollment_status=parse_optional_text(
                row.get(schema.ENROLLMENT_STATUS),
                field_name=schema.ENROLLMENT_STATUS,
            ),
            enrollment_date=parse_required_date(
                row.get(schema.ENROLLMENT_DATE),
                field_name=schema.ENROLLMENT_DATE,
            ),
            service_start_date=parse_required_date(
                row.get(schema.SERVICE_START_DATE),
                field_name=schema.SERVICE_START_DATE,
            ),
            service_end_date=parse_optional_date(
                row.get(schema.SERVICE_END_DATE),
                field_name=schema.SERVICE_END_DATE,
            ),
            consent_status=parse_optional_text(
                row.get(schema.CONSENT_STATUS),
                field_name=schema.CONSENT_STATUS,
            ),
            consent_obtained_at=parse_optional_datetime(
                row.get(schema.CONSENT_OBTAINED_AT),
                field_name=schema.CONSENT_OBTAINED_AT,
            ),
            consent_method=parse_optional_text(
                row.get(schema.CONSENT_METHOD),
                field_name=schema.CONSENT_METHOD,
            ),
            consent_document_reference=parse_optional_text(
                row.get(schema.CONSENT_DOCUMENT_REFERENCE),
                field_name=schema.CONSENT_DOCUMENT_REFERENCE,
            ),
            discontinuation_reason=parse_optional_text(
                row.get(schema.DISCONTINUATION_REASON),
                field_name=schema.DISCONTINUATION_REASON,
            ),
        )


    @staticmethod
    def to_row(
        rtm_enrollment: RtmEnrollment,
    ) -> RawRow:
        schema = RtmEnrollmentColumns

        return {

            schema.ENROLLMENT_ID:
                rtm_enrollment.enrollment_id,

            schema.PATIENT_ID:
                rtm_enrollment.patient_id,

            schema.ENROLLMENT_STATUS:
                rtm_enrollment.enrollment_status,

            schema.ENROLLMENT_DATE:
                rtm_enrollment.enrollment_date,

            schema.SERVICE_START_DATE:
                rtm_enrollment.service_start_date,

            schema.SERVICE_END_DATE:
                rtm_enrollment.service_end_date,

            schema.CONSENT_STATUS:
                rtm_enrollment.consent_status,

            schema.CONSENT_OBTAINED_AT:
                rtm_enrollment.consent_obtained_at.isoformat(),

            schema.CONSENT_METHOD:
                rtm_enrollment.consent_method,

            schema.CONSENT_DOCUMENT_REFERENCE:
                rtm_enrollment.consent_document_reference,

            schema.DISCONTINUATION_REASON:
                rtm_enrollment.discontinuation_reason,

        }