# /src/application/use_cases/residents/payer/patient_payer_uc_dtos.py

from dataclasses import dataclass
from datetime import date

from src.domain.enums.billing.payer_enums import PayerType


@dataclass(frozen=True)
class PayerContactDTO:
    claims_address_line_1: str | None
    claims_address_line_2: str | None
    city: str | None
    state: str | None
    postal_code: str | None
    telephone: str | None
    website: str | None
    electronic_payer_id: str | None
    accepts_electronic_claims: bool


@dataclass(frozen=True)
class PatientPayerProfileDTO:
    patient_payer_id: str
    payer_id: str
    payer_name: str
    payer_type: PayerType
    member_id: str | None
    group_number: str | None
    effective_date: date | None
    termination_date: date | None
    is_primary: bool
    payer_contact: PayerContactDTO


@dataclass(frozen=True)
class GetPatientPayerProfileRequestDTO:
    patient_id: str


@dataclass(frozen=True)
class GetPatientPayerProfileResultDTO:
    patient_payer_profiles: tuple[PatientPayerProfileDTO, ...]
