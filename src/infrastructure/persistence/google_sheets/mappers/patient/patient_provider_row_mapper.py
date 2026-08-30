# /src/infrastructure/persistence/google_sheets/mappers/treatment/patient_provide_row_mapper.py

from src.domain.enums.access.status_and_method_enums import PatientProviderRoleEnum
from src.domain.entities.person.patient_entities import PatientProvider

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.patient.patient_provider_columns import (
    PatientProviderColumns)

from src.infrastructure.persistence.common.utils_parsing import (
    parse_optional_enum,
    parse_optional_date,
    parse_required_text,
)


class PatientProviderRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> PatientProvider:
        schema = PatientProviderColumns

        return PatientProvider(
            patient_provider_id=parse_required_text(
                row.get(schema.PATIENT_PROVIDER_ID),
                field_name=schema.PATIENT_PROVIDER_ID,
            ),
            patient_id=parse_required_text(
                row.get(schema.PATIENT_ID),
                field_name=schema.PATIENT_ID,
            ),
            provider_id=parse_required_text(
                row.get(schema.PROVIDER_ID),
                field_name=schema.PROVIDER_ID,
            ),
            role=parse_optional_enum(
                row.get(schema.ROLE),
                enum_type=PatientProviderRoleEnum,
                field_name=schema.ROLE,
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
