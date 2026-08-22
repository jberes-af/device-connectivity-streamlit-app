# /src/gui/streamlit/components/widgets/grid_card_property_fields_button_renderer.py

import streamlit as st

from src.gui.streamlit.components.cards.card_property_fields_button_renderer_vertical import (
    render_dashboard_card,
)

from src.interface_adapters.view_models.common.card_grid_view_model import (
    CardGridViewModel
)


def render_grid_card_properties_button(view_model: CardGridViewModel) -> None:
    columns = st.columns(int(view_model.columns))

    for i, vm in enumerate(view_model.cards):
        with columns[i % len(columns)]:
            render_dashboard_card(
                # id=vm.id,
                title=vm.title,
                # description=vm.description,
                property_fields=vm.property_fields,
                button_label=vm.button_label,
                button_icon=vm.button_icon,
                key=vm.button_key,
            )
