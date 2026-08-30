# /src/infrastructure/persistence/mappers/contact/resident_gateway_link_row_mapper.py

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.access.resident_gateway_link_columns import (
    ResidentGatewayLinkColumns)

from src.domain.entities.sensing.assignment_entities import ResidentGatewayLink

from src.infrastructure.persistence.common.utils_parsing import (
    parse_required_text,
    parse_optional_date,
)


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

            schema.ACTIVE_FROM_DATE:
                resident_gateway_link.active_from_date,

            schema.ACTIVE_TO_DATE:
                resident_gateway_link.active_to_date,

            schema.SETUP_DATE:
                resident_gateway_link.setup_date,

            schema.REMOVED_DATE:
                resident_gateway_link.removed_date,

        }
