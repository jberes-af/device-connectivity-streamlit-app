# /src/domain/enums/access/status_and_method_enums.py

from enum import StrEnum


class ConsentMethodEnum(StrEnum):
    WRITTEN = "written"
    ELECTRONIC_SIGNATURE = "electronic_signature"
    VERBAL = "verbal"
    PATIENT_PORTAL = "patient_portal"
    TELEPHONE = "telephone"
    OTHER = "other"


class ConsentStatusEnum(StrEnum):
    NOT_REQUESTED = "not_requested"
    PENDING = "pending"
    OBTAINED = "obtained"
    DECLINED = "declined"
    WITHDRAWN = "withdrawn"


class MonitoringStatusEnum(StrEnum):
    PENDING_SETUP = "pending_setup"
    ACTIVE = "active"
    PAUSED = "paused"
    DISCONTINUED = "discontinued"
    COMPLETED = "completed"


class EnrollmentStatusEnum(StrEnum):
    PENDING = "pending"
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
