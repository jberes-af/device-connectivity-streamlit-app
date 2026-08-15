# /src/infrastructure/persistence/schemas

class UserGatewayLinkColumns:
    TENANT_ID: str = "tenant_id"
    USER_ID: str = "user_id"
    GATEWAY_ID: str = "gateway_id"
    ORDER = (
TENANT_ID,
USER_ID,
GATEWAY_ID,
)