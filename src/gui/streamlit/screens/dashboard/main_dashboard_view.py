# /src/gui/streamlit/screens/dashboard/main_dashboard_view.py

from src.application.use_cases.dashboard.main_dashboard_uc_dtos import (
    # BuildDashboardMainPageRequestDTO,
    BuildDashboardMainPageResultDTO,
)

from src.gui.streamlit.screens.dashboard.dashboard_dependencies import (
    DashboardPageDependencies,
)

from src.gui.streamlit.screens.dashboard.main_dashboard_renderer import (
    render_main_dashboard,
)

from src.interface_adapters.view_models.dashboard.dashboard_view_models import (
    DashboardMainPageViewModel,
)


def render_dashboard_page(
        *,
        dependencies: DashboardPageDependencies,
) -> None:
    # request = BuildDashboardMainPageRequestDTO()

    result: BuildDashboardMainPageResultDTO = (
        dependencies
        .use_case
        .execute()
    )

    view_model: DashboardMainPageViewModel = (
        dependencies
        .presenter
        .present(
            result=result,
        )
    )

    render_main_dashboard(
        view_model=view_model,
    )


