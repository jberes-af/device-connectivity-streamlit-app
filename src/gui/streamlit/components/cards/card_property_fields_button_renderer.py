# /src/gui/streamlit/components/cards/card_property_fields_button_renderer.py

import streamlit as st

from src.interface_adapters.view_models.common.property_field_view_model import (
    PropertyFieldViewModel,
)

_CSS: str = """
<style>

/* =========================
   CARD FRAME
   ========================= */

[class*="st-key-card_container_"] {
    gap: 0 !important;
    padding: 0 !important;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #ededed;
}


/* =========================
   TOP / TITLE
   ========================= */

.card-title {
    padding-top: 6px;
    padding-right: 10px;
    padding-left: 10px;
    padding-bottom: 6px;

    font-size: 1.1rem;
    font-weight: 600;


    /* border-radius: 12px 12px 0 0; */
    border: none;
    background-color: #fbf1f3;

}


/* =========================
   MIDDLE / DESCRIPTION
   ========================= */




/* =========================
   BOTTOM / MORE BUTTON
   ========================= */

[class*="st-key-card_"] button {
    width: 100%;

    padding-top: 6px;
    padding-right: 6px;
    padding-left: 10px;
    padding-bottom: 6px;

    border: none;
    /* border-radius: 0 0 12px 12px; */

    background-color: white;
    box-shadow: none;

    /* justify-content: flex-end !important; */
}

[class*="st-key-card_"] button > div {
    width: 100%;
    justify-content: flex-end;
}

[class*="st-key-card_"] button p {
    text-align: right;
    font-size: 1.0rem;
    font-weight: 600;
    color: #0070C0;
}

[class*="st-key-card_"] button {
    padding-right: 6px;
}

[class*="st-key-card_"] button:hover {
    border: none;
    background-color: #f0f2f6;
}

/* =========================
   PROPERTY LABEL + VALUE
   ========================= */
        
.card-properties {
    height: 150px;
    padding: 12px 10px;

    background-color: white;
    overflow-y: auto;
    overflow-x: hidden;
}

.property-field {
    margin-bottom: 16px;
}

.property-field:last-child {
    margin-bottom: 0;
}

.property-label {
    color: #6B7280;
    font-size: 0.90rem;
    font-weight: 400;
    margin-bottom: 2px;
}

.property-value {
    color: #111827;
    font-size: 1rem;
    font-weight: 500;
}

</style>
"""


def render_dashboard_card(
        id: str,
        title: str,
        property_fields: tuple[PropertyFieldViewModel, ...],
        button_label: str,
        button_icon: str | None,
        key: str,
) -> None:
    st.markdown(
        _CSS,
        unsafe_allow_html=True,
    )

    fields_html = _render_property_fields(property_fields)

    with st.container(
            border=True,
            key=f"card_container_{key}",
    ):
        st.markdown(
            f"""
<div class="card-title">
    {title}
</div>

<div class="card-properties">
    {fields_html}
</div>
            """,
            unsafe_allow_html=True,
        )

        st.button(
            label=button_label,
            icon=button_icon,
            icon_position="right",
            key=f"card_{key}",
            type="tertiary",
            width="stretch",
        )


def _render_property_fields(
        property_fields: tuple[PropertyFieldViewModel, ...],
) -> str:
    return "".join(
        f"""
<div class="property-field">
    <div class="property-label">
        {field.label}
    </div>
    <div class="property-value">
        {field.value}
    </div>
</div>
        """
        for field in property_fields
    )
