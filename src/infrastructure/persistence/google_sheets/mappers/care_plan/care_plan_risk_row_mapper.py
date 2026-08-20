# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas import CarePlanRiskColumns

from src.domain.entities.entities import CarePlanRisk

from src.infrastructure.persistence.common.utils_parsing import *


class CarePlanRiskRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> CarePlanRisk:
        schema = CarePlanRiskColumns

        return CarePlanRisk(
            risk_id=parse_required_text(
                row.get(schema.RISK_ID),
                field_name=schema.RISK_ID,
            ),
            care_plan_id=parse_required_text(
                row.get(schema.CARE_PLAN_ID),
                field_name=schema.CARE_PLAN_ID,
            ),
            risk_type=parse_optional_text(
                row.get(schema.RISK_TYPE),
                field_name=schema.RISK_TYPE,
            ),
            severity=parse_optional_text(
                row.get(schema.SEVERITY),
                field_name=schema.SEVERITY,
            ),
            description=parse_required_text(
                row.get(schema.DESCRIPTION),
                field_name=schema.DESCRIPTION,
            ),
            mitigation_plan=parse_required_text(
                row.get(schema.MITIGATION_PLAN),
                field_name=schema.MITIGATION_PLAN,
            ),
            active=parse_optional_text(
                row.get(schema.ACTIVE),
                field_name=schema.ACTIVE,
            ),
        )


    @staticmethod
    def to_row(
        care_plan_risk: CarePlanRisk,
    ) -> RawRow:
        schema = CarePlanRiskColumns

        return {

            schema.RISK_ID:
                care_plan_risk.risk_id,

            schema.CARE_PLAN_ID:
                care_plan_risk.care_plan_id,

            schema.RISK_TYPE:
                care_plan_risk.risk_type,

            schema.SEVERITY:
                care_plan_risk.severity,

            schema.DESCRIPTION:
                care_plan_risk.card_text,

            schema.MITIGATION_PLAN:
                care_plan_risk.mitigation_plan,

            schema.ACTIVE:
                care_plan_risk.active,

        }