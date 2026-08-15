# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas import CarePlanColumns

from src.domain.entities.entities import CarePlan

from src.infrastructure.persistence.common.utils_parsing import *


class CarePlanRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> CarePlan:
        schema = CarePlanColumns

        return CarePlan(
            care_plan_id=parse_required_text(
                row.get(schema.CARE_PLAN_ID),
                field_name=schema.CARE_PLAN_ID,
            ),
            patient_id=parse_required_text(
                row.get(schema.PATIENT_ID),
                field_name=schema.PATIENT_ID,
            ),
            title=parse_required_text(
                row.get(schema.TITLE),
                field_name=schema.TITLE,
            ),
            summary=parse_optional_text(
                row.get(schema.SUMMARY),
                field_name=schema.SUMMARY,
            ),
            created_by_user_id=parse_required_text(
                row.get(schema.CREATED_BY_USER_ID),
                field_name=schema.CREATED_BY_USER_ID,
            ),
            responsible_coordinator_id=parse_optional_text(
                row.get(schema.RESPONSIBLE_COORDINATOR_ID),
                field_name=schema.RESPONSIBLE_COORDINATOR_ID,
            ),
            start_date=parse_required_date(
                row.get(schema.START_DATE),
                field_name=schema.START_DATE,
            ),
            target_review_date=parse_optional_date(
                row.get(schema.TARGET_REVIEW_DATE),
                field_name=schema.TARGET_REVIEW_DATE,
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


    @staticmethod
    def to_row(
        care_plan: CarePlan,
    ) -> RawRow:
        schema = CarePlanColumns

        return {

            schema.CARE_PLAN_ID:
                care_plan.care_plan_id,

            schema.PATIENT_ID:
                care_plan.patient_id,

            schema.TITLE:
                care_plan.title,

            schema.SUMMARY:
                care_plan.summary,

            schema.CREATED_BY_USER_ID:
                care_plan.created_by_user_id,

            schema.RESPONSIBLE_COORDINATOR_ID:
                care_plan.responsible_coordinator_id,

            schema.START_DATE:
                care_plan.start_date,

            schema.TARGET_REVIEW_DATE:
                care_plan.target_review_date,

            schema.STATUS:
                care_plan.status,

            schema.CREATED_AT:
                care_plan.created_at.isoformat(),

            schema.UPDATED_AT:
                care_plan.updated_at.isoformat(),

        }