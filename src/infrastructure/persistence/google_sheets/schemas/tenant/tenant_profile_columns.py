# /src/infrastructure/persistence/schemas/tenant/tenant_profile_columns.py

class TenantProfileColumns:
    TENANT_ID: str = "tenant_id"
    TENANT_NAME: str = "tenant_name"
    TENANT_TYPE: str = "tenant_type"

    TENANT_STREET: str = "tenant_street"
    TENANT_CITY: str = "tenant_city"
    TENANT_STATE: str = "tenant_state"
    TENANT_POSTAL_CODE: str = "tenant_postal_code"

    TENANT_TELEPHONE: str = "tenant_telephone"
    TENANT_MANAGER: str = "tenant_manager"
    TIMEZONE: str = "timezone"
    ORDER = (
        TENANT_ID,
        TENANT_NAME,
        TENANT_TYPE,
        TENANT_STREET,
        TENANT_CITY,
        TENANT_STATE,
        TENANT_POSTAL_CODE,
        TENANT_TELEPHONE,
        TENANT_MANAGER,
        TIMEZONE,
    )
