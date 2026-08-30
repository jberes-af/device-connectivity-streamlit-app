# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.schemas.user_tenant_membership_columns import UserTenantMembershipColumns

from src.domain.entities.entities import UserTenantMembership

from src.infrastructure.persistence.common.utils_parsing import *


class UserTenantMembershipRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> UserTenantMembership:
        schema = UserTenantMembershipColumns

        return UserTenantMembership(
            membership_id=parse_required_text(
                row.get(schema.MEMBERSHIP_ID),
                field_name=schema.MEMBERSHIP_ID,
            ),
            user_id=parse_required_text(
                row.get(schema.USER_ID),
                field_name=schema.USER_ID,
            ),
            tenant_id=parse_required_text(
                row.get(schema.TENANT_ID),
                field_name=schema.TENANT_ID,
            ),
            is_active=parse_optional_text(
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

            schema.MEMBERSHIP_ID:
                user_tenant_membership.membership_id,

            schema.USER_ID:
                user_tenant_membership.user_id,

            schema.TENANT_ID:
                user_tenant_membership.tenant_id,

            schema.IS_ACTIVE:
                user_tenant_membership.is_active,

        }