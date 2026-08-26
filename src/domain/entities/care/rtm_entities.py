# /src/domain/treatment/rtm_entities.py

"""
1. What condition does the treatment have?
2. What clinical problem/indication exists?
3. Why is remote monitoring needed?
4. What should be monitored?
5. How will the provider use the information?
6. Who determined medical necessity and when?
"""

from dataclasses import dataclass
from datetime import datetime, date

from src.domain.enums.care.rtm_enums import (
    ClinicalIndicationEnum,
    CommunicationMethod,
    DataReviewedType,
    ParticipantType,
    RtmActivityType,
    RtmClinicalUseEnum,
    RtmMonitoringReasonEnum,
    RtmNecessityStatus,
)

from src.domain.enums.person.patient_enums import (
    EnrollmentStatusEnum,
    ConsentStatusEnum,
    ConsentMethodEnum
)


@dataclass(frozen=True, slots=True)
class RtmMedicalNecessity:
    rtm_necessity_id: str
    patient_id: str
    rtm_program_id: str
    treatment_plan_id: str
    primary_diagnosis_code: str
    secondary_diagnosis_codes: tuple[str, ...]
    clinical_indications: tuple[ClinicalIndicationEnum, ...]
    clinical_indication_notes: str | None
    monitoring_reasons: tuple[RtmMonitoringReasonEnum, ...]
    monitoring_rationale: str
    expected_clinical_benefit: str
    intended_clinical_uses: tuple[RtmClinicalUseEnum, ...]
    determined_by_provider_id: str
    determined_at: datetime
    is_attested: bool
    attestation_version: str
    effective_from: datetime
    effective_to: datetime | None
    status: RtmNecessityStatus
    last_reviewed_at: datetime | None = None
    last_reviewed_by_provider_id: str | None = None


@dataclass(frozen=True, slots=True)
class RtmClinicalActivity:
    activity_id: str
    patient_id: str
    rtm_program_id: str
    provider_id: str
    occurred_at: datetime
    duration_minutes: int
    activity_type: RtmActivityType
    findings: str | None
    clinical_assessment: str | None
    intervention: str | None
    follow_up: str | None
    treatment_modified: bool
    created_at: datetime
    created_by_user_id: str


@dataclass(frozen=True, slots=True)
class ReviewedDataItem:
    reviewed_data_item_id: str
    activity_id: str
    data_type: DataReviewedType
    source_record_id: str


@dataclass(frozen=True, slots=True)
class RtmInteraction:
    interaction_id: str
    activity_id: str
    participant_type: ParticipantType
    participant_id: str | None
    communication_method: CommunicationMethod
    is_real_time: bool
    occurred_at: datetime
    duration_minutes: int
    summary: str


@dataclass(frozen=True)
class RtmEnrollment:
    enrollment_id: str
    patient_id: str
    enrollment_status: EnrollmentStatusEnum
    enrollment_date: date
    service_start_date: date
    service_end_date: date | None
    consent_status: ConsentStatusEnum
    consent_obtained_at: datetime | None
    consent_method: ConsentMethodEnum | None
    consent_document_reference: str | None
    discontinuation_reason: str | None
