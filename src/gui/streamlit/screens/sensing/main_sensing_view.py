# /src/gui/streamlit/screens/sensing/main_sensing_view.py

import streamlit as st

from src.application.use_cases.sensing.sensing_admin.build_view.build_admin_view_uc_dtos import (
    BuildSensingAdminViewRequestDTO,
    BuildSensingAdminViewResultDTO,
)

from src.gui.streamlit.screens.sensing.sensing_dependencies import (
    SensingPageDependencies
)

from src.gui.streamlit.screens.sensing.main_sensing_renderer import (
    render_main_sensing,
)

from src.interface_adapters.view_models.sensing.device_admin_view_models import (
    SensingAdministrationViewModel,
)


def render_sensing_page(
        *,
        dependencies: SensingPageDependencies,
) -> None:
    selected_tenant_name = st.session_state.get(
        "sensing_selected_tenant_name"
    )

    request = BuildSensingAdminViewRequestDTO(
        selected_tenant_name=selected_tenant_name,
    )

    result: BuildSensingAdminViewResultDTO = (
        dependencies
        .use_case
        .execute(
            request=request
        )
    )

    view_model: SensingAdministrationViewModel = (
        dependencies
        .presenter
        .present(
            result=result,
        )
    )

    render_main_sensing(
        view_model=view_model,
    )
