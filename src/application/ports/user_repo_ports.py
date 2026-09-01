# /src/application/ports/user_repo_ports.py

from typing import Protocol

from src.domain.entities.user.user_entities import UserProfile


class UserProfileRepositoryPort(Protocol):

    def list_user_profiles(self) -> tuple[UserProfile, ...]:
        ...

    def get_by_id(
            self,
            user_id: str,
    ) -> UserProfile:
        ...


