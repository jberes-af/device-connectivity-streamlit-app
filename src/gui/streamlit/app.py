# /src/gui/streamlit/app.py

from pathlib import Path

import sys

PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

# --- APPLICATION

from src.application.context import (
    # UserContext,
    SessionContext,
)

# --- GUI

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

from src.main.host_inputs import HostInputs, load_host_inputs

# --- PROGRAM

_APP_NAME = "Alerta Clinical Platform"
_DEFAULT_ROUTE_ID = "residents"

_PATH_FILE_FAVICON = PROJECT_ROOT / "src/gui/streamlit/static/favicon" / "favicon.ico"


def configure_page() -> None:
    st.set_page_config(
        page_title=_APP_NAME,
        page_icon=_PATH_FILE_FAVICON,
        layout="wide",
        initial_sidebar_state="expanded",
    )


def initialize_session_state() -> None:
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if "user" not in st.session_state:
        st.session_state["user"] = None


def render_login_phase(authentication: AuthenticationContainer) -> None:
    login_form = LoginForm(
        auth_controller=authentication.auth_controller,
        auth_presenter=authentication.auth_presenter,
    )

    login_form.render()


def render_authenticated_phase(app_container: AppContainer) -> None:
    user = st.session_state.get("user")
    if user:
        st.sidebar.success(f"Signed in as {user['email']}")

    # --- PAGE NAVIGATION / ROUTING

    render_router(
        app_name=_APP_NAME,
        default_route=_DEFAULT_ROUTE_ID,
        container=app_container
    )

    # --- LOGOUT

    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["user"] = None
        st.rerun()


@st.cache_resource
def get_infrastructure_container() -> InfrastructureContainer:
    runtime: RuntimeConfiguration = load_runtime_config()

    return build_infrastructure_container(
        settings=runtime.settings,
        app_config=runtime.app_config,
    )


def run_app() -> None:
    configure_page()

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

    render_authenticated_phase(
        app_container=app_container)


if __name__ == "__main__":
    run_app()
