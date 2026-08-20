# /src/gui/streamlit/screens/administration_screen.py

import streamlit as st

from src.main.compose_root_application import AppContainer


def render_administration_page(
        container: AppContainer,
) -> None:
    st.title("🚧 :material/note_alt: Administration")
    st.write("Clinical reviews and scheduled activities.")
