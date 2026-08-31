# /src/infrastructure/persistence/google_sheets/schemas/access/role_resource_scope_columns.py

class RoleResourceScopeColumns:
    ROLE: str = "role"
    RESOURCE_TYPE: str = "resource_type"
    SCOPE: str = "scope"
    ORDER = (
        ROLE,
        RESOURCE_TYPE,
        SCOPE,
    )
