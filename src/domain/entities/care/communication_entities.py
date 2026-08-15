# /src/domain/entities/communication_entities.py

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Communication:
    communication_id: str
    patient_id: str
    occurred_at: datetime
    method: CommunicationMethod
    communication_type: CommunicationType
    status: CommunicationStatus
    initiated_by_type: InitiatingPartyType
    initiated_by_id: str | None
    duration_minutes: int | None
    summary: str
    clinical_impact: str | None
    monitoring_period_id: str | None
    provider_review_id: str | None
    counts_toward_rtm_period: bool
    created_by_user_id: str
    created_at: datetime



@dataclass(frozen=True)
class CommunicationParticipant:
    communication_participant_id: str
    communication_id: str
    participant_role: ParticipantRole
    participant_id: str | None
    participant_name: str
    was_present: bool


@dataclass(frozen=True)
class CommunicationMonitoringData:
    communication_monitoring_data_id: str
    communication_id: str
    data_type: MonitoringDataType
    source_record_id: str | None
    summary: str


@dataclass(frozen=True)
class ClinicalCommunicationDecision:
    communication_decision_id: str
    communication_id: str
    decision_type: CommunicationDecisionType
    rationale: str
    follow_up_due_at: datetime | None
    responsible_provider_id: str | None
    completed: bool



@dataclass(frozen=True)
class CommunicationRTMQualification:
    communication_id: str
    was_interactive: bool
    patient_or_caregiver_participated: bool
    clinical_management_occurred: bool
    completed_successfully: bool
    qualifying_minutes: int
    counts_toward_rtm_period: bool
    qualification_notes: str | None
    confirmed_by_provider_id: str | None
    confirmed_at: datetime | None



@dataclass(frozen=True)
class CommunicationAttachment:
    attachment_id: str
    communication_id: str
    file_name: str
    content_type: str
    storage_reference: str
    uploaded_at: datetime