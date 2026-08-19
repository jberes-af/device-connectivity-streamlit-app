# /src/interface_adapters/view_models/common/tab_view_model.py

from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class TabItemViewModel(Generic[T]):
    tab_id: str
    label: str
    content: T


@dataclass(frozen=True, slots=True)
class TabViewModel(Generic[T]):
    tabs: tuple[TabItemViewModel[T], ...]