# /src/gui/streamlit/screens/dashboard_screen.py

import streamlit as st

from src.main.compose_root_application import AppContainer

def render_dashboard_page(
        container: AppContainer,
) -> None:
    st.title("🚧 :material/dashboard: Dashboard")
    st.write("Organization and patient monitoring overview.")



