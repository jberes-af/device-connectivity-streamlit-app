# /src/gui/streamlit/routing/router.py

from collections.abc import Callable

import streamlit as st

from src.gui.streamlit.routing.route_types import Route
from src.gui.streamlit.routing.routes import ROUTES

from src.main.compose_root_application import AppContainer


def _create_page_handler(
    route: Route,
    container: AppContainer,
) -> Callable[[], None]:
    def render() -> None:
        route.handler(container)

    return render


def render_router(
    app_name: str,
    default_route: str,
    container: AppContainer,
) -> None:
    pages = [
        st.Page(
            _create_page_handler(
                route=route,
                container=container,
            ),
            title=route.label,
            icon=route.icon,
            url_path=route.route_id,
            default=route.route_id == default_route,
        )
        for route in ROUTES
    ]

    page = st.navigation(
        {
            app_name.upper(): pages,
        },
        position="sidebar",
    )

    page.run()