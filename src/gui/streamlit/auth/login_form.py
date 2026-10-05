# /src/gui/streamlit/google_sheets/login_form.py

import streamlit as st

from src.application.context import (
    UserContext,
    SessionContext,
)

from src.interface_adapters.auth.auth_controller import (
    AuthController,
)

from src.interface_adapters.presenters.auth.auth_presenter import (
    AuthPresenter,
)


class LoginForm:
    def __init__(
            self,
            auth_controller: AuthController,
            auth_presenter: AuthPresenter,
    ) -> None:
        self.auth_controller = auth_controller
        self.auth_presenter = auth_presenter

    def render(self) -> None:
        st.write("Alerta Home Device Connectivity Web Application")
        st.title("🔐 Sign in")

        email = st.text_input(
            "📧 Email Address",
            placeholder="you@example.com",
            key="auth_user_name",
        )

        password = st.text_input(
            "🔑 Password",
            type="password",
            key="auth_pwd",
        )

        if not st.button("✅ Login"):
            return

        try:
            result = self.auth_controller.login(
                email=email,
                password=password,
            )

            view_model = self.auth_presenter.present_success(result)

        except Exception as exc:
            view_model = self.auth_presenter.present_error(
                str(exc)
            )

        if not view_model.success:
            st.error(view_model.message)
            return

        membership = result.memberships[0]

        st.session_state["session_context"] = SessionContext(
            user_context=UserContext(
                user_id=result.user_id,
                tenant_id=membership.tenant_id,
            )
        )

        st.success(view_model.message)
        st.rerun()
