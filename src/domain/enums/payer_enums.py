# /src/domain/enums/payer_enums.py

from enum import StrEnum


class PayerType(StrEnum):
    MEDICARE = "medicare"
    MEDICAID = "medicaid"
    COMMERCIAL = "commercial"
    MEDICARE_ADVANTAGE = "medicare_advantage"
    MEDICAID_MANAGED_CARE = "medicaid_managed_care"
    WORKERS_COMPENSATION = "workers_compensation"
    SELF_PAY = "self_pay"
    OTHER = "other"
