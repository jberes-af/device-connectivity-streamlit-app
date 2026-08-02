# /src/gui/streamlit/screens/schedule.py
from src.main.composition_root import AppContainer

import streamlit as st


def render_schedule_page(

        container: AppContainer,
) -> None:
    st.title("🚧 Schedule")
    st.write("Clinical reviews and scheduled activities.")
