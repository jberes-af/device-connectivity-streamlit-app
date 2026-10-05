# /src/gui/streamlit/app.py

from pathlib import Path

import logging
import streamlit as st
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

# --- APPLICATION

from src.application.context import (
    SessionContext,
)

from src.application.use_cases.access.access_scope_uc_dtos import (
    BuildAccessScopeRequestDTO,
    BuildAccessScopeResultDTO
)

# --- GUI

from src.gui.streamlit.session.session_context_adapter import (
    get_session_context,
)
from src.gui.streamlit.auth.login_form import LoginForm
from src.gui.streamlit.routing.router import render_router

from src.gui.streamlit.screens.sensing.sensing_dependencies import (
    SensingPageDependencies
)

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

from src.main.streamlit_containers.compose_root_streamlit_sensing import (
    build_sensing_page_dependencies
)

# --- PROGRAM

_APP_NAME = "Alerta Home Device Connectivity"
_DEFAULT_ROUTE_ID = "sensing"

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
        initial_sidebar_state="collapsed",
    )


def initialize_session_state() -> None:
    if "session_context" not in st.session_state:
        st.session_state["session_context"] = SessionContext()


def logout() -> None:
    st.session_state["session_context"] = SessionContext()
    st.rerun()


def ensure_access_scope(
        *,
        session: SessionContext,
        app_container: AppContainer,
) -> SessionContext:
    if session.user_context is None:
        raise RuntimeError(
            "Cannot build access scope without UserContext."
        )

    if session.access_scope is not None:
        return session

    request = BuildAccessScopeRequestDTO(
        user_id=session.user_context.user_id,
        tenant_id=session.user_context.tenant_id,
    )

    result: BuildAccessScopeResultDTO = (
        app_container
        .build_access_scope_use_case
        .execute(request=request)
    )

    session.access_scope = result.access_scope
    st.session_state["session_context"] = session

    return session


def render_authenticated_phase(
        *,
        session: SessionContext,
        app_container: AppContainer,
        # dashboard_dependencies: DashboardPageDependencies,
        sensing_dependencies: SensingPageDependencies,
) -> None:
    if session.access_scope is None:
        raise RuntimeError(
            "Authenticated phase requires AccessScope."
        )

    render_router(
        # app_name=_APP_NAME,
        # default_route=_DEFAULT_ROUTE_ID,
        # container=app_container,
        # access_scope=session.access_scope,
        # dashboard_dependencies=dashboard_dependencies,
        sensing_dependencies=sensing_dependencies,
    )

    # if st.sidebar.button("Logout"):
    # logout()


def render_login_phase(authentication: AuthenticationContainer) -> None:
    login_form = LoginForm(
        auth_controller=authentication.auth_controller,
        auth_presenter=authentication.auth_presenter,
    )

    login_form.render()


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

    infrastructure: InfrastructureContainer = get_infrastructure_container()

    bypass_authentication: bool = False

    # --- AUTHENTICATION


    if bypass_authentication:
        raise RuntimeError()

    else:
        session: SessionContext = get_session_context()

        if not session.is_authenticated:
            authentication = build_authentication_container(
                infrastructure=infrastructure,
            )

            render_login_phase(
                authentication=authentication,
            )

            return

    if session.user_context is None:
        raise RuntimeError(
            "Authenticated session is missing UserContext."
        )

    # --- APPLICATION COMPOSITION

    app_container: AppContainer = build_application_container(
        infrastructure=infrastructure,
        user_context=session.user_context,
    )

    # --- AUTHORIZATION

    session: SessionContext = ensure_access_scope(
        session=session,
        app_container=app_container,
    )

    # --- PAGE COMPOSITION


    sensing_dependencies: SensingPageDependencies = (
        build_sensing_page_dependencies(
            app_container=app_container,
        )
    )

    # --- ROUTING / RENDERING

    render_authenticated_phase(
        session=session,
        app_container=app_container,
        # dashboard_dependencies=dashboard_dependencies,
        sensing_dependencies=sensing_dependencies,
    )


if __name__ == "__main__":
    run_app()
