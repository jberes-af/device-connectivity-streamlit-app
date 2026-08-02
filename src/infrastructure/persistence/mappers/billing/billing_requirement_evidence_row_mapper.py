# AUTO GENERATED

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.billingrequirementevidence_columns import BillingRequirementEvidenceColumns

from src.domain.entities.patient_entities import BillingRequirementEvidence

from src.infrastructure.persistence.common.utils_parsing import *

class BillingRequirementEvidenceRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> BillingRequirementEvidence:

        schema = BillingRequirementEvidenceColumns

        return BillingRequirementEvidence(
            requirement_evidence_id=parse_required_text(
                row.get(schema.REQUIREMENT_EVIDENCE_ID),
                field_name=schema.REQUIREMENT_EVIDENCE_ID,
            ),
            assessment_id=parse_required_text(
                row.get(schema.ASSESSMENT_ID),
                field_name=schema.ASSESSMENT_ID,
            ),
            evidence_reference_id=parse_required_text(
                row.get(schema.EVIDENCE_REFERENCE_ID),
                field_name=schema.EVIDENCE_REFERENCE_ID,
            ),
            relevance_summary=parse_required_text(
                row.get(schema.RELEVANCE_SUMMARY),
                field_name=schema.RELEVANCE_SUMMARY,
            ),
        )