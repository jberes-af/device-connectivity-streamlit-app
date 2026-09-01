# /src/infrastructure/persistence/google_sheets/mappers/access/role_resource_scope_row_mapper.py

from src.domain.enums.access.resource_access_enums import (
    AccessResourceTypeEnum,
    ResourceScopeEnum,
)
from src.domain.enums.access.role_enums import UserRoleEnum

from src.domain.entities.access.authorization_entities import RoleResourceScope

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.access.role_resource_scope_columns import (
    RoleResourceScopeColumns
)

from src.infrastructure.persistence.common.utils_parsing import *


class RoleResourceScopeRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> RoleResourceScope:
        schema = RoleResourceScopeColumns

        return RoleResourceScope(
            role=parse_required_enum(
                row.get(schema.ROLE),
                enum_type=UserRoleEnum,
                field_name=schema.ROLE,
            ),
            resource_type=parse_required_enum(
                row.get(schema.RESOURCE_TYPE),
                enum_type=AccessResourceTypeEnum,
                field_name=schema.RESOURCE_TYPE,
            ),
            scope=parse_required_enum(
                row.get(schema.SCOPE),
                enum_type=ResourceScopeEnum,
                field_name=schema.SCOPE,
            ),
        )

    @staticmethod
    def to_row(
            role_resource_scope: RoleResourceScope,
    ) -> RawRow:
        schema = RoleResourceScopeColumns

        return {

            schema.ROLE:
                role_resource_scope.role,

            schema.RESOURCE_TYPE:
                role_resource_scope.resource_type,

            schema.SCOPE:
                role_resource_scope.scope,

        }
