# /src/infrastructure/persistence/schemas

class ResidentProfileColumns:
    RESIDENT_ID: str = "resident_id"
    TENANT_ID: str = "tenant_id"
    NAME: str = "name"
    PREFERRED_NAME: str = "preferred_name"
    CONTACT_INFORMATION: str = "contact_information"
    TENANT_FACILITY_PROFILE: str = "tenant_facility_profile"
    ROOM_REFERENCE: str = "room_reference"
    ACTIVE_STATUS: str = "active_status"
    ORDER = (
RESIDENT_ID,
TENANT_ID,
NAME,
PREFERRED_NAME,
CONTACT_INFORMATION,
TENANT_FACILITY_PROFILE,
ROOM_REFERENCE,
ACTIVE_STATUS,
)