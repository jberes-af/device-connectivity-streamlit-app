# /src/infrastructure/persistence/schemas

class RTMMedicalNecessityColumns:
    MEDICAL_NECESSITY_ID: str = "medical_necessity_id"
    PATIENT_ID: str = "patient_id"
    RTM_PROGRAM_ID: str = "rtm_program_id"
    TREATMENT_PLAN_ID: str = "treatment_plan_id"
    PRIMARY_DIAGNOSIS_CODE: str = "primary_diagnosis_code"
    SECONDARY_DIAGNOSIS_CODES: str = "secondary_diagnosis_codes"
    CLINICAL_INDICATIONS: str = "clinical_indications"
    CLINICAL_INDICATION_NOTES: str = "clinical_indication_notes"
    MONITORING_REASONS: str = "monitoring_reasons"
    MONITORING_RATIONALE: str = "monitoring_rationale"
    EXPECTED_CLINICAL_BENEFIT: str = "expected_clinical_benefit"
    INTENDED_CLINICAL_USES: str = "intended_clinical_uses"
    DETERMINED_BY_PROVIDER_ID: str = "determined_by_provider_id"
    DETERMINED_AT: str = "determined_at"
    IS_ATTESTED: str = "is_attested"
    ATTESTATION_VERSION: str = "attestation_version"
    EFFECTIVE_FROM: str = "effective_from"
    EFFECTIVE_TO: str = "effective_to"
    STATUS: str = "status"
    LAST_REVIEWED_AT: str = "last_reviewed_at"
    LAST_REVIEWED_BY_PROVIDER_ID: str = "last_reviewed_by_provider_id"
    ORDER = (
MEDICAL_NECESSITY_ID,
PATIENT_ID,
RTM_PROGRAM_ID,
TREATMENT_PLAN_ID,
PRIMARY_DIAGNOSIS_CODE,
SECONDARY_DIAGNOSIS_CODES,
CLINICAL_INDICATIONS,
CLINICAL_INDICATION_NOTES,
MONITORING_REASONS,
MONITORING_RATIONALE,
EXPECTED_CLINICAL_BENEFIT,
INTENDED_CLINICAL_USES,
DETERMINED_BY_PROVIDER_ID,
DETERMINED_AT,
IS_ATTESTED,
ATTESTATION_VERSION,
EFFECTIVE_FROM,
EFFECTIVE_TO,
STATUS,
LAST_REVIEWED_AT,
LAST_REVIEWED_BY_PROVIDER_ID,
)