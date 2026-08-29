# /src/gui/streamlit/app.py

from pathlib import Path

import logging
import sys

# import traceback


PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

# --- APPLICATION

from src.application.context import (
    # UserContext,
    SessionContext,
)

from src.application.use_cases.access.access_scope_uc_dtos import (
    AccessScopeRequestDTO,
    AccessScopeResultDTO,
)

# --- GUI

from src.gui.streamlit.screens.dashboard.dashboard_dependencies import (
    DashboardPageDependencies,
)

from src.gui.streamlit.session.session_context_adapter import (
    get_session_context,
)
from src.gui.streamlit.auth.login_form import LoginForm
from src.gui.streamlit.routing.router import render_router

# --- COMPOSITION ROOT

from src.main.compose_root_config import (
    RuntimeConfiguration,
    load_runtime_config,
)

from src.main.compose_root_authentication import (
    AuthenticationContainer,
    build_authentication_container,
)

from src.main.compose_root_infrastructure import (
    InfrastructureContainer,
    build_infrastructure_container,
)

from src.main.compose_root_application import (
    AppContainer,
    build_application_container,
)

from src.main.compose_root_streamlit_dashboard import (
    build_dashboard_page_dependencies,
)

from src.main.host_inputs import HostInputs, load_host_inputs

# --- PROGRAM

_APP_NAME = "Alerta Clinical Platform"
_DEFAULT_ROUTE_ID = "residents"

_PATH_FILE_FAVICON = PROJECT_ROOT / "src/gui/streamlit/static/favicon" / "favicon.ico"


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s |  %(message)s | %(filename)s:%(lineno)d",
    )


def configure_page() -> None:
    st.set_page_config(
        page_title=_APP_NAME,
        page_icon=_PATH_FILE_FAVICON,
        layout="wide",
        initial_sidebar_state="expanded",
    )


def initialize_session_state() -> None:
    if "session_context" not in st.session_state:
        st.session_state["session_context"] = SessionContext()

    if "access_scope" not in st.session_state:
        st.session_state["access_scope"] = None


def logout() -> None:
    st.session_state["session_context"] = SessionContext()
    st.session_state.pop("access_scope", None)
    st.session_state.pop("access_scope_user_id", None)

    st.rerun()


def get_or_load_access_scope(
        app_container: AppContainer,
) -> AccessScopeResultDTO:
    user_context = app_container.user_context

    access_scope = st.session_state.get("access_scope")
    cached_user_id = st.session_state.get("access_scope_user_id")

    if (
            access_scope is not None
            and cached_user_id == user_context.user_id
    ):
        return access_scope

    request = AccessScopeRequestDTO(
        user_id=user_context.user_id,
        tenant_id=user_context.tenant_id,
    )

    access_scope = (
        app_container
        .get_user_access_scope_use_case
        .execute(request=request)
    )

    st.session_state["access_scope"] = access_scope
    st.session_state["access_scope_user_id"] = (
        user_context.user_id
    )

    return access_scope


def render_login_phase(authentication: AuthenticationContainer) -> None:
    login_form = LoginForm(
        auth_controller=authentication.auth_controller,
        auth_presenter=authentication.auth_presenter,
    )

    login_form.render()


def render_authenticated_phase(
        app_container: AppContainer,
        dashboard_dependencies: DashboardPageDependencies,
) -> None:
    # user_context = app_container.user_context
    # st.sidebar.success(f"Signed in as {user_context.user_id}")

    access_scope = get_or_load_access_scope(
        app_container=app_container,
    )

    render_router(
        app_name=_APP_NAME,
        default_route=_DEFAULT_ROUTE_ID,
        container=app_container,
        access_scope=access_scope,
        dashboard_dependencies=dashboard_dependencies,
    )

    if st.sidebar.button("Logout"):
        logout()


@st.cache_resource
def get_infrastructure_container() -> InfrastructureContainer:
    runtime: RuntimeConfiguration = load_runtime_config()

    return build_infrastructure_container(
        settings=runtime.settings,
        app_config=runtime.app_config,
    )


def run_app() -> None:
    configure_logging()

    configure_page()

    initialize_session_state()

    infrastructure: InfrastructureContainer = (
        get_infrastructure_container())

    host_inputs: HostInputs = load_host_inputs()

    if host_inputs.bypass_authentication:
        session: SessionContext = host_inputs.session_context
    else:
        session: SessionContext = get_session_context()

        if not session.is_authenticated:
            authentication: AuthenticationContainer = (
                build_authentication_container(
                    infrastructure=infrastructure))

            render_login_phase(authentication=authentication)

            return

    app_container: AppContainer = build_application_container(
        infrastructure=infrastructure,
        user_context=session.user_context,
    )

    dashboard_dependencies: DashboardPageDependencies = (
        build_dashboard_page_dependencies(
            app_container=app_container,
        )
    )

    render_authenticated_phase(
        app_container=app_container,
        dashboard_dependencies=dashboard_dependencies,
    )


if __name__ == "__main__":
    run_app()
