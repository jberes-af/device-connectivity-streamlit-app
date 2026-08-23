# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.rtm_interaction_columns import RtmInteractionColumns

from src.domain.entities.entities import RtmInteraction

from src.infrastructure.persistence.common.utils_parsing import *


class RtmInteractionRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> RtmInteraction:
        schema = RtmInteractionColumns

        return RtmInteraction(
            interaction_id=parse_required_text(
                row.get(schema.INTERACTION_ID),
                field_name=schema.INTERACTION_ID,
            ),
            activity_id=parse_required_text(
                row.get(schema.ACTIVITY_ID),
                field_name=schema.ACTIVITY_ID,
            ),
            participant_type=parse_optional_text(
                row.get(schema.PARTICIPANT_TYPE),
                field_name=schema.PARTICIPANT_TYPE,
            ),
            participant_id=parse_optional_text(
                row.get(schema.PARTICIPANT_ID),
                field_name=schema.PARTICIPANT_ID,
            ),
            communication_method=parse_optional_text(
                row.get(schema.COMMUNICATION_METHOD),
                field_name=schema.COMMUNICATION_METHOD,
            ),
            is_real_time=parse_optional_text(
                row.get(schema.IS_REAL_TIME),
                field_name=schema.IS_REAL_TIME,
            ),
            occurred_at=parse_required_datetime(
                row.get(schema.OCCURRED_AT),
                field_name=schema.OCCURRED_AT,
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


    @staticmethod
    def to_row(
        rtm_interaction: RtmInteraction,
    ) -> RawRow:
        schema = RtmInteractionColumns

        return {

            schema.INTERACTION_ID:
                rtm_interaction.interaction_id,

            schema.ACTIVITY_ID:
                rtm_interaction.activity_id,

            schema.PARTICIPANT_TYPE:
                rtm_interaction.participant_type,

            schema.PARTICIPANT_ID:
                rtm_interaction.participant_id,

            schema.COMMUNICATION_METHOD:
                rtm_interaction.communication_method,

            schema.IS_REAL_TIME:
                rtm_interaction.is_real_time,

            schema.OCCURRED_AT:
                rtm_interaction.occurred_at.isoformat(),

            schema.DURATION_MINUTES:
                rtm_interaction.duration_minutes,

            schema.SUMMARY:
                rtm_interaction.summary,

        }