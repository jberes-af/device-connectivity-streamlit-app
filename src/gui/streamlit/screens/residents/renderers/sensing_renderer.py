# /src/gui/streamlit/screens/residents/renderers/sensing_renderer.py

import streamlit as st

from src.interface_adapters.view_models.residents.sensing.resident_sensing_view_model import (
    SensorSectionViewModel,
)

from src.gui.streamlit.components.cards.card_attribute_renderer_vertical import (
    render_attribute_card
)

from src.interface_adapters.view_models.widgets.card_view_models import (
    CardAttributeNameCountListViewModel,
)


def render_resident_sensing(
        resident_id: str,
        section_dash_vm: SensorSectionViewModel,
) -> None:
    st.markdown(f"#### {section_dash_vm.section_header}")

    # --- DASHBOARD CARDS

    dash_card_view_models: tuple[CardAttributeNameCountListViewModel, ...]
    dash_card_view_models = section_dash_vm.dash_card_grid_vm.cards

    columns = st.columns(int(section_dash_vm.dash_card_grid_vm.columns))

    for i, vm in enumerate(dash_card_view_models):
        with columns[i % len(columns)]:
            render_attribute_card(
                id=vm.id,
                title=vm.title,
                attribute_count=vm.attribute_count,
                attributes=vm.attributes,
                key=f"{vm.id}_{i}",
            )

    # --- DETAIL TABS

    st.write("")

    tabs_vm = section_dash_vm.sensing_detail_section_vm

    tabs = st.tabs(
        [tab.label for tab in tabs_vm.tabs]
    )

    for tab_container, tab_vm in zip(
            tabs,
            tabs_vm.tabs,
            strict=True,
    ):
        with tab_container:
            st.write(tab_vm.content)
