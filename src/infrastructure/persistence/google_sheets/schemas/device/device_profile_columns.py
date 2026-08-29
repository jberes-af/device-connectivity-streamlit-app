# /src/infrastructure/persistence/schemas/device/device_profile_columns.py

class DeviceAdministrationProfileColumns:
    DEVICE_ID: str = "device_id"
    DEVICE_TYPE: str = "device_type"
    TENANT_ID: str = "tenant_id"
    SENSOR_PURPOSE: str = "sensor_purpose"
    INSTALL_DATE: str = "install_date"
    REMOVED_DATE: str = "removed_date"
    OWNED_FROM_DATE: str = "owned_from_date"
    OWNED_TO_DATE: str = "owned_to_date"
    HARDWARE_VERSION: str = "hardware_version"
    FIRMWARE_VERSION_SENSOR: str = "firmware_version_sensor"
    FIRMWARE_VERSION_GATEWAY: str = "firmware_version_gateway"
    FIRMWARE_VERSION_CELLULAR: str = "firmware_version_cellular"
    ORDER = (
        DEVICE_ID,
        DEVICE_TYPE,
        TENANT_ID,
        SENSOR_PURPOSE,
        INSTALL_DATE,
        REMOVED_DATE,
        OWNED_FROM_DATE,
        OWNED_TO_DATE,
        HARDWARE_VERSION,
        FIRMWARE_VERSION_SENSOR,
        FIRMWARE_VERSION_GATEWAY,
        FIRMWARE_VERSION_CELLULAR,
    )
