# /src/application/use_cases/residents/provider/provider_uc_dtos.py

from dataclasses import dataclass

from src.domain.entities.care.provider_entities import ProviderProfile


# --- USE CASE

@dataclass(frozen=True)
class GetProviderProfileRequestDTO:
    provider_id: str


@dataclass(frozen=True)
class GetProviderProfileResultDTO:
    provider_profile: ProviderProfile
