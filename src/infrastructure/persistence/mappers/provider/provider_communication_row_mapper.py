# AUTO GENERATED

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.providercommunication_columns import ProviderCommunicationColumns

from src.domain.entities.patient_entities import ProviderCommunication

from src.infrastructure.persistence.common.utils_parsing import *

class ProviderCommunicationRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> ProviderCommunication:

        schema = ProviderCommunicationColumns

        return ProviderCommunication(
            communication_id=parse_required_text(
                row.get(schema.COMMUNICATION_ID),
                field_name=schema.COMMUNICATION_ID,
            ),
            patient_id=parse_required_text(
                row.get(schema.PATIENT_ID),
                field_name=schema.PATIENT_ID,
            ),
            provider_id=parse_required_text(
                row.get(schema.PROVIDER_ID),
                field_name=schema.PROVIDER_ID,
            ),
            occurred_at=parse_required_datetime(
                row.get(schema.OCCURRED_AT),
                field_name=schema.OCCURRED_AT,
            ),
            communication_method=parse_optional_text(
                row.get(schema.COMMUNICATION_METHOD),
                field_name=schema.COMMUNICATION_METHOD,
            ),
            duration_minutes=parse_required_int(
                row.get(schema.DURATION_MINUTES),
                field_name=schema.DURATION_MINUTES,
            ),
            summary=parse_required_text(
                row.get(schema.SUMMARY),
                field_name=schema.SUMMARY,
            ),
        )