# /src/infrastructure/persistence/google_sheets/schemas/access/user_tenant_role_assignment_columns.py

class UserTenantRoleAssignmentColumns:
    ROLE_ASSIGNMENT_ID: str = "role_assignment_id"
    MEMBERSHIP_ID: str = "membership_id"
    ROLE: str = "role"
    IS_ACTIVE: str = "is_active"
    ORDER = (
        ROLE_ASSIGNMENT_ID,
        MEMBERSHIP_ID,
        ROLE,
        IS_ACTIVE,
    )
