# /src/gui/streamlit/screens/dashboard.py

import streamlit as st

from src.main.composition_root import AppContainer

def render_dashboard_page(
        container: AppContainer,
) -> None:
    st.title("🚧 Dashboard")
    st.write("Organization and patient monitoring overview.")
