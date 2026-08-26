# /src/infrastructure/persistence/schemas/contact/resident_sensor_link_columns.py

class ResidentSensorLinkColumns:
    RESIDENT_ID: str = "resident_id"
    SENSOR_ID: str = "sensor_id"
    TENANT_ID: str = "tenant_id"
    ACTIVE_FROM_DATE: str = "active_from_date"
    ACTIVE_TO_DATE: str = "active_to_date"
    SETUP_DATE: str = "setup_date"
    REMOVED_DATE: str = "removed_date"
    ORDER = (
        RESIDENT_ID,
        SENSOR_ID,
        TENANT_ID,
        ACTIVE_FROM_DATE,
        ACTIVE_TO_DATE,
        SETUP_DATE,
        REMOVED_DATE,
    )
