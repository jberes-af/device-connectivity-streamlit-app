# /src/infrastructure/persistence/mappers/person/resident_sensor_link_row_mapper.py

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.access.resident_sensor_link_columns import (
    ResidentSensorLinkColumns,
)

from src.domain.entities.access.access_entities import ResidentSensorLink

from src.infrastructure.persistence.common.utils_parsing import (
    parse_optional_date,
    parse_required_text,
)


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
            active_from_date=parse_optional_date(
                row.get(schema.ACTIVE_FROM_DATE),
                field_name=schema.ACTIVE_FROM_DATE,
            ),
            active_to_date=parse_optional_date(
                row.get(schema.ACTIVE_TO_DATE),
                field_name=schema.ACTIVE_TO_DATE,
            ),
            setup_date=parse_optional_date(
                row.get(schema.SETUP_DATE),
                field_name=schema.SETUP_DATE,
            ),
            removed_date=parse_optional_date(
                row.get(schema.REMOVED_DATE),
                field_name=schema.REMOVED_DATE,
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

            schema.ACTIVE_FROM_DATE:
                resident_sensor_link.active_from_date,

            schema.ACTIVE_TO_DATE:
                resident_sensor_link.active_to_date,

            schema.SETUP_DATE:
                resident_sensor_link.setup_date,

            schema.REMOVED_DATE:
                resident_sensor_link.removed_date,

        }
