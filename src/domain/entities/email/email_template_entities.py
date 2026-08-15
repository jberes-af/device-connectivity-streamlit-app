# /src/domain/entities/email_template_entities.py

from dataclasses import dataclass
from enum import StrEnum


@dataclass(frozen=True, slots=True)
class SignatureLink:
    label: str
    url: str


@dataclass(frozen=True, slots=True)
class Signature:
    closing: str
    links: tuple[SignatureLink, ...]


class MessageFormat(StrEnum):
    PLAIN_TEXT = "plain_text"
    MARKDOWN = "markdown"
    HTML = "html"


@dataclass(frozen=True, slots=True)
class MessageTemplate:
    template_id: str
    title: str
    subject_template: str
    body_template: str
    format: MessageFormat


@dataclass(frozen=True, slots=True)
class MessageContext:
    first_name: str


@dataclass(frozen=True, slots=True)
class OutboundMessage:
    subject: str
    body: str
    format: MessageFormat
