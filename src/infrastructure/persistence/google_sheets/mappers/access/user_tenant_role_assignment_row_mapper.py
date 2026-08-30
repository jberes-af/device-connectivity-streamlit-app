# /src/infrastructure/persistence/google_sheets/mappers/access/user_tenant_role_assignment_row_mapper.py

from src.domain.enums.access.role_enums import UserRoleEnum

from src.domain.entities.access.membership_entities import (
    UserTenantRoleAssignment
)

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.access \
    .user_tenant_role_assignment_columns import (
    UserTenantRoleAssignmentColumns
)

from src.infrastructure.persistence.common.utils_parsing import (
    parse_required_bool,
    parse_required_enum,
    parse_required_text,
)


class UserTenantRoleAssignmentRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> UserTenantRoleAssignment:
        schema = UserTenantRoleAssignmentColumns

        return UserTenantRoleAssignment(
            role_assignment_id=parse_required_text(
                row.get(schema.ROLE_ASSIGNMENT_ID),
                field_name=schema.ROLE_ASSIGNMENT_ID,
            ),
            membership_id=parse_required_text(
                row.get(schema.MEMBERSHIP_ID),
                field_name=schema.MEMBERSHIP_ID,
            ),
            role=parse_required_enum(
                row.get(schema.ROLE),
                enum_type=UserRoleEnum,
                field_name=schema.ROLE,
            ),
            is_active=parse_required_bool(
                row.get(schema.IS_ACTIVE),
                field_name=schema.IS_ACTIVE,
            ),
        )

    @staticmethod
    def to_row(
            user_tenant_role_assignment: UserTenantRoleAssignment,
    ) -> RawRow:
        schema = UserTenantRoleAssignmentColumns

        return {

            schema.ROLE_ASSIGNMENT_ID:
                user_tenant_role_assignment.role_assignment_id,

            schema.MEMBERSHIP_ID:
                user_tenant_role_assignment.membership_id,

            schema.ROLE:
                user_tenant_role_assignment.role.value,

            schema.IS_ACTIVE:
                user_tenant_role_assignment.is_active,

        }
