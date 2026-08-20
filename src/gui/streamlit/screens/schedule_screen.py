# /src/gui/streamlit/screens/schedule_screen.py

import streamlit as st

from src.main.compose_root_application import AppContainer


def render_schedule_page(

        container: AppContainer,
) -> None:
    st.title("🚧 :material/calendar_month: Schedule")
    st.write("Clinical reviews and scheduled activities.")
