# /src/infrastructure/persistence/google_sheets/mappers/diagnosis/diagnosis_definition_row_mapper.py

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.diagnosis.diagnosis_definition_columns import (
    DiagnosisDefinitionColumns
)

from src.domain.entities.care.diagnosis_entities import DiagnosisDefinition

from src.infrastructure.persistence.common.utils_parsing import *


class DiagnosisDefinitionRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> DiagnosisDefinition:
        schema = DiagnosisDefinitionColumns

        return DiagnosisDefinition(
            diagnosis_id=parse_required_text(
                row.get(schema.DIAGNOSIS_ID),
                field_name=schema.DIAGNOSIS_ID,
            ),
            diagnosis_name=parse_required_text(
                row.get(schema.DIAGNOSIS_NAME),
                field_name=schema.DIAGNOSIS_NAME,
            ),
            diagnosis_description=parse_required_text(
                row.get(schema.DIAGNOSIS_DESCRIPTION),
                field_name=schema.DIAGNOSIS_DESCRIPTION,
            ),
        )

    @staticmethod
    def to_row(
            diagnosis_profile: DiagnosisDefinition,
    ) -> RawRow:
        schema = DiagnosisDefinitionColumns

        return {

            schema.DIAGNOSIS_ID:
                diagnosis_profile.diagnosis_id,

            schema.DIAGNOSIS_NAME:
                diagnosis_profile.diagnosis_name,

            schema.DIAGNOSIS_DESCRIPTION:
                diagnosis_profile.diagnosis_description,

        }
