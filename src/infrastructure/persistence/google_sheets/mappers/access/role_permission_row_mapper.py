# /src/infrastructure/persistence/google_sheets/mappers/access/role_permission_row_mapper.py

from src.domain.enums.access.permission_enums import PermissionEnum
from src.domain.enums.access.role_enums import UserRoleEnum

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.access.role_permission_columns import (
    RolePermissionColumns
)

from src.domain.entities.access.authorization_entities import RolePermission

from src.infrastructure.persistence.common.utils_parsing import (
    parse_required_enum,
)


class RolePermissionRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> RolePermission:
        schema = RolePermissionColumns

        return RolePermission(
            role=parse_required_enum(
                row.get(schema.ROLE),
                enum_type=UserRoleEnum,
                field_name=schema.ROLE,
            ),
            permission=parse_required_enum(
                row.get(schema.PERMISSION),
                enum_type=PermissionEnum,
                field_name=schema.PERMISSION,
            ),
        )

    @staticmethod
    def to_row(
            role_permission: RolePermission,
    ) -> RawRow:
        schema = RolePermissionColumns

        return {

            schema.ROLE:
                role_permission.role.value,

            schema.PERMISSION:
                role_permission.permission.value,

        }
