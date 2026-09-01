# /src/main/compose_root_m365.py

from docs.m365_email_ports import MailSenderPort

from src.infrastructure.config.settings_model import Settings

from src.infrastructure.services.m365.msal_token_provider import (
    MsalClientSecretTokenProvider,
)

from src.infrastructure.services.m365.graph_mail_sender import MicrosoftGraphMailSender


def build_m365_graph_mail_service(
        settings: Settings,
) -> MailSenderPort:

    token_provider = MsalClientSecretTokenProvider(
        tenant_id=settings.m365_authentication.m365_tenant_id,
        client_id=settings.m365_authentication.m365_client_id,
        client_secret=settings.m365_authentication.m365_client_secret,
    )

    mail_sender = MicrosoftGraphMailSender(
        token_provider=token_provider,
        # graph_base_url=settings.m365_graph_base_url,
        # timeout_seconds=30.0,
    )


    return mail_sender