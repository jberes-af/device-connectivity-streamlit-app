
# /src/gui/streamlit/screens/sensing_screen.py

import streamlit as st

from src.main.compose_root_application import AppContainer


def render_sensing_page(

        container: AppContainer,
) -> None:
    st.title("🚧 :material/sensors: Sensing")
