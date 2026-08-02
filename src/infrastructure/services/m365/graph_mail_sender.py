# infrastructure/m365/graph_mail_sender.py

from typing import Any, Sequence

from src.application.dto.send_email_dtos import MailSendResult

from src.application.ports.m365_email_ports import (
    AccessTokenProviderPort,
    MailSenderPort,
)

from src.domain.entities.m365_email_entities import (
    EmailAttachment,
    EmailRecipient,
    OutboundEmail,
)

import base64
import requests

class MicrosoftGraphMailSender(MailSenderPort):
    _GRAPH_BASE_URL = "https://graph.microsoft.com/v1.0"

    def __init__(
        self,
        *,
        token_provider: AccessTokenProviderPort,
        timeout_seconds: float = 30.0,
    ) -> None:
        self._token_provider = token_provider
        self._timeout_seconds = timeout_seconds
        # self._graph_base_url = graph_base_url.rstrip("/")

    def send_email(
            self,
            message: OutboundEmail,
    ) -> MailSendResult:

        token = self._token_provider.get_access_token()
        url = (
            f"{self._GRAPH_BASE_URL}"
            f"/users/{message.from_address}/sendMail"
        )

        payload = {
            "message": {
                "subject": message.subject,
                "body": self._build_body(message),
                "toRecipients": self._build_recipients(message.to_recipients),
                "ccRecipients": self._build_recipients(message.cc_recipients),
                "bccRecipients": self._build_recipients(message.bcc_recipients),
                "attachments": self._build_attachments(message.attachments),
            },
            "saveToSentItems": True,
        }

        response = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=self._timeout_seconds,
        )

        if response.status_code != 202:
            raise RuntimeError(
                "Microsoft Graph sendMail failed. "
                f"status={response.status_code}, body={response.text}"
            )

        return MailSendResult(
            accepted=True,
            provider="Microsoft Graph",
        )

    @staticmethod
    def _build_body(
            message: OutboundEmail,
    ) -> dict[str, str]:
        if not message.body_html:
            raise ValueError(
                "OutboundEmail.body_html is required."
            )

        return {
            "contentType": "html",
            "content": message.body_html,
        }

    """
    @staticmethod
    def _build_body(message: OutboundEmail) -> dict[str, str]:
        if message.body_html:
            return {
                "contentType": "HTML",
                "content": message.body_html,
            }
        return {
            "contentType": "Text",
            "content": message.body_text or "",
        }
    """

    @staticmethod
    def _build_recipients(
            recipients: Sequence[EmailRecipient],
    ) -> list[dict[str, Any]]:
        return [
            {
                "emailAddress": {
                    "address": recipient.address,
                    **({"name": recipient.name} if recipient.name else {}),
                }
            }
            for recipient in recipients
        ]

    @staticmethod
    def _build_attachments(
            attachments: Sequence[EmailAttachment],
    ) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        for attachment in attachments:
            result.append(
                {
                    "@odata.type": "#microsoft.graph.fileAttachment",
                    "name": attachment.filename,
                    "contentType": attachment.content_type,
                    "contentBytes": base64.b64encode(attachment.content_bytes).decode("ascii"),
                }
            )
        return result
