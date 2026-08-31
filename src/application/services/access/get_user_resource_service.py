# /src/application/services/access/get_user_resource_service.py

from src.domain.entities.access.resource_access_entities import (
    UserResourceAssignment,
)

from src.application.ports.access_repo_ports import (
    UserResourceAssignmentRepositoryPort,
)


class FetchUserResourceAssignmentService:

    def __init__(
            self,
            *,
            user_resource_assignment_repository: UserResourceAssignmentRepositoryPort
    ):
        self._user_resource_repo = user_resource_assignment_repository

    def fetch_resource_assignments_for_user(
            self,
            user_id: str,
            tenant_id: str,
    ) -> tuple[UserResourceAssignment, ...]:
        return tuple(
            self._user_resource_repo.list_for_user_and_tenant(
                user_id=user_id,
                tenant_id=tenant_id,
            )
        )
