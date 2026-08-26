# /src/gui/streamlit/components/badge_renderer.py


import streamlit as st

from src.interface_adapters.view_models.widgets.badge_view_model import (
    BadgeViewModel,
    BadgeVariant,
)


def render_badge(
        badge: BadgeViewModel,
) -> None:
    if badge.variant == BadgeVariant.SUCCESS:
        st.success(badge.label)

    elif badge.variant == BadgeVariant.WARNING:
        st.warning(badge.label)

    elif badge.variant == BadgeVariant.ERROR:
        st.error(badge.label)

    elif badge.variant == BadgeVariant.INFO:
        st.info(badge.label)

    else:
        st.write(badge.label)
