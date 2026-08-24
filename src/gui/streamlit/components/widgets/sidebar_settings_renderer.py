# /src/gui/streamlit/components/sidebar_settings_renderer.py

import streamlit as st

from src.application.context import UserContext

from src.application.use_cases.access.access_scope_uc_dtos import (
    AccessScopeResultDTO,
)

from src.gui.streamlit.screens.access import (
    render_account_and_access_page,
)


def render_sidebar_settings(
        user_context: UserContext,
        access_scope: AccessScopeResultDTO,
) -> None:
    with st.sidebar:
        st.divider()

        with st.popover(
                "Settings",
                icon=":material/settings:",
                use_container_width=True,
        ):
            render_account_and_access_page(
                user_context=user_context,
                access_scope=access_scope,
            )
