# /src/interface_adapters/view_models/widgets/card_view_models.py

from dataclasses import dataclass

from src.interface_adapters.view_models.common.badge_view_model import (
    BadgeViewModel)

from src.interface_adapters.view_models.common.property_field_view_model import (
    PropertyFieldViewModel,
)


@dataclass(frozen=True)
class MetricCardViewModel:
    label: str
    value: str
    delta: str | None = None
    help_text: str | None = None


@dataclass(frozen=True, kw_only=True)
class BaseCardViewModel:
    title: str
    id: str | None = None
    title_icon: str | None = None
    description: str | None = None


# --- DEFAULT CARD

@dataclass(frozen=True, kw_only=True)
class CardPropertyFieldsViewModel(BaseCardViewModel):
    badge: BadgeViewModel | None = None
    property_fields: tuple[PropertyFieldViewModel, ...] = ()
    metrics: tuple[MetricCardViewModel, ...] = ()


# --- ATTRIBUTE CARDS

@dataclass(frozen=True, kw_only=True)
class CardAttributeNameCountListViewModel(BaseCardViewModel):
    attribute_count: str
    attributes: tuple[str, ...]


# --- CARDS WITH BUTTONS

@dataclass(frozen=True, kw_only=True)
class CardPropertyFieldsButtonViewModel(BaseCardViewModel):
    property_fields: tuple[PropertyFieldViewModel, ...]
    button_label: str = "More"
    button_icon: str | None = None

    @property
    def button_key(self) -> str:
        return f"card_{self.id}"


@dataclass(frozen=True, kw_only=True)
class CardTitleTextButtonViewModel(BaseCardViewModel):
    card_text: str
    button_label: str = "Show more"
    button_icon: str | None = None

    @property
    def button_key(self) -> str:
        return f"card_{self.id}"
