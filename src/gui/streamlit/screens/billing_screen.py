# /src/gui/streamlit/screens/billing_screen.py

import streamlit as st

from src.main.compose_root_application import AppContainer


def render_billing_page(
        container: AppContainer,
) -> None:
    st.title("🚧 :material/receipt_long: Billing")
    st.write("Clinical reviews and scheduled activities.")
