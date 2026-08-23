# /src/infrastructure/persistence/google_sheets/mappers/treatment/treatment_plan_row_mapper.py

from src.domain.enums.care.treatment_enums import (
    TreatmentPlanStatus,
)

from src.domain.entities.care.treatment_entities import TreatmentPlan

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.treatment.treatment_plan_columns import (
    TreatmentPlanColumns
)

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
            rtm_program_id=parse_required_text(
                row.get(schema.RTM_PROGRAM_ID),
                field_name=schema.RTM_PROGRAM_ID,
            ),
            patient_id=parse_required_text(
                row.get(schema.PATIENT_ID),
                field_name=schema.PATIENT_ID,
            ),
            treating_provider_id=parse_required_text(
                row.get(schema.TREATING_PROVIDER_ID),
                field_name=schema.TREATING_PROVIDER_ID,
            ),
            start_date=parse_required_date(
                row.get(schema.START_DATE),
                field_name=schema.START_DATE,
            ),
            expected_end_date=parse_optional_date(
                row.get(schema.EXPECTED_END_DATE),
                field_name=schema.EXPECTED_END_DATE,
            ),
            status=parse_optional_enum(
                row.get(schema.STATUS),
                enum_type=TreatmentPlanStatus,
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

    @staticmethod
    def to_row(
            treatment_plan: TreatmentPlan,
    ) -> RawRow:
        schema = TreatmentPlanColumns

        return {

            schema.TREATMENT_PLAN_ID:
                treatment_plan.treatment_plan_id,

            schema.RTM_PROGRAM_ID:
                treatment_plan.rtm_program_id,

            schema.PATIENT_ID:
                treatment_plan.patient_id,

            schema.TREATING_PROVIDER_ID:
                treatment_plan.treating_provider_id,

            schema.START_DATE:
                treatment_plan.start_date,

            schema.EXPECTED_END_DATE:
                treatment_plan.expected_end_date,

            schema.STATUS:
                treatment_plan.status,

            schema.CREATED_AT:
                treatment_plan.created_at.isoformat(),

            schema.UPDATED_AT:
                treatment_plan.updated_at.isoformat(),

        }
