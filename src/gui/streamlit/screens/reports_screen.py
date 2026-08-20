# /src/gui/streamlit/screens/reports_screen.py

import streamlit as st

from src.main.compose_root_application import AppContainer


def render_reports_page(
        container: AppContainer,
) -> None:
    st.title("🚧 :material/analytics: Reports")
    st.write("Clinical reviews and scheduled activities.")
