# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas import ResidentProfileColumns

from src.domain.entities.entities import ResidentProfile

from src.infrastructure.persistence.common.utils_parsing import *


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
            name=parse_required_text(
                row.get(schema.NAME),
                field_name=schema.NAME,
            ),
            preferred_name=parse_required_text(
                row.get(schema.PREFERRED_NAME),
                field_name=schema.PREFERRED_NAME,
            ),
            contact_information=parse_optional_text(
                row.get(schema.CONTACT_INFORMATION),
                field_name=schema.CONTACT_INFORMATION,
            ),
            tenant_facility_profile=parse_optional_text(
                row.get(schema.TENANT_FACILITY_PROFILE),
                field_name=schema.TENANT_FACILITY_PROFILE,
            ),
            room_reference=parse_optional_text(
                row.get(schema.ROOM_REFERENCE),
                field_name=schema.ROOM_REFERENCE,
            ),
            active_status=parse_optional_text(
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

            schema.NAME:
                resident_profile.name,

            schema.PREFERRED_NAME:
                resident_profile.preferred_name,

            schema.CONTACT_INFORMATION:
                resident_profile.contact_information,

            schema.TENANT_FACILITY_PROFILE:
                resident_profile.tenant_facility_profile,

            schema.ROOM_REFERENCE:
                resident_profile.room_reference,

            schema.ACTIVE_STATUS:
                resident_profile.active_status,

        }