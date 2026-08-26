# /src/application/use_cases/residents/payer/payer_profile_uc_dtos.py

from dataclasses import dataclass

from src.domain.enums.billing.payer_enums import PayerType


@dataclass(frozen=True)
class PayerProfileDTO:
    payer_id: str
    payer_name: str
    payer_type: PayerType
    electronic_payer_id: str | None
    claims_address_line_1: str | None
    claims_address_line_2: str | None
    city: str | None
    state: str | None
    postal_code: str | None
    telephone: str | None
    website: str | None
    accepts_electronic_claims: bool


# --- USE CASE

@dataclass(frozen=True)
class GetPayerProfileRequestDTO:
    payer_id: str


@dataclass(frozen=True)
class GetPayerProfileResultDTO:
    payer_profile: PayerProfileDTO
