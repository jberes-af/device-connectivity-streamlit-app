# /src/infrastructure/persistence/google_sheets/mappers/access/user_resource_assignment_row_mapper.py

from src.domain.enums.access.resource_access_enums import AccessResourceTypeEnum

from src.domain.entities.access.resource_access_entities import (
    UserResourceAssignment
)

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.access.user_resource_assignment_columns import (
    UserResourceAssignmentColumns
)

from src.infrastructure.persistence.common.utils_parsing import *


class UserResourceAssignmentRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> UserResourceAssignment:
        schema = UserResourceAssignmentColumns

        return UserResourceAssignment(
            assignment_id=parse_required_text(
                row.get(schema.ASSIGNMENT_ID),
                field_name=schema.ASSIGNMENT_ID,
            ),
            user_id=parse_required_text(
                row.get(schema.USER_ID),
                field_name=schema.USER_ID,
            ),
            tenant_id=parse_required_text(
                row.get(schema.TENANT_ID),
                field_name=schema.TENANT_ID,
            ),
            resource_type=parse_required_enum(
                row.get(schema.RESOURCE_TYPE),
                enum_type=AccessResourceTypeEnum,
                field_name=schema.RESOURCE_TYPE,
            ),
            resource_id=parse_required_text(
                row.get(schema.RESOURCE_ID),
                field_name=schema.RESOURCE_ID,
            ),
            granted_by_user_id=parse_required_text(
                row.get(schema.GRANTED_BY_USER_ID),
                field_name=schema.GRANTED_BY_USER_ID,
            ),
            granted_at=parse_required_datetime(
                row.get(schema.GRANTED_AT),
                field_name=schema.GRANTED_AT,
            ),
            is_active=parse_required_bool(
                row.get(schema.IS_ACTIVE),
                field_name=schema.IS_ACTIVE,
            ),
        )

    @staticmethod
    def to_row(
            user_resource_assignment: UserResourceAssignment,
    ) -> RawRow:
        schema = UserResourceAssignmentColumns

        return {

            schema.ASSIGNMENT_ID:
                user_resource_assignment.assignment_id,

            schema.USER_ID:
                user_resource_assignment.user_id,

            schema.TENANT_ID:
                user_resource_assignment.tenant_id,

            schema.RESOURCE_TYPE:
                user_resource_assignment.resource_type.value,

            schema.RESOURCE_ID:
                user_resource_assignment.resource_id,

            schema.GRANTED_BY_USER_ID:
                user_resource_assignment.granted_by_user_id,

            schema.GRANTED_AT:
                user_resource_assignment.granted_at.isoformat(),

            schema.IS_ACTIVE:
                user_resource_assignment.is_active,

        }
