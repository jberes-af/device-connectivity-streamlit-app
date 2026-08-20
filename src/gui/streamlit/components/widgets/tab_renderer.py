# /src/gui/streamlit/components/tab_renderer.py

from collections.abc import Callable

import streamlit as st


def render_tabs(
    *,
    labels: tuple[str, ...],
    renderers: tuple[Callable[[], None], ...],
) -> None:

    if len(labels) != len(renderers):
        raise ValueError(
            "Tab labels and renderers must have the same length."
        )

    tabs = st.tabs(list(labels))

    for tab, render_content in zip(
        tabs,
        renderers,
        strict=True,
    ):
        with tab:
            render_content()