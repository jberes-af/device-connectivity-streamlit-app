# /src/interface_adapters/view_models/common/card_view_model.py

from dataclasses import dataclass

from .badge_view_model import BadgeViewModel
from .property_grid_view_model import (
    PropertyGridViewModel,
)
from .metric_view_model import MetricViewModel


@dataclass(frozen=True)
class CardViewModel:
    title: str

    icon: str | None = None

    badge: BadgeViewModel | None = None

    property_grid: PropertyGridViewModel | None = None

    metrics: tuple[
        MetricViewModel,
        ...
    ] = ()
