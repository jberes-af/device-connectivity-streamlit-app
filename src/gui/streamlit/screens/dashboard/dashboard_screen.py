# /src/gui/streamlit/screens/dashboard_screen.py

import streamlit as st

# --- APPLICATION


# --- GUI


from src.gui.streamlit.components.grids.grid_card_multi_renderer import (
    # render_card_grid,
    render_metric_card_grid,
)

# --- INTERFACE ADAPTERS


from src.interface_adapters.presenters.dashboard.demo_top_metrics_presenter import (
    DemoResidentDashMetricsPresenter
)

from src.interface_adapters.view_models.widgets.card_grid_view_model import (
    CardGridViewModel
)

# --- MAIN

from src.main.compose_root_application import AppContainer


def render_dashboard_page(
        container: AppContainer,
) -> None:
    presenter = DemoResidentDashMetricsPresenter()

    _render_top_section(
        metrics_grid_vm=presenter.present(),
    )


def _render_top_section(
        metrics_grid_vm: CardGridViewModel,
) -> None:
    st.title("🚧 :material/dashboard: Dashboard")
    st.write("Organization and treatment monitoring overview.")
    st.write("")
    # st.title(header_vm.page_title)
    # st.write(header_vm.page_subtitle)

    render_metric_card_grid(metrics_grid_vm)

    st.divider()
