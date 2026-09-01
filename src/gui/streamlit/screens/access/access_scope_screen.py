import streamlit as st

from src.application.context import AccessScope, UserContext


_CSS_EXPANDER_ACCESS = """
<style>
    [data-testid="stExpander"] details {
        border-style: none;
    }
</style>
"""


def render_account_and_access_page(
        user_context: UserContext,
        access_scope: AccessScope,
) -> None:
    st.title(":material/account_circle: Account & Access")

    st.caption("User roles")
    for role in sorted(access_scope.roles, key=lambda item: item.value):
        st.write(role.value)

    st.caption("Organization")
    st.write(f"Active tenant ID: {user_context.tenant_id}")

    if access_scope.tenant_ids:
        st.write("Authorized tenant IDs:")
        for tenant_id in sorted(access_scope.tenant_ids):
            st.write(tenant_id)
    else:
        st.write("Authorized tenant boundary: platform")

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
