# /src/gui/streamlit/components/widgets/card_summary_detail.py

from html import escape

import streamlit as st

_CSS_SUMMARY_DETAIL: str = """
<style>

/* =========================
   CARD FRAME
   ========================= */

[class*="st-key-card_summary_detail_container_"] {
    gap: 0 !important;
    padding: 0 !important;

    border: 1px solid #ededed;
    border-radius: 12px;

    overflow: hidden;
}

[class*="st-key-card_summary_detail_container_"]
[data-testid="stMarkdownContainer"] {
    margin: 0 !important;
    padding: 0 !important;
}

[class*="st-key-card_summary_detail_container_"]
[data-testid="stMarkdownContainer"] p {
    margin: 0 !important;
    padding: 0 !important;
}


/* =========================
   TITLE
   ========================= */

.card-summary-detail-title {
    padding: 6px 10px;

    background-color: #fbf1f3;

    font-size: 1.1rem;
    font-weight: 500;
}


/* =========================
   PRIMARY VALUE
   ========================= */

.card-summary-detail-primary-value {
    padding: 10px 12px 4px 12px;

    background-color: white;

    font-size: 1.4rem;
    font-weight: 600;
}


/* =========================
   DETAILS
   ========================= */

.card-summary-detail-properties {
    min-height: 72px;

    padding: 4px 12px 10px 12px;
    margin: 0;

    background-color: white;

    color: #6B7280;

    font-size: 0.90rem;
    font-weight: 400;
}

.card-summary-detail-field {
    margin: 0 0 6px 0;
    padding: 0;
}

.card-summary-detail-field:last-child {
    margin-bottom: 0;
}


/* =========================
   ACTION BUTTON
   ========================= */

[class*="st-key-card_summary_detail_container_"] button {
    width: 100%;

    padding: 6px 10px;

    border: none;
    background-color: white;
    box-shadow: none;
}

[class*="st-key-card_summary_detail_container_"] button > div {
    width: 100%;
    justify-content: flex-end;
}

[class*="st-key-card_summary_detail_container_"] button p {
    text-align: right;

    font-size: 0.95rem;
    font-weight: 600;

    color: #0070C0;
}

[class*="st-key-card_summary_detail_container_"] button:hover {
    border: none;
    background-color: #f0f2f6;
}

</style>
"""


def render_summary_detail_card(
        *,
        title: str,
        primary_value: str,
        details: tuple[str, ...],
        button_label: str,
        button_icon: str | None,
        key: str,
) -> bool:
    st.markdown(
        _CSS_SUMMARY_DETAIL,
        unsafe_allow_html=True,
    )

    details_html = _create_detail_list(details)

    with st.container(
            border=False,
            key=f"card_summary_detail_container_{key}",
    ):
        st.markdown(
            f"""
<div class="card-summary-detail-title">
    {escape(title)}
</div>

<div class="card-summary-detail-primary-value">
    {escape(primary_value)}
</div>

<div class="card-summary-detail-properties">
    {details_html}
</div>
""",
            unsafe_allow_html=True,
        )

        clicked: bool = st.button(
            label=button_label,
            icon=button_icon,
            icon_position="right",
            key=f"card_summary_detail_button_{key}",
            type="tertiary",
            width="stretch",
        )

    return clicked


def _create_detail_list(
        details: tuple[str, ...],
) -> str:
    return "".join(
        f"""
<div class="card-summary-detail-field">
    {escape(detail)}
</div>
"""
        for detail in details
    )
