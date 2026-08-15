# /src/domain/entities/sensing/notification_entities.py

from dataclasses import dataclass

from src.domain.enums.sensing.notification_enums import NotificationMessageStatusEnum


@dataclass(frozen=True)
class NotificationMessageDTO:
    notification_id: str
    tenant_id: str
    recipient_user_id: str
    channel: str
    title: str
    message: str
    status: NotificationMessageStatusEnum
    created_at_iso: str
    sent_at_iso: str | None = None
    delivered_at_iso: str | None = None
    failed_at_iso: str | None = None
    source_event_id: str | None = None
    source_event_type: str | None = None
