# /src/application/use_cases/payer/payer_profile_uc_dtos.py

from dataclasses import dataclass

from src.domain.entities.billing.payer_entities import PayerProfile


# --- USE CASE

@dataclass(frozen=True)
class GetPayerProfileRequestDTO:
    payer_id: str


@dataclass(frozen=True)
class GetPayerProfileResultDTO:
    payer_profile: PayerProfile
