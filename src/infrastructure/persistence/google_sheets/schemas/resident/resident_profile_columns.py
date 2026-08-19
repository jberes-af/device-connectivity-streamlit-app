# /src/infrastructure/persistence/schemas/resident/resident_profile_columns.py

class ResidentProfileColumns:
    RESIDENT_ID: str = "resident_id"
    TENANT_ID: str = "tenant_id"
    FULL_NAME: str = "full_name"
    PREFERRED_NAME: str = "preferred_name"
    DATE_OF_BIRTH: str = "date_of_birth"
    ROOM_REFERENCE: str = "room_reference"
    ACTIVE_STATUS: str = "active_status"
    ORDER = (
        RESIDENT_ID,
        TENANT_ID,
        FULL_NAME,
        PREFERRED_NAME,
        DATE_OF_BIRTH,
        ROOM_REFERENCE,
        ACTIVE_STATUS,
    )
