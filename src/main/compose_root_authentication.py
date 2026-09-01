# /src/main/compose_root_authentication.py

from dataclasses import dataclass

from src.application.auth.ports import AuthenticationPort

from src.application.ports.user_repo_ports import (
    UserProfileRepositoryPort,
)

from src.application.ports.access_repo_ports import UserTenantMembershipRepositoryPort

from src.application.auth.login_user_use_case import LoginUser

from src.infrastructure.auth.firebase.firebase_client_auth_service import (
    FirebaseAuthenticationAdapter,
)

from src.infrastructure.auth.firebase.pyrebase_config_mapper import (
    PyrebaseConfigMapper,
)

from src.interface_adapters.auth.auth_controller import (
    AuthController,
)
from src.interface_adapters.presenters.auth.auth_presenter import (
    AuthPresenter,
)

from src.main.compose_root_infrastructure import (
    InfrastructureContainer,
)


@dataclass(frozen=True, slots=True)
class AuthenticationContainer:
    auth_controller: AuthController
    auth_presenter: AuthPresenter


def build_authentication_container(
    infrastructure: InfrastructureContainer,
) -> AuthenticationContainer:

    # --- INFRASTRUCTURE ADAPTER
    pyrebase_config = PyrebaseConfigMapper.from_settings(
        infrastructure.settings.firebase_web,
    )

    auth_service: AuthenticationPort = FirebaseAuthenticationAdapter(
        web_config=pyrebase_config,
    )

    user_repository: UserProfileRepositoryPort = (
        infrastructure.user_repository.user_profile_repository
    )

    membership_repository: UserTenantMembershipRepositoryPort = (
        infrastructure.access_repository.user_tenant_membership_repository
    )

    # --- APPLICATION USE CASE
    login_user = LoginUser(
        authentication=auth_service,
        user_repository=user_repository,
        membership_repository=membership_repository,
    )

    # --- INTERFACE ADAPTERS

    auth_controller = AuthController(
        login_user=login_user,
    )

    auth_presenter = AuthPresenter()

    return AuthenticationContainer(
        auth_controller=auth_controller,
        auth_presenter=auth_presenter,
    )

