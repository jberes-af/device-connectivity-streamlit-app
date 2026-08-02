# /src/gui/streamlit/screens/administration.py
from src.main.composition_root import AppContainer

import streamlit as st


def render_administration_page(
        container: AppContainer,
) -> None:
    st.title("🚧 Administration")
    st.write("Clinical reviews and scheduled activities.")
