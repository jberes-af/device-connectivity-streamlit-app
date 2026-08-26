# /src/gui/streamlit/screens/residents/renderers/resident_contact_renderer.py

from streamlit.elements.lib.column_types import Column

import logging
import streamlit as st

from src.gui.streamlit.components.cards.card_property_value_renderer_hor import (
    render_card_horizontal_properties,
)

from src.interface_adapters.view_models.widgets.card_view_models import (
    CardPropertyFieldsViewModel,
)

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel)

from src.interface_adapters.view_models.residents.main_page.resident_main_view_model import (
    ResidentContactViewModel,
)

logger = logging.getLogger(__name__)


def render_resident_contact_info(
        resident_id: str,
        view_model: ResidentContactViewModel,
) -> None:
    # st.markdown("#### 🚧 Resident")
    st.markdown(f"#### {view_model.section_title}")

    """
    logger.info(
        "ENTER render_resident_resident resident_id=%s",
        resident_id,
    )

    st.warning(
        f"DEBUG: render_resident_resident entered for {resident_id}"
    )
    """

    profile_grid: CardGridViewModel = view_model.resident_profile_card_grid
    contact_grid: CardGridViewModel = view_model.in_case_of_need_card_grid

    # --- RENDER RESIDENT PROFILE INFORMATION

    cols_p: Column = st.columns(profile_grid.columns)

    # logging.info("Resident Contact Section Columns %s", cols_p)

    cards_vm_p: tuple[CardPropertyFieldsViewModel, ...] = profile_grid.cards

    for i, vm in enumerate(cards_vm_p):
        with cols_p[i % len(cols_p)]:
            render_card_horizontal_properties(
                title=vm.title,
                property_fields=vm.property_fields,
                key=f"{vm.id}_{i}",
            )

    # --- RENDER RESIDENT IN-CASE-OF-NEED CONTACT INFO

    cols_c = st.columns(contact_grid.columns)
    cards_vm_c: tuple[CardPropertyFieldsViewModel, ...] = contact_grid.cards
    for i, vm in enumerate(cards_vm_c):
        with cols_c[i % len(cols_c)]:
            render_card_horizontal_properties(
                title=vm.title,
                property_fields=vm.property_fields,
                key=f"{vm.id}_{i}",
            )
