# /src/gui/streamlit/screens/billing.py

import streamlit as st
from src.main.composition_root import AppContainer


def render_billing_page(

        container: AppContainer,
) -> None:
    st.title("🚧 Billing")
    st.write("Clinical reviews and scheduled activities.")
