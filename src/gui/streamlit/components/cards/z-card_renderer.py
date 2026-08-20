# /src/gui/streamlit/components/z-card_renderer.py

from scripts.property_grid_renderer import (
    render_property_grid)

from src.gui.streamlit.components.cards.badge_renderer import (
    render_badge,
)

from src.interface_adapters.view_models.common.card_view_models import (
    CardPropertyFieldsViewModel)

import streamlit as st


def render_card(
        card: CardPropertyFieldsViewModel,
):
    with st.container(border=True):

        title = card.title

        if card.icon:
            title = f"{card.icon} {title}"

        st.subheader(title)

        if card.badge:
            render_badge(card.badge)

        if card.property_grid:
            render_property_grid(
                card.property_grid,
            )
