# /src/interface_adapters/view_models/widgets/tab_view_model.py

from dataclasses import dataclass
from typing import Generic, TypeVar

from src.interface_adapters.view_models.sensing.resident_sensing_view_model import (
    SENSING_SEGMENT_ORDER,
)

from src.interface_adapters.view_models.resident.resident_main_view_model import (
    TREATMENT_SEGMENT_ORDER,
)

T = TypeVar("T")

SegmentNames = (
        SENSING_SEGMENT_ORDER
        | TREATMENT_SEGMENT_ORDER
)


@dataclass(frozen=True, slots=True)
class TabItemViewModel(Generic[T]):
    tab_id: str | SegmentNames
    label: str
    content: T


@dataclass(frozen=True, slots=True)
class TabViewModel(Generic[T]):
    tabs: tuple[TabItemViewModel[T], ...]
