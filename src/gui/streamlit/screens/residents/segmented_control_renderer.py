# src/gui/streamlit/components/widgets/segmented_control_renderer.py

from typing import Any

import streamlit as st

from src.interface_adapters.view_models.residents.main_page.segmented_controls_view_model import (
    ResidentSectionEnum,
    ResidentSegmentedControlViewModel,
)

_CSS_VERTICAL_SEGMENT_CONTROL: str = """
<style>

/* =========================
   ALL SEGMENT BUTTONS
   ========================= */

[class*="st-key-vertical_segment_"] button,
[class*="st-key-vertical_segment_selected_"] button {
    border: none !important;
    box-shadow: none !important;
    background-color: transparent !important;

    justify-content: flex-start !important;
    text-align: left !important;
}


[class*="st-key-vertical_segment_"] button > div,
[class*="st-key-vertical_segment_selected_"] button > div {
    width: 100%;
    justify-content: flex-start !important;
}

/* =========================
   SELECTED SEGMENT
   ========================= */

[class*="st-key-vertical_segment_selected_"] button {
    background-color: #fbf1f3 !important;
    font-weight: 600 !important;
}


/* =========================
   HOVER
   ========================= */

[class*="st-key-vertical_segment_"] button:hover,
[class*="st-key-vertical_segment_selected_"] button:hover {
    border: none !important;
    box-shadow: none !important;
    background-color: #f5f5f5 !important;
}

</style>
"""


def render_segmented_control(
        view_model: ResidentSegmentedControlViewModel,
) -> ResidentSectionEnum | None:
    options = tuple(
        option.id
        for option in view_model.options
    )

    labels = {
        option.id: option.label
        for option in view_model.options
    }

    selected = st.segmented_control(
        label=view_model.label,
        options=options,
        default=view_model.selected_id,
        format_func=lambda option: labels[option],
        key=view_model.key,
        selection_mode="single",
    )

    return selected


def render_vertical_segmented_control(
        col: Any,
        view_model: ResidentSegmentedControlViewModel,
) -> ResidentSectionEnum | None:
    st.markdown(
        _CSS_VERTICAL_SEGMENT_CONTROL,
        unsafe_allow_html=True,
    )

    with col:
        selected = view_model.selected_id

        for option in view_model.options:
            is_selected = option.id == selected

            button_label = (
                f"{option.icon} {option.label}"
                if option.icon
                else option.label
            )

            if st.button(
                    label=button_label,
                    key=(
                            f"vertical_segment_"
                            f"{view_model.key}_"
                            f"{option.id.value}"
                    ),
                    type="secondary",
                    width="stretch",
            ):
                selected = option.id

    return selected
