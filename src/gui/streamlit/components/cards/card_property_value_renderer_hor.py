# /src/gui/streamlit/components/cards/card_property_value_renderer_hor.py

from html import escape

import streamlit as st

from src.interface_adapters.view_models.widgets.property_field_view_model import (
    PropertyFieldViewModel,
)

_CSS_HORIZONTAL: str = """
<style>

/* =========================
   CARD FRAME
   ========================= */

[class*="st-key-card_horizontal_container_"] {
    gap: 0 !important;
    padding: 0 !important;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #ededed;
}

/* =========================
   TOP / TITLE
   ========================= */

.card-horizontal-title {
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
   PROPERTY LABEL + VALUE
   ========================= */

.card-horizontal-properties {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    column-gap: 24px;
    row-gap: 12px;

    padding-top: 12px;
    padding-right: 10px;
    padding-bottom: 30px;
    padding-left: 10px;

    background-color: white;
}

.card-horizontal-row {
    display: grid;
    grid-template-columns: 120px minmax(0, 1fr);
    column-gap: 12px;
    align-items: start;
}

.card-horizontal-label {
    color: #6B7280;
    font-size: 0.90rem;
    font-weight: 400;
}

.card-horizontal-value {
    color: #111827;
    font-size: 1rem;
    font-weight: 500;
    min-width: 0;
    overflow-wrap: anywhere;
}



/* =========================
   MOBILE
   ========================= */

@media (max-width: 640px) {
    .card-horizontal-properties {
        grid-template-columns: minmax(0, 1fr);
        column-gap: 0;
        row-gap: 12px;
    }
}


@media (max-width: 400px) {
    .card-horizontal-row {
        grid-template-columns: minmax(0, 1fr);
        row-gap: 2px;
    }
}

</style>
"""


def render_card_horizontal_properties(
        title: str,
        property_fields: tuple[PropertyFieldViewModel, ...],
        key: str,
) -> None:
    st.markdown(
        _CSS_HORIZONTAL,
        unsafe_allow_html=True,
    )

    fields_html = _render_property_fields(property_fields)

    with st.container(
            border=True,
            key=f"card_horizontal_container_{key}",
    ):
        st.markdown(
            f"""
<div class="card-horizontal-title">
    {escape(title)}
</div>

<div class="card-horizontal-properties">
    {fields_html}
</div>
""",
            unsafe_allow_html=True,
        )


def _render_property_fields(
        property_fields: tuple[PropertyFieldViewModel, ...],
) -> str:
    return "".join(
        f"""
<div class="card-horizontal-row">
    <div class="card-horizontal-label">
        {escape(field.label)}
    </div>
    <div class="card-horizontal-value">
        {escape(field.value or "—")}
    </div>
</div>
"""
        for field in property_fields
    )
