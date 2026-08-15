# /src/infrastructure/persistence/schemas

class ResidentContactInformationColumns:
    RESIDENT_ID: str = "resident_id"
    RESIDENT_NAME: str = "resident_name"
    PRIMARY_CONTACT_NAME: str = "primary_contact_name"
    PRIMARY_CONTACT_EMAIL: str = "primary_contact_email"
    PRIMARY_CONTACT_TELEPHONE: str = "primary_contact_telephone"
    PRIMARY_CONTACT_ADDRESS: str = "primary_contact_address"
    ORDER = (
RESIDENT_ID,
RESIDENT_NAME,
PRIMARY_CONTACT_NAME,
PRIMARY_CONTACT_EMAIL,
PRIMARY_CONTACT_TELEPHONE,
PRIMARY_CONTACT_ADDRESS,
)