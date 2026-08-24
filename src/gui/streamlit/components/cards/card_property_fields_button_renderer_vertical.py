# /src/gui/streamlit/components/cards/card_property_fields_button_renderer_vertical.py

from html import escape

import streamlit as st

from src.interface_adapters.view_models.widgets.property_field_view_model import (
    PropertyFieldViewModel,
)

_CSS_VERTICAL: str = """
<style>

/* =========================
   CARD FRAME
   ========================= */

[class*="st-key-card_vertical_container_"] {
    gap: 0 !important;
    padding: 0 !important;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #ededed;
}


/* =========================
   TOP / TITLE
   ========================= */

.card-vertical-title {
    padding: 6px 10px;

    font-size: 1.1rem;
    font-weight: 600;

    border: none;
    background-color: #fbf1f3;
}


/* =========================
   BOTTOM / MORE BUTTON
   ========================= */

[class*="st-key-card_vertical_container_"] button {
    width: 100%;

    padding: 6px 6px 6px 10px;

    border: none;
    background-color: white;
    box-shadow: none;
}

[class*="st-key-card_vertical_container_"] button > div {
    width: 100%;
    justify-content: flex-end;
}

[class*="st-key-card_vertical_container_"] button p {
    text-align: right;
    font-size: 1rem;
    font-weight: 600;
    color: #0070C0;
}

[class*="st-key-card_vertical_container_"] button:hover {
    border: none;
    background-color: #f0f2f6;
}


/* =========================
   PROPERTY LABEL + VALUE
   ========================= */

.card-vertical-properties {
    height: 150px;
    padding: 12px 10px;

    background-color: white;

    overflow-y: auto;
    overflow-x: hidden;
}

.card-vertical-field {
    margin-bottom: 16px;
}

.card-vertical-field:last-child {
    margin-bottom: 0;
}

.card-vertical-label {
    margin-bottom: 2px;

    color: #6B7280;
    font-size: 0.90rem;
    font-weight: 400;
}

.card-vertical-value {
    color: #111827;
    font-size: 1rem;
    font-weight: 500;

    overflow-wrap: anywhere;
}

</style>
"""


def render_dashboard_card(
        title: str,
        property_fields: tuple[PropertyFieldViewModel, ...],
        button_label: str,
        button_icon: str | None,
        key: str,
) -> None:
    st.markdown(
        _CSS_VERTICAL,
        unsafe_allow_html=True,
    )

    fields_html = _render_property_fields(
        property_fields=property_fields,
    )

    with st.container(
            border=True,
            key=f"card_vertical_container_{key}",
    ):
        st.markdown(
            f"""
<div class="card-vertical-title">
    {escape(title)}
</div>

<div class="card-vertical-properties">
    {fields_html}
</div>
""",
            unsafe_allow_html=True,
        )

        st.button(
            label=button_label,
            icon=button_icon,
            icon_position="right",
            key=f"card_vertical_button_{key}",
            type="tertiary",
            width="stretch",
        )


def _render_property_fields(
        property_fields: tuple[PropertyFieldViewModel, ...],
) -> str:
    return "".join(
        f"""
<div class="card-vertical-field">
    <div class="card-vertical-label">
        {escape(field.label)}
    </div>
    <div class="card-vertical-value">
        {escape(field.value or "—")}
    </div>
</div>
"""
        for field in property_fields
    )
