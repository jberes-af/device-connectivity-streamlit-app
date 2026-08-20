# /src/gui/streamlit/session/session_context_adapter.py

import streamlit as st

from src.application.context import SessionContext


def get_session_context() -> SessionContext:
    context = st.session_state.get_all_sensor_events("session_context")

    if context is None:
        context = SessionContext()
        st.session_state["session_context"] = context

    if not isinstance(context, SessionContext):
        raise TypeError(
            "Invalid session_context stored in Streamlit session state."
        )

    return context