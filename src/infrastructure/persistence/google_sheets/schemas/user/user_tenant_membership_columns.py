# /src/infrastructure/persistence/schemas/user/user_tenant_membership_columns.py

class UserTenantMembershipColumns:
    USER_ID: str = "user_id"
    TENANT_ID: str = "tenant_id"
    ROLE: str = "role"
    IS_ACTIVE: str = "is_active"
    ORDER = (
        USER_ID,
        TENANT_ID,
        ROLE,
        IS_ACTIVE,
    )
