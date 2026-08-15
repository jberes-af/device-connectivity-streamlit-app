# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas import ResidentGatewayLinkColumns

from src.domain.entities.entities import ResidentGatewayLink

from src.infrastructure.persistence.common.utils_parsing import *


class ResidentGatewayLinkRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> ResidentGatewayLink:
        schema = ResidentGatewayLinkColumns

        return ResidentGatewayLink(
            resident_id=parse_required_text(
                row.get(schema.RESIDENT_ID),
                field_name=schema.RESIDENT_ID,
            ),
            gateway_id=parse_required_text(
                row.get(schema.GATEWAY_ID),
                field_name=schema.GATEWAY_ID,
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
        resident_gateway_link: ResidentGatewayLink,
    ) -> RawRow:
        schema = ResidentGatewayLinkColumns

        return {

            schema.RESIDENT_ID:
                resident_gateway_link.resident_id,

            schema.GATEWAY_ID:
                resident_gateway_link.gateway_id,

            schema.TENANT_ID:
                resident_gateway_link.tenant_id,

            schema.ACTIVE_FROM_ISO:
                resident_gateway_link.active_from_iso,

            schema.ACTIVE_TO_ISO:
                resident_gateway_link.active_to_iso,

        }