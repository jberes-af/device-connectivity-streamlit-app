# /src/gui/streamlit/components/badge_renderer.py


import streamlit as st

from src.interface_adapters.view_models.widgets.badge_view_model import (
    BadgeViewModel,
    BadgeStyle,
)


def render_badge(
        badge: BadgeViewModel,
) -> None:
    if badge.style == BadgeStyle.SUCCESS:
        st.success(badge.text)

    elif badge.style == BadgeStyle.WARNING:
        st.warning(badge.text)

    elif badge.style == BadgeStyle.ERROR:
        st.error(badge.text)

    elif badge.style == BadgeStyle.INFO:
        st.info(badge.text)

    else:
        st.write(badge.text)
