# /src/gui/streamlit/components/table_searchable_renderer.py

import pandas as pd
import streamlit as st

from src.interface_adapters.view_models.widgets.table_view_model import (
    TableViewModel,
)

_SELECTED_DOMAIN_ID_KEY = "selected_domain_id"

_TABLE_HEIGHT: int = 200

def render_searchable_table(
        view_model: TableViewModel,
        *,
        key: str,
        domain_id_column: str,
        placeholder: str = "Search table...",
) -> str | None:

    col1, _ = st.columns([1, 1])

    with col1:

        search_text = st.text_input(
            "Search",
            key=f"{key}_search",
            placeholder=placeholder,
            label_visibility="collapsed",
        )

    dataframe = _to_dataframe(view_model)
    filtered_dataframe = dataframe

    if search_text:
        normalized_search = search_text.strip().casefold()

        matches = dataframe.astype(str).apply(
            lambda column: column.str.casefold().str.contains(
                normalized_search,
                regex=False,
                na=False,
            )
        )

        filtered_dataframe = dataframe[
            matches.any(axis=1)
        ]

    st.caption(
        f"Showing {len(filtered_dataframe):,} "
        f"of {len(dataframe):,} records"
    )

    event = st.dataframe(
        filtered_dataframe,
        width="stretch",
        hide_index=True,
        height=_TABLE_HEIGHT,
        key=f"{key}_table",
        on_select="rerun",
        selection_mode="single-row",
    )

    session_key = f"{key}_selected_domain_id"

    selected_rows = event.selection.rows

    if selected_rows:
        selected_row_index = selected_rows[0]

        selected_domain_id = str(
            filtered_dataframe.iloc[
                selected_row_index
            ][domain_id_column]
        )

        st.session_state[session_key] = selected_domain_id

    return st.session_state.get(session_key)


def _to_dataframe(
        view_model: TableViewModel,
) -> pd.DataFrame:
    rows = []

    for row in view_model.rows:
        rows.append(
            {
                view_model.row_label_header: row.label,
                **{
                    header: cell.value
                    for header, cell in zip(
                        view_model.column_headers,
                        row.cells,
                    )
                },
            }
        )

    return pd.DataFrame(rows)


"""
def render_searchable_table(
    view_model: TableViewModel,
    *,
    key: str,
    placeholder: str = "Search table...",
) -> None:

    search_text = st.text_input(
        "Search",
        key=f"{key}_search",
        placeholder=placeholder,
        label_visibility="collapsed",
    )

    filtered_dataframe = dataframe.copy()

    if search_text:
        normalized_search = search_text.strip().casefold()

        row_matches = filtered_dataframe.astype(str).apply(
            lambda column: column.str.casefold().str.contains(
                normalized_search,
                regex=False,
                na=False,
            )
        )

        filtered_dataframe = filtered_dataframe[
            row_matches.any(axis=1)
        ]

    st.caption(
        f"Showing {len(filtered_dataframe):,} "
        f"of {len(dataframe):,} records"
    )

    st.dataframe(
        filtered_dataframe,
        width="stretch",
        hide_index=True,
        key=f"{key}_table",
    )
"""
