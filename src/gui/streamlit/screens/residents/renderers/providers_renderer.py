# /src/gui/streamlit/screens/residents/renderers/providers_renderer.py


from streamlit.elements.lib.column_types import Column

# import logging
import streamlit as st

from src.gui.streamlit.components.cards.card_property_value_renderer_hor import (
    render_card_horizontal_properties,
)

# from src.interface_adapters.view_models.widgets.card_view_models import (
#    MetricCardViewModel,
# )

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel,
)

from src.interface_adapters.view_models.residents.main_page.resident_main_view_model import (
    ResidentProviderViewModel,
)


def render_patient_provider_section(
        resident_id: str,
        view_model: ResidentProviderViewModel,
) -> None:
    st.markdown(f"#### {view_model.section_title}")

    for model in view_model.provider_card_grid:
        _render_content(
            view_model=model,
        )

        st.write("")


def _render_content(
        view_model: CardGridViewModel,
) -> None:
    cols: Column = st.columns(view_model.columns)

    # logging.info("Resident Contact Section Columns %s", cols_p)

    for i, vm in enumerate(view_model.cards):
        with cols[i % len(cols)]:
            render_card_horizontal_properties(
                title=vm.title,
                property_fields=vm.property_fields,
                key=f"{vm.id}_{i}",
            )
