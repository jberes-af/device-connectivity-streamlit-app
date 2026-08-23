# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.r_tm_medical_necessity_columns import RTMMedicalNecessityColumns

from src.domain.entities.entities import RTMMedicalNecessity

from src.infrastructure.persistence.common.utils_parsing import *


class RTMMedicalNecessityRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> RTMMedicalNecessity:
        schema = RTMMedicalNecessityColumns

        return RTMMedicalNecessity(
            medical_necessity_id=parse_required_text(
                row.get(schema.RTM_NECESSITY_ID),
                field_name=schema.RTM_NECESSITY_ID,
            ),
            patient_id=parse_required_text(
                row.get(schema.PATIENT_ID),
                field_name=schema.PATIENT_ID,
            ),
            rtm_program_id=parse_required_text(
                row.get(schema.RTM_PROGRAM_ID),
                field_name=schema.RTM_PROGRAM_ID,
            ),
            treatment_plan_id=parse_required_text(
                row.get(schema.TREATMENT_PLAN_ID),
                field_name=schema.TREATMENT_PLAN_ID,
            ),
            primary_diagnosis_code=parse_required_text(
                row.get(schema.PRIMARY_DIAGNOSIS_CODE),
                field_name=schema.PRIMARY_DIAGNOSIS_CODE,
            ),
            secondary_diagnosis_codes=parse_tuple(
                row.get(schema.SECONDARY_DIAGNOSIS_CODES),
                field_name=schema.SECONDARY_DIAGNOSIS_CODES,
            ),
            clinical_indications=parse_tuple(
                row.get(schema.CLINICAL_INDICATIONS),
                field_name=schema.CLINICAL_INDICATIONS,
            ),
            clinical_indication_notes=parse_optional_text(
                row.get(schema.CLINICAL_INDICATION_NOTES),
                field_name=schema.CLINICAL_INDICATION_NOTES,
            ),
            monitoring_reasons=parse_tuple(
                row.get(schema.MONITORING_REASONS),
                field_name=schema.MONITORING_REASONS,
            ),
            monitoring_rationale=parse_required_text(
                row.get(schema.MONITORING_RATIONALE),
                field_name=schema.MONITORING_RATIONALE,
            ),
            expected_clinical_benefit=parse_required_text(
                row.get(schema.EXPECTED_CLINICAL_BENEFIT),
                field_name=schema.EXPECTED_CLINICAL_BENEFIT,
            ),
            intended_clinical_uses=parse_tuple(
                row.get(schema.INTENDED_CLINICAL_USES),
                field_name=schema.INTENDED_CLINICAL_USES,
            ),
            determined_by_provider_id=parse_required_text(
                row.get(schema.DETERMINED_BY_PROVIDER_ID),
                field_name=schema.DETERMINED_BY_PROVIDER_ID,
            ),
            determined_at=parse_required_datetime(
                row.get(schema.DETERMINED_AT),
                field_name=schema.DETERMINED_AT,
            ),
            is_attested=parse_optional_text(
                row.get(schema.IS_ATTESTED),
                field_name=schema.IS_ATTESTED,
            ),
            attestation_version=parse_required_text(
                row.get(schema.ATTESTATION_VERSION),
                field_name=schema.ATTESTATION_VERSION,
            ),
            effective_from=parse_required_datetime(
                row.get(schema.EFFECTIVE_FROM),
                field_name=schema.EFFECTIVE_FROM,
            ),
            effective_to=parse_optional_datetime(
                row.get(schema.EFFECTIVE_TO),
                field_name=schema.EFFECTIVE_TO,
            ),
            status=parse_optional_text(
                row.get(schema.STATUS),
                field_name=schema.STATUS,
            ),
            last_reviewed_at=parse_optional_datetime(
                row.get(schema.LAST_REVIEWED_AT),
                field_name=schema.LAST_REVIEWED_AT,
            ),
            last_reviewed_by_provider_id=parse_optional_text(
                row.get(schema.LAST_REVIEWED_BY_PROVIDER_ID),
                field_name=schema.LAST_REVIEWED_BY_PROVIDER_ID,
            ),
        )


    @staticmethod
    def to_row(
        r_tm_medical_necessity: RTMMedicalNecessity,
    ) -> RawRow:
        schema = RTMMedicalNecessityColumns

        return {

            schema.RTM_NECESSITY_ID:
                r_tm_medical_necessity.rtm_necessity_id,

            schema.PATIENT_ID:
                r_tm_medical_necessity.patient_id,

            schema.RTM_PROGRAM_ID:
                r_tm_medical_necessity.rtm_program_id,

            schema.TREATMENT_PLAN_ID:
                r_tm_medical_necessity.treatment_plan_id,

            schema.PRIMARY_DIAGNOSIS_CODE:
                r_tm_medical_necessity.primary_diagnosis_code,

            schema.SECONDARY_DIAGNOSIS_CODES:
                r_tm_medical_necessity.secondary_diagnosis_codes,

            schema.CLINICAL_INDICATIONS:
                r_tm_medical_necessity.clinical_indications,

            schema.CLINICAL_INDICATION_NOTES:
                r_tm_medical_necessity.clinical_indication_notes,

            schema.MONITORING_REASONS:
                r_tm_medical_necessity.monitoring_reasons,

            schema.MONITORING_RATIONALE:
                r_tm_medical_necessity.monitoring_rationale,

            schema.EXPECTED_CLINICAL_BENEFIT:
                r_tm_medical_necessity.expected_clinical_benefit,

            schema.INTENDED_CLINICAL_USES:
                r_tm_medical_necessity.intended_clinical_uses,

            schema.DETERMINED_BY_PROVIDER_ID:
                r_tm_medical_necessity.determined_by_provider_id,

            schema.DETERMINED_AT:
                r_tm_medical_necessity.determined_at.isoformat(),

            schema.IS_ATTESTED:
                r_tm_medical_necessity.is_attested,

            schema.ATTESTATION_VERSION:
                r_tm_medical_necessity.attestation_version,

            schema.EFFECTIVE_FROM:
                r_tm_medical_necessity.effective_from.isoformat(),

            schema.EFFECTIVE_TO:
                r_tm_medical_necessity.effective_to.isoformat(),

            schema.STATUS:
                r_tm_medical_necessity.status,

            schema.LAST_REVIEWED_AT:
                r_tm_medical_necessity.last_reviewed_at.isoformat(),

            schema.LAST_REVIEWED_BY_PROVIDER_ID:
                r_tm_medical_necessity.last_reviewed_by_provider_id,

        }