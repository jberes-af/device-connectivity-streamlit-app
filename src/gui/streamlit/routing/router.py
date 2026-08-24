# /src/gui/streamlit/routing/router.py

from collections.abc import Callable

import streamlit as st

from src.application.use_cases.access.access_scope_uc_dtos import (
    AccessScopeResultDTO,
)

from src.gui.streamlit.routing.route_types import Route
from src.gui.streamlit.routing.routes import ROUTES

from src.gui.streamlit.screens.access.access_scope_screen import (
    render_account_and_access_page,
)

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
    access_scope: AccessScopeResultDTO,
) -> None:
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
        for route in ROUTES
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

    page.run()
