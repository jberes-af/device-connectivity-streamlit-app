# /src/infrastructure/persistence/mappers/resident/resident_contact_information_row_mapper.py

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.resident.resident_contact_information_columns import (
    ResidentContactInformationColumns,
)

from src.domain.entities.person.resident_entities import ResidentContactInformation

from src.infrastructure.persistence.common.utils_parsing import (
    parse_required_text,
)


class ResidentContactInformationRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> ResidentContactInformation:
        schema = ResidentContactInformationColumns

        return ResidentContactInformation(
            resident_id=parse_required_text(
                row.get(schema.RESIDENT_ID),
                field_name=schema.RESIDENT_ID,
            ),
            contact_name=parse_required_text(
                row.get(schema.PRIMARY_CONTACT_NAME),
                field_name=schema.PRIMARY_CONTACT_NAME,
            ),
            contact_email=parse_required_text(
                row.get(schema.PRIMARY_CONTACT_EMAIL),
                field_name=schema.PRIMARY_CONTACT_EMAIL,
            ),
            contact_telephone=parse_required_text(
                row.get(schema.PRIMARY_CONTACT_TELEPHONE),
                field_name=schema.PRIMARY_CONTACT_TELEPHONE,
            ),
            contact_address=parse_required_text(
                row.get(schema.PRIMARY_CONTACT_ADDRESS),
                field_name=schema.PRIMARY_CONTACT_ADDRESS,
            ),
        )

    @staticmethod
    def to_row(
            resident_contact_information: ResidentContactInformation,
    ) -> RawRow:
        schema = ResidentContactInformationColumns

        return {

            schema.RESIDENT_ID:
                resident_contact_information.resident_id,

            schema.PRIMARY_CONTACT_NAME:
                resident_contact_information.contact_name,

            schema.PRIMARY_CONTACT_EMAIL:
                resident_contact_information.contact_email,

            schema.PRIMARY_CONTACT_TELEPHONE:
                resident_contact_information.contact_telephone,

            schema.PRIMARY_CONTACT_ADDRESS:
                resident_contact_information.contact_address,

        }
