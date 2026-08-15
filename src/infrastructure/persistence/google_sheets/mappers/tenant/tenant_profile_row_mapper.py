# /src/infrastructure/persistence/google_sheets/mappers/tenant/tenant_profile_row_mapper.py

from src.domain.enums.person.tenant_enums import TenantTypeEnum
from src.domain.entities.person.tenant_entities import (
    TenantProfile,
)

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.tenant.tenant_profile_columns import (
    TenantProfileColumns,
)

from src.infrastructure.persistence.common.utils_parsing import (
    parse_optional_enum,
    parse_optional_text,
    parse_required_text,
)


class TenantProfileRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> TenantProfile:
        schema = TenantProfileColumns

        return TenantProfile(
            tenant_id=parse_required_text(
                row.get(schema.TENANT_ID),
                field_name=schema.TENANT_ID,
            ),
            tenant_name=parse_required_text(
                row.get(schema.TENANT_NAME),
                field_name=schema.TENANT_NAME,
            ),
            tenant_type=parse_optional_enum(
                row.get(schema.TENANT_TYPE),
                enum_type=TenantTypeEnum,
                field_name=schema.TENANT_TYPE,
            ),

            tenant_street=parse_required_text(
                row.get(schema.TENANT_STREET),
                field_name=schema.TENANT_STREET,
            ),

            tenant_city=parse_required_text(
                row.get(schema.TENANT_CITY),
                field_name=schema.TENANT_CITY,
            ),

            tenant_state=parse_required_text(
                row.get(schema.TENANT_STATE),
                field_name=schema.TENANT_STATE,
            ),

            tenant_postal_code=parse_required_text(
                row.get(schema.TENANT_POSTAL_CODE),
                field_name=schema.TENANT_POSTAL_CODE,
            ),

            tenant_telephone=parse_required_text(
                row.get(schema.TENANT_TELEPHONE),
                field_name=schema.TENANT_TELEPHONE,
            ),
            tenant_manager=parse_required_text(
                row.get(schema.TENANT_MANAGER),
                field_name=schema.TENANT_MANAGER,
            ),
            timezone=parse_optional_text(
                row.get(schema.TIMEZONE),
                field_name=schema.TIMEZONE,
            ),
        )

    @staticmethod
    def to_row(
            tenant_profile: TenantProfile,
    ) -> RawRow:
        schema = TenantProfileColumns

        return {

            schema.TENANT_ID:
                tenant_profile.tenant_id,

            schema.TENANT_NAME:
                tenant_profile.tenant_name,

            schema.TENANT_TYPE:
                tenant_profile.tenant_type,

            schema.TENANT_STREET:
                tenant_profile.tenant_street,

            schema.TENANT_CITY:
                tenant_profile.tenant_city,

            schema.TENANT_STATE:
                tenant_profile.tenant_state,

            schema.TENANT_POSTAL_CODE:
                tenant_profile.tenant_postal_code,

            schema.TENANT_TELEPHONE:
                tenant_profile.tenant_telephone,

            schema.TENANT_MANAGER:
                tenant_profile.tenant_manager,

            schema.TIMEZONE:
                tenant_profile.timezone,

        }
