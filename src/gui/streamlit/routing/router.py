# /src/gui/streamlit/routing/router.py

from collections.abc import Callable

import streamlit as st

from src.application.context import AccessScope

from src.gui.streamlit.routing.route_types import Route
# from src.gui.streamlit.routing.routes import build_routes


from src.gui.streamlit.screens.sensing.sensing_dependencies import (
    SensingPageDependencies,
)

from src.gui.streamlit.screens.sensing.main_sensing_view import (
    render_sensing_page,
)

from src.main.compose_root_application import AppContainer


def _create_page_handler(
        route: Route,
        container: AppContainer,
) -> Callable[[], None]:
    if route.handler is not None:
        return route.handler

    legacy_handler = route.legacy_handler

    if legacy_handler is None:
        raise RuntimeError("Route has no configured handler.")

    def render() -> None:
        legacy_handler(container)

    return render


def render_router(
        # app_name: str,
        # default_route: str,
        # container: AppContainer,
        # access_scope: AccessScope,
        # dashboard_dependencies: DashboardPageDependencies,
        sensing_dependencies: SensingPageDependencies,
) -> None:
    render_sensing_page(
        dependencies=sensing_dependencies,
    )


"""

routes = build_routes(
    app_container=container,
    access_scope=access_scope,
    # dashboard_dependencies=dashboard_dependencies,
    sensing_dependencies=sensing_dependencies,
)

main_pages = [
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
    for route in routes
]

def render_account_page() -> None:
    render_account_and_access_page(
        user_context=container.user_context,
        access_scope=access_scope,
    )

account_page = st.Page(
    render_account_page,
    title="Account & Access",
    icon=":material/account_circle:",
    url_path="account",
)

page = st.navigation(
    {
        app_name.upper(): main_pages,
        "ACCOUNT": [
            account_page,
        ],
    },
    position="sidebar",
)

page = st.navigation(
    {
        app_name.upper(): main_pages,
    },
    # position="sidebar",
)

page.run()

"""
