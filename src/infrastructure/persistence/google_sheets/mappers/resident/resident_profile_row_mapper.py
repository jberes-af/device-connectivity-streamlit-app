# /src/infrastructure/persistence/mappers/person/resident_profile_row_mapper.py

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.resident.resident_profile_columns import (
    ResidentProfileColumns,
)

from src.domain.entities.person.resident_entities import ResidentProfile

from src.infrastructure.persistence.common.utils_parsing import (
    parse_optional_bool,
    parse_optional_date,
    parse_optional_text,
    parse_required_text,
)


class ResidentProfileRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> ResidentProfile:
        schema = ResidentProfileColumns

        return ResidentProfile(
            resident_id=parse_required_text(
                row.get(schema.RESIDENT_ID),
                field_name=schema.RESIDENT_ID,
            ),
            tenant_id=parse_required_text(
                row.get(schema.TENANT_ID),
                field_name=schema.TENANT_ID,
            ),
            full_name=parse_required_text(
                row.get(schema.FULL_NAME),
                field_name=schema.FULL_NAME,
            ),
            preferred_name=parse_required_text(
                row.get(schema.PREFERRED_NAME),
                field_name=schema.PREFERRED_NAME,
            ),
            date_of_birth=parse_optional_date(
                row.get(schema.DATE_OF_BIRTH),
                field_name=schema.DATE_OF_BIRTH,
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

            room_reference=parse_optional_text(
                row.get(schema.ROOM_REFERENCE),
                field_name=schema.ROOM_REFERENCE,
            ),
            active_status=parse_optional_bool(
                row.get(schema.ACTIVE_STATUS),
                field_name=schema.ACTIVE_STATUS,
            ),
        )

    @staticmethod
    def to_row(
            resident_profile: ResidentProfile,
    ) -> RawRow:
        schema = ResidentProfileColumns

        return {

            schema.RESIDENT_ID:
                resident_profile.resident_id,

            schema.TENANT_ID:
                resident_profile.tenant_id,

            schema.FULL_NAME:
                resident_profile.full_name,

            schema.PREFERRED_NAME:
                resident_profile.preferred_name,

            schema.DATE_OF_BIRTH:
                resident_profile.date_of_birth,

            schema.TELEPHONE:
                resident_profile.telephone,

            schema.EMAIL:
                resident_profile.email,

            schema.ADDRESS_LINE_1:
                resident_profile.address_line_2,

            schema.ADDRESS_LINE_2:
                resident_profile.address_line_2,

            schema.CITY:
                resident_profile.city,

            schema.STATE:
                resident_profile.state,

            schema.POSTAL_CODE:
                resident_profile.postal_code,

            schema.ROOM_REFERENCE:
                resident_profile.room_reference,

            schema.ACTIVE_STATUS:
                resident_profile.active_status,

        }
