from __future__ import annotations

from typing import Any, Mapping

from firebase.schemas.user_schema import UserRtdbSchema

# Adjust this import to match your project.
from src.domain.entities.person.user_entities import UserAccount, UserProfile


class UserRtdbMapper:
    @staticmethod
    def to_domain(user_id: str, data: Mapping[str, Any] | None) -> UserAccount:
        raw = data or {}

        telephone = (
            raw.get(UserRtdbSchema.FIELD_TELEPHONE)
            or raw.get(UserRtdbSchema.FIELD_PHONE)
            or ""
        )

        profile = UserProfile(
            user_id=user_id,
            user_name=str(raw.get(UserRtdbSchema.FIELD_NAME, "") or ""),
            user_telephone=str(telephone),
            user_email_address=str(raw.get(UserRtdbSchema.FIELD_EMAIL, "") or ""),
            user_image="",
            color_scheme="",
        )

        return UserAccount(
            user_id=user_id,
            user_profile=profile,
        )

    @staticmethod
    def to_rtdb(entity: UserAccount) -> dict[str, Any]:
        profile = entity.user_profile

        return {
            UserRtdbSchema.FIELD_NAME: profile.user_name,
            UserRtdbSchema.FIELD_TELEPHONE: profile.user_telephone,
            UserRtdbSchema.FIELD_EMAIL: profile.user_email_address,
        }
