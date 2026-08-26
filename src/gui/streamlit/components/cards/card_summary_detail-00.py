# /src/gui/streamlit/components/widgets/card_summary_detail-00.py


from html import escape

import streamlit as st

_CSS_SUMMARY_DETAIL: str = """
<style>

/* =========================
   CARD FRAME
   ========================= */

[class*="st-key-card_kpi_detail_container_"] {
    gap: 0 !important;
    padding: 0 !important;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #ededed;
}

[class*="st-key-card_kpi_detail_container_"]
[data-testid="stMarkdownContainer"] {
    margin: 0 !important;
    padding: 0 !important;
}

[class*="st-key-card_kpi_detail_container_"]
[data-testid="stMarkdownContainer"] p {
    margin: 0 !important;
    padding: 0 !important;
}


/* =========================
   TITLE
   ========================= */

.card-kpi_detail-title {
    padding: 6px 10px;

    font-size: 1.1rem;
    font-weight: 400;

    border: none;
    background-color: #fbf1f3;
}


/* =========================
   COUNT
   ========================= */

.card-kpi_detail-count {
    padding: 8px 10px;

    background-color: white;

    font-size: 2rem;
    font-weight: 600;
}


/* =========================
   ATTRIBUTES
   ========================= */

.card-kpi_detail-properties {
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

.card-kpi_detail-field {
    margin: 0 0 6px 0;
    padding: 0;
}

.card-kpi_detail-field:last-child {
    margin-bottom: 0;
}

/* =========================
   BOTTOM / MORE BUTTON
   ========================= */

[class*="st-key-kpi_detail_container_"] button {
    width: 100%;

    padding: 6px 6px 6px 10px;

    border: none;
    background-color: white;
    box-shadow: none;
}

[class*="st-key-kpi_detail_container_"] button > div {
    width: 100%;
    justify-content: flex-end;
}

[class*="st-key-kpi_detail_container_"] button p {
    text-align: right;
    font-size: 1rem;
    font-weight: 600;
    color: #0070C0;
}

[class*="st-key-kpi_detail_container_"] button:hover {
    border: none;
    background-color: #f0f2f6;
}




</style>
"""


def render_kpi_detail_card(
        id: str,
        title: str,
        kpi_detail_count: str,
        kpi_details: tuple[str, ...],
        button_label: str,
        button_icon: str | None,
        key: str,
) -> None:
    st.markdown(
        _CSS_SUMMARY_DETAIL,
        unsafe_allow_html=True,
    )

    kpi_details_html = _create_list(kpi_details)

    with st.container(
            border=True,
            key=f"card_kpi_detail_container_{key}",
    ):
        st.markdown(
            f"""
<div class="card-kpi_detail-title">
    {escape(title)}
</div>


<div class="card-kpi_detail-properties">
    {kpi_details_html}
</div>
""",
            unsafe_allow_html=True,
        )

        st.button(
            label=button_label,
            icon=button_icon,
            icon_position="right",
            key=f"card_kpi_detail_button_{key}",
            type="tertiary",
            width="stretch",
        )


def _create_list(
        data: tuple[str, ...],
) -> str:
    return "".join(
        f"""
<div class="card-kpi_detail-field">
    {escape(field)}
</div>
"""
        for field in data
    )
