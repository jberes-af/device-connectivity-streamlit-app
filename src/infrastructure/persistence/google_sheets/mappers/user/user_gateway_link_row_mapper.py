# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas import UserGatewayLinkColumns

from src.domain.entities.entities import UserGatewayLink

from src.infrastructure.persistence.common.utils_parsing import *


class UserGatewayLinkRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> UserGatewayLink:
        schema = UserGatewayLinkColumns

        return UserGatewayLink(
            tenant_id=parse_required_text(
                row.get(schema.TENANT_ID),
                field_name=schema.TENANT_ID,
            ),
            user_id=parse_required_text(
                row.get(schema.USER_ID),
                field_name=schema.USER_ID,
            ),
            gateway_id=parse_required_text(
                row.get(schema.GATEWAY_ID),
                field_name=schema.GATEWAY_ID,
            ),
        )


    @staticmethod
    def to_row(
        user_gateway_link: UserGatewayLink,
    ) -> RawRow:
        schema = UserGatewayLinkColumns

        return {

            schema.TENANT_ID:
                user_gateway_link.tenant_id,

            schema.USER_ID:
                user_gateway_link.user_id,

            schema.GATEWAY_ID:
                user_gateway_link.gateway_id,

        }