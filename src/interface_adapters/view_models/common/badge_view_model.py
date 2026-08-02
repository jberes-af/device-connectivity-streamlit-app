# /src/interface_adapters/view_models/common/badge_view_model.py

from dataclasses import dataclass
from enum import StrEnum


class BadgeStyle(StrEnum):
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"
    INFO = "info"
    NEUTRAL = "neutral"


@dataclass(frozen=True)
class BadgeViewModel:
    text: str
    style: BadgeStyle = BadgeStyle.NEUTRAL
