# /src/domain/entities/payer_entities.py

from dataclasses import dataclass

from src.domain.enums.billing.payer_enums import PayerType


@dataclass(frozen=True)
class PayerProfile:
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
