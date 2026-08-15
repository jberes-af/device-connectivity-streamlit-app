# notification_enums.py


from enum import StrEnum


class NotificationMessageStatusEnum(StrEnum):
    CREATED = "Created"
    DELIVERED = "Delivered"
    FAILED = "Failed"
    SENT = "Sent"
