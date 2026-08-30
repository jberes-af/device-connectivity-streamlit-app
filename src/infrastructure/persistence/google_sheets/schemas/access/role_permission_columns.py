# /src/infrastructure/persistence/google_sheets/schemas/access/role_permission_columns.py

class RolePermissionColumns:
    ROLE: str = "role"
    PERMISSION: str = "permission"
    ORDER = (
        ROLE,
        PERMISSION,
    )
