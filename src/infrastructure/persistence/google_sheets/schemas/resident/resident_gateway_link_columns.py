# /src/infrastructure/persistence/schemas

class ResidentGatewayLinkColumns:
    RESIDENT_ID: str = "resident_id"
    GATEWAY_ID: str = "gateway_id"
    TENANT_ID: str = "tenant_id"
    ACTIVE_FROM_ISO: str = "active_from_iso"
    ACTIVE_TO_ISO: str = "active_to_iso"
    ORDER = (
RESIDENT_ID,
GATEWAY_ID,
TENANT_ID,
ACTIVE_FROM_ISO,
ACTIVE_TO_ISO,
)