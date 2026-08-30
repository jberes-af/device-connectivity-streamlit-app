# /src/infrastructure/persistence/google_sheets/schemas/access/user_tenant_membership_columns.py

class UserTenantMembershipColumns:
    MEMBERSHIP_ID: str = "membership_id"
    USER_ID: str = "user_id"
    TENANT_ID: str = "tenant_id"
    IS_ACTIVE: str = "is_active"
    ORDER = (
        MEMBERSHIP_ID,
        USER_ID,
        TENANT_ID,
        IS_ACTIVE,
    )
