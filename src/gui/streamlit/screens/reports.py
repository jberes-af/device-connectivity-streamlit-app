# /src/gui/streamlit/screens/reports.py
from src.main.composition_root import AppContainer

import streamlit as st


def render_reports_page(
        container: AppContainer,
) -> None:
    st.title("🚧 Reports")
    st.write("Clinical reviews and scheduled activities.")
