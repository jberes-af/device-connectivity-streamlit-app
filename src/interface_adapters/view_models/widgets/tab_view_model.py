# /src/interface_adapters/view_models/widgets/tab_view_model.py

from dataclasses import dataclass


@dataclass(frozen=True)
class TabItemViewModel:
    tab_id: str
    label: str
    content: str


@dataclass(frozen=True)
class TabViewModel:
    tabs: tuple[TabItemViewModel, ...] = ()