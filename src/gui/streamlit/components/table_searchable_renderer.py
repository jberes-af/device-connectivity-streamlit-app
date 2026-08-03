# /src/gui/streamlit/components/table_searchable_renderer.py

import pandas as pd
import streamlit as st


def render_searchable_table(
    dataframe: pd.DataFrame,
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
