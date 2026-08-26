# /src/interface_adapters/view_models/widgets/badge_view_model.py

from dataclasses import dataclass
from enum import StrEnum


class BadgeVariant(StrEnum):
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"
    INFO = "info"
    NEUTRAL = "neutral"


@dataclass(frozen=True)
class BadgeViewModel:
    label: str
    variant: BadgeVariant = BadgeVariant.NEUTRAL
