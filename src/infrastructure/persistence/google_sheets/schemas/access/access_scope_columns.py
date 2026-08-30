# /src/infrastructure/persistence/google_sheets/schemas/access/access_scope_columns.py

class AccessScopeColumns:
    USER_ID: str = "user_id"
    TENANT_ID: str = "tenant_id"
    ROLES: str = "roles"
    PERMISSIONS: str = "permissions"
    RESIDENT_SCOPE: str = "resident_scope"
    SENSOR_SCOPE: str = "sensor_scope"
    GATEWAY_SCOPE: str = "gateway_scope"
    RESIDENT_IDS: str = "resident_ids"
    SENSOR_IDS: str = "sensor_ids"
    GATEWAY_IDS: str = "gateway_ids"
    ORDER = (
        USER_ID,
        TENANT_ID,
        ROLES,
        PERMISSIONS,
        RESIDENT_SCOPE,
        SENSOR_SCOPE,
        GATEWAY_SCOPE,
        RESIDENT_IDS,
        SENSOR_IDS,
        GATEWAY_IDS,
    )
