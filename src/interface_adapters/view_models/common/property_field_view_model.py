# /src/interface_adapters/view_models/common/property_field_view_model.py

from dataclasses import dataclass
from enum import StrEnum


class PropertyStatus(StrEnum):
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"
    INFO = "info"


@dataclass(frozen=True)
class PropertyFieldViewModel:
    label: str
    value: str
    status: PropertyStatus | None = None
    tooltip: str | None = None
