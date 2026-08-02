# AUTO GENERATED

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.patient.patient_diagnosis_columns import (
    PatientDiagnosisColumns)

from src.domain.entities.patient_entities import PatientDiagnosis

from src.infrastructure.persistence.common.utils_parsing import *


class PatientDiagnosisRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> PatientDiagnosis:
        schema = PatientDiagnosisColumns

        return PatientDiagnosis(
            patient_diagnosis_id=parse_required_text(
                row.get(schema.PATIENT_DIAGNOSIS_ID),
                field_name=schema.PATIENT_DIAGNOSIS_ID,
            ),
            patient_id=parse_required_text(
                row.get(schema.PATIENT_ID),
                field_name=schema.PATIENT_ID,
            ),
            diagnosis_id=parse_required_text(
                row.get(schema.DIAGNOSIS_ID),
                field_name=schema.DIAGNOSIS_ID,
            ),
            diagnosed_date=parse_optional_date(
                row.get(schema.DIAGNOSED_DATE),
                field_name=schema.DIAGNOSED_DATE,
            ),
            resolved_date=parse_optional_date(
                row.get(schema.RESOLVED_DATE),
                field_name=schema.RESOLVED_DATE,
            ),
            is_primary=parse_optional_bool(
                row.get(schema.IS_PRIMARY),
                field_name=schema.IS_PRIMARY,
            ),
        )
