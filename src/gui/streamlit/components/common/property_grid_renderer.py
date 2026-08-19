# /src/gui/streamlit/components/property_grid_renderer.py

from src.gui.streamlit.components.common.property_field_renderer import render_property_field

from src.interface_adapters.view_models.common.property_grid_view_model import (
    PropertyGridViewModel,
)

import streamlit as st


def render_property_grid(
        grid: PropertyGridViewModel,
):
    cols = st.columns(grid.columns)

    for index, field in enumerate(grid.fields):
        with cols[index % grid.columns]:
            render_property_field(field)
