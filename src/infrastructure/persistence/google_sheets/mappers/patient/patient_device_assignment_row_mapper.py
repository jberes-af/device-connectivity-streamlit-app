# /src/infrastructure/persistence/google_sheets/mappers/treatment/patient_device_assignment_row_mapper.py

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.patient.patient_device_assignment_columns import (
    PatientDeviceAssignmentColumns)

from src.domain.entities.resident.patient_entities import PatientDeviceAssignment

from src.infrastructure.persistence.common.utils_parsing import (
    parse_optional_bool,
    parse_optional_date,
    parse_required_date,
    parse_required_text,
)


class PatientDeviceAssignmentRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> PatientDeviceAssignment:
        schema = PatientDeviceAssignmentColumns

        return PatientDeviceAssignment(
            assignment_id=parse_required_text(
                row.get(schema.ASSIGNMENT_ID),
                field_name=schema.ASSIGNMENT_ID,
            ),
            patient_id=parse_required_text(
                row.get(schema.PATIENT_ID),
                field_name=schema.PATIENT_ID,
            ),
            device_id=parse_required_text(
                row.get(schema.DEVICE_ID),
                field_name=schema.DEVICE_ID,
            ),
            assigned_date=parse_required_date(
                row.get(schema.ASSIGNED_DATE),
                field_name=schema.ASSIGNED_DATE,
            ),
            removed_date=parse_optional_date(
                row.get(schema.REMOVED_DATE),
                field_name=schema.REMOVED_DATE,
            ),
            setup_completed=parse_optional_bool(
                row.get(schema.SETUP_COMPLETED),
                field_name=schema.SETUP_COMPLETED,
            ),
            setup_date=parse_optional_date(
                row.get(schema.SETUP_DATE),
                field_name=schema.SETUP_DATE,
            ),
            patient_education_completed=parse_optional_bool(
                row.get(schema.PATIENT_EDUCATION_COMPLETED),
                field_name=schema.PATIENT_EDUCATION_COMPLETED,
            ),
            patient_education_date=parse_optional_date(
                row.get(schema.PATIENT_EDUCATION_DATE),
                field_name=schema.PATIENT_EDUCATION_DATE,
            ),
        )
