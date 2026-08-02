# /src/gui/streamlit/routing/router.py

from src.gui.streamlit.routing.route_types import Route
from src.gui.streamlit.routing.routes import ROUTES

from src.main.composition_root import AppContainer

import streamlit as st

_SELECTED_ROUTE_KEY = "selected_route_id"
_DEFAULT_ROUTE_ID = "dashboard"
_APP_NAME = "Alerta RTM Clinical Platform"


def _get_route(route_id: str) -> Route | None:
    return next(
        (
            route
            for route in ROUTES
            if route.route_id == route_id
        ),
        None,
    )


def _initialize_selected_route() -> None:
    if _SELECTED_ROUTE_KEY not in st.session_state:
        st.session_state[_SELECTED_ROUTE_KEY] = (
            _DEFAULT_ROUTE_ID
        )


def _select_route(route_id: str) -> None:
    st.session_state[_SELECTED_ROUTE_KEY] = route_id


def render_sidebar_navigation() -> str:
    _initialize_selected_route()

    selected_route_id: str = st.session_state[
        _SELECTED_ROUTE_KEY
    ]

    with st.sidebar:
        st.title(_APP_NAME)
        st.divider()

        for route in ROUTES:
            is_selected = (
                    route.route_id == selected_route_id
            )

            label = (
                f"{route.icon} {route.label}"
                if route.icon
                else route.label
            )

            if st.button(
                    label=label,
                    key=f"navigation_{route.route_id}",
                    type="primary" if is_selected else "secondary",
                    use_container_width=True,
            ):
                _select_route(route.route_id)
                st.rerun()

    return st.session_state[_SELECTED_ROUTE_KEY]


def render_selected_route(
        route_id: str,
        container: AppContainer,
) -> None:
    route = _get_route(route_id)

    if route is None:
        st.error(
            f"The requested page could not be found: "
            f"{route_id}"
        )
        return

    route.handler(container)


def render_router(
        container: AppContainer,
) -> None:
    route_id = render_sidebar_navigation()
    render_selected_route(
        route_id,
        container
    )
