# /src/interface_adapters/view_models/widgets/table_view_model.py

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TableCellViewModel:
    value: str


@dataclass(frozen=True, slots=True)
class TableRowViewModel:
    row_key: str
    label: str
    cells: tuple[TableCellViewModel, ...]


@dataclass(frozen=True, slots=True)
class TableViewModel:
    title: str
    row_label_header: str
    column_headers: tuple[str, ...]
    rows: tuple[TableRowViewModel, ...]
