# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.diagnosis_profile_columns import DiagnosisProfileColumns

from src.domain.entities.entities import DiagnosisProfile

from src.infrastructure.persistence.common.utils_parsing import *


class DiagnosisProfileRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> DiagnosisProfile:
        schema = DiagnosisProfileColumns

        return DiagnosisProfile(
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
        diagnosis_profile: DiagnosisProfile,
    ) -> RawRow:
        schema = DiagnosisProfileColumns

        return {

            schema.DIAGNOSIS_ID:
                diagnosis_profile.diagnosis_id,

            schema.DIAGNOSIS_NAME:
                diagnosis_profile.diagnosis_name,

            schema.DIAGNOSIS_DESCRIPTION:
                diagnosis_profile.diagnosis_description,

        }