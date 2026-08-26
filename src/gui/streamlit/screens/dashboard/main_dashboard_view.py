# /src/gui/streamlit/screens/dashboard/main_dashboard_view.py

from src.application.use_cases.dashboard.main_dashboard_uc_dtos import (
    # BuildDashboardMainPageRequestDTO,
    BuildDashboardMainPageResultDTO,
)

from src.gui.streamlit.screens.dashboard.main_dashboard_renderer import (
    render_main_dashboard,
)

from src.interface_adapters.view_models.dashboard.dashboard_view_models import (
    DashboardMainPageViewModel,
)

from src.main.compose_root_application import AppContainer


def render_dashboard_page(
        container: AppContainer,
) -> None:
    # request = BuildDashboardMainPageRequestDTO()

    result: BuildDashboardMainPageResultDTO = (
        container
        .build_main_dashboard_use_case
        .execute()
    )

    view_model: DashboardMainPageViewModel = (
        container
        .main_dashboard_presenter
        .present(
            result=result,
        )
    )

    render_main_dashboard(
        view_model=view_model,
    )


