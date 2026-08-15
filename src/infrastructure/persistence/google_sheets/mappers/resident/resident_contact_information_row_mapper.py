# /src/infrastructure/persistence/mappers

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas import ResidentContactInformationColumns

from src.domain.entities.entities import ResidentContactInformation

from src.infrastructure.persistence.common.utils_parsing import *


class ResidentContactInformationRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> ResidentContactInformation:
        schema = ResidentContactInformationColumns

        return ResidentContactInformation(
            resident_id=parse_required_text(
                row.get(schema.RESIDENT_ID),
                field_name=schema.RESIDENT_ID,
            ),
            resident_name=parse_required_text(
                row.get(schema.RESIDENT_NAME),
                field_name=schema.RESIDENT_NAME,
            ),
            primary_contact_name=parse_required_text(
                row.get(schema.PRIMARY_CONTACT_NAME),
                field_name=schema.PRIMARY_CONTACT_NAME,
            ),
            primary_contact_email=parse_required_text(
                row.get(schema.PRIMARY_CONTACT_EMAIL),
                field_name=schema.PRIMARY_CONTACT_EMAIL,
            ),
            primary_contact_telephone=parse_required_text(
                row.get(schema.PRIMARY_CONTACT_TELEPHONE),
                field_name=schema.PRIMARY_CONTACT_TELEPHONE,
            ),
            primary_contact_address=parse_required_text(
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

            schema.RESIDENT_NAME:
                resident_contact_information.resident_name,

            schema.PRIMARY_CONTACT_NAME:
                resident_contact_information.primary_contact_name,

            schema.PRIMARY_CONTACT_EMAIL:
                resident_contact_information.primary_contact_email,

            schema.PRIMARY_CONTACT_TELEPHONE:
                resident_contact_information.primary_contact_telephone,

            schema.PRIMARY_CONTACT_ADDRESS:
                resident_contact_information.primary_contact_address,

        }