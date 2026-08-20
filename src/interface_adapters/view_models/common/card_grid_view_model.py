# /src/interface_adapters/view_models/widgets/card_grid_view_model.py

from dataclasses import dataclass, field

from src.interface_adapters.view_models.common.card_view_models import (
    CardAttributeNameCountListViewModel,
    CardPropertyFieldsButtonViewModel,
    CardTitleTextButtonViewModel,
    CardPropertyFieldsViewModel,
)

from src.interface_adapters.view_models.common.metric_view_model import (
    MetricViewModel,
)

type CardGridItemViewModel = (
        CardPropertyFieldsViewModel
        | CardAttributeNameCountListViewModel
        | CardPropertyFieldsButtonViewModel
        | CardTitleTextButtonViewModel
        | MetricViewModel
)


@dataclass(frozen=True)
class CardGridViewModel:
    columns: int = 3
    cards: tuple[CardGridItemViewModel, ...] = field(
        default_factory=tuple
    )
