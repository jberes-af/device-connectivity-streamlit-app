# /src/infrastructure/persistence/mappers/person/user_resident_access_row_mapper.py

# from src.domain.enums.person.tenant_enums import UserRoleEnum

from src.domain.enums.person.resident_enums import ResidentAccessLevelEnum
from src.domain.entities.access.access_entities import UserResidentAccess

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.access.user_resident_access_columns import (
    UserResidentAccessColumns
)

from src.infrastructure.persistence.common.utils_parsing import (
    parse_optional_bool,
    parse_optional_date,
    parse_optional_enum,
    parse_required_text,
)


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
            access_level=parse_optional_enum(
                row.get(schema.ACCESS_LEVEL),
                enum_type=ResidentAccessLevelEnum,
                field_name=schema.ACCESS_LEVEL,
            ),
            granted_by_user_id=parse_required_text(
                row.get(schema.GRANTED_BY_USER_ID),
                field_name=schema.GRANTED_BY_USER_ID,
            ),
            granted_at_date=parse_optional_date(
                row.get(schema.GRANTED_AT_DATE),
                field_name=schema.GRANTED_AT_DATE,
            ),
            active=parse_optional_bool(
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

            schema.GRANTED_AT_DATE:
                user_resident_access.granted_at_date,

            schema.ACTIVE:
                user_resident_access.active,

        }
