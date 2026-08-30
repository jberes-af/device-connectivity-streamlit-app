# /src/infrastructure/persistence/google_sheets/schemas/access/user_resource_assignment_columns.py

class UserResourceAssignmentColumns:
    ASSIGNMENT_ID: str = "assignment_id"
    USER_ID: str = "user_id"
    TENANT_ID: str = "tenant_id"
    RESOURCE_TYPE: str = "resource_type"
    RESOURCE_ID: str = "resource_id"
    GRANTED_BY_USER_ID: str = "granted_by_user_id"
    GRANTED_AT: str = "granted_at"
    IS_ACTIVE: str = "is_active"
    ORDER = (
        ASSIGNMENT_ID,
        USER_ID,
        TENANT_ID,
        RESOURCE_TYPE,
        RESOURCE_ID,
        GRANTED_BY_USER_ID,
        GRANTED_AT,
        IS_ACTIVE,
    )
