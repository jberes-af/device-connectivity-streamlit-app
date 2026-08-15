# /src/infrastructure/persistence/schemas

class UserSensorLinkColumns:
    TENANT_ID: str = "tenant_id"
    USER_ID: str = "user_id"
    SENSOR_ID: str = "sensor_id"
    ORDER = (
TENANT_ID,
USER_ID,
SENSOR_ID,
)