# /src/domain/entities/provider_entities.py

from dataclasses import dataclass
from datetime import date, datetime

from src.domain.enums.provider_enums import (
    ClinicalFindingType,
    CommunicationMethod,
    DataReviewedType,
    ReviewStatus,
    TimeCategory,
)


@dataclass(frozen=True)
class Provider:
    provider_id: str
    national_provider_identifier: str | None
    first_name: str
    middle_name: str | None
    last_name: str
    credentials: str | None
    specialty: str | None
    organization_id: str | None
    telephone: str | None
    email: str | None
    address_line_1: str | None
    address_line_2: str | None
    city: str | None
    state: str | None
    postal_code: str | None
    is_active: bool


@dataclass(frozen=True)
class ProviderReview:
    review_id: str
    patient_id: str
    measurement_period_id: str
    reviewing_provider_id: str
    reviewed_at: datetime
    started_at: datetime
    completed_at: datetime
    review_status: ReviewStatus
    total_elapsed_minutes: int
    billable_minutes: int


@dataclass(frozen=True)
class ClinicalFinding:
    clinical_finding_id: str
    review_id: str
    finding_type: ClinicalFindingType
    summary: str


@dataclass(frozen=True)
class ProviderCommunication:
    communication_id: str
    patient_id: str
    provider_id: str
    occurred_at: datetime
    communication_method: CommunicationMethod
    duration_minutes: int
    summary: str



@dataclass(frozen=True)
class ReviewTimeEntry:
    time_entry_id: str
    review_id: str
    category: TimeCategory
    minutes: int


@dataclass(frozen=True)
class ReviewedDataItem:
    reviewed_data_item_id: str
    review_id: str
    data_type: DataReviewedType
