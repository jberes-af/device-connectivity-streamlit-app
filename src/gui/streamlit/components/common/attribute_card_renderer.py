# /src/gui/streamlit/components/common/attribute_card_renderer.py

from html import escape

import streamlit as st

_CSS_ATTRIBUTE = """
<style>

[class*="st-key-card_container_"] {
    gap: 0 !important;
    padding: 0 !important;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #ededed;
}

.card-title {
    padding: 6px 10px;

    font-size: 1.1rem;
    font-weight: 400;

    border: none;
    background-color: #fbf1f3;
}

.count-properties {
    padding: 8px 10px;

    background-color: white;

    font-size: 2.0rem;
    font-weight: 600;
}

.attributes-properties {
    height: 100px;
    padding: 0px 0px;
    box-sizing: border-box;

    background-color: white;

    overflow-y: auto;
    overflow-x: hidden;

    color: #6B7280;
    font-size: 0.90rem;
    font-weight: 400;
}

.property-list {
    list-style: none;
    margin: 0;
    padding: 0;
    /* padding-left: 0.9rem; */
}

.property-field {
    margin-bottom: 8px;
}

.property-field:last-child {
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
            key=f"card_container_{key}",
    ):
        st.markdown(
            f"""
<div class="card-title">
    {escape(title)}
</div>

<div class="count-properties">
    {escape(attribute_count)}
</div>

<div class="attributes-properties">
    {attributes_html}
</div>
""",
            unsafe_allow_html=True,
        )


def _create_list(data: tuple[str, ...]) -> str:
    items = "".join(
        f'<li class="property-field">{escape(field)}</li>'
        for field in data
    )

    return f'<ul class="property-list">{items}</ul>'
