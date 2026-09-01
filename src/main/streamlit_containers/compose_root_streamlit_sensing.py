# src/main/compose_root_streamlit_sensing.py

from src.gui.streamlit.screens.sensing.sensing_dependencies import (
    SensingPageDependencies,
)

from src.main.compose_root_application import (
    AppContainer,
)


def build_sensing_page_dependencies(
        *,
        app_container: AppContainer,
) -> SensingPageDependencies:
    return SensingPageDependencies(
        build_sensing_admin_view_use_case=app_container.build_sensing_admin_view_use_case,
        presenter=app_container.sensing_admin_page_presenter,
    )
