# /src/infrastructure/config/m365_settings_loader.py

from src.infrastructure.config.settings_model import M365Settings

from src.infrastructure.config.secret_provider import (
    SecretProvider,
)


def load_microsoft365_settings(
    secret_provider: SecretProvider,
) -> M365Settings:

    m365 = M365Settings(
        m365_tenant_id=secret_provider.get_required("M365_TENANT_ID"),
        m365_client_id=secret_provider.get_required("M365_CLIENT_ID"),
        m365_client_secret=secret_provider.get_required("M365_CLIENT_SECRET"),
    )

    return m365

