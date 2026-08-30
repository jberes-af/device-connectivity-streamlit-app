# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.role_permission_columns import RolePermissionColumns

from src.domain.entities.entities import RolePermission

from src.infrastructure.persistence.common.utils_parsing import *


class RolePermissionRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> RolePermission:
        schema = RolePermissionColumns

        return RolePermission(
            role=parse_optional_text(
                row.get(schema.ROLE),
                field_name=schema.ROLE,
            ),
            permission=parse_optional_text(
                row.get(schema.PERMISSION),
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
                role_permission.role,

            schema.PERMISSION:
                role_permission.permission,

        }