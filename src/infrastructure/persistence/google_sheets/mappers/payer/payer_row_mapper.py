# /src/infrastructure/persistence/mappers

from src.domain.entities.billing.payer_entities import Payer
from src.domain.enums.billing.payer_enums import PayerType

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.payer.payer_columns import (
    PayerColumns,
)

from src.infrastructure.persistence.common.utils_parsing import (
    parse_optional_bool,
    parse_optional_text,
    parse_required_text,
)


class PayerRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> Payer:
        schema = PayerColumns

        return Payer(
            payer_id=parse_required_text(
                row.get(schema.PAYER_ID),
                field_name=schema.PAYER_ID,
            ),
            payer_name=parse_required_text(
                row.get(schema.PAYER_NAME),
                field_name=schema.PAYER_NAME,
            ),
            payer_type=PayerType(parse_optional_text(
                row.get(schema.PAYER_TYPE),
                field_name=schema.PAYER_TYPE,
            )),
            electronic_payer_id=parse_optional_text(
                row.get(schema.ELECTRONIC_PAYER_ID),
                field_name=schema.ELECTRONIC_PAYER_ID,
            ),
            claims_address_line_1=parse_optional_text(
                row.get(schema.CLAIMS_ADDRESS_LINE_1),
                field_name=schema.CLAIMS_ADDRESS_LINE_1,
            ),
            claims_address_line_2=parse_optional_text(
                row.get(schema.CLAIMS_ADDRESS_LINE_2),
                field_name=schema.CLAIMS_ADDRESS_LINE_2,
            ),
            city=parse_optional_text(
                row.get(schema.CITY),
                field_name=schema.CITY,
            ),
            state=parse_optional_text(
                row.get(schema.STATE),
                field_name=schema.STATE,
            ),
            postal_code=parse_optional_text(
                row.get(schema.POSTAL_CODE),
                field_name=schema.POSTAL_CODE,
            ),
            telephone=parse_optional_text(
                row.get(schema.TELEPHONE),
                field_name=schema.TELEPHONE,
            ),
            website=parse_optional_text(
                row.get(schema.WEBSITE),
                field_name=schema.WEBSITE,
            ),
            accepts_electronic_claims=parse_optional_bool(
                row.get(schema.ACCEPTS_ELECTRONIC_CLAIMS),
                field_name=schema.ACCEPTS_ELECTRONIC_CLAIMS,
            ),
        )

    @staticmethod
    def to_row(
            payer: Payer,
    ) -> RawRow:
        schema = PayerColumns

        return {

            schema.PAYER_ID: payer.payer_id,

            schema.PAYER_NAME: payer.payer_name,

            schema.PAYER_TYPE: payer.payer_type.value,

            schema.ELECTRONIC_PAYER_ID: payer.electronic_payer_id,

            schema.CLAIMS_ADDRESS_LINE_1: payer.claims_address_line_1,

            schema.CLAIMS_ADDRESS_LINE_2: payer.claims_address_line_2,

            schema.CITY: payer.city,

            schema.STATE: payer.state,

            schema.POSTAL_CODE:
                payer.postal_code,

            schema.TELEPHONE:
                payer.telephone,

            schema.WEBSITE:
                payer.website,

            schema.ACCEPTS_ELECTRONIC_CLAIMS:
                payer.accepts_electronic_claims,

        }
