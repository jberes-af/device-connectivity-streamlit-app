# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas import UserSensorLinkColumns

from src.domain.entities.entities import UserSensorLink

from src.infrastructure.persistence.common.utils_parsing import *


class UserSensorLinkRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> UserSensorLink:
        schema = UserSensorLinkColumns

        return UserSensorLink(
            tenant_id=parse_required_text(
                row.get(schema.TENANT_ID),
                field_name=schema.TENANT_ID,
            ),
            user_id=parse_required_text(
                row.get(schema.USER_ID),
                field_name=schema.USER_ID,
            ),
            sensor_id=parse_required_text(
                row.get(schema.SENSOR_ID),
                field_name=schema.SENSOR_ID,
            ),
        )


    @staticmethod
    def to_row(
        user_sensor_link: UserSensorLink,
    ) -> RawRow:
        schema = UserSensorLinkColumns

        return {

            schema.TENANT_ID:
                user_sensor_link.tenant_id,

            schema.USER_ID:
                user_sensor_link.user_id,

            schema.SENSOR_ID:
                user_sensor_link.sensor_id,

        }