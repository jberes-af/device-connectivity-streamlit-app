# /src/gui/streamlit/components/grids/grid_card_multi_renderer.py

import streamlit as st

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel,
)


def render_two_part_button_card_grid(
        view_model: CardGridViewModel,
        *,
        key: str,
) -> str | None:
    if not view_model.cards:
        return None

    columns = st.columns(view_model.columns)

    for index, card in enumerate(view_model.cards):
        with columns[index % view_model.columns]:
            with st.container(border=True):
                st.subheader(card.title)
                st.write(card.card_text)

                if st.button(
                        card.button_label,
                        key=f"{key}_{card.button_key}",
                        width="stretch",
                ):
                    return card.id

    return None


def render_card_grid(
        view_model: CardGridViewModel,
        *,
        key: str,
) -> str | None:
    if not view_model.cards:
        return None

    columns = st.columns(view_model.columns)

    for index, card in enumerate(view_model.cards):
        with columns[index % view_model.columns]:
            with st.container(border=True):
                st.subheader(card.title)
                st.write(card.card_text)

                if st.button(
                        card.button_label,
                        key=f"{key}_{card.button_key}",
                        width="stretch",
                ):
                    return card.id

    return None


def render_metric_card_grid(
        view_model: CardGridViewModel,
) -> str | None:
    if not view_model.cards:
        return None

    columns = st.columns(view_model.columns)

    for index, card in enumerate(view_model.cards):
        with columns[index % view_model.columns]:
            st.metric(
                label=card.label,
                value=card.value,
                delta=card.delta,
                help=card.help_text,
                border=False,
            )

    return None
