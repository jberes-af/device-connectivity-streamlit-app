# /src/gui/streamlit/app.py

import streamlit as st

from src.gui.streamlit.routing.router import render_router

from src.main.composition_root import (
    AppContainer,
    build_app_container,
)

_APP_NAME = "Alerta RTM Clinical Platform"


def run_app() -> None:
    st.set_page_config(
        page_title=_APP_NAME,
        page_icon=":material/health_and_safety:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    container: AppContainer = build_app_container()

    render_router(
        container=container
    )


if __name__ == "__main__":
    run_app()
