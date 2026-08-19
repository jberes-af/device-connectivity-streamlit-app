# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.clinical_communication_decision_columns import ClinicalCommunicationDecisionColumns

from src.domain.entities.entities import ClinicalCommunicationDecision

from src.infrastructure.persistence.common.utils_parsing import *


class ClinicalCommunicationDecisionRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> ClinicalCommunicationDecision:
        schema = ClinicalCommunicationDecisionColumns

        return ClinicalCommunicationDecision(
            communication_decision_id=parse_required_text(
                row.get(schema.COMMUNICATION_DECISION_ID),
                field_name=schema.COMMUNICATION_DECISION_ID,
            ),
            communication_id=parse_required_text(
                row.get(schema.COMMUNICATION_ID),
                field_name=schema.COMMUNICATION_ID,
            ),
            decision_type=parse_optional_text(
                row.get(schema.DECISION_TYPE),
                field_name=schema.DECISION_TYPE,
            ),
            rationale=parse_required_text(
                row.get(schema.RATIONALE),
                field_name=schema.RATIONALE,
            ),
            follow_up_due_at=parse_optional_datetime(
                row.get(schema.FOLLOW_UP_DUE_AT),
                field_name=schema.FOLLOW_UP_DUE_AT,
            ),
            responsible_provider_id=parse_optional_text(
                row.get(schema.RESPONSIBLE_PROVIDER_ID),
                field_name=schema.RESPONSIBLE_PROVIDER_ID,
            ),
            completed=parse_optional_text(
                row.get(schema.COMPLETED),
                field_name=schema.COMPLETED,
            ),
        )


    @staticmethod
    def to_row(
        clinical_communication_decision: ClinicalCommunicationDecision,
    ) -> RawRow:
        schema = ClinicalCommunicationDecisionColumns

        return {

            schema.COMMUNICATION_DECISION_ID:
                clinical_communication_decision.communication_decision_id,

            schema.COMMUNICATION_ID:
                clinical_communication_decision.communication_id,

            schema.DECISION_TYPE:
                clinical_communication_decision.decision_type,

            schema.RATIONALE:
                clinical_communication_decision.rationale,

            schema.FOLLOW_UP_DUE_AT:
                clinical_communication_decision.follow_up_due_at.isoformat(),

            schema.RESPONSIBLE_PROVIDER_ID:
                clinical_communication_decision.responsible_provider_id,

            schema.COMPLETED:
                clinical_communication_decision.completed,

        }