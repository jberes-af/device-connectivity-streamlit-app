# src/gui/streamlit/components/widgets/segmented_control_renderer.py

from typing import Any

import streamlit as st

from src.interface_adapters.view_models.resident.segmented_controls_view_model import (
    ResidentSectionEnum,
    ResidentSegmentedControlViewModel,
)


def render_segmented_control(
        view_model: ResidentSegmentedControlViewModel,
) -> ResidentSectionEnum | None:
    # Actual values managed by Streamlit
    options = [
        option.id
        for option in view_model.options
    ]

    # Map enum -> display label
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
    with col:
        selected = view_model.selected_id

        for option in view_model.options:
            is_selected = option.id == selected

            if st.button(
                    option.label,
                    key=f"{view_model.key}_{option.id.value}",
                    type="primary" if is_selected else "secondary",
                    width="stretch",
            ):
                selected = option.id

        return selected
