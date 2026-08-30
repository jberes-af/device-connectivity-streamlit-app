# /src/infrastructure/persistence/google_sheets/mappers/access/access_scope_row_mapper.py


from src.domain.enums.access.permission_enums import (
    PermissionEnum,
)
from src.domain.enums.access.role_enums import UserRoleEnum
from src.domain.enums.access.resource_access_enums import (
    AccessResourceTypeEnum,
    ResourceScopeEnum,
)

from src.application.context import AccessScope

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.access.access_scope_columns import (
    AccessScopeColumns
)

from src.infrastructure.persistence.common.utils_parsing import *


class AccessScopeRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> AccessScope:
        schema = AccessScopeColumns

        return AccessScope(
            user_id=parse_required_text(
                row.get(schema.USER_ID),
                field_name=schema.USER_ID,
            ),
            tenant_id=parse_required_text(
                row.get(schema.TENANT_ID),
                field_name=schema.TENANT_ID,
            ),
            roles=parse_optional_enum(
                row.get(schema.ROLES),
                enum_type=UserRoleEnum,
                field_name=schema.ROLES,
            ),
            permissions=parse_optional_enum(
                row.get(schema.PERMISSIONS),
                enum_type=PermissionEnum,
                field_name=schema.PERMISSIONS,
            ),
            resident_scope=parse_optional_text(
                row.get(schema.RESIDENT_SCOPE),
                field_name=schema.RESIDENT_SCOPE,
            ),
            sensor_scope=parse_optional_text(
                row.get(schema.SENSOR_SCOPE),
                field_name=schema.SENSOR_SCOPE,
            ),
            gateway_scope=parse_optional_text(
                row.get(schema.GATEWAY_SCOPE),
                field_name=schema.GATEWAY_SCOPE,
            ),
            resident_ids=parse_optional_text(
                row.get(schema.RESIDENT_IDS),
                field_name=schema.RESIDENT_IDS,
            ),
            sensor_ids=parse_optional_text(
                row.get(schema.SENSOR_IDS),
                field_name=schema.SENSOR_IDS,
            ),
            gateway_ids=parse_optional_text(
                row.get(schema.GATEWAY_IDS),
                field_name=schema.GATEWAY_IDS,
            ),
        )

    @staticmethod
    def to_row(
            access_scope: AccessScope,
    ) -> RawRow:
        schema = AccessScopeColumns

        return {

            schema.USER_ID:
                access_scope.user_id,

            schema.TENANT_ID:
                access_scope.tenant_id,

            schema.ROLES:
                access_scope.roles,

            schema.PERMISSIONS:
                access_scope.permissions,

            schema.RESIDENT_SCOPE:
                access_scope.resident_scope,

            schema.SENSOR_SCOPE:
                access_scope.sensor_scope,

            schema.GATEWAY_SCOPE:
                access_scope.gateway_scope,

            schema.RESIDENT_IDS:
                access_scope.resident_ids,

            schema.SENSOR_IDS:
                access_scope.sensor_ids,

            schema.GATEWAY_IDS:
                access_scope.gateway_ids,

        }
