# /src/infrastructure/persistence/google_sheets/mappers/rtm/rtm_necessity_row_mapper.py

from src.domain.entities.care.rtm_entities import (
    RtmMedicalNecessity,
)

from src.domain.enums.care.rtm_enums import (
    ClinicalIndicationEnum,
    RtmClinicalUseEnum,
    RtmMedicalNecessityStatus,
    RtmMonitoringReasonEnum,
)

from src.infrastructure.persistence.common.types import (
    RawRow,
)

from src.infrastructure.persistence.common.utils_parsing import (
    parse_optional_datetime,
    parse_optional_enum_tuple,
    parse_optional_text,
    parse_optional_text_tuple,
    parse_required_bool,
    parse_required_datetime,
    parse_required_enum,
    parse_required_text,
)

from src.infrastructure.persistence.google_sheets.schemas.rtm.rtm_necessity_columns import (
    RtmNecessityColumns,
)


class RtmNecessityRowMapper:

    @staticmethod
    def to_domain(
            row: RawRow,
    ) -> RtmMedicalNecessity:
        schema = RtmNecessityColumns

        return RtmMedicalNecessity(
            rtm_necessity_id=parse_required_text(
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
            secondary_diagnosis_codes=parse_optional_text_tuple(
                row.get(schema.SECONDARY_DIAGNOSIS_CODES),
                field_name=schema.SECONDARY_DIAGNOSIS_CODES,
            ),
            clinical_indications=parse_optional_enum_tuple(
                row.get(schema.CLINICAL_INDICATIONS),
                enum_type=ClinicalIndicationEnum,
                field_name=schema.CLINICAL_INDICATIONS,
            ),
            clinical_indication_notes=parse_optional_text(
                row.get(schema.CLINICAL_INDICATION_NOTES),
                field_name=schema.CLINICAL_INDICATION_NOTES,
            ),
            monitoring_reasons=parse_optional_enum_tuple(
                row.get(schema.MONITORING_REASONS),
                enum_type=RtmMonitoringReasonEnum,
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
            intended_clinical_uses=parse_optional_enum_tuple(
                row.get(schema.INTENDED_CLINICAL_USES),
                enum_type=RtmClinicalUseEnum,
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
            is_attested=parse_required_bool(
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
            status=parse_required_enum(
                row.get(schema.STATUS),
                enum_type=RtmMedicalNecessityStatus,
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
            medical_necessity: RtmMedicalNecessity,
    ) -> RawRow:
        schema = RtmNecessityColumns

        return {
            schema.RTM_NECESSITY_ID:
                medical_necessity.rtm_necessity_id,

            schema.PATIENT_ID:
                medical_necessity.patient_id,

            schema.RTM_PROGRAM_ID:
                medical_necessity.rtm_program_id,

            schema.TREATMENT_PLAN_ID:
                medical_necessity.treatment_plan_id,

            schema.PRIMARY_DIAGNOSIS_CODE:
                medical_necessity.primary_diagnosis_code,

            schema.SECONDARY_DIAGNOSIS_CODES:
                ",".join(
                    medical_necessity.secondary_diagnosis_codes
                ),

            schema.CLINICAL_INDICATIONS:
                ",".join(
                    indication.value
                    for indication
                    in medical_necessity.clinical_indications
                ),

            schema.CLINICAL_INDICATION_NOTES:
                medical_necessity.clinical_indication_notes or "",

            schema.MONITORING_REASONS:
                ",".join(
                    reason.value
                    for reason
                    in medical_necessity.monitoring_reasons
                ),

            schema.MONITORING_RATIONALE:
                medical_necessity.monitoring_rationale,

            schema.EXPECTED_CLINICAL_BENEFIT:
                medical_necessity.expected_clinical_benefit,

            schema.INTENDED_CLINICAL_USES:
                ",".join(
                    clinical_use.value
                    for clinical_use
                    in medical_necessity.intended_clinical_uses
                ),

            schema.DETERMINED_BY_PROVIDER_ID:
                medical_necessity.determined_by_provider_id,

            schema.DETERMINED_AT:
                medical_necessity.determined_at.isoformat(),

            schema.IS_ATTESTED:
                medical_necessity.is_attested,

            schema.ATTESTATION_VERSION:
                medical_necessity.attestation_version,

            schema.EFFECTIVE_FROM:
                medical_necessity.effective_from.isoformat(),

            schema.EFFECTIVE_TO:
                (
                    medical_necessity.effective_to.isoformat()
                    if medical_necessity.effective_to
                    else ""
                ),

            schema.STATUS:
                medical_necessity.status.value,

            schema.LAST_REVIEWED_AT:
                (
                    medical_necessity.last_reviewed_at.isoformat()
                    if medical_necessity.last_reviewed_at
                    else ""
                ),

            schema.LAST_REVIEWED_BY_PROVIDER_ID:
                (
                        medical_necessity.last_reviewed_by_provider_id
                        or ""
                ),
        }
