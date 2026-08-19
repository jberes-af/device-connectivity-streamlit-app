# /src/infrastructure/persistence/mappers/resident/resident_profile_row_mapper.py

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

            schema.ROOM_REFERENCE:
                resident_profile.room_reference,

            schema.ACTIVE_STATUS:
                resident_profile.active_status,

        }
