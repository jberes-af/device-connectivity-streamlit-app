# /src/gui/streamlit/components/widgets/card_attribute_renderer_vertical.py

from html import escape

import streamlit as st

_CSS_ATTRIBUTE: str = """
<style>

/* =========================
   CARD FRAME
   ========================= */

[class*="st-key-card_attribute_container_"] {
    gap: 0 !important;
    padding: 0 !important;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #ededed;
}

[class*="st-key-card_attribute_container_"]
[data-testid="stMarkdownContainer"] {
    margin: 0 !important;
    padding: 0 !important;
}

[class*="st-key-card_attribute_container_"]
[data-testid="stMarkdownContainer"] p {
    margin: 0 !important;
    padding: 0 !important;
}


/* =========================
   TITLE
   ========================= */

.card-attribute-title {
    padding: 6px 10px;

    font-size: 1.1rem;
    font-weight: 400;

    border: none;
    background-color: #fbf1f3;
}


/* =========================
   COUNT
   ========================= */

.card-attribute-count {
    padding: 8px 10px;

    background-color: white;

    font-size: 2rem;
    font-weight: 600;
}


/* =========================
   ATTRIBUTES
   ========================= */

.card-attribute-properties {
    height: 100px;
    padding-left: 12px;
    margin: 0;

    background-color: white;
    overflow-y: auto;
    overflow-x: hidden;

    color: #6B7280;
    font-size: 0.90rem;
    font-weight: 400;
}

.card-attribute-field {
    margin: 0 0 6px 0;
    padding: 0;
}

.card-attribute-field:last-child {
    margin-bottom: 0;
}

</style>
"""


def render_attribute_card(
        id: str,
        title: str,
        attribute_count: str,
        attributes: tuple[str, ...],
        key: str,
) -> None:
    st.markdown(
        _CSS_ATTRIBUTE,
        unsafe_allow_html=True,
    )

    attributes_html = _create_list(attributes)

    with st.container(
            border=True,
            key=f"card_attribute_container_{key}",
    ):
        st.markdown(
            f"""
<div class="card-attribute-title">
    {escape(title)}
</div>

<div class="card-attribute-count">
    {escape(attribute_count)}
</div>

<div class="card-attribute-properties">
    {attributes_html}
</div>
""",
            unsafe_allow_html=True,
        )


def _create_list(
        data: tuple[str, ...],
) -> str:
    return "".join(
        f"""
<div class="card-attribute-field">
    {escape(field)}
</div>
"""
        for field in data
    )
