# /src/infrastructure/persistence/google_sheets/mappers/patient/rtm_enrollment_mapper.py

from src.domain.enums.access.status_and_method_enums import (
    EnrollmentStatusEnum,
    ConsentMethodEnum,
    ConsentStatusEnum,

)
from src.domain.entities.care.rtm_entities import RtmEnrollment

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.patient.rtm_enrollment_columns import (
    RtmEnrollmentColumns)

from src.infrastructure.persistence.common.utils_parsing import (
    parse_optional_enum,
    parse_optional_date,
    parse_optional_text,
    parse_required_date,
    parse_required_text,
)


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
            enrollment_status=parse_optional_enum(
                row.get(schema.ENROLLMENT_STATUS),
                enum_type=EnrollmentStatusEnum,
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
            consent_status=parse_optional_enum(
                row.get(schema.CONSENT_STATUS),
                enum_type=ConsentStatusEnum,
                field_name=schema.CONSENT_STATUS,
            ),
            consent_obtained_at=parse_optional_date(
                row.get(schema.CONSENT_OBTAINED_AT),
                field_name=schema.CONSENT_OBTAINED_AT,
            ),
            consent_method=parse_optional_enum(
                row.get(schema.CONSENT_METHOD),
                enum_type=ConsentMethodEnum,
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
