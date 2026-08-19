# /src/domain/enums/patient_enums.py

from enum import StrEnum


class PatientProviderRoleEnum(StrEnum):
    TREATING_PROVIDER = "treating_provider"
    ORDERING_PROVIDER = "ordering_provider"
    SUPERVISING_PROVIDER = "supervising_provider"
    PRIMARY_CARE_PROVIDER = "primary_care_provider"
    REFERRING_PROVIDER = "referring_provider"
    CONSULTING_PROVIDER = "consulting_provider"
    THERAPIST = "therapist"
    OTHER = "other"


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
