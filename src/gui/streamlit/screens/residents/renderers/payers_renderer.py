# /src/gui/streamlit/screens/residents/renderers/payers_renderer.py

from typing import Sequence

import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from src.gui.streamlit.components.cards.card_property_value_renderer_hor import (
    render_card_horizontal_properties,
)

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel,
)

from src.interface_adapters.view_models.widgets.tab_view_model import (
    TabViewModel,
)

from src.interface_adapters.view_models.residents.main_page.resident_main_view_model import (
    ResidentPayerAndRtmEnrollmentSectionViewModel,
)


def render_resident_payers_and_rtm_enrollment(
        *,
        view_model: ResidentPayerAndRtmEnrollmentSectionViewModel,
) -> None:
    st.markdown(
        f"#### {view_model.section_title}"
    )

    tabs = _render_tab_widget(
        tabs_vm=view_model.section_tabs,
    )

    patient_payers_tab, rtm_enrollment_tab = tabs

    _render_patient_payers_tab(
        tab=patient_payers_tab,
        models=(
            view_model
            .patient_payers
            .patient_payer_card_grids
        ),
    )

    _render_rtm_enrollment_tab(
        tab=rtm_enrollment_tab,
        model=(
            view_model
            .rtm_enrollment
            .enrollment_card_grid
        ),
    )


def _render_tab_widget(
        *,
        tabs_vm: TabViewModel,
) -> Sequence[DeltaGenerator]:
    return st.tabs(
        [tab.label for tab in tabs_vm.tabs]
    )


def _render_patient_payers_tab(
        *,
        tab: DeltaGenerator,
        models: tuple[CardGridViewModel, ...],
) -> None:
    with tab:
        for model in models:
            _render_card_grid(
                view_model=model,
            )

            st.write("")


def _render_rtm_enrollment_tab(
        *,
        tab: DeltaGenerator,
        model: CardGridViewModel,
) -> None:
    with tab:
        _render_card_grid(
            view_model=model,
        )


def _render_card_grid(
        *,
        view_model: CardGridViewModel,
) -> None:
    if not view_model.cards:
        return

    columns = st.columns(
        view_model.columns
    )

    for index, card in enumerate(
            view_model.cards,
    ):
        with columns[index % len(columns)]:
            render_card_horizontal_properties(
                title=card.title,
                property_fields=card.property_fields,
                key=f"{card.id}_{index}",
            )


"""
# ---------------

from streamlit.elements.lib.column_types import Column
from streamlit.delta_generator import DeltaGenerator
from typing import Sequence

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

from src.interface_adapters.view_models.widgets.tab_view_model import (
    TabViewModel,
)

from src.interface_adapters.view_models.residents.main_page.resident_main_view_model import (
    PatientPayerViewModel,
)

from src.interface_adapters.view_models.residents.main_page.resident_main_view_model import (
    ResidentPayerAndRtmEnrollmentSectionViewModel
)


def render_resident_payers(
        resident_id: str,
        view_model: ResidentPayerAndRtmEnrollmentSectionViewModel,
) -> None:
    st.markdown(f"#### {view_model.section_title}")

    tabs: Sequence[DeltaGenerator] = _render_tab_widget(
        tabs_vm=view_model.section_tabs
    )

    patient_payers_tab: DeltaGenerator = tabs[0]
    rtm_enrollment_tab: DeltaGenerator = tabs[1]

    _render_patient_payers_tab(
        tab=patient_payers_tab,
        models=view_model.patient_payers.patient_payer_card_grids
    )

    _render_rtm_enrollment_tab(
        tab=rtm_enrollment_tab,
        model=view_model.rtm_enrollment.enrollment_card_grid
    )


def _render_tab_widget(
        tabs_vm: TabViewModel,
) -> Sequence[DeltaGenerator]:
    st.write("")

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

    return tabs


def _render_patient_payers_tab(
        tab: DeltaGenerator,
        models: tuple[CardGridViewModel, ...]
) -> None:
    with tab:
        for model in models:
            _render_patient_payers_tab_content(
                view_model=model,
            )

            st.write("")


def _render_rtm_enrollment_tab(
        tab: DeltaGenerator,
        model: CardGridViewModel,
) -> None:
    with tab:
        _render_rtm_enrollment_tab_content(
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


def _render_patient_payers_tab_content(
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


def _render_rtm_enrollment_tab_content(
        view_model: CardGridViewModel,
) -> None:
    # st.markdown("#### 🚧 Resident")

    cols: Column = st.columns(view_model.columns)

    for i, vm in enumerate(view_model.cards):
        with cols[i % len(cols)]:
            render_card_horizontal_properties(
                title=vm.title,
                property_fields=vm.property_fields,
                key=f"{vm.id}_{i}",
            )
"""
