# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.communication_participant_columns import CommunicationParticipantColumns

from src.domain.entities.entities import CommunicationParticipant

from src.infrastructure.persistence.common.utils_parsing import *


class CommunicationParticipantRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> CommunicationParticipant:
        schema = CommunicationParticipantColumns

        return CommunicationParticipant(
            communication_participant_id=parse_required_text(
                row.get(schema.COMMUNICATION_PARTICIPANT_ID),
                field_name=schema.COMMUNICATION_PARTICIPANT_ID,
            ),
            communication_id=parse_required_text(
                row.get(schema.COMMUNICATION_ID),
                field_name=schema.COMMUNICATION_ID,
            ),
            participant_role=parse_optional_text(
                row.get(schema.PARTICIPANT_ROLE),
                field_name=schema.PARTICIPANT_ROLE,
            ),
            participant_id=parse_optional_text(
                row.get(schema.PARTICIPANT_ID),
                field_name=schema.PARTICIPANT_ID,
            ),
            participant_name=parse_required_text(
                row.get(schema.PARTICIPANT_NAME),
                field_name=schema.PARTICIPANT_NAME,
            ),
            was_present=parse_optional_text(
                row.get(schema.WAS_PRESENT),
                field_name=schema.WAS_PRESENT,
            ),
        )


    @staticmethod
    def to_row(
        communication_participant: CommunicationParticipant,
    ) -> RawRow:
        schema = CommunicationParticipantColumns

        return {

            schema.COMMUNICATION_PARTICIPANT_ID:
                communication_participant.communication_participant_id,

            schema.COMMUNICATION_ID:
                communication_participant.communication_id,

            schema.PARTICIPANT_ROLE:
                communication_participant.participant_role,

            schema.PARTICIPANT_ID:
                communication_participant.participant_id,

            schema.PARTICIPANT_NAME:
                communication_participant.participant_name,

            schema.WAS_PRESENT:
                communication_participant.was_present,

        }