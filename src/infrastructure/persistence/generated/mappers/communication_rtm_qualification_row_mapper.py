# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.communication_rtm_qualification_columns import CommunicationRTMQualificationColumns

from src.domain.entities.entities import CommunicationRTMQualification

from src.infrastructure.persistence.common.utils_parsing import *


class CommunicationRTMQualificationRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> CommunicationRTMQualification:
        schema = CommunicationRTMQualificationColumns

        return CommunicationRTMQualification(
            communication_id=parse_required_text(
                row.get(schema.COMMUNICATION_ID),
                field_name=schema.COMMUNICATION_ID,
            ),
            was_interactive=parse_optional_text(
                row.get(schema.WAS_INTERACTIVE),
                field_name=schema.WAS_INTERACTIVE,
            ),
            patient_or_caregiver_participated=parse_optional_text(
                row.get(schema.PATIENT_OR_CAREGIVER_PARTICIPATED),
                field_name=schema.PATIENT_OR_CAREGIVER_PARTICIPATED,
            ),
            clinical_management_occurred=parse_optional_text(
                row.get(schema.CLINICAL_MANAGEMENT_OCCURRED),
                field_name=schema.CLINICAL_MANAGEMENT_OCCURRED,
            ),
            completed_successfully=parse_optional_text(
                row.get(schema.COMPLETED_SUCCESSFULLY),
                field_name=schema.COMPLETED_SUCCESSFULLY,
            ),
            qualifying_minutes=parse_required_int(
                row.get(schema.QUALIFYING_MINUTES),
                field_name=schema.QUALIFYING_MINUTES,
            ),
            counts_toward_rtm_period=parse_optional_text(
                row.get(schema.COUNTS_TOWARD_RTM_PERIOD),
                field_name=schema.COUNTS_TOWARD_RTM_PERIOD,
            ),
            qualification_notes=parse_optional_text(
                row.get(schema.QUALIFICATION_NOTES),
                field_name=schema.QUALIFICATION_NOTES,
            ),
            confirmed_by_provider_id=parse_optional_text(
                row.get(schema.CONFIRMED_BY_PROVIDER_ID),
                field_name=schema.CONFIRMED_BY_PROVIDER_ID,
            ),
            confirmed_at=parse_optional_datetime(
                row.get(schema.CONFIRMED_AT),
                field_name=schema.CONFIRMED_AT,
            ),
        )


    @staticmethod
    def to_row(
        communication_rtm_qualification: CommunicationRTMQualification,
    ) -> RawRow:
        schema = CommunicationRTMQualificationColumns

        return {

            schema.COMMUNICATION_ID:
                communication_rtm_qualification.communication_id,

            schema.WAS_INTERACTIVE:
                communication_rtm_qualification.was_interactive,

            schema.PATIENT_OR_CAREGIVER_PARTICIPATED:
                communication_rtm_qualification.patient_or_caregiver_participated,

            schema.CLINICAL_MANAGEMENT_OCCURRED:
                communication_rtm_qualification.clinical_management_occurred,

            schema.COMPLETED_SUCCESSFULLY:
                communication_rtm_qualification.completed_successfully,

            schema.QUALIFYING_MINUTES:
                communication_rtm_qualification.qualifying_minutes,

            schema.COUNTS_TOWARD_RTM_PERIOD:
                communication_rtm_qualification.counts_toward_rtm_period,

            schema.QUALIFICATION_NOTES:
                communication_rtm_qualification.qualification_notes,

            schema.CONFIRMED_BY_PROVIDER_ID:
                communication_rtm_qualification.confirmed_by_provider_id,

            schema.CONFIRMED_AT:
                communication_rtm_qualification.confirmed_at.isoformat(),

        }