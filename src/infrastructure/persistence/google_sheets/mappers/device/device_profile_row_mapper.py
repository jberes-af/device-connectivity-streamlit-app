# /src/infrastructure/persistence/google_sheets/mappers/device/device_profile_row_mapper.py

from src.domain.enums.sensing.device_enums import (
    DeviceTypeEnum,
    # SensorTypeEnum,
    SensorPurposeEnum,
)

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.device.device_profile_columns import (
    DeviceAdministrationProfileColumns
)

from src.domain.entities.sensing.device_entities import (
    DeviceAdministrationProfile
)

from src.infrastructure.persistence.common.utils_parsing import *


class DeviceAdministrationProfileRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> DeviceAdministrationProfile:
        schema = DeviceAdministrationProfileColumns

        return DeviceAdministrationProfile(
            device_id=parse_required_text(
                row.get(schema.DEVICE_ID),
                field_name=schema.DEVICE_ID,
            ),
            device_type=parse_optional_enum(
                row.get(schema.DEVICE_TYPE),
                enum_type=DeviceTypeEnum,
                field_name=schema.DEVICE_TYPE,
            ),
            tenant_id=parse_required_text(
                row.get(schema.TENANT_ID),
                field_name=schema.TENANT_ID,
            ),
            sensor_purpose=parse_optional_enum(
                row.get(schema.SENSOR_PURPOSE),
                enum_type=SensorPurposeEnum,
                field_name=schema.SENSOR_PURPOSE,
            ),
            install_date=parse_optional_date(
                row.get(schema.INSTALL_DATE),
                field_name=schema.INSTALL_DATE,
            ),
            removed_date=parse_optional_date(
                row.get(schema.REMOVED_DATE),
                field_name=schema.REMOVED_DATE,
            ),
            owned_from_date=parse_optional_date(
                row.get(schema.OWNED_FROM_DATE),
                field_name=schema.OWNED_FROM_DATE,
            ),
            owned_to_date=parse_optional_date(
                row.get(schema.OWNED_TO_DATE),
                field_name=schema.OWNED_TO_DATE,
            ),
            hardware_version=parse_optional_text(
                row.get(schema.HARDWARE_VERSION),
                field_name=schema.HARDWARE_VERSION,
            ),
            firmware_version_sensor=parse_optional_text(
                row.get(schema.FIRMWARE_VERSION_SENSOR),
                field_name=schema.FIRMWARE_VERSION_SENSOR,
            ),
            firmware_version_gateway=parse_optional_text(
                row.get(schema.FIRMWARE_VERSION_GATEWAY),
                field_name=schema.FIRMWARE_VERSION_GATEWAY,
            ),
            firmware_version_cellular=parse_optional_text(
                row.get(schema.FIRMWARE_VERSION_CELLULAR),
                field_name=schema.FIRMWARE_VERSION_CELLULAR,
            ),
        )

    @staticmethod
    def to_row(
            device_administration_profile: DeviceAdministrationProfile,
    ) -> RawRow:
        schema = DeviceAdministrationProfileColumns

        return {

            schema.DEVICE_ID:
                device_administration_profile.device_id,

            schema.DEVICE_TYPE:
                device_administration_profile.device_type,

            schema.TENANT_ID:
                device_administration_profile.tenant_id,

            schema.SENSOR_PURPOSE:
                device_administration_profile.sensor_purpose,

            schema.INSTALL_DATE:
                device_administration_profile.install_date,

            schema.REMOVED_DATE:
                device_administration_profile.removed_date,

            schema.OWNED_FROM_DATE:
                device_administration_profile.owned_from_date,

            schema.OWNED_TO_DATE:
                device_administration_profile.owned_to_date,

            schema.HARDWARE_VERSION:
                device_administration_profile.hardware_version,

            schema.FIRMWARE_VERSION_SENSOR:
                device_administration_profile.firmware_version_sensor,

            schema.FIRMWARE_VERSION_GATEWAY:
                device_administration_profile.firmware_version_gateway,

            schema.FIRMWARE_VERSION_CELLULAR:
                device_administration_profile.firmware_version_cellular,

        }
