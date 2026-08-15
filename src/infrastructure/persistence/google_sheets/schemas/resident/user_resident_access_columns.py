# /src/infrastructure/persistence/schemas

class UserResidentAccessColumns:
    USER_ID: str = "user_id"
    TENANT_ID: str = "tenant_id"
    RESIDENT_ID: str = "resident_id"
    ACCESS_LEVEL: str = "access_level"
    GRANTED_BY_USER_ID: str = "granted_by_user_id"
    GRANTED_AT_ISO: str = "granted_at_iso"
    ACTIVE: str = "active"
    ORDER = (
USER_ID,
TENANT_ID,
RESIDENT_ID,
ACCESS_LEVEL,
GRANTED_BY_USER_ID,
GRANTED_AT_ISO,
ACTIVE,
)