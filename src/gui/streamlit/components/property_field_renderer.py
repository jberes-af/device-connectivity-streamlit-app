# /src/gui/streamlit/components/property_field_renderer.py

from src.interface_adapters.view_models.common.property_field_view_model import (
    PropertyStatus,
    PropertyFieldViewModel,
)

import streamlit as st


def render_property_field(
        field: PropertyFieldViewModel,
):
    st.caption(field.label)

    if field.status == PropertyStatus.SUCCESS:
        st.success(field.value)

    elif field.status == PropertyStatus.WARNING:
        st.warning(field.value)

    elif field.status == PropertyStatus.ERROR:
        st.error(field.value)

    else:
        st.write(field.value)
