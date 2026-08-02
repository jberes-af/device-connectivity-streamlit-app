# /src/interface_adapters/view_models/common/property_grid_view_model.py

from dataclasses import dataclass

from .property_field_view_model import (
    PropertyFieldViewModel,
)


@dataclass(frozen=True)
class PropertyGridViewModel:
    columns: int = 3

    fields: tuple[
        PropertyFieldViewModel,
        ...
    ] = ()
