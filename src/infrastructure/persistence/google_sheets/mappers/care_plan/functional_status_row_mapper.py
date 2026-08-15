# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas import FunctionalStatusColumns

from src.domain.entities.entities import FunctionalStatus

from src.infrastructure.persistence.common.utils_parsing import *


class FunctionalStatusRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> FunctionalStatus:
        schema = FunctionalStatusColumns

        return FunctionalStatus(
            functional_status_id=parse_required_text(
                row.get(schema.FUNCTIONAL_STATUS_ID),
                field_name=schema.FUNCTIONAL_STATUS_ID,
            ),
            patient_id=parse_required_text(
                row.get(schema.PATIENT_ID),
                field_name=schema.PATIENT_ID,
            ),
            assessment_date=parse_required_date(
                row.get(schema.ASSESSMENT_DATE),
                field_name=schema.ASSESSMENT_DATE,
            ),
            assessed_by_user_id=parse_required_text(
                row.get(schema.ASSESSED_BY_USER_ID),
                field_name=schema.ASSESSED_BY_USER_ID,
            ),
            mobility=parse_optional_text(
                row.get(schema.MOBILITY),
                field_name=schema.MOBILITY,
            ),
            transfers=parse_optional_text(
                row.get(schema.TRANSFERS),
                field_name=schema.TRANSFERS,
            ),
            bathing=parse_optional_text(
                row.get(schema.BATHING),
                field_name=schema.BATHING,
            ),
            dressing=parse_optional_text(
                row.get(schema.DRESSING),
                field_name=schema.DRESSING,
            ),
            toileting=parse_optional_text(
                row.get(schema.TOILETING),
                field_name=schema.TOILETING,
            ),
            eating=parse_optional_text(
                row.get(schema.EATING),
                field_name=schema.EATING,
            ),
            continence=parse_optional_text(
                row.get(schema.CONTINENCE),
                field_name=schema.CONTINENCE,
            ),
            cognition=parse_optional_text(
                row.get(schema.COGNITION),
                field_name=schema.COGNITION,
            ),
            fall_risk=parse_optional_text(
                row.get(schema.FALL_RISK),
                field_name=schema.FALL_RISK,
            ),
            notes=parse_optional_text(
                row.get(schema.NOTES),
                field_name=schema.NOTES,
            ),
        )


    @staticmethod
    def to_row(
        functional_status: FunctionalStatus,
    ) -> RawRow:
        schema = FunctionalStatusColumns

        return {

            schema.FUNCTIONAL_STATUS_ID:
                functional_status.functional_status_id,

            schema.PATIENT_ID:
                functional_status.patient_id,

            schema.ASSESSMENT_DATE:
                functional_status.assessment_date,

            schema.ASSESSED_BY_USER_ID:
                functional_status.assessed_by_user_id,

            schema.MOBILITY:
                functional_status.mobility,

            schema.TRANSFERS:
                functional_status.transfers,

            schema.BATHING:
                functional_status.bathing,

            schema.DRESSING:
                functional_status.dressing,

            schema.TOILETING:
                functional_status.toileting,

            schema.EATING:
                functional_status.eating,

            schema.CONTINENCE:
                functional_status.continence,

            schema.COGNITION:
                functional_status.cognition,

            schema.FALL_RISK:
                functional_status.fall_risk,

            schema.NOTES:
                functional_status.notes,

        }