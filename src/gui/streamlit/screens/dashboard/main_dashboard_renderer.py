# /src/gui/streamlit/screens/dashboard/main_dashboard_renderer

# /src/gui/streamlit/screens/dashboard/main_dashboard_renderer.py

import streamlit as st

from src.gui.streamlit.components.cards.badge_renderer import (
    render_badge,
)
from src.gui.streamlit.components.cards.card_summary_detail import (
    render_summary_detail_card,
)

from src.interface_adapters.view_models.dashboard.dashboard_view_models import (
    DashboardMainPageViewModel,
    DashboardResidentAttentionViewModel,
    DashboardSummaryDetailCardViewModel,
    MetricCardViewModel,
)


_KPI_COLUMNS: int = 4
_SUMMARY_DETAIL_COLUMNS: int = 3
_ATTENTION_COLUMN_WIDTHS: tuple[float, ...] = (
    2.0,   # Resident
    4.5,   # Issue
    1.5,   # Priority
    1.0,   # Since
)


def render_main_dashboard(
        view_model: DashboardMainPageViewModel,
) -> str | None:
    """
    Render the main dashboard page.

    Returns:
        str | None:
            A semantic identifier for a selected resident or
            summary-detail action.

            Resident selections:
                "resident:<resident_id>"

            Summary-detail selections:
                "summary:<card_id>"
    """

    _render_page_header()

    _render_kpi_section(
        cards=view_model.kpi_cards,
    )

    st.divider()

    selected_resident_id = _render_resident_attention_section(
        view_model=view_model.resident_attention,
    )

    if selected_resident_id is not None:
        return f"resident:{selected_resident_id}"

    st.divider()

    selected_summary_card_id = _render_summary_detail_section(
        cards=view_model.summary_detail_cards,
    )

    if selected_summary_card_id is not None:
        return f"summary:{selected_summary_card_id}"

    return None


# =============================================================================
# PAGE HEADER
# =============================================================================


def _render_page_header() -> None:
    st.title("🚧 :material/dashboard: Dashboard")
    st.write("Organization and treatment monitoring overview.")


# =============================================================================
# KPI SECTION
# =============================================================================


def _render_kpi_section(
        *,
        cards: tuple[MetricCardViewModel, ...],
) -> None:
    if not cards:
        return

    column_count = min(
        _KPI_COLUMNS,
        len(cards),
    )

    columns = st.columns(column_count)

    for index, card in enumerate(cards):
        with columns[index % column_count]:
            _render_metric_card(card)


def _render_metric_card(
        card: MetricCardViewModel,
) -> None:
    st.metric(
        label=card.label,
        value=card.value,
        delta=card.delta,
        help=card.help_text,
        border=False,
    )


# =============================================================================
# RESIDENTS REQUIRING ATTENTION
# =============================================================================


def _render_resident_attention_section(
        *,
        view_model: DashboardResidentAttentionViewModel,
) -> str | None:
    st.subheader(view_model.title)

    if not view_model.rows:
        st.caption("No residents currently require attention.")
        return None

    _render_resident_attention_header()

    for row_index, row in enumerate(view_model.rows):
        columns = st.columns(
            _ATTENTION_COLUMN_WIDTHS,
            vertical_alignment="center",
        )

        with columns[0]:
            resident_clicked = st.button(
                label=row.resident_name,
                key=(
                    "dashboard_attention_resident_"
                    f"{row.resident_id}_{row_index}"
                ),
                type="tertiary",
            )

        with columns[1]:
            st.write(row.issue)

        with columns[2]:
            render_badge(row.priority)

        with columns[3]:
            st.write(row.since or "—")

        if resident_clicked:
            return row.resident_id

    return None


def _render_resident_attention_header() -> None:
    columns = st.columns(
        _ATTENTION_COLUMN_WIDTHS,
        vertical_alignment="center",
    )

    with columns[0]:
        st.caption("RESIDENT")

    with columns[1]:
        st.caption("ISSUE")

    with columns[2]:
        st.caption("PRIORITY")

    with columns[3]:
        st.caption("SINCE")


# =============================================================================
# SUMMARY DETAIL SECTION
# =============================================================================


def _render_summary_detail_section(
        *,
        cards: tuple[DashboardSummaryDetailCardViewModel, ...],
) -> str | None:
    if not cards:
        return None

    column_count = min(
        _SUMMARY_DETAIL_COLUMNS,
        len(cards),
    )

    columns = st.columns(
        column_count,
        vertical_alignment="top",
    )

    for index, card in enumerate(cards):
        with columns[index % column_count]:
            clicked = render_summary_detail_card(
                title=card.title,
                primary_value=card.primary_value,
                details=card.details,
                button_label=card.button_label,
                button_icon=":material/arrow_forward:",
                key=f"dashboard_summary_{card.card_id}",
            )

        if clicked:
            return card.card_id

    return None
