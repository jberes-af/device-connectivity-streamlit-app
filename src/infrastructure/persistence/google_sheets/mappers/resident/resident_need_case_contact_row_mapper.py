# /src/infrastructure/persistence/mappers/resident/resident_need_case_contact_row_mapper.py

from src.infrastructure.persistence.common.types import RawRow

from src.infrastructure.persistence.google_sheets.schemas.resident.resident_need_case_contact_columns import (
    ResidentNeedCaseContactColumns,
)

from src.domain.entities.person.resident_entities import ResidentInCaseOfNeedContact

from src.infrastructure.persistence.common.utils_parsing import (
    parse_required_text,
)


class ResidentNeedCaseContactRowMapper:

    @staticmethod
    def to_domain(row: RawRow) -> ResidentInCaseOfNeedContact:
        schema = ResidentNeedCaseContactColumns

        return ResidentInCaseOfNeedContact(
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
            contact_relationship=parse_required_text(
                row.get(schema.PRIMARY_CONTACT_RELATIONSHIP),
                field_name=schema.PRIMARY_CONTACT_RELATIONSHIP,
            ),
        )

    @staticmethod
    def to_row(
            resident_contact_information: ResidentInCaseOfNeedContact,
    ) -> RawRow:
        schema = ResidentNeedCaseContactColumns

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

            schema.PRIMARY_CONTACT_RELATIONSHIP:
                resident_contact_information.contact_relationship,

        }
