# AUTO GENERATED

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.patient.patient_payer_columns import (
    PatientPayerColumns)

from src.domain.entities.patient_entities import PatientPayer

from src.infrastructure.persistence.common.utils_parsing import *

class PatientPayerRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> PatientPayer:

        schema = PatientPayerColumns

        return PatientPayer(
            patient_payer_id=parse_required_text(
                row.get(schema.PATIENT_PAYER_ID),
                field_name=schema.PATIENT_PAYER_ID,
            ),
            patient_id=parse_required_text(
                row.get(schema.PATIENT_ID),
                field_name=schema.PATIENT_ID,
            ),
            payer_id=parse_required_text(
                row.get(schema.PAYER_ID),
                field_name=schema.PAYER_ID,
            ),
            member_id=parse_required_text(
                row.get(schema.MEMBER_ID),
                field_name=schema.MEMBER_ID,
            ),
            group_number=parse_optional_text(
                row.get(schema.GROUP_NUMBER),
                field_name=schema.GROUP_NUMBER,
            ),
            is_primary=parse_optional_bool(
                row.get(schema.IS_PRIMARY),
                field_name=schema.IS_PRIMARY,
            ),
            effective_date=parse_optional_date(
                row.get(schema.EFFECTIVE_DATE),
                field_name=schema.EFFECTIVE_DATE,
            ),
            termination_date=parse_optional_date(
                row.get(schema.TERMINATION_DATE),
                field_name=schema.TERMINATION_DATE,
            ),
        )