from src.gui.streamlit.screens.dashboard.dashboard_dependencies import (
    DashboardPageDependencies,
)

from src.main.compose_root_application import (
    AppContainer,
)


def build_dashboard_page_dependencies(
        app_container: AppContainer,
) -> DashboardPageDependencies:
    return DashboardPageDependencies(
        use_case=app_container.build_main_dashboard_use_case,
        presenter=app_container.main_dashboard_presenter,
    )
