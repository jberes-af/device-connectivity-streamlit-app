# /src/infrastructure/persistence/google_sheets/mappers/tenant/user_tenant_membership_row_mapper.py

from src.domain.enums.person.tenant_enums import UserRoleEnum

from src.domain.entities.access.access_entities import UserTenantMembership

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.access.user_tenant_membership_columns import (
    UserTenantMembershipColumns,
)

from src.infrastructure.persistence.common.utils_parsing import (
    parse_optional_bool,
    parse_optional_enum,
    parse_required_text,
)


class UserTenantMembershipRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> UserTenantMembership:
        schema = UserTenantMembershipColumns

        return UserTenantMembership(
            user_id=parse_required_text(
                row.get(schema.USER_ID),
                field_name=schema.USER_ID,
            ),
            tenant_id=parse_required_text(
                row.get(schema.TENANT_ID),
                field_name=schema.TENANT_ID,
            ),
            role=parse_optional_enum(
                row.get(schema.ROLE),
                enum_type=UserRoleEnum,
                field_name=schema.ROLE,
            ),
            is_active=parse_optional_bool(
                row.get(schema.IS_ACTIVE),
                field_name=schema.IS_ACTIVE,
            ),
        )

    @staticmethod
    def to_row(
            user_tenant_membership: UserTenantMembership,
    ) -> RawRow:
        schema = UserTenantMembershipColumns

        return {

            schema.USER_ID:
                user_tenant_membership.user_id,

            schema.TENANT_ID:
                user_tenant_membership.tenant_id,

            schema.ROLE:
                user_tenant_membership.role,

            schema.IS_ACTIVE:
                user_tenant_membership.is_active,

        }
