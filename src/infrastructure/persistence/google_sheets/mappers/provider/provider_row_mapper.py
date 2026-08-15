# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.provider.provider_columns import (
    ProviderColumns,
)

from src.domain.entities.care.provider_entities import Provider

from src.infrastructure.persistence.common.utils_parsing import (
    parse_optional_bool,
    parse_optional_text,
    parse_required_text,
)


class ProviderRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> Provider:
        schema = ProviderColumns

        return Provider(
            provider_id=parse_required_text(
                row.get(schema.PROVIDER_ID),
                field_name=schema.PROVIDER_ID,
            ),
            national_provider_identifier=parse_optional_text(
                row.get(schema.NATIONAL_PROVIDER_IDENTIFIER),
                field_name=schema.NATIONAL_PROVIDER_IDENTIFIER,
            ),
            first_name=parse_required_text(
                row.get(schema.FIRST_NAME),
                field_name=schema.FIRST_NAME,
            ),
            middle_name=parse_optional_text(
                row.get(schema.MIDDLE_NAME),
                field_name=schema.MIDDLE_NAME,
            ),
            last_name=parse_required_text(
                row.get(schema.LAST_NAME),
                field_name=schema.LAST_NAME,
            ),
            credentials=parse_optional_text(
                row.get(schema.CREDENTIALS),
                field_name=schema.CREDENTIALS,
            ),
            specialty=parse_optional_text(
                row.get(schema.SPECIALTY),
                field_name=schema.SPECIALTY,
            ),
            organization_id=parse_optional_text(
                row.get(schema.ORGANIZATION_ID),
                field_name=schema.ORGANIZATION_ID,
            ),
            telephone=parse_optional_text(
                row.get(schema.TELEPHONE),
                field_name=schema.TELEPHONE,
            ),
            email=parse_optional_text(
                row.get(schema.EMAIL),
                field_name=schema.EMAIL,
            ),
            address_line_1=parse_optional_text(
                row.get(schema.ADDRESS_LINE_1),
                field_name=schema.ADDRESS_LINE_1,
            ),
            address_line_2=parse_optional_text(
                row.get(schema.ADDRESS_LINE_2),
                field_name=schema.ADDRESS_LINE_2,
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
            is_active=parse_optional_bool(
                row.get(schema.IS_ACTIVE),
                field_name=schema.IS_ACTIVE,
            ),
        )

    @staticmethod
    def to_row(
            provider: Provider,
    ) -> RawRow:
        schema = ProviderColumns

        return {

            schema.PROVIDER_ID:
                provider.provider_id,

            schema.NATIONAL_PROVIDER_IDENTIFIER:
                provider.national_provider_identifier,

            schema.FIRST_NAME:
                provider.first_name,

            schema.MIDDLE_NAME:
                provider.middle_name,

            schema.LAST_NAME:
                provider.last_name,

            schema.CREDENTIALS:
                provider.credentials,

            schema.SPECIALTY:
                provider.specialty,

            schema.ORGANIZATION_ID:
                provider.organization_id,

            schema.TELEPHONE:
                provider.telephone,

            schema.EMAIL:
                provider.email,

            schema.ADDRESS_LINE_1:
                provider.address_line_1,

            schema.ADDRESS_LINE_2:
                provider.address_line_2,

            schema.CITY:
                provider.city,

            schema.STATE:
                provider.state,

            schema.POSTAL_CODE:
                provider.postal_code,

            schema.IS_ACTIVE:
                provider.is_active,

        }
