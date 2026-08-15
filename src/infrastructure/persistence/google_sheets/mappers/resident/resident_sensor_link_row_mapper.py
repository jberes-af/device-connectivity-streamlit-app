# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas import ResidentSensorLinkColumns

from src.domain.entities.entities import ResidentSensorLink

from src.infrastructure.persistence.common.utils_parsing import *


class ResidentSensorLinkRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> ResidentSensorLink:
        schema = ResidentSensorLinkColumns

        return ResidentSensorLink(
            resident_id=parse_required_text(
                row.get(schema.RESIDENT_ID),
                field_name=schema.RESIDENT_ID,
            ),
            sensor_id=parse_required_text(
                row.get(schema.SENSOR_ID),
                field_name=schema.SENSOR_ID,
            ),
            tenant_id=parse_required_text(
                row.get(schema.TENANT_ID),
                field_name=schema.TENANT_ID,
            ),
            active_from_iso=parse_optional_text(
                row.get(schema.ACTIVE_FROM_ISO),
                field_name=schema.ACTIVE_FROM_ISO,
            ),
            active_to_iso=parse_optional_text(
                row.get(schema.ACTIVE_TO_ISO),
                field_name=schema.ACTIVE_TO_ISO,
            ),
        )


    @staticmethod
    def to_row(
        resident_sensor_link: ResidentSensorLink,
    ) -> RawRow:
        schema = ResidentSensorLinkColumns

        return {

            schema.RESIDENT_ID:
                resident_sensor_link.resident_id,

            schema.SENSOR_ID:
                resident_sensor_link.sensor_id,

            schema.TENANT_ID:
                resident_sensor_link.tenant_id,

            schema.ACTIVE_FROM_ISO:
                resident_sensor_link.active_from_iso,

            schema.ACTIVE_TO_ISO:
                resident_sensor_link.active_to_iso,

        }