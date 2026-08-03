# /src/interface_adapters/view_models/common/card_grid_view_model.py

from dataclasses import dataclass

from src.interface_adapters.view_models.common.card_view_model import (
    CardViewModel,
)

@dataclass(frozen=True)
class CardGridViewModel:
    columns: int = 3

    cards: tuple[
        CardViewModel,
        ...
    ] = ()
