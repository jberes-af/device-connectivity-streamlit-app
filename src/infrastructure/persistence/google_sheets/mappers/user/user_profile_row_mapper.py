# /src/infrastructure/persistence/google_sheets/mappers/tenant/user_profile_row_mapper.py


from src.domain.entities.user.user_entities import UserProfile

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.user.user_profile_columns import (
    UserProfileColumns,
)

from src.infrastructure.persistence.common.utils_parsing import *


class UserProfileRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> UserProfile:
        schema = UserProfileColumns

        return UserProfile(
            user_id=parse_required_text(
                row.get(schema.USER_ID),
                field_name=schema.USER_ID,
            ),
            user_name=parse_required_text(
                row.get(schema.USER_NAME),
                field_name=schema.USER_NAME,
            ),
            user_telephone=parse_required_text(
                row.get(schema.USER_TELEPHONE),
                field_name=schema.USER_TELEPHONE,
            ),
            user_email_address=parse_required_text(
                row.get(schema.USER_EMAIL_ADDRESS),
                field_name=schema.USER_EMAIL_ADDRESS,
            ),
            user_image=parse_required_text(
                row.get(schema.USER_IMAGE),
                field_name=schema.USER_IMAGE,
            ),
            color_scheme=parse_required_text(
                row.get(schema.COLOR_SCHEME),
                field_name=schema.COLOR_SCHEME,
            ),
        )

    @staticmethod
    def to_row(
            user_profile: UserProfile,
    ) -> RawRow:
        schema = UserProfileColumns

        return {

            schema.USER_ID:
                user_profile.user_id,

            schema.USER_NAME:
                user_profile.user_name,

            schema.USER_TELEPHONE:
                user_profile.user_telephone,

            schema.USER_EMAIL_ADDRESS:
                user_profile.user_email_address,

            schema.USER_IMAGE:
                user_profile.user_image,

            schema.COLOR_SCHEME:
                user_profile.color_scheme,

        }
