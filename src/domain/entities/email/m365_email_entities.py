# /src/domain/entities/m365_email_entities.py

from dataclasses import dataclass, field
from typing import Sequence


@dataclass(frozen=True)
class EmailRecipient:
    address: str
    name: str | None = None


@dataclass(frozen=True)
class EmailAttachment:
    filename: str
    content_type: str
    content_bytes: bytes
    attachment_id: str | None = None


@dataclass(frozen=True)
class OutboundEmail:
    from_address: str
    to_recipients: Sequence[EmailRecipient]
    subject: str
    body_html: str
    cc_recipients: Sequence[EmailRecipient] = field(default_factory=tuple)
    bcc_recipients: Sequence[EmailRecipient] = field(default_factory=tuple)
    attachments: Sequence[EmailAttachment] = field(default_factory=tuple)

    def validate(self) -> None:
        if not self.from_address.strip():
            raise ValueError("from_address is required.")

        if not self.to_recipients:
            raise ValueError("At least one to_recipient is required.")

        if not self.subject.strip():
            raise ValueError("subject is required.")

        if not self.body_html.strip():
            raise ValueError("body_html is required.")
