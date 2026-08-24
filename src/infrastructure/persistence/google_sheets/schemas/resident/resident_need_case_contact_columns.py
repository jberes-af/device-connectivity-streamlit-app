# /src/infrastructure/persistence/schemas/person/resident_need_case_contact_columns.py

class ResidentNeedCaseContactColumns:
    RESIDENT_ID: str = "resident_id"
    PRIMARY_CONTACT_NAME: str = "primary_contact_name"
    PRIMARY_CONTACT_EMAIL: str = "primary_contact_email"
    PRIMARY_CONTACT_TELEPHONE: str = "primary_contact_telephone"
    PRIMARY_CONTACT_ADDRESS: str = "primary_contact_address"
    PRIMARY_CONTACT_RELATIONSHIP: str = "primary_contact_relationship"

    ORDER = (
        RESIDENT_ID,
        PRIMARY_CONTACT_NAME,
        PRIMARY_CONTACT_EMAIL,
        PRIMARY_CONTACT_TELEPHONE,
        PRIMARY_CONTACT_ADDRESS,
        PRIMARY_CONTACT_RELATIONSHIP,
    )
