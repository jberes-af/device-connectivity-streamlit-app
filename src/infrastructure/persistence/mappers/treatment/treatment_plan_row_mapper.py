# AUTO GENERATED

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.treatmentplan_columns import TreatmentPlanColumns

from src.domain.entities.patient_entities import TreatmentPlan

from src.infrastructure.persistence.common.utils_parsing import *

class TreatmentPlanRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> TreatmentPlan:

        schema = TreatmentPlanColumns

        return TreatmentPlan(
            treatment_plan_id=parse_required_text(
                row.get(schema.TREATMENT_PLAN_ID),
                field_name=schema.TREATMENT_PLAN_ID,
            ),
            patient_id=parse_required_text(
                row.get(schema.PATIENT_ID),
                field_name=schema.PATIENT_ID,
            ),
            treating_provider_id=parse_required_text(
                row.get(schema.TREATING_PROVIDER_ID),
                field_name=schema.TREATING_PROVIDER_ID,
            ),
            functional_limitation=parse_required_text(
                row.get(schema.FUNCTIONAL_LIMITATION),
                field_name=schema.FUNCTIONAL_LIMITATION,
            ),
            medical_necessity_for_rtm=parse_required_text(
                row.get(schema.MEDICAL_NECESSITY_FOR_RTM),
                field_name=schema.MEDICAL_NECESSITY_FOR_RTM,
            ),
            remote_monitoring_rationale=parse_required_text(
                row.get(schema.REMOTE_MONITORING_RATIONALE),
                field_name=schema.REMOTE_MONITORING_RATIONALE,
            ),
            start_date=parse_required_date(
                row.get(schema.START_DATE),
                field_name=schema.START_DATE,
            ),
            expected_end_date=parse_optional_date(
                row.get(schema.EXPECTED_END_DATE),
                field_name=schema.EXPECTED_END_DATE,
            ),
            status=parse_optional_text(
                row.get(schema.STATUS),
                field_name=schema.STATUS,
            ),
            created_at=parse_required_datetime(
                row.get(schema.CREATED_AT),
                field_name=schema.CREATED_AT,
            ),
            updated_at=parse_required_datetime(
                row.get(schema.UPDATED_AT),
                field_name=schema.UPDATED_AT,
            ),
        )