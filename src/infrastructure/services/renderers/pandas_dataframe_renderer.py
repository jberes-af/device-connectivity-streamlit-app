# /src/infrastructure/services/renderers/pandas_dataframe_renderer.py

import pandas as pd

from src.interface_adapters.view_models.common.table_view_model import (
    TableViewModel,
)


class PandasDataFrameRenderer:
    def to_dataframe(
            self,
            table: TableViewModel,
    ) -> pd.DataFrame:
        expected_cell_count = len(table.column_headers)

        data: list[list[str]] = []

        for row in table.rows:
            if len(row.cells) != expected_cell_count:
                raise ValueError(
                    f"Table row {row.row_key!r} has "
                    f"{len(row.cells)} cells; expected "
                    f"{expected_cell_count}."
                )

            cell_values = [
                cell.value
                for cell in row.cells
            ]

            data.append(
                [
                    row.label,
                    *cell_values,
                ]
            )

        headers = [
            table.row_label_header,
            *table.column_headers,
        ]

        return pd.DataFrame(
            data=data,
            columns=headers,
        )


class TransposedPandasDataFrameRenderer:
    def __init__(
            self,
            base_renderer: PandasDataFrameRenderer | None = None,
    ) -> None:
        self._base_renderer = (
                base_renderer or PandasDataFrameRenderer()
        )

    def to_dataframe(
            self,
            table: TableViewModel,
    ) -> pd.DataFrame:
        dataframe = self._base_renderer.to_dataframe(table)

        return (
            dataframe
            .set_index(table.row_label_header)
            .transpose()
            .reset_index(names="Field")
        )
