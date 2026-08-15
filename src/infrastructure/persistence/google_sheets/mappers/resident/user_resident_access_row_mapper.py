# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas import UserResidentAccessColumns

from src.domain.entities.entities import UserResidentAccess

from src.infrastructure.persistence.common.utils_parsing import *


class UserResidentAccessRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> UserResidentAccess:
        schema = UserResidentAccessColumns

        return UserResidentAccess(
            user_id=parse_required_text(
                row.get(schema.USER_ID),
                field_name=schema.USER_ID,
            ),
            tenant_id=parse_required_text(
                row.get(schema.TENANT_ID),
                field_name=schema.TENANT_ID,
            ),
            resident_id=parse_required_text(
                row.get(schema.RESIDENT_ID),
                field_name=schema.RESIDENT_ID,
            ),
            access_level=parse_optional_text(
                row.get(schema.ACCESS_LEVEL),
                field_name=schema.ACCESS_LEVEL,
            ),
            granted_by_user_id=parse_required_text(
                row.get(schema.GRANTED_BY_USER_ID),
                field_name=schema.GRANTED_BY_USER_ID,
            ),
            granted_at_iso=parse_required_text(
                row.get(schema.GRANTED_AT_ISO),
                field_name=schema.GRANTED_AT_ISO,
            ),
            active=parse_optional_text(
                row.get(schema.ACTIVE),
                field_name=schema.ACTIVE,
            ),
        )


    @staticmethod
    def to_row(
        user_resident_access: UserResidentAccess,
    ) -> RawRow:
        schema = UserResidentAccessColumns

        return {

            schema.USER_ID:
                user_resident_access.user_id,

            schema.TENANT_ID:
                user_resident_access.tenant_id,

            schema.RESIDENT_ID:
                user_resident_access.resident_id,

            schema.ACCESS_LEVEL:
                user_resident_access.access_level,

            schema.GRANTED_BY_USER_ID:
                user_resident_access.granted_by_user_id,

            schema.GRANTED_AT_ISO:
                user_resident_access.granted_at_iso,

            schema.ACTIVE:
                user_resident_access.active,

        }