# /src/gui/streamlit/screens/access_scope_screen.py

import streamlit as st

from src.application.context import UserContext

from src.application.use_cases.access.access_scope_uc_dtos import (
    AccessScopeResultDTO,
)

# from src.main.compose_root_application import AppContainer


_CSS_EXPANDER_ACCESS = """
<style>
    [data-testid="stExpander"] details {
        border-style: none;
    }
</style>
"""


def render_account_and_access_page(
        user_context: UserContext,
        access_scope: AccessScopeResultDTO,
) -> None:
    st.title("🚧 :material/account_circle: Account & Access")
    # st.write("Organization and treatment monitoring overview.")

    st.caption("User Role")

    st.write("")
    st.write("")

    st.write(user_context.role.value)

    st.write("")
    st.write("")

    st.caption("Organization")
    st.write(access_scope.tenant_profile.tenant_name)
    st.write(f"Tenant ID:       {access_scope.tenant_profile.tenant_id}")
    st.write(f"Tenant Type:     {access_scope.tenant_profile.tenant_type}")
    st.write(f"Address:         {access_scope.tenant_profile.tenant_street}")
    st.write(f"                 {access_scope.tenant_profile.tenant_city} •"
             f" {access_scope.tenant_profile.tenant_state} • "
             f"{access_scope.tenant_profile.tenant_postal_code}")
    st.write(f"Manager:         {access_scope.tenant_profile.tenant_manager}")

    st.write("")
    st.write("")

    st.caption("Access Scope")

    st.markdown(
        _CSS_EXPANDER_ACCESS,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        with st.expander(
                f"Residents ({len(access_scope.resident_ids)})"
        ):
            for resident_id in access_scope.resident_ids:
                st.write(resident_id)

    with col2:

        with st.expander(
                f"Sensors ({len(access_scope.sensor_ids)})",
        ):
            for sensor_id in access_scope.sensor_ids:
                st.write(sensor_id)

    with col3:

        with st.expander(
                f"Gateways ({len(access_scope.gateway_ids)})",
        ):
            for gateway_id in access_scope.gateway_ids:
                st.write(gateway_id)
