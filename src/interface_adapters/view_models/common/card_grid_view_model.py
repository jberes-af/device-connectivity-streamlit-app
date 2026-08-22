# /src/interface_adapters/view_models/widgets/card_grid_view_model.py

from dataclasses import dataclass, field

from src.interface_adapters.view_models.common.card_view_models import (
    CardAttributeNameCountListViewModel,
    CardPropertyFieldsButtonViewModel,
    CardTitleTextButtonViewModel,
    CardPropertyFieldsViewModel, MetricCardViewModel,
)

type CardGridItemViewModel = (
        CardPropertyFieldsViewModel
        | CardAttributeNameCountListViewModel
        | CardPropertyFieldsButtonViewModel
        | CardTitleTextButtonViewModel
        | MetricCardViewModel
)


@dataclass(frozen=True)
class CardGridViewModel:
    columns: int = 3
    cards: tuple[CardGridItemViewModel, ...] = field(
        default_factory=tuple
    )
