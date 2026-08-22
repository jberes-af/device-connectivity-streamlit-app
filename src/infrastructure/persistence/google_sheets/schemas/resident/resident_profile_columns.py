# /src/infrastructure/persistence/schemas/resident/resident_profile_columns.py

class ResidentProfileColumns:
    RESIDENT_ID: str = "resident_id"
    TENANT_ID: str = "tenant_id"
    FULL_NAME: str = "full_name"
    PREFERRED_NAME: str = "preferred_name"
    DATE_OF_BIRTH: str = "date_of_birth"
    TELEPHONE: str = "telephone"
    EMAIL: str = "email"
    ADDRESS_LINE_1: str = "address_line_1"
    ADDRESS_LINE_2: str = "address_line_2"
    CITY: str = "city"
    STATE: str = "state"
    POSTAL_CODE: str = "postal_code"
    ROOM_REFERENCE: str = "room_reference"
    ACTIVE_STATUS: str = "active_status"
    ORDER = (
        RESIDENT_ID,
        TENANT_ID,
        FULL_NAME,
        PREFERRED_NAME,
        DATE_OF_BIRTH,
        TELEPHONE,
        EMAIL,
        ADDRESS_LINE_1,
        ADDRESS_LINE_2,
        CITY,
        STATE,
        POSTAL_CODE,
        ROOM_REFERENCE,
        ACTIVE_STATUS,
    )
