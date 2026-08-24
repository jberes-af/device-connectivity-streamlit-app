# /src/infrastructure/persistence/schemas/person/resident_gateway_link_columns.py

class ResidentGatewayLinkColumns:
    RESIDENT_ID: str = "resident_id"
    GATEWAY_ID: str = "gateway_id"
    TENANT_ID: str = "tenant_id"
    ACTIVE_FROM_DATE: str = "active_from_date"
    ACTIVE_TO_DATE: str = "active_to_date"
    SETUP_DATE: str = "setup_date"
    REMOVED_DATE: str = "removed_date"
    ORDER = (
        RESIDENT_ID,
        GATEWAY_ID,
        TENANT_ID,
        ACTIVE_FROM_DATE,
        ACTIVE_TO_DATE,
        SETUP_DATE,
        REMOVED_DATE,
    )
