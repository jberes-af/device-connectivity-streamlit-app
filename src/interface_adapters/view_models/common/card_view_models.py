# /src/interface_adapters/view_models/common/card_view_models.py

from dataclasses import dataclass

from src.interface_adapters.view_models.common.badge_view_model import (
    BadgeViewModel)

from src.interface_adapters.view_models.common.property_grid_view_model import (
    PropertyGridViewModel)

from src.interface_adapters.view_models.common.property_field_view_model import (
    PropertyFieldViewModel,
)

from src.interface_adapters.view_models.common.metric_view_model import (
    MetricViewModel
)


@dataclass(frozen=True)
class CardViewModel:
    title: str
    icon: str | None = None
    badge: BadgeViewModel | None = None
    property_grid: PropertyGridViewModel | None = None
    metrics: tuple[MetricViewModel, ...] = ()


@dataclass(frozen=True)
class CardTitleTextButtonViewModel:
    id: str
    title: str
    description: str
    button_label: str = "Show more"

    @property
    def button_key(self) -> str:
        return f"dashboard_card_{self.id}"


@dataclass(frozen=True)
class CardPropertyFieldsButtonViewModel:
    id: str
    title: str
    property_fields: tuple[PropertyFieldViewModel, ...]
    description: str | None = None
    button_label: str = "More"
    button_icon: str | None = None

    @property
    def button_key(self) -> str:
        return f"dashboard_card_{self.id}"


@dataclass(frozen=True)
class CardAttributeNameCountListViewModel:
    id: str
    title: str
    attribute_count: str
    attributes: tuple[str, ...]
