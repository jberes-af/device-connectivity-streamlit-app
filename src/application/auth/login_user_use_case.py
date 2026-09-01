# /src/application/auth/login_user_use_case.py


from src.domain.entities.user.user_entities import (
    UserProfile,
)
from src.domain.entities.access.membership_entities import UserTenantMembership

from src.application.auth.dto import (
    AuthenticatedUserDTO,
    LoginRequestDTO,
    LoginResultDTO,
)
from src.application.auth.ports import AuthenticationPort

from src.application.ports.user_repo_ports import (
    UserProfileRepositoryPort,
)

from src.application.ports.access_repo_ports import UserTenantMembershipRepositoryPort


class LoginUser:
    def __init__(
            self,
            authentication: AuthenticationPort,
            user_repository: UserProfileRepositoryPort,
            membership_repository: UserTenantMembershipRepositoryPort,
    ) -> None:
        self._authentication = authentication
        self._user_profile_repo = user_repository
        self._tenant_membership_repo = membership_repository

    def execute(
            self,
            request: LoginRequestDTO,
    ) -> LoginResultDTO:
        authenticated_user: AuthenticatedUserDTO = (
            self._authentication.authenticate(
                email=request.email,
                password=request.password,
            ))

        # --- USER PROFILE

        user: UserProfile = self._user_profile_repo.get_by_id(
            authenticated_user.uid,
        )

        if user is None:
            raise ValueError(
                "Authenticated user is not registered in the application."
            )

        memberships = self._list_active_by_user_id(
            user_id=authenticated_user.uid,
        )

        if not memberships:
            raise ValueError(
                "User does not have an active tenant membership."
            )

        if len(memberships) != 1:
            raise ValueError(
                "MVP login requires exactly one active tenant membership."
            )

        return LoginResultDTO(
            user_id=authenticated_user.uid,
            email=authenticated_user.email,
            display_name=user.user_name,
            memberships=memberships,
        )

    def _list_active_by_user_id(
            self,
            user_id: str,
    ) -> tuple[UserTenantMembership, ...]:
        memberships: tuple[UserTenantMembership, ...] = (
            self._tenant_membership_repo.list_for_user_id(
                user_id=user_id,
            ))

        return tuple(
            membership
            for membership in memberships
            if membership.is_active
        )
